import hashlib
from itertools import permutations
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, second, third, variable = sympy.symbols('a b c x')
left_shift, right_shift, even_shift, argument = sympy.symbols('u v w y')
exponents = (first, second, third)
quintic = sympy.Poly(sympy.cancel(
    support_quotient(exponents, complement=True).charpoly(variable).as_expr() / variable), variable)
substituted = sympy.expand(quintic.as_expr().subs(dict(zip(
    exponents, (4 * left_shift + 3, 4 * right_shift + 3, 4 * even_shift + 2)))))


def verify_congruence(expression, expected, modulus, generators):
    polynomial = sympy.Poly(sympy.expand(expression), *generators, domain=sympy.ZZ)
    difference = sympy.Poly(sympy.expand(expression - expected), *generators, domain=sympy.ZZ)
    assert all(int(coefficient) % modulus == 0 for coefficient in difference.coeffs())
    return {'modulus': modulus, 'expected': str(expected),
            'coefficient_count': len(polynomial.terms()),
            'difference_coefficients_checked': len(difference.terms()),
            'all_difference_coefficients_divisible': True}


shifted = sympy.Poly(sympy.expand(substituted.subs(variable, 2 * argument + 1)),
                     left_shift, right_shift, even_shift, argument, domain=sympy.ZZ)
assert all(int(coefficient) % 8 == 0 for coefficient in shifted.coeffs())
checks = {
    'integer_shifted_polynomial': {'divisor': 8, 'coefficients_checked': len(shifted.terms())},
    'shifted_modulo_two': verify_congruence(shifted.as_expr() / 8, argument ** 3, 2,
                                          (left_shift, right_shift, even_shift, argument)),
    'endpoint_modulo_32': verify_congruence(substituted.subs(variable, 1),
                                           16 * (left_shift + right_shift), 32,
                                           (left_shift, right_shift, even_shift)),
    'derivative_modulo_16': verify_congruence(sympy.diff(substituted, variable).subs(variable, 1),
                                            8 * (left_shift + right_shift + 1), 16,
                                            (left_shift, right_shift, even_shift)),
}
symmetry_checks = 0
for ordering in permutations(exponents):
    assert sympy.expand(quintic.as_expr().subs(dict(zip(exponents, ordering)), simultaneous=True)
                        - quintic.as_expr()) == 0
    symmetry_checks += 1


def integer_determinant(matrix):
    size = len(matrix)
    total = 0
    for ordering in permutations(range(size)):
        inversions = sum(ordering[left_index] > ordering[right_index]
                         for left_index in range(size) for right_index in range(left_index + 1, size))
        term = (-1) ** inversions
        for row, column in enumerate(ordering):
            term *= matrix[row][column]
        total += term
    return total


def independent_matrix(triple):
    left, right, even = triple
    return [
        [right + even + right * even, -right, -even, 0, 0, -right * even],
        [-left, left + even + left * even, -even, 0, -left * even, 0],
        [-left, -right, left + right + left * right, -left * right, 0, 0],
        [0, 0, -even, even, 0, 0],
        [0, -right, 0, 0, right, 0],
        [-left, 0, 0, 0, 0, left],
    ]


fixtures = []
for triple in ((3, 3, 2), (7, 7, 6), (19, 27, 10), (23, 39, 14)):
    matrix = independent_matrix(triple)
    assert sympy.Matrix(matrix) == support_quotient(triple, complement=True)
    assert integer_determinant(matrix) == 0
    values = []
    for value in range(1, 7):
        shifted_matrix = [[value * int(row == column) - matrix[row][column]
                           for column in range(6)] for row in range(6)]
        determinant = integer_determinant(shifted_matrix)
        assert determinant % value == 0
        values.append((value, determinant // value))
    independent = sympy.Poly(sympy.interpolate(values, variable), variable, domain=sympy.ZZ)
    generic = sympy.Poly(quintic.as_expr().subs(dict(zip(exponents, triple))), variable)
    assert independent == generic
    unit_matrix = [[int(row == column) - matrix[row][column]
                    for column in range(6)] for row in range(6)]
    determinant_derivative = sum(integer_determinant([
        [unit_matrix[row][column] for column in range(6) if column != removed]
        for row in range(6) if row != removed]) for removed in range(6))
    endpoint = int(independent.eval(1))
    derivative = int(independent.diff().eval(1))
    assert derivative == determinant_derivative - endpoint
    shifts = ((triple[0] - 3) // 4, (triple[1] - 3) // 4, (triple[2] - 2) // 4)
    assert endpoint % 32 == 16 * (shifts[0] + shifts[1]) % 32
    assert derivative % 16 == 8 * (shifts[0] + shifts[1] + 1) % 16
    direct_shifted = sympy.Poly(sympy.expand(independent.as_expr().subs(variable, 2 * argument + 1) / 8),
                               argument, domain=sympy.ZZ)
    assert sympy.Poly(direct_shifted.as_expr(), argument, modulus=2) == sympy.Poly(argument ** 3, argument, modulus=2)
    assert any(factor.degree() > 1 for factor, multiplicity in independent.factor_list()[1])
    fixtures.append({'odd_odd_even_exponents': triple, 'shifts_u_v_w': shifts,
                     'independent_coefficients': [int(coefficient) for coefficient in independent.all_coeffs()],
                     'integer_determinant_interpolation_points': values,
                     'h_at_one': endpoint, 'h_prime_at_one': derivative,
                     'determinant_derivative_at_one': determinant_derivative,
                     'endpoint_modulo_32': endpoint % 32, 'derivative_modulo_16': derivative % 16,
                     'nonlinear_rational_factor': True})

print(json.dumps({
    'exponent_family': 'All positive permutations of (3,3,2) modulo4',
    'symbolic_checks': checks, 'generic_symmetry_checks': symmetry_checks,
    'fixtures': fixtures,
    'independent_six_by_six_determinants': 28,
    'independent_five_by_five_principal_cofactors': 24,
    'written_proof': 'Integer roots force two even and three odd roots. h(2y+1)/8 modulo2=y^3 forces all odd roots to be1mod4. Then64|h(1)and16|hprime(1). The endpoint congruence forces u+v even, while the derivative congruence forces u+v odd.',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy': sympy.__version__,
    'scope': 'Uniform written root-distribution/divisibility proof. Symbolic coefficient identities and four independent integer polynomial/derivative fixtures. No exponent scan, numerical spectrum or Lean. FullQ3 and nonsquarefree higher-prime vectors remain open.'
}, indent=2))
