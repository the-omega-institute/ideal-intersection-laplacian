import hashlib
import json
from itertools import permutations
from math import prod
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding


def integer_determinant(matrix):
    size = len(matrix)
    total = 0
    for ordering in permutations(range(size)):
        inversions = sum(ordering[first] > ordering[second]
                         for first in range(size) for second in range(first + 1, size))
        total += (-1) ** inversions * prod(matrix[row][ordering[row]] for row in range(size))
    return total


def symbolic_checks():
    first, tail, gap, variable, growth, excess_gap, margin = sympy.symbols('a b r x u v w')
    matrix = sympy.Matrix(operator(first, tail, tail + gap))
    diagonal = sympy.diag(1, tail + gap, tail, tail * (tail + gap))
    assert diagonal * matrix == matrix.T * diagonal
    polynomial = matrix.charpoly(variable).as_expr()
    midpoint = first + tail + 1 + gap / 2
    positive_bracket = (4 * first ** 2 * tail ** 2 + 4 * first ** 2 * tail * gap
                        + 8 * first ** 2 * tail + 4 * first ** 2 * gap
                        + 4 * first * tail ** 3 + 6 * first * tail ** 2 * gap
                        + 8 * first * tail ** 2 + 2 * first * tail * gap ** 2
                        + 8 * first * tail * gap + 4 * first * tail
                        + 2 * first * gap ** 2 + 2 * first * gap
                        + 4 * tail ** 3 + 6 * tail ** 2 * gap + 4 * tail ** 2
                        + 2 * tail * gap ** 2 + 4 * tail * gap + gap ** 2)
    midpoint_identity = gap ** 2 * (2 * first + 1) * positive_bracket / 16
    assert sympy.expand(polynomial.subs(variable, midpoint) - midpoint_identity) == 0
    assert all(value > 0 for value in sympy.Poly(positive_bracket, first, tail, gap).coeffs())
    lower_expression = sympy.expand(-16 * polynomial.subs(variable, midpoint - sympy.Rational(1, 2)))
    transformed = sympy.Poly(sympy.expand(lower_expression.subs(tail, gap ** 2 + margin)
                                          .subs({first: growth + 1, gap: excess_gap + 2})),
                             growth, excess_gap, margin)
    assert len(transformed.terms()) == 91 and transformed.TC() == 10521
    assert all(value > 0 for value in transformed.coeffs())
    coverage = ((first ** 2 - 1) * (4 * first + gap) + (first - 1) * (2 * first - 1)
                - 2 * first * (2 * first + gap))
    coverage_written = 4 * first ** 3 + (gap - 2) * first ** 2 - (2 * gap + 7) * first + 1 - gap
    assert sympy.expand(coverage - coverage_written) == 0
    lower_coverage = 4 * first ** 3 - 2 * first ** 2 - 8 * first + 1
    assert sympy.expand(coverage_written - lower_coverage
                        - (gap - 2) * first ** 2 - (first - gap) * (2 * first + 1)) == 0
    assert sympy.expand(lower_coverage - (2 * first * (2 * first ** 2 - first - 4) + 1)) == 0
    return {'generic_symmetry_midpoint_identity': 'passed',
            'positive_midpoint_bracket': str(positive_bracket),
            'positive_midpoint_bracket_terms': len(sympy.Poly(positive_bracket, first, tail, gap).terms()),
            'lower_endpoint_negative_identity': str(lower_expression),
            'complete_lower_endpoint_positive_expansion': {
                'substitution': 'a=1+u,r=2+v,b=r^2+w',
                'terms_u_power_v_power_w_power_coefficient':
                [list(monomial) + [int(coefficient)] for monomial, coefficient in transformed.terms()],
                'positive_coefficient_count': 91, 'constant': 10521},
            'new_coverage_family': '(a,a,2a,2a+r),r>=3,a>=r^2',
            'coverage_product_tail_failure_margin': str(coverage_written),
            'coverage_strict_positive_lower_bound': str(lower_coverage)}


def fixed_control(first, tail, gap):
    maximum = tail + gap
    control = support_embedding(first, tail, maximum)
    matrix = operator(first, tail, maximum)
    variable = sympy.Symbol('x')

    def determinant_at(endpoint):
        return integer_determinant([[endpoint * (row == column) - matrix[row][column]
                                     for column in range(4)] for row in range(4)])

    values = [(endpoint, determinant_at(endpoint)) for endpoint in range(6)]
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    assert sympy.Poly(sympy.interpolate(values[:5], variable), variable) == polynomial
    assert polynomial.eval(5) == values[-1][1]
    doubled_endpoints = [2 * first + 2 * tail + gap + 1, 2 * first + 2 * tail + gap + 2]
    scaled_values = [integer_determinant([[endpoint * (row == column) - 2 * matrix[row][column]
                                         for column in range(4)] for row in range(4)])
                     for endpoint in doubled_endpoints]
    endpoints = [sympy.Rational(endpoint, 2) for endpoint in doubled_endpoints]
    assert scaled_values == [16 * polynomial.eval(endpoint) for endpoint in endpoints]
    in_region = gap >= 2 and tail >= gap ** 2
    root_count = int(polynomial.count_roots(*endpoints))
    if in_region:
        assert scaled_values[0] < 0 < scaled_values[1] and root_count == 1
    else:
        assert (first, tail, gap) == (1, 1, 2)
        assert scaled_values == [471, 1584] and root_count == 0
    graph_vertices = control['graph_vertices']
    graph_endpoints = [graph_vertices + 1 - endpoint for endpoint in reversed(endpoints)]
    control.update({'a': first, 'b': tail, 'tail_gap': gap, 'in_midpoint_theorem_region': in_region,
                    'quartic_coefficients': [int(value) for value in polynomial.all_coeffs()],
                    'six_direct_integer_determinant_values': values,
                    'two_direct_doubled_matrix_determinants': scaled_values,
                    'restricted_half_unit_interval': [str(endpoint) for endpoint in endpoints],
                    'graph_half_unit_interval': [str(endpoint) for endpoint in graph_endpoints],
                    'sturm_roots_in_interval': root_count})
    return control


def main():
    dependency = Path(__file__).with_name('check_four_prime_pair_three.py')
    report = {'written_theorem': 'Every positive four-prime vector(a,a,b,b+r),r>=2,b>=r^2,has a restricted root between a+b+(r+1)/2 and a+b+(r+2)/2; this open half-unit interval contains no integer, so the graph is nonintegral. No ordering condition on a and b.',
              'symbolic': symbolic_checks(),
              'fixed_controls': [fixed_control(*control) for control in
                                 ((1, 4, 2), (5, 10, 3), (30, 9, 3), (5, 16, 4),
                                  (25, 50, 5), (100, 200, 10), (1, 1, 2))],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'support_embedding_dependency_sha256': hashlib.sha256(dependency.read_bytes()).hexdigest(),
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded three-parameter region with a positive generic midpoint and complete 91-coefficient lower identity. Seven specified support/integer-determinant/Sturm controls include one limitation outside the hypothesis. No exponent scan, finite exponent base, expanded graph, floating eigensolver, historical finite-base rerun or Lean. General single-pair and fully unequal four-prime classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
