import hashlib
from itertools import permutations, product
import json
from pathlib import Path

import sympy

from check_higher_derivatives import a, b, c, x, build_h_C_derivatives
from check_six_support_quotient import support_quotient


exponents = (a, b, c)
left_shift, odd_shift, sum_shift, argument = sympy.symbols('u v t z')
quintic = sympy.Poly(sympy.cancel(
    support_quotient(exponents, complement=True).charpoly(x).as_expr() / x), x)
assert sympy.expand(quintic.as_expr() - build_h_C_derivatives(0)[0]) == 0
for ordering in permutations(exponents):
    assert sympy.expand(quintic.as_expr().subs(dict(zip(exponents, ordering)), simultaneous=True)
                        - quintic.as_expr()) == 0

role_exponents = (4 * left_shift + 1, 4 * odd_shift + 3, 16 * sum_shift - 4 * left_shift - 2)
shifted = sympy.Poly(sympy.expand(quintic.as_expr().subs(dict(zip(exponents, role_exponents)))
                                  .subs(x, 4 * argument + 3)),
                     left_shift, odd_shift, sum_shift, argument, domain=sympy.ZZ)
assert all(int(coefficient) % 64 == 0 for coefficient in shifted.coeffs())
expected = argument ** 3 + odd_shift * argument ** 2 + odd_shift * argument + sum_shift + 1
difference = sympy.Poly(sympy.expand(shifted.as_expr() / 64 - expected),
                        left_shift, odd_shift, sum_shift, argument, domain=sympy.ZZ)
assert all(int(coefficient) % 2 == 0 for coefficient in difference.coeffs())
assert sympy.expand(role_exponents[0] + role_exponents[2] + 4 * role_exponents[1]
                    - (16 * (sum_shift + odd_shift) + 11)) == 0

binary_patterns = []
for bits in product(range(2), repeat=3):
    polynomial = sympy.Poly(expected.subs(dict(zip(
        (left_shift, odd_shift, sum_shift), bits))), argument, modulus=2)
    factors = polynomial.factor_list()[1]
    splits = all(factor.degree() == 1 for factor, multiplicity in factors)
    assert splits == ((bits[1] + bits[2]) % 2 == 1)
    if splits:
        residue = 0 if bits[1] == 0 else 1
        assert polynomial == sympy.Poly((argument - residue) ** 3, argument, modulus=2)
    else:
        assert any(factor == sympy.Poly(argument ** 2 + argument + 1, argument, modulus=2)
                   for factor, multiplicity in factors)
    binary_patterns.append({'shift_parities_u_v_t': bits, 'polynomial': str(polynomial.as_expr()),
                            'factorization': str(sympy.factor(polynomial.as_expr(), modulus=2)),
                            'splits_over_binary_field': splits,
                            'hypothetical_odd_roots_modulo_eight': 4 * bits[1] + 3 if splits else None})


def independent_matrix(triple):
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
    total = 0
    size = len(matrix)
    for ordering in permutations(range(size)):
        inversions = sum(ordering[left_index] > ordering[right_index]
                         for left_index in range(size) for right_index in range(left_index + 1, size))
        term = (-1) ** inversions
        for row, column in enumerate(ordering):
            term *= matrix[row][column]
        total += term
    return total


fixtures = []
for triple, excluded in (((13, 19, 18), True), ((9, 31, 38), True),
                         ((9, 23, 22), False), ((17, 27, 30), False)):
    matrix = independent_matrix(triple)
    assert sympy.Matrix(matrix) == support_quotient(triple, complement=True)
    assert integer_determinant(matrix) == 0
    values = []
    for value in range(1, 7):
        determinant = integer_determinant([[value * int(row == column) - matrix[row][column]
                                           for column in range(6)] for row in range(6)])
        assert determinant % value == 0
        values.append((value, determinant // value))
    independent = sympy.Poly(sympy.interpolate(values, x), x, domain=sympy.ZZ)
    assert independent == sympy.Poly(quintic.as_expr().subs(dict(zip(exponents, triple))), x)
    assert (triple[0] + triple[2]) % 16 == 15
    assert int(independent.eval(3)) % 64 == 0
    binary = sympy.Poly(sympy.expand(independent.as_expr().subs(x, 4 * argument + 3) / 64),
                        argument, domain=sympy.ZZ)
    split = all(factor.degree() == 1 for factor, multiplicity in
                sympy.Poly(binary.as_expr(), argument, modulus=2).factor_list()[1])
    assert split != excluded
    assert excluded == ((triple[0] + triple[2] + 4 * triple[1]) % 32 != 27)
    assert any(factor.degree() > 1 for factor, multiplicity in independent.factor_list()[1])
    fixtures.append({'residue_role_exponents_a_b_c': triple,
                     'ordered_exponents': sorted(triple),
                     'independent_coefficients': [int(coefficient) for coefficient in independent.all_coeffs()],
                     'integer_determinant_interpolation_points': values,
                     'old_sum_modulo_sixteen': (triple[0] + triple[2]) % 16,
                     'new_weighted_sum_modulo_thirty_two': (triple[0] + triple[2] + 4 * triple[1]) % 32,
                     'h_at_three': int(independent.eval(3)),
                     'shifted_binary_polynomial': str(sympy.Poly(binary.as_expr(), argument, modulus=2).as_expr()),
                     'excluded_by_new_theorem': excluded,
                     'nonlinear_rational_factor': True})

print(json.dumps({
    'base_commit': 'dd9e7a7dc03e21e1335a6aa2b2517c77f797a077',
    'written_theorem': 'For positive residue roles a=1,b=3,c=2mod4, integer spectrum requires a+c+4b=27mod32, with all permutations and no size/ratio bound.',
    'generic_direct_reflected_quintic_and_six_symmetry_checks': 'passed',
    'integer_scaled_shift': {'substitution': '(a,b,c)=(4u+1,4v+3,16t-4u-2),x=4z+3',
                             'divisor': 64, 'coefficients_checked': len(shifted.terms()),
                             'all_coefficients_divisible': True},
    'coefficientwise_binary_identity': {'expected': str(expected),
                                        'difference_coefficients_checked': len(difference.terms()),
                                        'all_difference_coefficients_even': True},
    'binary_patterns': binary_patterns,
    'derived_modulo_thirty_two_counts': {'role_ordered_classes': 512,
                                         'excluded_by_prior_sum_modulo_sixteen': 384,
                                         'surviving_prior_sum': 128,
                                         'additional_exclusions': 64,
                                         'additional_exclusions_after_all_permutations': 384,
                                         'remaining_compatible_classes': 64,
                                         'basis': 'Eight residues per role; prior sum removes three of four sums, then parity t+v removes half of the survivors. Counts follow algebra, not a scan.'},
    'survivor_root_information': 'If roots are integers, all three odd roots are bmod8; hence512dividesh(b). Compatibility is not integrality.',
    'fixtures': fixtures, 'independent_six_by_six_integer_determinants': 28,
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy': sympy.__version__,
    'scope': 'Written infinite-family obstruction by a non-splitting binary cubic. Arbitrary-shift coefficient identities, eight shift-parity specializations and four independent integer interpolation fixtures. No expanded exponent-range or modulus scan, numerical spectrum or Lean. FullQ3 and higher-prime nonsquarefree vectors remain open.'
}, indent=2))
