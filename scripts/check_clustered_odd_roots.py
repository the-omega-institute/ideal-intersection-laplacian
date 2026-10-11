import hashlib
from itertools import permutations, product
import json
from pathlib import Path

import sympy

from check_higher_derivatives import a, b, c, x, build_h_C_derivatives
from check_six_support_quotient import support_quotient


exponents = (a, b, c)
left_shift, odd_shift, total_shift, argument = sympy.symbols('u v t z')
quintic = sympy.Poly(sympy.cancel(
    support_quotient(exponents, complement=True).charpoly(x).as_expr() / x), x)
assert sympy.expand(quintic.as_expr() - build_h_C_derivatives(0)[0]) == 0
for ordering in permutations(exponents):
    assert sympy.expand(quintic.as_expr().subs(dict(zip(exponents, ordering)), simultaneous=True)
                        - quintic.as_expr()) == 0
value_factor = a ** 2 * b ** 2 * c ** 2 * (a + c - b * (b + 2))
assert sympy.expand(quintic.eval(b) - value_factor) == 0
derivative = quintic.diff().as_expr().subs(x, b)
odd_exponent = 4 * odd_shift + 3
role_exponents = (4 * left_shift + 1, odd_exponent,
                  odd_exponent * (odd_exponent + 2) + 128 * total_shift - 4 * left_shift - 1)
derivative_polynomial = sympy.Poly(sympy.expand(derivative.subs(
    dict(zip(exponents, role_exponents)), simultaneous=True)),
    left_shift, odd_shift, total_shift, domain=sympy.ZZ)
expected_derivative = 16 * (odd_shift ** 2 - odd_shift + 2)
derivative_difference = sympy.Poly(sympy.expand(derivative_polynomial.as_expr() - expected_derivative),
                                  left_shift, odd_shift, total_shift, domain=sympy.ZZ)
assert all(int(coefficient) % 64 == 0 for coefficient in derivative_difference.coeffs())
derivative_residue_rows = []
for residue in range(4):
    lifted = sympy.Poly(derivative_difference.as_expr().subs(odd_shift, 4 * odd_shift + residue)
                        + expected_derivative.subs(odd_shift, 4 * odd_shift + residue),
                        left_shift, odd_shift, total_shift, domain=sympy.ZZ)
    expected = 32 if residue in (0, 1) else 0
    assert all(int(coefficient) % 64 == 0 for coefficient in
               sympy.Poly(lifted.as_expr() - expected, left_shift, odd_shift, total_shift).coeffs())
    derivative_residue_rows.append({'v_modulo_four': residue,
                                    'b_modulo_sixteen': 4 * residue + 3,
                                    'derivative_modulo_sixty_four': expected})

shift_checks = []
binary_patterns = []
for odd_residue in (11, 15):
    odd_exponent = 16 * odd_shift + odd_residue
    role_exponents = (4 * left_shift + 1, odd_exponent,
                      odd_exponent * (odd_exponent + 2) + 128 * total_shift - 4 * left_shift - 1)
    shifted = sympy.Poly(sympy.expand(quintic.as_expr().subs(
        dict(zip(exponents, role_exponents)), simultaneous=True).subs(x, 8 * argument + odd_exponent)),
        left_shift, odd_shift, total_shift, argument, domain=sympy.ZZ)
    assert all(int(coefficient) % 512 == 0 for coefficient in shifted.coeffs())
    coefficient = 1 + odd_shift + (left_shift ** 2 if odd_residue == 11 else 0)
    expected = argument ** 3 + argument ** 2 + coefficient * argument + total_shift
    difference = sympy.Poly(sympy.expand(shifted.as_expr() / 512 - expected),
                            left_shift, odd_shift, total_shift, argument, domain=sympy.ZZ)
    assert all(int(value) % 2 == 0 for value in difference.coeffs())
    shift_checks.append({'b_residue_modulo_sixteen': odd_residue,
                         'substitution': str(role_exponents),
                         'scaled_integer_coefficients_checked': len(shifted.terms()),
                         'binary_identity': str(expected),
                         'binary_difference_coefficients_checked': len(difference.terms())})
    for bits in product(range(2), repeat=3):
        binary = sympy.Poly(expected.subs(dict(zip((left_shift, odd_shift, total_shift), bits))),
                            argument, modulus=2)
        splits = all(factor.degree() == 1 for factor, multiplicity in binary.factor_list()[1])
        assert splits == ((bits[2] + bits[1] + (bits[0] if odd_residue == 11 else 0)) % 2 == 1)
        binary_patterns.append({'b_residue_modulo_sixteen': odd_residue,
                                'shift_parities_u_v_t': bits,
                                'polynomial': str(binary.as_expr()),
                                'factorization': str(sympy.factor(binary.as_expr(), modulus=2)),
                                'splits_over_binary_field': splits})


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
for triple, expected_stage in (((13, 27, 34), 'value'), ((13, 19, 386), 'derivative'),
                               ((29, 27, 754), 'binary_cubic'), ((45, 47, 2258), 'binary_cubic'),
                               ((25, 27, 758), 'compatible'), ((29, 27, 882), 'compatible'),
                               ((29, 31, 994), 'compatible'), ((45, 47, 2386), 'compatible')):
    matrix = independent_matrix(triple)
    assert sympy.Matrix(matrix) == support_quotient(triple, complement=True)
    assert integer_determinant(matrix) == 0
    values = []
    for endpoint in range(1, 7):
        determinant = integer_determinant([[endpoint * int(row == column) - matrix[row][column]
                                           for column in range(6)] for row in range(6)])
        assert determinant % endpoint == 0
        values.append((endpoint, determinant // endpoint))
    independent = sympy.Poly(sympy.interpolate(values, x), x, domain=sympy.ZZ)
    assert independent == sympy.Poly(quintic.as_expr().subs(dict(zip(exponents, triple))), x)
    left, middle, right = triple
    endpoint_value = int(independent.eval(middle))
    endpoint_derivative = int(independent.diff().eval(middle))
    shifted_matrix = [[middle * int(row == column) - matrix[row][column]
                       for column in range(6)] for row in range(6)]
    determinant_derivative = sum(integer_determinant([
        [shifted_matrix[row][column] for column in range(6) if column != removed]
        for row in range(6) if row != removed]) for removed in range(6))
    assert determinant_derivative == endpoint_value + middle * endpoint_derivative
    assert endpoint_value == left ** 2 * middle ** 2 * right ** 2 * (left + right - middle * (middle + 2))
    assert (left + right + 4 * middle) % 32 == 27
    sum_remainder = (left + right - middle * (middle + 2)) % 128
    binary_expression = None
    if sum_remainder:
        stage = 'value'
        assert endpoint_value % 512 != 0
    elif middle % 16 not in (11, 15):
        stage = 'derivative'
        assert endpoint_value % 512 == 0 and endpoint_derivative % 64 == 32
    else:
        assert endpoint_value % 512 == 0 and endpoint_derivative % 64 == 0
        binary = sympy.Poly(sympy.expand(independent.as_expr().subs(x, 8 * argument + middle) / 512),
                            argument, domain=sympy.ZZ)
        binary = sympy.Poly(binary.as_expr(), argument, modulus=2)
        binary_expression = str(binary.as_expr())
        splits = all(factor.degree() == 1 for factor, multiplicity in binary.factor_list()[1])
        stage = 'compatible' if splits else 'binary_cubic'
    assert stage == expected_stage
    assert any(factor.degree() > 1 for factor, multiplicity in independent.factor_list()[1])
    fixtures.append({'residue_role_exponents_a_b_c': triple,
                     'independent_coefficients': [int(coefficient) for coefficient in independent.all_coeffs()],
                     'integer_determinant_interpolation_points': values,
                     'h_at_b': endpoint_value, 'h_prime_at_b': endpoint_derivative,
                     'independent_principal_cofactor_sum': determinant_derivative,
                     'prior_weighted_sum_modulo_thirty_two': 27,
                     'sum_difference_modulo_one_twenty_eight': sum_remainder,
                     'b_modulo_sixteen': middle % 16,
                     'binary_shifted_polynomial': binary_expression,
                     'new_obstruction_stage': stage,
                     'nonlinear_rational_factor': True})

print(json.dumps({
    'base_commit': '58e9a22c3bcaf7bb2b046c8f3664ca8b7cf48540',
    'written_theorem': 'For positive residue roles (1,3,2)mod4, integer spectrum requires a+c=b(b+2)mod128, b=11or15mod16, and the specified third-shift parity condition. All permutations; no size/ratio bound.',
    'generic_direct_reflected_quintic_and_six_symmetry_checks': 'passed',
    'exact_value_identity': str(value_factor),
    'derivative_identity': {'substitution': '(a,b,c)=(4u+1,4v+3,b(b+2)+128t-a)',
                            'expected_modulo_sixty_four': str(expected_derivative),
                            'difference_coefficients_checked': len(derivative_difference.terms())},
    'derivative_residue_rows': derivative_residue_rows,
    'third_shift_coefficient_checks': shift_checks,
    'binary_patterns': binary_patterns,
    'third_shift_conditions': {'b=16v+11': 't+u+v=1mod2', 'b=16v+15': 't+v=1mod2',
                               'parameters': 'a=4u+1,t=(a+c-b(b+2))/128'},
    'fixtures': fixtures,
    'independent_six_by_six_integer_determinants': 56,
    'independent_five_by_five_integer_principal_cofactors': 48,
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy': sympy.__version__,
    'scope': 'Written infinite-family necessary conditions from clustered odd roots, exact value identity, derivative and third shifted binary cubic. Arbitrary-shift coefficient identities, four derivative residues, sixteen binary parity patterns and eight independent full-quintic/derivative fixtures. No exponent or modulus range scan, numerical spectrum or Lean. Compatible controls are not integral. FullQ3 and higher-prime nonsquarefree vectors remain open.'
}, indent=2))
