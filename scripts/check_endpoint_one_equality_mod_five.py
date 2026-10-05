import hashlib
import json
from itertools import combinations_with_replacement, permutations
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def multiply_mod(first, second, prime):
    coefficients = [0] * (len(first) + len(second) - 1)
    for first_index, first_value in enumerate(first):
        for second_index, second_value in enumerate(second):
            coefficients[first_index + second_index] += first_value * second_value
    return tuple(value % prime for value in coefficients)


def integer_determinant(matrix):
    total = 0
    for ordering in permutations(range(len(matrix))):
        inversions = sum(ordering[first_index] > ordering[second_index]
                         for first_index in range(len(matrix))
                         for second_index in range(first_index + 1, len(matrix)))
        term = -1 if inversions % 2 else 1
        for row, column in enumerate(ordering):
            term *= matrix[row][column]
        total += term
    return total


def independent_matrix(exponents):
    first, middle, last = exponents
    return [[middle + last + middle * last, -middle, -last, 0, 0, -middle * last],
            [-first, first + last + first * last, -last, 0, -first * last, 0],
            [-first, -middle, first + middle + first * middle, -first * middle, 0, 0],
            [0, 0, -last, last, 0, 0],
            [0, -middle, 0, 0, middle, 0],
            [-first, 0, 0, 0, 0, first]]


def determinant_at(matrix, value):
    shifted = [[value * (row == column) - entry for column, entry in enumerate(entries)]
               for row, entries in enumerate(matrix)]
    return integer_determinant(shifted)


def certificate():
    first, middle, last, product, variable = sympy.symbols('a b c q x')
    quotient = support_quotient((first, middle, last), complement=True)
    quintic = sympy.Poly(sympy.cancel(quotient.charpoly(variable).as_expr() / variable), variable)
    for ordering in permutations((first, middle, last)):
        substituted = quintic.as_expr().subs(dict(zip((first, middle, last), ordering)), simultaneous=True)
        assert sympy.expand(substituted - quintic.as_expr()) == 0
    total = middle * (middle + 2)
    curve = ((3 * middle - 1) * product ** 2
             + middle * (middle ** 2 + 4 * middle - 1) * product
             - (middle ** 2 + 2 * middle - 1) * (middle ** 2 + 3 * middle - 1)
             * (middle ** 3 + 3 * middle ** 2 + 3 * middle - 1))
    alpha = product + middle ** 3 + 5 * middle ** 2 + 8 * middle - 1
    beta = (product * middle * (middle ** 2 + 5 * middle + 5)
            + 2 * middle ** 5 + 12 * middle ** 4 + 25 * middle ** 3
            + 16 * middle ** 2 - 8 * middle + 1)
    constant = product * middle * (middle + 3) * (product + middle * (middle ** 2 + 3 * middle + 3))
    cubic = variable ** 3 - alpha * variable ** 2 + beta * variable - constant
    equality_quintic = quintic.as_expr().subs(last, total - first)
    expected = ((variable - 1) * (variable - middle) * cubic
                + variable * (variable - middle) * curve).subs(product, first * (total - first))
    assert sympy.expand(equality_quintic - expected) == 0
    discriminant = sympy.discriminant(cubic, variable)
    residue_tables = {}
    determinant_checks = 0
    for prime in (3, 5):
        split_cubics = set()
        for roots in combinations_with_replacement(range(prime), 3):
            coefficients = (1,)
            for root in roots:
                coefficients = multiply_mod(coefficients, (1, -root), prime)
            split_cubics.add(coefficients)
        assert len(split_cubics) == (10 if prime == 3 else 35)
        rows = []
        square_values = {value * value % prime for value in range(prime)}
        for first_value in range(prime):
            for middle_value in range(prime):
                last_value = (middle_value * (middle_value + 2) - first_value) % prime
                substitutions = {first: first_value, middle: middle_value,
                                 product: first_value * last_value}
                curve_value = int(curve.subs(substitutions)) % prime
                determinant = determinant_at(independent_matrix((first_value, middle_value, last_value)), 1)
                assert determinant % prime == (1 - middle_value) * curve_value % prime
                determinant_checks += 1
                if curve_value:
                    continue
                polynomial = sympy.Poly(cubic.subs(substitutions), variable, modulus=prime)
                coefficients = tuple(int(value) % prime for value in polynomial.all_coeffs())
                factorization = sympy.factor_list(polynomial.as_expr(), variable, modulus=prime)
                routine_splits = all(sympy.degree(factor, variable) == 1 for factor, multiplicity in factorization[1])
                assert routine_splits == (coefficients in split_cubics)
                discr = int(discriminant.subs(substitutions)) % prime
                roots = [candidate for candidate in range(prime) if int(polynomial.eval(candidate)) % prime == 0]
                rows.append({'a': first_value, 'b': middle_value, 'c': last_value,
                             'cubic_coefficients_descending': coefficients,
                             'discriminant': discr, 'discriminant_is_square': discr in square_values,
                             'distinct_roots': roots, 'splits_completely': routine_splits,
                             'factorization': str(sympy.factor(polynomial.as_expr(), modulus=prime))})
        residue_tables[str(prime)] = {'pairs_checked': prime ** 2, 'curve_zero_rows': rows,
                                     'split_rows': [[row['a'], row['b']] for row in rows if row['splits_completely']]}
    assert residue_tables['3']['split_rows'] == [[row['a'], row['b']] for row in residue_tables['3']['curve_zero_rows']]
    assert residue_tables['5']['split_rows'] == [[0, 2], [1, 0], [2, 0], [3, 0], [3, 2], [4, 0]]
    nonsplit_square = [row for row in residue_tables['5']['curve_zero_rows']
                      if row['discriminant_is_square'] and not row['splits_completely']]
    assert len(nonsplit_square) == 1 and (nonsplit_square[0]['a'], nonsplit_square[0]['b']) == (4, 1)
    first_factor = (variable - 1) ** 2 * (variable - 3) * (variable ** 2 + 3 * variable + 4)
    second_cubic = variable ** 3 + variable ** 2 + 4 * variable + 3
    second_factor = (variable - 1) ** 2 * second_cubic
    assert [int(second_cubic.subs(variable, value)) % 5 for value in range(5)] == [3, 4, 3, 1, 4]
    assert sympy.discriminant(second_cubic, variable) % 5 == 1
    assert (3 ** 2 - 4 * 4) % 5 == 3
    global_classes = []
    for residues, factor in [((1, 1, 2), first_factor), ((1, 4, 4), second_factor)]:
        for ordering in sorted(set(permutations(residues))):
            specialized = quintic.as_expr().subs(dict(zip((first, middle, last), ordering)))
            assert sympy.Poly(specialized - factor, variable, modulus=5).is_zero
        matrix = independent_matrix(residues)
        direct = support_quotient(residues, complement=True)
        assert direct == sympy.Matrix(matrix)
        characteristic = direct.charpoly(variable).as_expr()
        for value in range(7):
            assert determinant_at(matrix, value) == int(characteristic.subs(variable, value))
            determinant_checks += 1
        global_classes.append({'residues_mod_5': residues, 'quintic_factorization_mod_5': str(factor),
                               'all_distinct_permutations_checked': 3})
    fixtures = []
    for exponents in [(9, 16, 19), (11, 16, 22), (14, 21, 469), (26, 41, 1737), (9, 9, 136)]:
        matrix = independent_matrix(exponents)
        direct = support_quotient(exponents, complement=True)
        assert direct == sympy.Matrix(matrix)
        characteristic = direct.charpoly(variable).as_expr()
        for value in range(7):
            assert determinant_at(matrix, value) == int(characteristic.subs(variable, value))
            determinant_checks += 1
        expected_factor = first_factor if sorted(value % 5 for value in exponents) == [1, 1, 2] else second_factor
        assert sympy.Poly(characteristic - variable * expected_factor, variable, modulus=5).is_zero
        fixtures.append({'exponents': exponents, 'E': exponents[0] + exponents[2] - exponents[1] * (exponents[1] + 2),
                         'h_C_at_1': int(characteristic.subs(variable, 1)),
                         'quintic_coefficients_descending': [int(value) for value in sympy.Poly(characteristic / variable, variable).all_coeffs()]})
    prior = Path(__file__).resolve().parents[1] / 'results/endpoint-one-equality-cubic.json'
    return {'global_result': 'Every positive triple that is a permutation of (1,1,2) or (1,4,4) modulo5 is Laplacian nonintegral.',
            'global_classes': global_classes, 'generic_equality_identity_verified': True,
            'generic_six_permutations_verified': True, 'equality_residue_tables': residue_tables,
            'square_discriminant_nonsplit_curve_row': nonsplit_square[0],
            'irreducible_cubic_values_mod_5': [3, 4, 3, 1, 4], 'irreducible_quadratic_discriminant_mod_5': 3,
            'independent_integer_determinants': determinant_checks, 'direct_fixtures': fixtures,
            'prior_cubic_certificate_sha256': hashlib.sha256(prior.read_bytes()).hexdigest(),
            'source_sha256': {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                              for path in (Path(__file__), Path(__file__).with_name('check_six_support_quotient.py'))},
            'sympy': sympy.__version__,
            'scope': 'Written global modulo-five splitting obstruction and exact complete equality-residue tables at fixed primes3and5. 34residue pairs, separate root-multiset/routine splitting checks, 83independent720term integer determinants, five fixed controls. No exponent-range search, higher two-adic lift, integer equality-point enumeration, finite exponent base, rank or Lean. Equality integer feasibility/globalQ3 remain open.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
