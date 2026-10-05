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
    first, middle, maximum, variable, slack = sympy.symbols('a b c x u')
    matrix = sympy.Matrix(operator(first, middle, maximum))
    diagonal = sympy.diag(1, maximum, middle, middle * maximum)
    assert diagonal * matrix == matrix.T * diagonal
    polynomial = matrix.charpoly(variable).as_expr()
    lower = first * middle * (middle - maximum) * (first + middle + 1) * (
        first * middle * maximum + first * middle - first * maximum + middle * maximum)
    upper = -first * maximum * (middle - maximum) * (first + maximum + 1) * (
        first * middle * maximum - first * middle + first * maximum + middle * maximum)
    assert sympy.expand(polynomial.subs(variable, first + middle + 1) - lower) == 0
    assert sympy.expand(polynomial.subs(variable, first + maximum + 1) - upper) == 0
    assert sympy.expand(first * maximum * (middle - 1) + first * middle + middle * maximum
                        - (first * middle * maximum + first * middle - first * maximum + middle * maximum)) == 0
    assert sympy.expand(first * middle * (maximum - 1) + first * maximum + middle * maximum
                        - (first * middle * maximum - first * middle + first * maximum + middle * maximum)) == 0
    gap_two_midpoint = (2 * first + 1) * (
        first ** 2 * middle ** 2 + 4 * first ** 2 * middle + 2 * first ** 2
        + first * middle ** 3 + 5 * first * middle ** 2 + 7 * first * middle + 3 * first
        + middle ** 3 + 4 * middle ** 2 + 4 * middle + 1)
    assert sympy.expand(polynomial.subs({maximum: middle + 2, variable: first + middle + 2})
                        - gap_two_midpoint) == 0
    positive_midpoint = sympy.Poly(sympy.expand(gap_two_midpoint), first, middle)
    assert len(positive_midpoint.coeffs()) == 15 and all(coefficient > 0 for coefficient in positive_midpoint.coeffs())
    coverage = []
    for gap, expected in ((1, [4, 59, 281, 430]), (2, [4, 60, 289, 444])):
        failure = ((first ** 2 - 1) * (middle + maximum) + (first - 1) * (2 * first - 1)
                   - middle * maximum)
        specialized = sympy.expand(failure.subs({middle: 2 * first, maximum: 2 * first + gap}))
        written = 4 * first ** 3 + (gap - 2) * first ** 2 - (2 * gap + 7) * first + 1 - gap
        assert sympy.expand(specialized - written) == 0
        shifted = sympy.Poly(specialized.subs(first, slack + 5), slack)
        assert shifted.all_coeffs() == expected
        coverage.append({'tail_gap': gap, 'product_tail_failure_margin_at_b_equals_2a': str(written),
                         'positive_coefficients_at_a_equals_5_plus_u_descending': expected})
    return {'generic_symmetry_and_two_endpoint_factorizations': 'passed',
            'characteristic_polynomial_at_a_plus_b_plus_one': str(lower),
            'characteristic_polynomial_at_a_plus_c_plus_one': str(upper),
            'tail_gap_two_midpoint_identity': str(gap_two_midpoint),
            'midpoint_positive_coefficient_count': len(positive_midpoint.coeffs()),
            'new_coverage_families': coverage}


def fixed_control(first, middle, gap):
    maximum = middle + gap
    control = support_embedding(first, middle, maximum)
    matrix = operator(first, middle, maximum)
    variable = sympy.Symbol('x')

    def determinant_at(endpoint):
        return integer_determinant([[endpoint * (row == column) - matrix[row][column]
                                     for column in range(4)] for row in range(4)])

    values = [(endpoint, determinant_at(endpoint)) for endpoint in range(6)]
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    assert sympy.Poly(sympy.interpolate(values[:5], variable), variable) == polynomial
    assert polynomial.eval(5) == values[-1][1]
    lower = first + middle + 1
    upper = lower + 1
    endpoint_values = [determinant_at(endpoint) for endpoint in (lower, upper)]
    assert endpoint_values[0] < 0 < endpoint_values[1]
    assert endpoint_values == [polynomial.eval(endpoint) for endpoint in (lower, upper)]
    assert polynomial.count_roots(lower, upper) == 1
    graph_vertices = control['graph_vertices']
    control.update({'a': first, 'b': middle, 'tail_gap': gap,
                    'quartic_coefficients': [int(value) for value in polynomial.all_coeffs()],
                    'six_direct_integer_determinant_values': values,
                    'two_direct_interval_endpoint_values': endpoint_values,
                    'restricted_root_interval': [lower, upper],
                    'graph_root_interval': [graph_vertices - first - middle - 1, graph_vertices - first - middle],
                    'sturm_roots_in_interval': 1})
    return control


def main():
    dependency = Path(__file__).with_name('check_four_prime_pair_three.py')
    report = {'written_theorem': 'Every positive integer four-prime vector(a,a,b,b+r),r in {1,2},has a restricted root in(a+b+1,a+b+2) and a noninteger graph eigenvalue in(V-a-b-1,V-a-b); no ordering or size condition on a,b.',
              'general_root_window': 'Every positive integer a,b,c with b<c has a restricted root in(a+b+1,a+c+1); for wider tail gaps this interval alone does not exclude integers.',
              'symbolic': symbolic_checks(),
              'fixed_controls': [fixed_control(*control) for control in
                                 ((1, 1, 1), (5, 1, 2), (5, 10, 1), (20, 40, 2), (7, 50, 1), (30, 60, 2))],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'support_embedding_dependency_sha256': hashlib.sha256(dependency.read_bytes()).hexdigest(),
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded two-parameter nonintegrality families and a general wider root window, supported by six specified exact support/integer-determinant/Sturm controls. No exponent scan, finite exponent base, expanded vertex graph, floating eigensolver, historical finite-base rerun or Lean. General single-pair and fully unequal four-prime classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
