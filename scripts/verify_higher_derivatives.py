from collections import Counter
import hashlib
from itertools import combinations, permutations, product
import json
from math import factorial
from pathlib import Path

import sympy

from check_higher_derivatives import a, b, c, x, build_h_C_derivatives, is_mixed_parity


exponents = (a, b, c)
shifts = sympy.symbols('u v w')
argument = sympy.Symbol('y')
lift = sympy.Symbol('z')


def direct_matrix(triple):
    left, middle, right = triple
    return [
        [middle + right + middle * right, -middle, -right, 0, 0, -middle * right],
        [-left, left + right + left * right, -right, 0, -left * right, 0],
        [-left, -middle, left + middle + left * middle, -left * middle, 0, 0],
        [0, 0, -right, right, 0, 0],
        [0, -middle, 0, 0, middle, 0],
        [-left, 0, 0, 0, 0, left],
    ]


def integer_determinant(matrix):
    work = [row[:] for row in matrix]
    previous = sign = 1
    for pivot_index in range(len(work) - 1):
        if not work[pivot_index][pivot_index]:
            replacement = next((row for row in range(pivot_index + 1, len(work))
                                if work[row][pivot_index]), None)
            if replacement is None:
                return 0
            work[pivot_index], work[replacement] = work[replacement], work[pivot_index]
            sign = -sign
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, len(work)):
            for column in range(pivot_index + 1, len(work)):
                numerator = work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column]
                assert numerator % previous == 0
                work[row][column] = numerator // previous
            work[row][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


def independent_derivatives(triple, endpoint):
    matrix = direct_matrix(triple)
    shifted = [[endpoint * int(row == column) - matrix[row][column]
                for column in range(6)] for row in range(6)]
    values = []
    for order in range(4):
        derivative = factorial(order) * sum(integer_determinant([
            [shifted[row][column] for column in remaining] for row in remaining])
            for remaining in combinations(range(6), 6 - order))
        numerator = derivative - (order * values[-1] if order else 0)
        assert numerator % endpoint == 0
        values.append(numerator // endpoint)
    return values


def valuation(value):
    if value == 0:
        return None
    absolute = abs(value)
    return (absolute & -absolute).bit_length() - 1


def reduced(expression, generators, modulus):
    polynomial = sympy.Poly(sympy.expand(expression), *generators, domain=sympy.ZZ)
    return sympy.expand(sum((int(coefficient) % modulus) * sympy.prod(
        generator ** power for generator, power in zip(generators, monomial))
        for monomial, coefficient in polynomial.terms()))


derivatives = build_h_C_derivatives(3)
direct = sympy.cancel(sympy.Matrix(direct_matrix(exponents)).charpoly(x).as_expr() / x)
assert sympy.expand(derivatives[0] - direct) == 0
for order, expression in enumerate(derivatives):
    assert sympy.expand(expression - sympy.diff(direct, x, order)) == 0
    for ordering in permutations(exponents):
        assert sympy.expand(expression.subs(dict(zip(exponents, ordering)), simultaneous=True) - expression) == 0
evaluators = [sympy.lambdify((*exponents, x), expression, modules='math') for expression in derivatives]
assert evaluators[0](9, 9, 136, 1) == 0

root_rows = []
for residues in ((1, 0, 0), (1, 0, 2), (1, 2, 2), (3, 0, 0), (3, 0, 2), (3, 2, 2),
                 (1, 1, 0), (1, 1, 2), (1, 3, 0), (1, 3, 2), (3, 3, 0), (3, 3, 2)):
    substituted = derivatives[0].subs(dict(zip(exponents, (4 * shift + residue
                                                          for shift, residue in zip(shifts, residues)))))
    shifted = sympy.Poly(sympy.expand(substituted.subs(x, 2 * argument + 1)),
                         *shifts, argument, domain=sympy.ZZ)
    assert all(int(coefficient) % 8 == 0 for coefficient in shifted.coeffs())
    binary = reduced(shifted.as_expr() / 8, (*shifts, argument), 2)
    assert not binary.free_symbols.intersection(set(shifts))
    multiplicity = next(count for count in range(4) if sympy.Poly(binary, argument, modulus=2)
                        == sympy.Poly(argument ** count * (argument + 1) ** (3 - count), argument, modulus=2))
    root_rows.append({'exponent_residues_modulo_four': residues, 'shifted_polynomial_modulo_two': str(binary),
                     'odd_roots_one_modulo_four': multiplicity,
                     'coefficients_checked': len(shifted.terms())})
root_counts = {tuple(sorted(row['exponent_residues_modulo_four'])): row['odd_roots_one_modulo_four']
               for row in root_rows}

period_checks = []
for endpoint in (1, 3):
    for order, modulus in ((1, 16), (2, 8), (3, 4)):
        for parity in ((1, 0, 0), (1, 1, 0)):
            substituted = derivatives[order].subs(x, endpoint).subs(dict(zip(
                exponents, (2 * shift + bit for shift, bit in zip(shifts, parity)))))
            for coordinate in shifts:
                difference = sympy.Poly(sympy.expand(substituted.subs(coordinate, coordinate + 4 * lift) - substituted),
                                        *shifts, lift, domain=sympy.ZZ)
                assert all(int(coefficient) % modulus == 0 for coefficient in difference.coeffs())
                period_checks.append({'endpoint': endpoint, 'order': order, 'modulus': modulus, 'parity': parity,
                                      'coordinate': str(coordinate), 'coefficients_checked': len(difference.terms())})
    for parity in ((1, 0, 0), (1, 1, 0)):
        substituted = derivatives[3].subs(x, endpoint).subs(dict(zip(
            exponents, (2 * shift + bit for shift, bit in zip(shifts, parity)))))
        assert reduced(substituted, shifts, 4) == 2

representatives = []
distributions = [Counter() for order in range(4)]
joint = Counter()
derivative_failures = [set() for order in range(4)]
prior_exclusions = set()
for triple in product(range(8), repeat=3):
    if not is_mixed_parity(*triple):
        continue
    values = [int(evaluator(*triple, 1)) for evaluator in evaluators]
    assert values == independent_derivatives(triple, 1)
    valuations = [valuation(value) for value in values]
    labels = tuple('infinity' if value is None else str(value) for value in valuations)
    for distribution, label in zip(distributions, labels):
        distribution[label] += 1
    joint[labels] += 1
    multiplicity = root_counts[tuple(sorted(coordinate % 4 for coordinate in triple))]
    if (values[0] % 32 and int(evaluators[0](*triple, 3)) % 32) or sorted(
            coordinate % 4 for coordinate in triple) == [2, 3, 3]:
        prior_exclusions.add(triple)
    for endpoint, count in ((1, multiplicity), (3, 3 - multiplicity)):
        powers = (3 + count, max(2, count + 1), max(2, count), 1)
        for order in range(1, 4):
            if int(evaluators[order](*triple, endpoint)) % 2 ** powers[order]:
                derivative_failures[order].add(triple)
    representatives.append([*triple, *values, *valuations, multiplicity])
assert len(representatives) == 384
assert [len(derivative_failures[order]) for order in range(1, 4)] == [36, 0, 0]
assert len(prior_exclusions) == 48
assert derivative_failures[1] <= prior_exclusions
low_count = sum(row[3] != 0 and valuation(row[3]) < 6 for row in representatives)
assert low_count == 243

substituted = derivatives[0].subs(dict(zip(exponents, (4 * shifts[0] + 1, 4 * shifts[1] + 3, 4 * shifts[2] + 2))))
endpoint_polynomial = sympy.Poly(sympy.expand(substituted.subs(x, 3)), *shifts, domain=sympy.ZZ)
assert all(int(coefficient) % 16 == 0 for coefficient in endpoint_polynomial.coeffs())
target = (2 * shifts[1] + 1) * (shifts[0] + shifts[2] + 1)
difference = sympy.Poly(sympy.expand(endpoint_polynomial.as_expr() / 16 - target), *shifts, domain=sympy.ZZ)
assert all(int(coefficient) % 4 == 0 for coefficient in difference.coeffs())
target_rows = []
for triple in product(range(1, 16, 4), range(3, 16, 4), range(2, 16, 4)):
    value = int(evaluators[0](*triple, 3)) % 64
    assert (value == 0) == ((triple[0] + triple[2]) % 16 == 15)
    target_rows.append([*triple, value])
assert sum(row[-1] != 0 for row in target_rows) == 48
assert sum(int(evaluators[0](*row[:3], 1)) % 32 != 0 and row[-1] % 32 != 0
           for row in target_rows) == 32

fixtures = []
for triple in ((14, 25, 27), (10, 29, 31)):
    odd_one = next(coordinate for coordinate in triple if coordinate % 4 == 1)
    even = next(coordinate for coordinate in triple if coordinate % 4 == 2)
    assert (odd_one + even) % 16 == 7
    values = [int(evaluator(*triple, 3)) for evaluator in evaluators]
    assert values == independent_derivatives(triple, 3)
    assert values[0] % 32 == 0 and values[0] % 64 == 32
    polynomial = sympy.Poly(direct.subs(dict(zip(exponents, triple))), x)
    assert any(factor.degree() > 1 for factor, multiplicity in polynomial.factor_list()[1])
    fixtures.append({'exponents': triple, 'h_and_first_three_derivatives_at_three': values,
                     'h_three_modulo_64': values[0] % 64, 'nonlinear_rational_factor': True})

lift_controls = []
for triple in ((0, 0, 1), (8, 16, 9), (1, 3, 6), (9, 3, 6)):
    values = [int(evaluator(*triple, 1)) for evaluator in evaluators]
    assert values == independent_derivatives(triple, 1)
    lift_controls.append({'exponents': triple, 'values_at_one': values,
                          'valuations': [valuation(value) for value in values],
                          'h_three': int(evaluators[0](*triple, 3))})

result = {
    'original_source_commit': 'a0f544953ad4de3b3c8758d357493c078056f370',
    'script_sha256': hashlib.sha256(Path(__file__).with_name('check_higher_derivatives.py').read_bytes()).hexdigest(),
    'verifier_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'sympy': sympy.__version__,
    'generic_direct_reflection_and_derivatives': 'passed',
    'representative_valuation_distributions': [dict(sorted(counter.items())) for counter in distributions],
    'joint_representative_patterns': [{'valuations': labels, 'count': count} for labels, count in sorted(joint.items())],
    'valuation_of_zero': 'infinity, encoded as null in numeric rows; not99',
    'representative_rows_columns': ['a', 'b', 'c', 'h1', 'hprime1', 'hsecond1', 'hthird1',
                                    'v2_h1', 'v2_hprime1', 'v2_hsecond1', 'v2_hthird1', 'odd_roots_one_modulo_four'],
    'representative_rows': '__ROWS__', 'representatives_below_valuation_six': low_count,
    'uniform_odd_root_distributions': root_rows,
    'written_threshold_powers_at_one': ['3+k', 'max(2,k+1)', 'max(2,k)', '1'],
    'derivative_coordinate_period_eight_checks': period_checks,
    'first_second_third_derivative_failure_counts_at_one_or_three': [36, 0, 0],
    'third_derivative_modulo_four_all_mixed_parities': 2,
    'new_written_family': 'a=1,b=3,c=2mod4 and a+c!=15mod16, with all permutations, is nonintegral.',
    'coefficientwise_endpoint_identity': 'h_C(3)/16=(2v+1)(u+w+1)mod4 for exponents(4u+1,4v+3,4w+2)',
    'endpoint_identity_coefficients_checked': len(difference.terms()),
    'targeted_modulo_sixteen_rows': target_rows,
    'targeted_modulo_sixteen_exclusions': 48,
    'additional_role_ordered_exclusions_beyond_previous_modulo_eight_classes': 16,
    'fixtures': fixtures, 'noninvariant_valuation_lift_controls': lift_controls,
    'independent_principal_minor_determinants': (384 + 2 + 4) * 42,
    'scope': 'Written conditional derivative divisibilities and new infinite-family necessary sum congruence. All384requested representatives checked via exact principal minors, with full values and distributions saved. Thirtysix symbolic derivative-period identities and twelve mod4root-distribution identities. Sixtyfour derived role-ordered mod16classes encode the new theorem; no added exponent range or unconstrained modulus scan. Second/third derivative thresholds give no further exclusions at the current mod4root information. Full valuations of representatives are not uniform class data. No Lean or numerical spectrum; fullQ3 remains open.'
}
payload = json.dumps(result, indent=2)
rows = '[\n' + ',\n'.join('    ' + json.dumps(row) for row in representatives) + '\n  ]'
print(payload.replace('"__ROWS__"', rows))
