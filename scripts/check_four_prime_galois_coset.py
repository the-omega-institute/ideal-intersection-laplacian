import hashlib
import json
from pathlib import Path

import sympy

from check_four_prime_a6_elliptic import ALPHA, BETA, GAMMA, DELTA, BASE_HEIGHT, cubic, quartic, to_weierstrass
from check_four_prime_affine_integrality import field_coordinates


def zero_on_quartic(expression, radical, height, tail):
    numerator = sympy.together(expression).as_numer_denom()[0]
    reduced = sympy.rem(sympy.expand(numerator), radical ** 2 - ALPHA, radical)
    assert sympy.expand(sympy.rem(reduced, height ** 2 - quartic(tail), height)) == 0


def subtract(point, other, radical):
    if point == other:
        return None
    slope = sympy.radsimp((point[1] + other[1]) / (point[0] - other[0]))
    first = sympy.simplify(slope ** 2 - GAMMA - point[0] - other[0])
    second = sympy.simplify(-point[1] + slope * (point[0] - first))
    return first, second


def symbolic_checks():
    tail, height, radical = sympy.symbols('b W s')
    first, second = field_coordinates(tail, height)
    field_first = first[0] + first[1] * radical
    field_second = second[0] + second[1] * radical
    base_first = 2 * BASE_HEIGHT * radical
    base_second = BETA * BASE_HEIGHT + DELTA * radical
    fixed_first = BETA ** 2 / (4 * ALPHA) - GAMMA
    fixed_second_coefficient = (BETA * (GAMMA - BETA ** 2 / (4 * ALPHA)) - 2 * ALPHA * DELTA) / (2 * ALPHA)
    fixed_second = fixed_second_coefficient * radical
    assert fixed_first == sympy.Rational(196265550, 203)
    assert fixed_second_coefficient == sympy.Rational(-712421190000, 41209)
    assert sympy.rem(sympy.expand(cubic(fixed_first, fixed_second)), radical ** 2 - ALPHA, radical) == 0
    assert sympy.rem(sympy.expand(cubic(base_first, base_second)), radical ** 2 - ALPHA, radical) == 0
    slope = (4 * ALPHA * tail + BETA) / (2 * radical)
    conjugate_first = first[0] - first[1] * radical
    conjugate_second = second[0] - second[1] * radical
    assert sympy.cancel((field_second + conjugate_second) / (field_first - conjugate_first) - slope) == 0
    difference_first = slope ** 2 - GAMMA - field_first - conjugate_first
    difference_second = -field_second + slope * (field_first - fixed_first)
    zero_on_quartic(difference_first - fixed_first, radical, height, tail)
    zero_on_quartic(difference_second - fixed_second, radical, height, tail)
    rational_first = (2 * BASE_HEIGHT * (height + BASE_HEIGHT) + DELTA * tail) / tail ** 2
    rational_second = ((rational_first ** 2 - 4 * BASE_HEIGHT ** 2 * ALPHA) * tail
                       - DELTA * rational_first - 2 * BASE_HEIGHT ** 2 * BETA) / (2 * BASE_HEIGHT)
    translation_slope = (-rational_second - base_second) / (rational_first - base_first)
    translated_first = translation_slope ** 2 - GAMMA - rational_first - base_first
    translated_second = -base_second + translation_slope * (base_first - field_first)
    zero_on_quartic(translated_first - field_first, radical, height, tail)
    zero_on_quartic(translated_second - field_second, radical, height, tail)
    assert fixed_second_coefficient != 0 and BASE_HEIGHT != 0
    assert sympy.factorint(ALPHA) == {5: 1, 7: 1, 29: 1, 43: 1}
    return {
        'fixed_difference_T_U': str(fixed_first),
        'fixed_difference_T_V_coefficient_s': str(fixed_second_coefficient),
        'T_on_E0_and_sigma_T_equals_negative_T': True,
        'base_Pstar_U_coefficients_one_s': [0, int(2 * BASE_HEIGHT)],
        'base_Pstar_V_coefficients_one_s': [int(BETA * BASE_HEIGHT), int(DELTA)],
        'Pstar_on_E0': True,
        'generic_difference_P_minus_sigma_P_equals_T': True,
        'generic_translation_P_equals_Pstar_minus_previous_rational_R': True,
        'difference_slope': '(4alpha*b+beta)/(2s)',
        'difference_denominator_nonzero_on_positive_domain': 'U-sigma(U)=4sW; f(b)>0 for b>0',
        'translation_denominator_nonzero_for_finite_rational_R': 'R_U rational, Pstar_U=1950s irrational',
        'coset': '{P in E0(K): P-sigma(P)=T}=Pstar+E0(Q)',
        'previous_chart_relation': 'P-Pstar=-R, including rational-chart O at b=0,W=975',
    }


def fixed_controls():
    radical = sympy.sqrt(ALPHA)
    base = (2 * BASE_HEIGHT * radical, BETA * BASE_HEIGHT + DELTA * radical)
    fixed = (sympy.Rational(196265550, 203), sympy.Rational(-712421190000, 41209) * radical)
    controls = []
    for tail, height in ((sympy.Integer(55), sympy.Integer(781950)),
                         (sympy.Integer(55), sympy.Integer(-781950)),
                         (sympy.Integer(0), sympy.Integer(975)),
                         (sympy.Integer(0), sympy.Integer(-975))):
        assert height ** 2 == quartic(tail)
        first, second = field_coordinates(tail, height)
        point = (first[0] + first[1] * radical, second[0] + second[1] * radical)
        conjugate = (first[0] - first[1] * radical, second[0] - second[1] * radical)
        assert subtract(point, conjugate, radical) == fixed
        translated = subtract(point, base, radical)
        if tail:
            horizontal, vertical = to_weierstrass(tail, height)
            rational = ((100 * horizontal - 3 * GAMMA) / 9, -1000 * vertical / 27)
            assert translated == rational
        elif height == BASE_HEIGHT:
            assert translated is None
        else:
            assert translated == (-1257750, -1794390000)
        controls.append({'b': int(tail), 'W': int(height), 'P_minus_sigma_P_equals_T': True,
                         'Q_equals_P_minus_Pstar': 'O' if translated is None else [str(value) for value in translated],
                         'Q_rational_and_equals_negative_previous_chart': True})
    return controls


def main():
    dependencies = ('check_four_prime_a6_elliptic.py', 'check_four_prime_affine_integrality.py')
    report = {
        'written_result': 'The quadratic-field images lie in the exact Galois-difference coset Pstar+E0(Q), and translating by -Pstar gives the negative of the preceding rational chart.',
        'symbolic': symbolic_checks(), 'specified_affine_controls': fixed_controls(),
        'candidate_group_parameterization_requires_full_E0_K_basis': False,
        'translated_integrality_complete_algorithm_run': False,
        'rank_computed': False, 'rational_or_number_field_basis_certified': False,
        'integral_points_enumerated': False, 'new_nonintegrality_classification': False,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in dependencies},
        'sympy_version': sympy.__version__,
        'scope': 'Generic exact elliptic group-law/difference/translation identities and four specified affine controls. The full O_K integrality and original conjugate/quartic/tail filter remain required. No rank/basis/complete point algorithm, arbitrary scan, graph or historical finite-base rerun, floats or Lean.',
    }
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
