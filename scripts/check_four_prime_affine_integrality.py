import hashlib
import json
from math import isqrt
from pathlib import Path

import sympy

from check_four_prime_a6_elliptic import ALPHA, BETA, GAMMA, DELTA, BASE_HEIGHT, cubic, original_tail, quartic
from check_four_prime_pair_three import operator


def field_coordinates(tail, height):
    return ((2 * ALPHA * tail ** 2 + BETA * tail, 2 * height),
            ((4 * ALPHA * tail + BETA) * height,
             4 * ALPHA * tail ** 3 + 3 * BETA * tail ** 2 + 2 * GAMMA * tail + DELTA))


def recover(first, second):
    height = first[1] / sympy.Integer(2)
    tail = (2 * second[0] - BETA * first[1]) / (4 * ALPHA * first[1])
    return sympy.cancel(tail), sympy.cancel(height)


def symbolic_checks():
    tail, maximum, height, radical, horizontal, vertical, omega = sympy.symbols('b c W s X Y omega')
    first, second = field_coordinates(tail, height)
    field_first = first[0] + first[1] * radical
    field_second = second[0] + second[1] * radical
    identity = sympy.rem(sympy.expand(cubic(field_first, field_second)), radical ** 2 - ALPHA, radical)
    assert sympy.rem(identity, height ** 2 - quartic(tail), height) == 0
    quotient, remainder = sympy.div(identity, height ** 2 - quartic(tail), height)
    assert remainder == 0
    recovered_tail, recovered_height = recover(first, second)
    assert sympy.cancel(recovered_tail - tail) == 0
    assert sympy.cancel(recovered_height - height) == 0
    for coefficients in (first, second):
        expanded = coefficients[0] + coefficients[1] * radical
        assert sympy.expand(expanded.subs(radical, 2 * omega - 1)
                            - (coefficients[0] - coefficients[1]) - 2 * coefficients[1] * omega) == 0
        assert all(value.is_Integer for value in sympy.Poly(coefficients[0], tail, height).coeffs())
        assert all(value.is_Integer for value in sympy.Poly(coefficients[1], tail, height).coeffs())
    assert sympy.factorint(ALPHA) == {5: 1, 7: 1, 29: 1, 43: 1}
    assert ALPHA % 4 == 1
    assert all(sympy.isprime(prime) for prime in (5, 7, 29, 43))
    floor = isqrt(int(ALPHA))
    assert floor == 208 and floor ** 2 < ALPHA < (floor + 1) ** 2
    leading = -13 * tail ** 2 + 420 * tail - 35
    linear = 420 * tail ** 2 + 5300 * tail + 1900
    constant = 5 * (55 - tail) * (7 * tail + 5)
    variable = sympy.Symbol('x')
    endpoint = sympy.Matrix(operator(6, tail, maximum)).charpoly(variable).as_expr().subs(variable, 2)
    assert sympy.expand(endpoint - leading * maximum ** 2 - linear * maximum - constant) == 0
    assert sympy.expand((leading * maximum + linear / 2) ** 2 - quartic(tail) - leading * endpoint) == 0
    recovered_maximum = original_tail(tail, height)
    substituted = sympy.together(endpoint.subs(maximum, recovered_maximum)).as_numer_denom()[0]
    assert sympy.rem(substituted, height ** 2 - quartic(tail), height) == 0
    assert sympy.discriminant(leading, tail) == 4 * ALPHA
    assert all(value > 0 for value in sympy.Poly(quartic(tail), tail).all_coeffs())
    linear_cubic = BETA * DELTA - 4 * ALPHA * BASE_HEIGHT ** 2
    constant_cubic = BASE_HEIGHT ** 2 * BETA ** 2 + ALPHA * DELTA ** 2 - 4 * ALPHA * BASE_HEIGHT ** 2 * GAMMA
    assert linear_cubic == 5047497487500 and constant_cubic == 1053718156603125000
    discriminant = 16 * sympy.discriminant(variable ** 3 + GAMMA * variable ** 2 + linear_cubic * variable + constant_cubic, variable)
    assert discriminant == -309476819336418859764366000000000000000 != 0
    scaled_first = (100 * horizontal - 3 * GAMMA) / 9
    scaled_second = 1000 * vertical / 27
    short_equation = vertical ** 2 - horizontal ** 3 + 78162568812 * horizontal - 8433576786332241
    assert sympy.expand(cubic(scaled_first, scaled_second) - sympy.Rational(1000000, 729) * short_equation) == 0
    return {'polynomial_U_coefficients_one_s': [str(value) for value in first],
            'polynomial_V_coefficients_one_s': [str(value) for value in second],
            'cubic_coefficients_U_squared_U_constant': [int(GAMMA), int(linear_cubic), int(constant_cubic)],
            'cubic_discriminant': int(discriminant),
            'curve_identity_quotient_by_W_squared_minus_f_mod_s_squared_minus_alpha': str(sympy.factor(quotient)),
            'quotient_ideal_identity_verified': True, 'coefficient_inverse_verified': True,
            'inverse_b': '(2v0-beta*u1)/(4alpha*u1)', 'inverse_W': 'u1/2',
            'positive_b_implies_W_nonzero': 'all five f coefficients positive',
            'square_completion_and_c_recovery_verified': True,
            'field_discriminant': int(ALPHA), 'field_radical_squarefree_factors': [5, 7, 29, 43],
            'ring_of_integers': 'Z[(1+s)/2],s^2=43645',
            'polynomial_image_coordinates_in_Z_s': True,
            'rational_A_equals_zero_fibers': [],
            'short_model_fixed_allowed_denominator_primes': [2, 5],
            'short_model_scaling_identity_verified': True}


def fixed_controls():
    controls = []
    for tail, height in ((sympy.Integer(55), sympy.Integer(781950)),
                         (sympy.Integer(55), sympy.Integer(-781950)),
                         (sympy.Integer(0), sympy.Integer(975)),
                         (sympy.Integer(0), sympy.Integer(-975))):
        assert height ** 2 == quartic(tail) and height % 5 == 0
        first, second = field_coordinates(tail, height)
        assert all(value.is_Integer for value in first + second)
        assert recover(first, second) == (tail, height)
        assert field_coordinates(*recover(first, second)) == (first, second)
        maximum = original_tail(tail, height)
        admissible = bool(tail > 0 and maximum.is_integer and maximum > 0)
        controls.append({'b': int(tail), 'W': int(height),
                         'U_coefficients_one_s': [int(value) for value in first],
                         'V_coefficients_one_s': [int(value) for value in second],
                         'coordinates_are_algebraic_integers': True,
                         'coefficient_round_trip': True, 'recovered_c': str(maximum),
                         'positive_integer_tail_filter_passes': admissible})
    assert controls[1]['U_coefficients_one_s'] == [327434250, -1563900]
    assert controls[1]['V_coefficients_one_s'] == [-8409324885000, 40238718000]
    assert [control['recovered_c'] for control in controls] == ['0', '26065/271', '-5/7', '55']
    assert not any(control['positive_integer_tail_filter_passes'] for control in controls)
    return controls


def main():
    dependencies = ('check_four_prime_a6_elliptic.py', 'check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py')
    report = {'written_result': 'An injective integrality-preserving polynomial reduction of positive integer p(2;6,b,c)=0 tails to O_K-integral points on the explicit nonsingular cubic over K=Q(sqrt(43645)), with an exact complete-list recovery filter.',
              'symbolic': symbolic_checks(), 'specified_affine_controls': fixed_controls(),
              'complete_filter': ['discard u1=0', 'recover b,W and require positive integer b and integer W',
                                  'check all four conjugate-coefficient identities and W^2=f(b)',
                                  'recover c with A(b) divisibility and positive integer c; require b,c>=6 for repeated minimum'],
              'complete_integral_point_target': 'O_K-integral E0(K) points; rational E0(Q) points alone are insufficient',
              'rank_computed': False, 'number_field_basis_certified': False,
              'integral_points_enumerated': False, 'new_nonintegrality_classification': False,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in dependencies},
              'sympy_version': sympy.__version__,
              'scope': 'Written polynomial-integrality reduction over the specific quadratic field, generic quotient-ideal and recovery identities, four specified affine controls, squarefree factor/ring-of-integers input and fixed short-model denominator primes. No field rank/basis or complete point algorithm, parameter scan, graph expansion, historical finite-base rerun, floats or Lean. Previous rational-chart warning, finiteness and all other results retain their scopes.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
