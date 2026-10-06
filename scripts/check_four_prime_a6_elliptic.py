import hashlib
import json
from math import isqrt
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator
from check_four_prime_single_pair_midpoint import integer_determinant


ALPHA = sympy.Integer(43645)
BETA = sympy.Integer(1152400)
GAMMA = sympy.Integer(6640150)
DELTA = sympy.Integer(4524000)
BASE_HEIGHT = sympy.Integer(975)
WEIERSTRASS_LINEAR = sympy.Integer(-78162568812)
WEIERSTRASS_CONSTANT = sympy.Integer(8433576786332241)


def quartic(tail):
    return ALPHA * tail ** 4 + BETA * tail ** 3 + GAMMA * tail ** 2 + DELTA * tail + BASE_HEIGHT ** 2


def cubic(first, second):
    linear = BETA * DELTA - 4 * BASE_HEIGHT ** 2 * ALPHA
    constant = BASE_HEIGHT ** 2 * BETA ** 2 + ALPHA * DELTA ** 2 - 4 * BASE_HEIGHT ** 2 * ALPHA * GAMMA
    return second ** 2 - first ** 3 - GAMMA * first ** 2 - linear * first - constant


def to_weierstrass(tail, height):
    first = (2 * BASE_HEIGHT * (height + BASE_HEIGHT) + DELTA * tail) / tail ** 2
    denominator = first ** 2 - 4 * BASE_HEIGHT ** 2 * ALPHA
    second = (denominator * tail - DELTA * first - 2 * BASE_HEIGHT ** 2 * BETA) / (2 * BASE_HEIGHT)
    return sympy.cancel((9 * first + 3 * GAMMA) / 100), sympy.cancel(27 * second / 1000)


def from_weierstrass(horizontal, vertical):
    first = (100 * horizontal - 3 * GAMMA) / 9
    second = 1000 * vertical / 27
    tail = (2 * BASE_HEIGHT * second + DELTA * first + 2 * BASE_HEIGHT ** 2 * BETA) / (first ** 2 - 4 * BASE_HEIGHT ** 2 * ALPHA)
    height = (first * tail ** 2 - DELTA * tail) / (2 * BASE_HEIGHT) - BASE_HEIGHT
    return sympy.cancel(tail), sympy.cancel(height)


def original_tail(tail, height):
    leading = -13 * tail ** 2 + 420 * tail - 35
    return sympy.cancel((height - 210 * tail ** 2 - 2650 * tail - 950) / leading)


def zero_modulo(expression, equation, variable):
    numerator = sympy.together(expression).as_numer_denom()[0]
    assert sympy.expand(sympy.rem(numerator, equation, variable)) == 0


def symbolic_checks():
    tail, maximum, height, horizontal, vertical, first, second = sympy.symbols('b c W X Y U V')
    matrix = operator(6, tail, maximum)
    endpoint = integer_determinant([[2 * (row == column) - matrix[row][column]
                                     for column in range(4)] for row in range(4)])
    leading = -13 * tail ** 2 + 420 * tail - 35
    linear = 420 * tail ** 2 + 5300 * tail + 1900
    constant = 5 * (55 - tail) * (7 * tail + 5)
    assert sympy.expand(endpoint - leading * maximum ** 2 - linear * maximum - constant) == 0
    lifted_height = leading * maximum + linear / 2
    assert sympy.expand(lifted_height ** 2 - quartic(tail) - leading * endpoint) == 0
    denominator = first ** 2 - 4 * BASE_HEIGHT ** 2 * ALPHA
    quadratic_linear = -2 * DELTA * first - 4 * BASE_HEIGHT ** 2 * BETA
    quadratic_constant = DELTA ** 2 - 4 * BASE_HEIGHT ** 2 * first - 4 * BASE_HEIGHT ** 2 * GAMMA
    assert sympy.expand(quadratic_linear ** 2 - 4 * denominator * quadratic_constant
                        + 16 * BASE_HEIGHT ** 2 * cubic(first, 0)) == 0
    curve = vertical ** 2 - horizontal ** 3 - WEIERSTRASS_LINEAR * horizontal - WEIERSTRASS_CONSTANT
    assert sympy.expand(cubic((100 * horizontal - 3 * GAMMA) / 9, 1000 * vertical / 27)
                        - sympy.Rational(1000000, 729) * curve) == 0
    quartic_equation = height ** 2 - quartic(tail)
    mapped_horizontal, mapped_vertical = to_weierstrass(tail, height)
    zero_modulo(curve.subs({horizontal: mapped_horizontal, vertical: mapped_vertical}), quartic_equation, height)
    recovered_tail, recovered_height = from_weierstrass(horizontal, vertical)
    zero_modulo(recovered_height ** 2 - quartic(recovered_tail), curve, vertical)
    round_tail, round_height = from_weierstrass(mapped_horizontal, mapped_vertical)
    zero_modulo(round_tail - tail, quartic_equation, height)
    zero_modulo(round_height - height, quartic_equation, height)
    round_horizontal, round_vertical = to_weierstrass(recovered_tail, recovered_height)
    zero_modulo(round_horizontal - horizontal, curve, vertical)
    zero_modulo(round_vertical - vertical, curve, vertical)
    compact = (2340 * vertical + 1628640 * horizontal - 253444000680) / ((2 * horizontal - 398409) ** 2 - 5377107645)
    assert sympy.cancel(compact - recovered_tail) == 0
    assert 351 ** 2 * ALPHA == 5377107645
    assert sympy.discriminant(leading, tail) == 4 * ALPHA
    floor = isqrt(int(ALPHA))
    assert floor == 208 and floor ** 2 < ALPHA < (floor + 1) ** 2
    discriminant = -16 * (4 * WEIERSTRASS_LINEAR ** 3 + 27 * WEIERSTRASS_CONSTANT ** 2)
    assert discriminant == -164468670344965775252034431406000 != 0
    assert quartic(0) == BASE_HEIGHT ** 2
    assert original_tail(0, BASE_HEIGHT) == sympy.Rational(-5, 7)
    assert original_tail(0, -BASE_HEIGHT) == 55
    exceptional_first = DELTA ** 2 / (4 * BASE_HEIGHT ** 2) - GAMMA
    exceptional_second = (-DELTA * exceptional_first - 2 * BASE_HEIGHT ** 2 * BETA) / (2 * BASE_HEIGHT)
    assert exceptional_first == -1257750 and exceptional_second == 1794390000
    exceptional_horizontal = (9 * exceptional_first + 3 * GAMMA) / 100
    exceptional_vertical = 27 * exceptional_second / 1000
    assert (exceptional_horizontal, exceptional_vertical) == (86007, 48448530)
    assert curve.subs({horizontal: exceptional_horizontal, vertical: exceptional_vertical}) == 0
    assert from_weierstrass(exceptional_horizontal, exceptional_vertical) == (0, -BASE_HEIGHT)
    zero_numerator_second = (-DELTA * first - 2 * BASE_HEIGHT ** 2 * BETA) / (2 * BASE_HEIGHT)
    assert sympy.expand(cubic(first, zero_numerator_second)
                        - (first ** 2 - 4 * BASE_HEIGHT ** 2 * ALPHA)
                        * (DELTA ** 2 - 4 * BASE_HEIGHT ** 2 * first - 4 * BASE_HEIGHT ** 2 * GAMMA)
                        / (4 * BASE_HEIGHT ** 2)) == 0
    return {'a6_endpoint_reconstructed_by_symbolic_permutation_determinant': True,
            'square_completion_identity': 'W^2-f(b)=A(b)*p(2;6,b,c)',
            'quadratic_discriminant_derivation': True, 'forward_and_inverse_curve_identities': True,
            'both_map_compositions': True, 'compact_inverse_b': str(compact),
            'quartic_coefficients_descending': [int(value) for value in (ALPHA, BETA, GAMMA, DELTA, BASE_HEIGHT ** 2)],
            'weierstrass_a_invariants': [0, 0, 0, int(WEIERSTRASS_LINEAR), int(WEIERSTRASS_CONSTANT)],
            'weierstrass_discriminant': int(discriminant), 'alpha_nonsquare_interval': [208, 209],
            'rational_A_equals_zero_fibers': [], 'rational_inverse_denominator_zero_fibers': [],
            'rational_quartic_points_at_infinity': [],
            'b_zero_positive_height': {'b': 0, 'W': 975, 'c': '-5/7', 'image': 'O'},
            'b_zero_negative_height': {'b': 0, 'W': -975, 'c': '55', 'image_X_Y': [86007, 48448530]},
            'only_finite_E_point_with_inverse_b_zero': [86007, 48448530]}


def rational_controls():
    controls = []
    for tail, height in ((sympy.Integer(55), sympy.Integer(781950)),
                         (sympy.Integer(55), sympy.Integer(-781950)),
                         (sympy.Rational(-5, 7), sympy.Rational(-5850, 7)),
                         (sympy.Rational(-5, 7), sympy.Rational(5850, 7))):
        assert height ** 2 == quartic(tail)
        horizontal, vertical = to_weierstrass(tail, height)
        assert vertical ** 2 == horizontal ** 3 + WEIERSTRASS_LINEAR * horizontal + WEIERSTRASS_CONSTANT
        assert from_weierstrass(horizontal, vertical) == (tail, height)
        maximum = original_tail(tail, height)
        controls.append({'b': str(tail), 'W': str(height), 'c': str(maximum),
                         'X': str(horizontal), 'Y': str(vertical), 'exact_round_trip': True,
                         'positive_integer_graph_tail_pair': bool(tail.is_integer and tail > 0 and maximum.is_integer and maximum > 0)})
    assert (controls[0]['X'], controls[0]['Y'], controls[0]['c']) == ('252030', '68869359', '0')
    assert (controls[1]['X'], controls[1]['Y'], controls[1]['c']) == ('19517052/121', '6328630035/1331', '26065/271')
    return controls


def main():
    dependencies = ('check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py')
    report = {'written_result': 'Explicit birational equivalence of p(2;6,b,c)=0 to Y^2=X^3-78162568812X+8433576786332241, with both maps and all rational exceptional points accounted for.',
              'symbolic': symbolic_checks(), 'specified_rational_round_trips': rational_controls(),
              'integrality_filter': 'Recover b and W, then c=(W-210b^2-2650b-950)/A(b); require positive integers b,c, or b,c>=6 for repeated minimum.',
              'weierstrass_integral_points_alone_are_complete_quartic_certificate': False,
              'rank_computed': False, 'mordell_weil_basis_certified': False,
              'minimal_model_claimed': False, 'integral_points_enumerated': False,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in dependencies},
              'sympy_version': sympy.__version__,
              'scope': 'Generic exact coordinate/curve/composition identities and four specified rational controls, plus nonsquare denominator and exceptional-point analysis. No graph control rerun, exponent scan, expanded graph, historical finite-base rerun, rank/basis/complete integral-point computation, floats or Lean. Previous finiteness and joint manuscript decisions retain their scopes.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
