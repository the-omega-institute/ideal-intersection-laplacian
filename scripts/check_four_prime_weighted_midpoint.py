import hashlib
import json
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def symbolic_checks():
    first, tail, gap, variable, slack, margin = sympy.symbols('a b r x v z')
    matrix = sympy.Matrix(operator(first, tail, tail + gap))
    diagonal = sympy.diag(1, tail + gap, tail, tail * (tail + gap))
    assert diagonal * matrix == matrix.T * diagonal
    polynomial = matrix.charpoly(variable).as_expr()
    midpoint = first + tail + 1 + gap / 2
    bracket = (4 * first ** 2 * tail ** 2 + 4 * first ** 2 * tail * gap + 8 * first ** 2 * tail
               + 4 * first ** 2 * gap + 4 * first * tail ** 3 + 6 * first * tail ** 2 * gap
               + 8 * first * tail ** 2 + 2 * first * tail * gap ** 2 + 8 * first * tail * gap
               + 4 * first * tail + 2 * first * gap ** 2 + 2 * first * gap + 4 * tail ** 3
               + 6 * tail ** 2 * gap + 4 * tail ** 2 + 2 * tail * gap ** 2 + 4 * tail * gap + gap ** 2)
    assert sympy.expand(16 * polynomial.subs(variable, midpoint) - gap ** 2 * (2 * first + 1) * bracket) == 0
    assert all(value > 0 for value in sympy.Poly(bracket, first, tail, gap).coeffs())
    lower = -256 * first ** 3 * polynomial.subs(variable, midpoint - sympy.Rational(1, 2))
    substituted = sympy.cancel(lower.subs(tail, ((2 * first + 1) * gap ** 2 + margin) / (4 * first)))
    expansion = sympy.Poly(sympy.expand(substituted.subs(gap, slack + 3)), first, slack, margin)
    assert len(expansion.terms()) == 128 and expansion.TC() == 729
    assert all(value > 0 for value in expansion.coeffs())
    gap_three_rows = []
    expected = {1: [26, 62, 68, 28], 2: [37, 98, 150, 84],
                3: [36, 72, 224, 184], 4: [17, 161, 565, 1265]}
    for value in (1, 2, 3, 4):
        endpoint = sympy.expand(polynomial.subs({gap: 3, tail: value, variable: first + value + 2}))
        shifted = endpoint if value <= 3 else sympy.expand(endpoint.subs(first, first + 5))
        coefficients = sympy.Poly(shifted, first).all_coeffs()
        assert coefficients == expected[value] and all(coefficient > 0 for coefficient in coefficients)
        gap_three_rows.append({'b': value, 'polynomial': str(endpoint),
                               'positive_variable': 'a' if value <= 3 else 'u=a-5',
                               'positive_coefficients_descending': [int(coefficient) for coefficient in coefficients]})
    assert 4 * 5 * 5 - (2 * 5 + 1) * 9 == 1
    minimum_slack, tail_slack = sympy.symbols('u w')
    gap_three_margin = sympy.Poly(sympy.expand((4 * first * tail - (2 * first + 1) * 9)
                                              .subs({first: minimum_slack + 5, tail: tail_slack + 5})),
                                  minimum_slack, tail_slack)
    assert gap_three_margin.as_expr() == 4 * minimum_slack * tail_slack + 2 * minimum_slack + 20 * tail_slack + 1
    family_first = gap * (gap - 1) / 2
    family_tail = gap * (gap - 1)
    family_margin = sympy.expand(4 * family_first * family_tail - (2 * family_first + 1) * gap ** 2)
    assert sympy.expand(family_margin - gap ** 2 * (gap ** 2 - 3 * gap + 1)) == 0
    product_failure = ((first ** 2 - 1) * (2 * tail + gap) + (first - 1) * (2 * first - 1)
                       - tail * (tail + gap))
    failure_at_family = sympy.expand(product_failure.subs({first: family_first, tail: family_tail}))
    failure_shifted = sympy.Poly((8 * failure_at_family).subs(gap, slack + 4), slack)
    assert all(value > 0 for value in failure_shifted.coeffs())
    failure_at_twice = sympy.expand(product_failure.subs(tail, 2 * first))
    assert sympy.expand(failure_at_twice - (4 * first ** 3 + (gap - 2) * first ** 2
                                           - (2 * gap + 7) * first + 1 - gap)) == 0
    return {'generic_symmetry_and_midpoint_identity': 'passed', 'positive_midpoint_bracket': str(bracket),
            'weighted_lower_endpoint_positive_expansion': {
                'identity': '-256a^3 p(m-1/2),r=3+v,b=((2a+1)r^2+z)/(4a)',
                'terms_a_power_v_power_z_power_coefficient':
                [list(monomial) + [int(coefficient)] for monomial, coefficient in expansion.terms()],
                'positive_coefficient_count': 128, 'constant': 729},
            'gap_three_small_tail_rows': gap_three_rows,
            'gap_three_all_a_b_at_least_five_margin': str(gap_three_margin.as_expr()),
            'new_below_square_family': '(r(r-1)/2,r(r-1)/2,r(r-1),r^2),r>=4',
            'new_below_square_family_weighted_margin': str(family_margin),
            'new_below_square_family_product_failure': str(failure_at_family),
            'eight_times_new_family_product_failure_coefficients_at_r_equals_4_plus_v': [int(value) for value in failure_shifted.all_coeffs()]}


def fixed_control(first, tail, gap, mode='weighted'):
    maximum = tail + gap
    control = support_embedding(first, tail, maximum)
    matrix = operator(first, tail, maximum)
    variable = sympy.Symbol('x')
    values = [(endpoint, integer_determinant([[endpoint * (row == column) - matrix[row][column]
                                              for column in range(4)] for row in range(4)]))
              for endpoint in range(6)]
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    assert sympy.Poly(sympy.interpolate(values[:5], variable), variable) == polynomial
    assert polynomial.eval(5) == values[-1][1]
    doubled = [2 * first + 2 * tail + gap + 1, 2 * first + 2 * tail + gap + 2]
    if mode == 'small_b_gap_three':
        assert (first, tail, gap) == (5, 4, 3)
        doubled = [2 * (first + tail + 1), 2 * (first + tail + 2)]
    scaled_values = [integer_determinant([[endpoint * (row == column) - 2 * matrix[row][column]
                                         for column in range(4)] for row in range(4)]) for endpoint in doubled]
    endpoints = [sympy.Rational(endpoint, 2) for endpoint in doubled]
    assert scaled_values == [16 * polynomial.eval(endpoint) for endpoint in endpoints]
    roots = int(polynomial.count_roots(*endpoints))
    margin = 4 * first * tail - (2 * first + 1) * gap ** 2
    if mode == 'weighted':
        assert gap >= 3 and margin >= 0
        assert scaled_values[0] < 0 < scaled_values[1] and roots == 1
    elif mode == 'small_b_gap_three':
        assert scaled_values[0] < 0 < scaled_values[1] and roots == 1
    else:
        assert mode == 'diagnostic' and (first, tail, gap) == (1, 1, 3)
        assert scaled_values == [2944, 5427] and roots == 0
    control.update({'a': first, 'b': tail, 'tail_gap': gap, 'control_mode': mode,
                    'weighted_condition_margin': margin,
                    'quartic_coefficients': [int(value) for value in polynomial.all_coeffs()],
                    'six_direct_integer_determinant_values': values,
                    'two_direct_doubled_matrix_determinants': scaled_values,
                    'restricted_interval': [str(endpoint) for endpoint in endpoints],
                    'sturm_roots_in_interval': roots})
    return control


def main():
    directory = Path(__file__).parent
    helpers = ['check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py']
    report = {'written_theorem': 'Every positive(a,a,b,b+r),r>=3,4ab>=(2a+1)r^2,is nonintegral via the same open half-unit midpoint interval; no ordering condition on a,b.',
              'gap_three_corollary': 'Every positive(a,a,b,b+3)is nonintegral: weighted region covers a,b>=5, four written small-b cubics cover a>=5,b<=4, prior unit/pair-two/three/four results cover a<=4.',
              'symbolic': symbolic_checks(),
              'fixed_controls': [fixed_control(5, 5, 3), fixed_control(5, 9, 4), fixed_control(10, 20, 5),
                                 fixed_control(5, 55, 10), fixed_control(30, 5, 3), fixed_control(100, 600, 30),
                                 fixed_control(5, 4, 3, 'small_b_gap_three'), fixed_control(1, 1, 3, 'diagnostic')],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256((directory / name).read_bytes()).hexdigest() for name in helpers},
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded weighted three-parameter region and complete positive tail-gap-three corollary. Eight specified support/integer-determinant/Sturm controls. No exponent scan, finite exponent base, expanded graph, floating eigensolver, historical finite-base rerun or Lean. General single-pair and fully unequal four-prime classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
