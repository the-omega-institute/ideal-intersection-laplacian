"""
Diagnostic for the still-open region 4 <= a < b < c < 4a^2 - 2a.

For n = p1^a p2^b p3^c with a < b < c, we build the Laplacian
quotient matrix B of the graph H obtained by removing universal
vertices from the ideal intersection graph. The cells are indexed
by the nonempty proper subsets of {1,2,3}, and B is 6x6 with
row sums zero. Its characteristic polynomial is x*h(x) with h of
degree 5.

For each (a, b, c) in the region, we check whether h has a
noninteger root. Since h is monic with integer coefficients,
every rational root is an integer; hence h has no noninteger
root iff h factors into five linear factors over Z.

The original h here is the quotient quintic for H, denoted g_B in
the output. The complement quintic h_C(x)=-g_B(N-x) is reported
separately: its endpoints are the ones used in the interval proofs.
The generic determinant is computed once and specialized exactly.
This script is a DIAGNOSTIC, not an all-exponent proof. It requires sympy.
"""

import sys
import argparse
import hashlib
import json
import csv
from math import isqrt
from pathlib import Path

try:
    from sympy import symbols, Matrix, Poly, cancel, expand, lambdify
except ImportError:
    print("ERROR: sympy is required. pip install sympy")
    sys.exit(1)


x = symbols('x')


def quotient_matrix(a, b, c):
    """
    Return the 6x6 Laplacian quotient matrix B for H.

    Cells are (1,), (2,), (3,), (1,2), (1,3), (2,3) in this order,
    with sizes a, b, c, ab, ac, bc respectively. Two cells are
    adjacent in the quotient iff their supports intersect. For a
    cell-constant vector, internal neighbors cancel in the Laplacian
    action, so the diagonal of B is exactly the number of external
    neighbors of any vertex in the cell.
    """
    k = {1: a, 2: b, 3: c}
    cells = [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
    n = len(cells)

    # Cell sizes
    sizes = []
    for S in cells:
        s = 1
        for i in S:
            s *= k[i]
        sizes.append(s)

    # Build B
    B = [[0] * n for _ in range(n)]
    for i, S in enumerate(cells):
        external = 0
        for j, T in enumerate(cells):
            if j != i and set(S) & set(T):
                external += sizes[j]
        B[i][i] = external
        for j, T in enumerate(cells):
            if j != i and set(S) & set(T):
                B[i][j] = -sizes[j]

    return Matrix(B)


def quintic(B):
    """Return h(x) = charpoly(B) / x as a Poly over Z."""
    char_expr = B.charpoly(x).as_expr()
    return Poly(cancel(char_expr / x), x)


def has_noninteger_root(h):
    """
    Return True iff h has a noninteger root.

    h is monic with integer coefficients, so every rational root is
    an integer. Thus h has a noninteger root iff h does NOT factor
    into five linear factors over Z.

    Fast pre-filter: if the discriminant is a nonzero non-square,
    the answer is immediately True.
    """
    return noninteger_witness(h) != 'integer_spectrum'


def noninteger_witness(polynomial, discriminant=None):
    if discriminant is None:
        discriminant = int(polynomial.discriminant())
    if discriminant != 0 and (discriminant < 0 or isqrt(discriminant) ** 2 != discriminant):
        return 'nonsquare_discriminant'
    factors = polynomial.factor_list()[1]
    return 'nonlinear_factor' if any(factor.degree() >= 2 for factor, multiplicity in factors) else 'integer_spectrum'


def horner(coefficients, argument):
    value = 0
    for coefficient in coefficients:
        value = value * argument + coefficient
    return value


def sign_char(v):
    if v > 0: return '+'
    if v < 0: return '-'
    return '0'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--a-max', type=int, default=7)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--certificate-csv', type=Path)
    arguments = parser.parse_args()
    if arguments.a_max < 4:
        parser.error('--a-max must be at least4')
    first, second, third = symbols('a b c')
    generic_matrix = quotient_matrix(first, second, third)
    from check_six_support_quotient import support_quotient
    assert generic_matrix == support_quotient((first, second, third))
    generic_quintic = quintic(generic_matrix)
    complement_quintic = quintic(support_quotient((first, second, third), complement=True))
    total = first + second + third + first * second + first * third + second * third
    assert expand(generic_quintic.as_expr() + complement_quintic.as_expr().subs(x, total - x)) == 0
    specialize = lambdify((first, second, third), generic_quintic.all_coeffs(), modules='math', cse=True)
    records = []
    independent_cases = []
    record_digest = hashlib.sha256()
    certificate_stream = arguments.certificate_csv.open('w', newline='') if arguments.certificate_csv else None
    certificate_writer = csv.writer(certificate_stream, lineterminator='\n') if certificate_stream else None
    if certificate_writer:
        certificate_writer.writerow(['a', 'b', 'c', 'discriminant', 'floor_sqrt'])
    if not arguments.json:
        print('Open region 4<=a<b<c<4a^2-2a; requested4<=a<=7' if arguments.a_max == 7
              else f'Open region 4<=a<b<c<4a^2-2a; a_max={arguments.a_max}', flush=True)
        print('g_B=det(xI-B)/x for H; h_C=-g_B(N-x) for its complement.', flush=True)
    for minimum in range(4, arguments.a_max + 1):
        cutoff = 4 * minimum * minimum - 2 * minimum
        patterns = {'g_B': {}, 'h_C': {}}
        witnesses = {}
        pair_count = 0
        noninteger_count = 0
        for middle in range(minimum + 1, cutoff - 1):
            for maximum in range(middle + 1, cutoff):
                coefficients = specialize(minimum, middle, maximum)
                assert all(isinstance(value, int) for value in coefficients)
                polynomial = Poly.from_list(coefficients, x, domain='ZZ')
                discriminant = int(polynomial.discriminant())
                witness = noninteger_witness(polynomial, discriminant)
                if certificate_writer:
                    certificate_writer.writerow([minimum, middle, maximum, discriminant,
                                                 isqrt(discriminant) if discriminant >= 0 else ''])
                witnesses[witness] = witnesses.get(witness, 0) + 1
                pair_count += 1
                noninteger_count += witness != 'integer_spectrum'
                vertex_count = minimum + middle + maximum + minimum * middle + minimum * maximum + middle * maximum
                original_values = [horner(coefficients, argument) for argument in (1, 2, 3)]
                complement_values = [-horner(coefficients, vertex_count - argument) for argument in (1, 2, 3)]
                for name, values in (('g_B', original_values), ('h_C', complement_values)):
                    pattern = ''.join(sign_char(value) for value in values)
                    if pattern not in patterns[name]:
                        patterns[name][pattern] = {'count': 0, 'first_example': [minimum, middle, maximum],
                                                   'endpoint_values': values}
                    patterns[name][pattern]['count'] += 1
                record_digest.update(json.dumps([minimum, middle, maximum, coefficients, witness,
                                                 original_values, complement_values], separators=(',', ':')).encode())
        expected_count = (cutoff - minimum - 1) * (cutoff - minimum - 2) // 2
        assert pair_count == expected_count
        representatives = {(minimum, minimum + 1, minimum + 2), (minimum, cutoff - 2, cutoff - 1)}
        representatives.update(tuple(value['first_example']) for value in patterns['h_C'].values())
        for exponents in sorted(representatives):
            matrix = quotient_matrix(*exponents)
            assert matrix == support_quotient(exponents)
            polynomial = quintic(matrix)
            coefficients = specialize(*exponents)
            assert polynomial == Poly.from_list(coefficients, x, domain='ZZ')
            reflected = quintic(support_quotient(exponents, complement=True))
            vertex_count = sum(exponents) + sum(exponents[index] * exponents[other]
                                               for index in range(3) for other in range(index + 1, 3))
            assert all(reflected.eval(argument) == -horner(coefficients, vertex_count - argument)
                       for argument in (1, 2, 3))
            factors = polynomial.factor_list()[1]
            assert any(factor.degree() >= 2 for factor, multiplicity in factors)
            independent_cases.append({'exponents': exponents, 'matrix_charpoly_reflection_and_factorization': 'passed'})
        record = {'a': minimum, 'c_cutoff_exclusive': cutoff, 'pairs': pair_count,
                  'with_noninteger_root': noninteger_count, 'witness_counts': witnesses,
                  'sign_patterns': patterns}
        records.append(record)
        if not arguments.json:
            print(f'\na={minimum}, c<{cutoff}, pairs={pair_count}, with noninteger root={noninteger_count}', flush=True)
            print('  exact witness counts:', witnesses, flush=True)
            for name in ('g_B', 'h_C'):
                for pattern, value in sorted(patterns[name].items(), key=lambda item: (-item[1]['count'], item[0])):
                    print(f"  {name}(1,2,3)={pattern}: {value['count']}; first example={tuple(value['first_example'])}", flush=True)
    if certificate_stream:
        certificate_stream.close()
    result = {'requested_a_max': arguments.a_max, 'total_pairs': sum(record['pairs'] for record in records),
              'total_with_noninteger_root': sum(record['with_noninteger_root'] for record in records),
              'general_matrix_and_complement_reflection_identities': 'passed',
              'exact_specialization': 'Generic H quotient determinant once; integer coefficient specialization for every requested triple; discriminant nonsquare or exact rational factorization witness.',
              'cases': records, 'independent_matrix_cases': independent_cases,
              'ordered_case_records_sha256': record_digest.hexdigest(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Finite diagnostic in the stated requested region only. H and complement signs are distinct. Different endpoint patterns do not preclude a uniform proof. No floating-point spectra or Lean.'}
    if arguments.certificate_csv:
        result['discriminant_certificate'] = str(arguments.certificate_csv)
        result['discriminant_certificate_sha256'] = hashlib.sha256(arguments.certificate_csv.read_bytes()).hexdigest()
    if arguments.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"\nTotal: {result['total_with_noninteger_root']}/{result['total_pairs']} have noninteger quotient roots.", flush=True)
        print(f"Independent matrix/charpoly/reflection/factorization representatives: {len(independent_cases)}.", flush=True)
        print('This finite run is not an all-exponent proof; nonuniform signs do not force a case-by-case proof.', flush=True)


if __name__ == "__main__":
    main()
