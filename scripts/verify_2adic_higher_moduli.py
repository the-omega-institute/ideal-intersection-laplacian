import hashlib
from itertools import product
import json
from pathlib import Path

import sympy

from check_2adic_higher_moduli import a, b, c, x, h_C_at, is_mixed_parity


exponents = (a, b, c)
shifts = sympy.symbols('u v w')
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
    size = len(work)
    previous = 1
    sign = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            replacement = next((row for row in range(pivot_index + 1, size)
                                if work[row][pivot_index]), None)
            if replacement is None:
                return 0
            work[pivot_index], work[replacement] = work[replacement], work[pivot_index]
            sign = -sign
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column]
                assert numerator % previous == 0
                work[row][column] = numerator // previous
            work[row][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


direct = sympy.Poly(sympy.cancel(sympy.Matrix(direct_matrix(exponents)).charpoly(x).as_expr() / x), x)
endpoints = [h_C_at(value) for value in (1, 3)]
for value, expression in zip((1, 3), endpoints):
    assert sympy.expand(expression - direct.eval(value)) == 0
    for ordering in ((b, a, c), (a, c, b)):
        assert sympy.expand(expression.subs(dict(zip(exponents, ordering)), simultaneous=True) - expression) == 0
evaluators = [sympy.lambdify(exponents, expression, modules='math') for expression in endpoints]
assert evaluators[0](9, 9, 136) == 0

period_checks = []
for value, expression in zip((1, 3), endpoints):
    for parity in ((1, 0, 0), (1, 1, 0)):
        substituted = sympy.expand(expression.subs(dict(zip(
            exponents, (2 * shift + bit for shift, bit in zip(shifts, parity))))))
        for index in range(3):
            difference = sympy.Poly(sympy.expand(
                substituted.subs(shifts[index], shifts[index] + 4 * lift) - substituted), *shifts, lift)
            assert all(int(coefficient) % 32 == 0 for coefficient in difference.coeffs())
            period_checks.append({'endpoint': value, 'parity': parity, 'coordinate': index,
                                  'coefficient_count': len(difference.terms()),
                                  'all_coefficients_divisible_by_32': True})


def new_family(triple):
    return sorted(value % 4 for value in triple) == [2, 3, 3]


base_rows = []
counts = []
determinants = 0
for modulus in (8, 16, 32):
    mixed = excluded = combined = 0
    for triple in product(range(modulus), repeat=3):
        if not is_mixed_parity(*triple):
            continue
        mixed += 1
        values = tuple(int(evaluator(*triple)) % 32 for evaluator in evaluators)
        matrix = direct_matrix(triple)
        for value, expected in zip((1, 3), values):
            shifted = [[value * int(row == column) - matrix[row][column]
                        for column in range(6)] for row in range(6)]
            determinant = integer_determinant(shifted)
            assert determinant % value == 0
            assert (determinant // value) % 32 == expected
            determinants += 1
        base = tuple(coordinate % 8 for coordinate in triple)
        assert values == tuple(int(evaluator(*base)) % 32 for evaluator in evaluators)
        endpoint_excluded = all(values)
        excluded += int(endpoint_excluded)
        combined += int(endpoint_excluded or new_family(triple))
        if modulus == 8:
            base_rows.append({'exponent_residues': triple, 'h_one_modulo_32': values[0],
                              'h_three_modulo_32': values[1], 'endpoint_divisor_excluded': bool(endpoint_excluded),
                              'new_modulo_four_family': new_family(triple)})
    assert (mixed, excluded) == {8: (384, 36), 16: (3072, 288), 32: (24576, 2304)}[modulus]
    assert combined == {8: 48, 16: 384, 32: 3072}[modulus]
    counts.append({'modulus': modulus, 'mixed_ordered_classes': mixed,
                   'endpoint_divisor_exclusions': excluded, 'endpoint_divisor_survivors': mixed - excluded,
                   'combined_with_written_modulo_four_theorem_exclusions': combined,
                   'combined_survivors': mixed - combined})

excluded_rows = [row for row in base_rows if row['endpoint_divisor_excluded']]
unordered = sorted({tuple(sorted(row['exponent_residues'])) for row in excluded_rows})
assert unordered == [(1, 2, 3), (1, 2, 7), (2, 3, 7), (3, 5, 6), (3, 6, 7), (5, 6, 7)]

print(json.dumps({
    'source_commit': '1539ca6bbde3dc0a6f886d878a855621cc81af40',
    'original_script_sha256': hashlib.sha256(Path(__file__).with_name('check_2adic_higher_moduli.py').read_bytes()).hexdigest(),
    'verifier_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy': sympy.__version__, 'generic_direct_complement_reflection': 'passed',
    'known_endpoint_one_control': {'exponents': [9, 9, 136], 'value': 0},
    'coefficientwise_period_eight_checks': period_checks,
    'period_check_coefficients': sum(row['coefficient_count'] for row in period_checks),
    'counts': counts,
    'base_modulo_eight_columns': ['a', 'b', 'c', 'h_one_modulo_32', 'h_three_modulo_32',
                                  'endpoint_divisor_excluded', 'new_modulo_four_family'],
    'base_modulo_eight_rows': [[*row['exponent_residues'], row['h_one_modulo_32'],
                               row['h_three_modulo_32'], row['endpoint_divisor_excluded'],
                               row['new_modulo_four_family']] for row in base_rows],
    'six_unordered_excluded_patterns_modulo_eight': unordered,
    'independent_integer_determinants': determinants,
    'interpretation': 'Both endpoint values modulo32 already have coordinate period8 on all mixed-parity triples. The M16/M32 tables are exact lifts and add no endpoint-divisor exclusions. The written (3,3,2)mod4 theorem adds12ordered exclusions at M8 via root distribution and derivative divisibility, not the endpoint-divisor test alone.',
    'scope': 'All28032ordered mixed residue triples at exactly the requested moduli8,16,32;56064independent integer Bareiss endpoint determinants. Twelve symbolic period identities covering all six mixed parity patterns by permutation symmetry. Full residue information encoded by384base rows and coordinate period8. No exponent scan, added modulus, numerical spectrum or Lean. Survivors are congruence compatibility, not integral spectra; fullQ3 remains open.'
}, indent=2))
