import hashlib
import json
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def symbolic_checks():
    first, tail, gap, variable, slack, margin, growth = sympy.symbols('a b r x v z s')
    matrix = sympy.Matrix(operator(first, tail, tail + gap))
    diagonal = sympy.diag(1, tail + gap, tail, tail * (tail + gap))
    assert diagonal * matrix == matrix.T * diagonal
    polynomial = matrix.charpoly(variable).as_expr()
    midpoint = first + tail + 1 + gap / 2
    bracket = sympy.Poly(sympy.cancel(16 * polynomial.subs(variable, midpoint)
                                     / (gap ** 2 * (2 * first + 1))), first, tail, gap)
    assert len(bracket.terms()) == 18 and all(value > 0 for value in bracket.coeffs())
    lower = -8192 * first ** 3 * polynomial.subs(variable, midpoint - 1)
    substituted = sympy.cancel(lower.subs(tail, ((2 * first + 1) * gap ** 2 + margin) / (8 * first)))
    expansion = sympy.Poly(sympy.expand(substituted.subs(gap, slack + 2)), first, slack, margin)
    assert len(expansion.terms()) == 128 and expansion.TC() == 1024
    assert all(value > 0 for value in expansion.coeffs())
    small_tail_rows = []
    expected = {1: [42, 91, 108, 54], 2: [48, 84, 189, 153],
                3: [22, 209, 608, 889], 4: [48, 848, 1657, 272]}
    for value in (1, 2, 3, 4):
        endpoint = sympy.expand(polynomial.subs({gap: 4, tail: value, variable: first + value + 2}))
        if value == 3:
            shifted = endpoint.subs(first, growth + 5).expand()
        elif value == 4:
            shifted = -endpoint.subs(first, growth + 1).expand()
        else:
            shifted = endpoint.subs(first, growth)
        coefficients = sympy.Poly(shifted, growth).all_coeffs()
        assert coefficients == expected[value] and all(coefficient > 0 for coefficient in coefficients)
        small_tail_rows.append({'b': value, 'p_at_a_plus_b_plus_2': str(endpoint),
                                'positive_expression': str(shifted),
                                'positive_variable': 'a-5' if value == 3 else 'a-1' if value == 4 else 'a',
                                'endpoint_sign': 'negative' if value == 4 else 'positive',
                                'positive_coefficients_descending': [int(value) for value in coefficients]})
    first_slack, tail_slack = sympy.symbols('u w')
    gap_four_margin = sympy.expand((8 * first * tail - 16 * (2 * first + 1))
                                   .subs({first: first_slack + 5, tail: tail_slack + 5}))
    assert gap_four_margin == 8 * first_slack * tail_slack + 8 * first_slack + 40 * tail_slack + 24
    family_first, family_tail, family_gap = 2 * growth, 4 * growth ** 2 + growth, 4 * growth
    substitutions = {first: family_first, tail: family_tail, gap: family_gap}
    assert sympy.expand((8 * first * tail - (2 * first + 1) * gap ** 2).subs(substitutions)) == 0
    old_margin = sympy.expand((4 * first * tail - (2 * first + 1) * gap ** 2).subs(substitutions))
    assert sympy.expand(old_margin + 8 * growth ** 2 * (4 * growth + 1)) == 0
    failure = sympy.expand(((first ** 2 - 1) * (2 * tail + gap) + (first - 1) * (2 * first - 1)
                           - tail * (tail + gap)).subs(substitutions))
    assert sympy.expand(failure - (growth - 1) * (16 * growth ** 3 + 16 * growth ** 2 + 11 * growth - 1)) == 0
    return {'generic_symmetry_and_positive_midpoint': 'passed', 'positive_midpoint_bracket': str(bracket.as_expr()),
            'even_gap_lower_endpoint_positive_expansion': {
                'identity': '-8192a^3 p(m-1),r=2+v,b=((2a+1)r^2+z)/(8a)',
                'terms_a_power_v_power_z_power_coefficient':
                [list(monomial) + [int(coefficient)] for monomial, coefficient in expansion.terms()],
                'positive_coefficient_count': 128, 'constant': 1024},
            'gap_four_small_tail_rows': small_tail_rows,
            'gap_four_a_b_at_least_five_margin': str(gap_four_margin),
            'new_equality_family': '(2s,2s,4s^2+s,4s^2+5s),s>=3',
            'new_family_previous_weighted_margin': str(old_margin),
            'new_family_product_tail_failure': str(failure)}


def fixed_control(first, tail, gap, mode='even'):
    control = support_embedding(first, tail, tail + gap)
    matrix = operator(first, tail, tail + gap)
    variable = sympy.Symbol('x')
    values = [(endpoint, integer_determinant([[endpoint * (row == column) - matrix[row][column]
                                              for column in range(4)] for row in range(4)]))
              for endpoint in range(6)]
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    assert sympy.Poly(sympy.interpolate(values[:5], variable), variable) == polynomial
    assert polynomial.eval(5) == values[-1][1]
    assert gap % 2 == 0
    endpoints = [first + tail + gap // 2, first + tail + gap // 2 + 1]
    if mode == 'small_tail_positive':
        assert gap == 4 and tail <= 3 and first >= 5
        endpoints = [first + tail + 1, first + tail + 2]
    endpoint_values = [integer_determinant([[endpoint * (row == column) - matrix[row][column]
                                           for column in range(4)] for row in range(4)]) for endpoint in endpoints]
    assert endpoint_values == [polynomial.eval(endpoint) for endpoint in endpoints]
    roots = int(polynomial.count_roots(*endpoints))
    margin = 8 * first * tail - (2 * first + 1) * gap ** 2
    if mode == 'even':
        assert gap >= 2 and margin >= 0
        assert endpoint_values[0] < 0 < endpoint_values[1] and roots == 1
    elif mode in ('small_tail_positive', 'small_tail_negative'):
        if mode == 'small_tail_negative':
            assert gap == 4 and tail == 4
        assert endpoint_values[0] < 0 < endpoint_values[1] and roots == 1
    else:
        assert mode == 'diagnostic' and (first, tail, gap) == (5, 5, 6)
        assert endpoint_values == [115624, 510741] and roots == 0
    vertices = control['graph_vertices']
    control.update({'a': first, 'b': tail, 'tail_gap': gap, 'control_mode': mode,
                    'even_condition_margin': margin,
                    'previous_weighted_condition_margin': 4 * first * tail - (2 * first + 1) * gap ** 2,
                    'quartic_coefficients': [int(value) for value in polynomial.all_coeffs()],
                    'six_direct_integer_determinant_values': values,
                    'two_direct_endpoint_determinants': endpoint_values,
                    'restricted_interval': endpoints,
                    'graph_interval': [vertices + 1 - endpoint for endpoint in reversed(endpoints)],
                    'sturm_roots_in_interval': roots})
    return control


def main():
    directory = Path(__file__).parent
    helpers = ['check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py']
    report = {'written_theorem': 'Every positive(a,a,b,b+r),even r>=2,8ab>=(2a+1)r^2,is nonintegral via a restricted root in(a+b+r/2,a+b+r/2+1); no ordering between a,b; equality included.',
              'gap_four_corollary': 'Every positive(a,a,b,b+4)is nonintegral: a,b>=5 satisfy the even bound; three positive small-tail cubics and one negative cubic cover a>=5,b<=4; prior unit/pair-two/three/four proofs cover a<=4.',
              'symbolic': symbolic_checks(),
              'fixed_controls': [fixed_control(1, 3, 2), fixed_control(5, 5, 4), fixed_control(10, 20, 8),
                                 fixed_control(6, 39, 12), fixed_control(10, 105, 20),
                                 fixed_control(5, 3, 4, 'small_tail_positive'),
                                 fixed_control(5, 4, 4, 'small_tail_negative'),
                                 fixed_control(5, 5, 6, 'diagnostic')],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256((directory / name).read_bytes()).hexdigest() for name in helpers},
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded even-gap three-parameter region and complete positive tail-gap-four corollary. Eight specified support/integer-determinant/Sturm controls including two equality examples and one outside-condition diagnostic. No exponent scan, finite exponent base, expanded graph, floating eigensolver, historical finite-base rerun or Lean. General single-pair and fully unequal four-prime classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
