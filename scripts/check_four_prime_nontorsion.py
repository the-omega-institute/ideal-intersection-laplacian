import hashlib
import json
from pathlib import Path

import sympy

from check_four_prime_a6_elliptic import ALPHA, GAMMA, WEIERSTRASS_LINEAR, WEIERSTRASS_CONSTANT, to_weierstrass
from check_four_prime_affine_integrality import field_coordinates


def checks():
    radical, first, second = sympy.symbols('s U V')
    linear, constant = WEIERSTRASS_LINEAR, WEIERSTRASS_CONSTANT
    fixed_first = sympy.Rational(196265550, 203)
    fixed_second_coefficient = sympy.Rational(-712421190000, 41209)
    short_first = (9 * fixed_first + 3 * GAMMA) / 100
    short_second_coefficient = 27 * fixed_second_coefficient / 1000
    assert ALPHA * short_second_coefficient ** 2 == short_first ** 3 + linear * short_first + constant
    twist_linear = ALPHA ** 2 * linear
    twist_constant = ALPHA ** 3 * constant
    twist_first = ALPHA * short_first
    twist_second = ALPHA ** 2 * short_second_coefficient
    assert twist_first == 12492018795 and twist_second == -889155076709250
    assert twist_first.is_Integer and twist_second.is_Integer
    assert twist_second ** 2 == twist_first ** 3 + twist_linear * twist_first + twist_constant
    twist_discriminant = -16 * (4 * twist_linear ** 3 + 27 * twist_constant ** 2)
    short_discriminant = -16 * (4 * linear ** 3 + 27 * constant ** 2)
    assert twist_discriminant == ALPHA ** 6 * short_discriminant != 0
    assert sympy.isprime(1201) and twist_second % 1201 == 0
    assert twist_discriminant % 1201 == 4
    assert (4 * twist_linear ** 3 + 27 * twist_constant ** 2) % 1201 != 0
    field_equation = second ** 2 - first ** 3 - linear * first - constant
    mapped_first = ALPHA * first
    mapped_second = ALPHA * radical * second
    mapped_equation = mapped_second ** 2 - mapped_first ** 3 - twist_linear * mapped_first - twist_constant
    assert sympy.rem(sympy.expand(mapped_equation - ALPHA ** 3 * field_equation), radical ** 2 - ALPHA, radical) == 0
    rational_first, rational_second = to_weierstrass(sympy.Integer(55), sympy.Integer(-781950))
    assert rational_first == sympy.Rational(19517052, 121)
    assert rational_second == sympy.Rational(6328630035, 1331)
    assert rational_second ** 2 == rational_first ** 3 + linear * rational_first + constant
    assert not rational_first.is_Integer
    control_first, control_second = field_coordinates(sympy.Integer(55), sympy.Integer(-781950))
    assert control_first == (327434250, -1563900)
    assert control_second == (-8409324885000, 40238718000)
    return {
        'short_E_a_invariants': [0, 0, 0, int(linear), int(constant)],
        'T_short_X': str(short_first), 'T_short_Y_coefficient_s': str(short_second_coefficient),
        'quadratic_twist_d': int(ALPHA),
        'twist_a_invariants': [0, 0, 0, int(twist_linear), int(twist_constant)],
        'twist_T_rational_X_Y': [int(twist_first), int(twist_second)],
        'twist_map_identity': '(X,Y)->(dX,dsY),s^2=d',
        'twist_map_identity_verified': True,
        'twist_T_on_curve': True, 'twist_discriminant': int(twist_discriminant),
        'nagell_lutz_witness_prime': 1201, 'twist_T_Y_mod_witness': 0,
        'twist_discriminant_mod_witness': 4,
        'T_infinite_order_by_nagell_lutz': True,
        'specified_rational_S_X_Y': [str(rational_first), str(rational_second)],
        'specified_rational_S_nonintegral_X': True,
        'S_infinite_order_by_nagell_lutz': True,
        'S_galois_sign': 1, 'T_galois_sign': -1,
        'S_T_independent_over_Z': True,
        'proved_rank_lower_bounds': {'E_Q': 1, 'quadratic_twist_Q': 1, 'E_K': 2},
        'all_nonzero_multiples_of_coset_points_are_nonrational': True,
        'all_images_under_nonzero_Q_defined_isogenies_are_nonrational': True,
    }


def main():
    dependencies = ('check_four_prime_a6_elliptic.py', 'check_four_prime_affine_integrality.py')
    report = {
        'written_result': 'The fixed Galois difference T has infinite order; multiplication and Q-defined isogenies cannot rationalize the coset. An explicit rational infinite-order point is independent of T, giving rank E(K)>=2.',
        'exact_checks': checks(),
        'proof_input': 'Nagell-Lutz theorem on nonsingular short Weierstrass equations with integer coefficients; Galois eigenspace independence and finite isogeny kernel.',
        'exact_rank_computed': False, 'rational_or_field_basis_certified': False,
        'complete_integral_point_algorithm_run': False, 'integral_points_enumerated': False,
        'new_nonintegrality_classification': False,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in dependencies},
        'sympy_version': sympy.__version__,
        'scope': 'Written infinite-order and Galois/isogeny obstruction proofs, exact twist/curve identities and two specified infinite-order witnesses. Proved rank lower bounds, not exact ranks or a basis. No point enumeration, arbitrary scan, graph or historical finite-base rerun, floats or Lean.',
    }
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
