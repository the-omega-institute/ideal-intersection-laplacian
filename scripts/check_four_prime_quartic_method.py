import hashlib
import json
from math import isqrt
from pathlib import Path

import sympy

from check_four_prime_a6_elliptic import ALPHA, BETA, GAMMA, DELTA, BASE_HEIGHT, WEIERSTRASS_LINEAR, WEIERSTRASS_CONSTANT, quartic


def checks():
    tail, height, radical, variable = sympy.symbols('b W s x')
    polynomial = quartic(tail)
    assert all(value > 0 for value in sympy.Poly(polynomial, tail).all_coeffs())
    quartic_discriminant = sympy.discriminant(polynomial, tail)
    assert quartic_discriminant != 0
    linear_cubic = BETA * DELTA - 4 * BASE_HEIGHT ** 2 * ALPHA
    constant_cubic = BASE_HEIGHT ** 2 * BETA ** 2 + ALPHA * DELTA ** 2 - 4 * ALPHA * BASE_HEIGHT ** 2 * GAMMA
    paper_linear = -GAMMA ** 2 / 3 + BETA * DELTA - 4 * BASE_HEIGHT ** 2 * ALPHA
    paper_constant = (2 * GAMMA ** 3 / 27 - BETA * GAMMA * DELTA / 3
                      - sympy.Rational(8, 3) * BASE_HEIGHT ** 2 * ALPHA * GAMMA
                      + BASE_HEIGHT ** 2 * BETA ** 2 + ALPHA * DELTA ** 2)
    assert sympy.expand((variable - GAMMA / 3) ** 3 + GAMMA * (variable - GAMMA / 3) ** 2
                        + linear_cubic * (variable - GAMMA / 3) + constant_cubic
                        - variable ** 3 - paper_linear * variable - paper_constant) == 0
    assert sympy.Rational(81, 10000) * paper_linear == WEIERSTRASS_LINEAR
    assert sympy.Rational(729, 1000000) * paper_constant == WEIERSTRASS_CONSTANT
    paper_cubic = variable ** 3 + paper_linear * variable + paper_constant
    cubic_discriminant = sympy.discriminant(paper_cubic, variable)
    assert cubic_discriminant < 0
    base_first = 2 * BASE_HEIGHT * radical + GAMMA / 3
    base_second = BETA * BASE_HEIGHT + DELTA * radical
    assert sympy.rem(sympy.expand(base_second ** 2 - paper_cubic.subs(variable, base_first)), radical ** 2 - ALPHA, radical) == 0
    decreasing_numerator = (BASE_HEIGHT * tail * sympy.diff(polynomial, tail)
                            - 4 * BASE_HEIGHT * polynomial - (DELTA * tail + 4 * BASE_HEIGHT ** 2) * height)
    expected = (-BASE_HEIGHT * (BETA * tail ** 3 + 2 * GAMMA * tail ** 2
                               + 3 * DELTA * tail + 4 * BASE_HEIGHT ** 2)
                - (DELTA * tail + 4 * BASE_HEIGHT ** 2) * height)
    assert sympy.expand(decreasing_numerator - expected) == 0
    derivative = sympy.diff((2 * BASE_HEIGHT * sympy.sqrt(polynomial) + DELTA * tail + 2 * BASE_HEIGHT ** 2) / tail ** 2, tail)
    assert sympy.simplify(derivative * tail ** 3 * sympy.sqrt(polynomial)
                          - expected.subs(height, sympy.sqrt(polynomial))) == 0
    rational_first = (2 * BASE_HEIGHT * (height + BASE_HEIGHT) + DELTA * tail) / tail ** 2
    rational_second = ((rational_first ** 2 - 4 * BASE_HEIGHT ** 2 * ALPHA) * tail
                       - DELTA * rational_first - 2 * BASE_HEIGHT ** 2 * BETA) / (2 * BASE_HEIGHT)
    total_derivative = sympy.diff(rational_first, tail) + sympy.diff(rational_first, height) * sympy.diff(polynomial, tail) / (2 * height)
    differential_numerator = sympy.together(rational_second + height * total_derivative).as_numer_denom()[0]
    assert sympy.rem(sympy.expand(differential_numerator), height ** 2 - polynomial, height) == 0
    excluded_second = DELTA ** 2 / (4 * BASE_HEIGHT ** 2) - GAMMA
    assert excluded_second == -1257750
    value_at_one = polynomial.subs(tail, 1)
    root_bound = isqrt(int(value_at_one)) + 1
    assert value_at_one == 13310820 and root_bound == 3649
    assert (root_bound - 1) ** 2 < value_at_one < root_bound ** 2
    height_constant = 2 * BASE_HEIGHT * root_bound + DELTA + 2 * BASE_HEIGHT ** 2
    assert height_constant == 13540800
    return {
        'quartic_coefficients_descending': [int(value) for value in (ALPHA, BETA, GAMMA, DELTA, BASE_HEIGHT ** 2)],
        'quartic_discriminant': int(quartic_discriminant),
        'paper_short_A': str(paper_linear), 'paper_short_B': str(paper_constant),
        'paper_short_cubic_discriminant': str(cubic_discriminant),
        'paper_short_model_has_exactly_one_real_root': True,
        'paper_to_previous_short_scaling': '(X,Y)=(9x/100,27y/1000)',
        'paper_asymptotic_point': '(1950s+6640150/3,1123590000+4524000s)',
        'asymptotic_point_equals_shifted_Pstar': True,
        'common_coordinate_field_degree_for_rational_basis_and_P0': 2,
        'paper_sign_sigma': 1,
        'F_star_derivative_times_b_cubed_sqrt_f': str(expected),
        'F_star_strictly_decreasing_for_all_positive_b': True,
        'rational_chart_differential_identity_verified': 'R_V=-W*dR_U/db on W^2=f(b)',
        'F_star_limit': '1950s',
        'paper_forbidden_F_star_values': ['-1950s', '-1257750'],
        'positive_domain_avoids_both_forbidden_values': True,
        'monotonicity_cutoff_u0': 0,
        'integral_upper_bound_for_positive_b': 'integral_b^infinity du/sqrt(f(u)) < 1/(sqrt(43645)*b)',
        'c9': '1/sqrt(43645)',
        'f_one': int(value_at_one), 'integer_upper_bound_sqrt_f_one': root_bound,
        'rational_height_bound_for_integer_b_ge_one': 'h(R_U)<=log(13540800)+2log(b)',
        'c10_for_integral_cubic_E0': 'log(13540800)',
        'paper_reduction_case': 'Section 5 Case 2, inhomogeneous Proposition 4',
        'case_two_proof_input': 'Infinite-order T=Pstar-sigma(Pstar) excludes rational dependence of the asymptotic logarithm on rational-group logarithms and the real period',
    }


def main():
    dependencies = ('check_four_prime_a6_elliptic.py', 'check_four_prime_nontorsion.py')
    report = {
        'written_result': 'Source-audited specialization of Tzanakis (1996) to the a6 quartic, with exact model identification, positive-domain monotonicity, initial integral/height estimates and proof of the inhomogeneous reduction case.',
        'method_source': {'author': 'N. Tzanakis', 'year': 1996, 'journal': 'Acta Arithmetica',
                          'volume': 75, 'issue': 2, 'pages': '165-190', 'DOI': '10.4064/aa-75-2-165-190'},
        'exact_checks': checks(),
        'full_rational_basis_required': True,
        'exact_rank_or_full_basis_computed': False,
        'initial_mordell_weil_coefficient_bound_computed': False,
        'LLL_reduction_run': False, 'complete_integral_points_enumerated': False,
        'new_nonintegrality_classification': False,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in dependencies},
        'sympy_version': sympy.__version__,
        'scope': 'Application of an existing published quartic method, with written specialization and exact algebraic checks. No numeric elliptic logarithms, regulator/height-correction/David constants, initial coefficient bound, LLL, coefficient scan, full point list, graph or historical finite-base rerun, floats or Lean.',
    }
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
