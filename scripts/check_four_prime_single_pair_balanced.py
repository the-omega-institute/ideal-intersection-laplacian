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
    first, middle, maximum, gap, tail_gap, slack = sympy.symbols('a b c d e u')
    matrix = sympy.Matrix(operator(first, middle, maximum))
    diagonal = sympy.diag(1, maximum, middle, middle * maximum)
    assert diagonal * matrix == matrix.T * diagonal
    elementary = lambda entry: sympy.diag(entry + 1, 1)
    disjoint = lambda entry: sympy.Matrix([[1, entry], [1, 0]])
    tensor = ((first + 1) * sympy.kronecker_product(elementary(middle), elementary(maximum))
              + first * sympy.kronecker_product(disjoint(middle), disjoint(maximum)))
    assert matrix == tensor
    supports = range(1, 15)
    exponents = (first, first, middle, maximum)
    weights = {support: prod(entry for index, entry in enumerate(exponents) if support & (1 << index))
               for support in supports}
    basis = [{support: 1 if support == (1 | tail) else -1 if support == (2 | tail) else 0
              for support in supports} for tail in (0, 8, 4, 12)]
    for column, values in enumerate(basis):
        assert sympy.expand(sum(weights[support] * values[support] for support in supports)) == 0
        for support in supports:
            action = sum(weights[neighbor] * (values[support] - values[neighbor])
                         for neighbor in supports if not support & neighbor)
            expected = sum(basis[row][support] * (matrix[row, column] - int(row == column)) for row in range(4))
            assert sympy.expand(action - expected) == 0
    substitution = {first: gap + tail_gap + slack + 6,
                    middle: 2 * gap + tail_gap + slack + 6,
                    maximum: 2 * gap + 2 * tail_gap + slack + 6}
    corner = (first + 1) * (middle + 1) * (maximum + 1) + first - 3
    middle_diagonal = (first + 1) * (middle + 1) - 3
    maximum_diagonal = (first + 1) * (maximum + 1) - 3
    middle_minor = middle_diagonal * maximum_diagonal - first ** 2 * middle * maximum
    third_minor = (corner * middle_minor - first ** 2 *
                   (maximum * maximum_diagonal + middle * middle_diagonal - 2 * first * middle * maximum))
    written_minors = [corner, corner * middle_diagonal - first ** 2 * maximum,
                      third_minor, (first - 2) * third_minor - first ** 2 * middle * maximum * middle_minor]
    expansions = []
    for size, count, constant in zip((1, 2, 3, 4), (20, 56, 84, 83), (346, 15700, 279400, 54880)):
        minor = sympy.expand((matrix - 3 * sympy.eye(4))[:size, :size].det())
        assert sympy.expand(minor - written_minors[size - 1]) == 0
        polynomial = sympy.Poly(sympy.expand(minor.subs(substitution)), gap, tail_gap, slack)
        assert len(polynomial.terms()) == count and polynomial.TC() == constant
        assert all(coefficient > 0 for coefficient in polynomial.coeffs())
        expansions.append({'leading_minor_size': size, 'generic_minor': str(minor),
                           'terms_d_power_e_power_u_power_coefficient':
                           [list(monomial) + [int(coefficient)] for monomial, coefficient in polynomial.terms()]})
    upper = (-(2 * first + 3) * middle * maximum
             + (first ** 2 - 2 * first - 3) * (middle + maximum) + 2 * first ** 2 - 9 * first + 9)
    assert sympy.expand((matrix - 4 * sympy.eye(4)).extract([0, 3], [0, 3]).det() - upper) == 0
    upper_shifted = (-(2 * first + 3) * gap * tail_gap
                     - (first ** 2 + 5 * first + 3) * (gap + tail_gap) - 5 * first ** 2 - 15 * first + 9)
    assert sympy.expand(upper.subs({middle: first + gap, maximum: first + tail_gap}) - upper_shifted) == 0
    product_failure = -middle * maximum + (first ** 2 - 1) * (middle + maximum) + (first - 1) * (2 * first - 1)
    assert sympy.expand((matrix - 2 * sympy.eye(4)).extract([0, 3], [0, 3]).det() - product_failure) == 0
    failure = sympy.Poly(sympy.expand(product_failure.subs(substitution)), gap, tail_gap, slack)
    assert all(coefficient > 0 for coefficient in failure.coeffs())
    first_failure = ((first ** 2 - first - 1) * middle * maximum
                     + (first ** 2 - 1) * (first + 1) * (middle + maximum)
                     + first * (first ** 2 - 1) - (first - 1))
    assert sympy.expand(first_failure - ((first ** 2 - 1) *
                         ((first + 1) * (middle + 1) * (maximum + 1) - 1 - first * middle * maximum)
                         - (first - 1) - first * middle * maximum)) == 0
    other_failure = (((middle ** 2 - 1) * (2 * first + 1) - first ** 2) * maximum
                     + (middle ** 2 - 1) * (first ** 2 + 2 * first) - (middle - 1))
    assert sympy.expand(other_failure - ((middle ** 2 - 1) *
                         ((first + 1) ** 2 * (maximum + 1) - 1 - first ** 2 * maximum)
                         - (middle - 1) - first ** 2 * maximum)) == 0
    return {'tensor_symmetry_generic_support_embedding': 'passed', 'generic_support_column_actions': 56,
            'balanced_substitution': {str(key): str(value) for key, value in substitution.items()},
            'complete_positive_leading_minor_expansions': expansions,
            'positive_leading_minor_coefficients_checked': 243,
            'universal_repeated_minimum_upper_minor_at_four': str(upper),
            'upper_minor_with_independent_tail_offsets': str(upper_shifted),
            'product_failure_margin': str(product_failure),
            'product_failure_transformed_positive_coefficients': len(failure.coeffs()),
            'small_exponent_failure_margins': [str(first_failure), str(other_failure)]}


def fixed_control(first, middle, maximum):
    control = support_embedding(first, middle, maximum)
    matrix = operator(first, middle, maximum)
    variable = sympy.Symbol('x')
    values = []
    for endpoint in range(6):
        shifted = [[endpoint * (row == column) - matrix[row][column] for column in range(4)] for row in range(4)]
        values.append((endpoint, integer_determinant(shifted)))
    interpolated = sympy.Poly(sympy.interpolate(values[:5], variable), variable)
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    assert interpolated == polynomial and polynomial.eval(5) == values[-1][1]
    in_region = first <= middle <= maximum <= 2 * first - 6
    endpoint = 3 if in_region else 2
    leading = [integer_determinant([[matrix[row][column] - endpoint * (row == column)
                                   for column in range(size)] for row in range(size)]) for size in (1, 2, 3, 4)]
    assert all(value > 0 for value in leading)
    assert polynomial.count_roots(endpoint, endpoint + 1) == 1
    if not in_region:
        assert (first, middle, maximum) == (20, 35, 35)
        assert polynomial.eval(3) < 0
    upper_minor = integer_determinant([[matrix[row][column] - 4 * (row == column)
                                       for column in (0, 3)] for row in (0, 3)])
    assert upper_minor < 0
    control.update({'a': first, 'b': middle, 'c': maximum, 'in_balanced_theorem_region': in_region,
                    'quartic_coefficients': [int(value) for value in polynomial.all_coeffs()],
                    'six_direct_integer_determinant_values': values, 'leading_minor_endpoint': endpoint,
                    'leading_minors': leading, 'empty_full_minor_at_four': upper_minor,
                    'smallest_restricted_root_interval': [endpoint, endpoint + 1], 'sturm_roots_in_interval': 1})
    return control


def main():
    dependency = Path(__file__).with_name('check_four_prime_pair_three.py')
    report = {'written_theorem': 'Every positive integer four-prime vector(a,a,b,c),a<=b<=c<=2a-6,has 3<kappa_min(K)<4 and a noninteger graph eigenvalue in(V-3,V-2).',
              'additional_upper_bound': 'kappa_min(K)<4 for every a>=5,b>=a,c>=a; not a complete single-pair nonintegrality theorem.',
              'symbolic': symbolic_checks(),
              'fixed_controls': [fixed_control(*control) for control in
                                 ((6, 6, 6), (7, 7, 8), (8, 9, 10), (10, 11, 14), (30, 40, 54), (20, 35, 35))],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'support_embedding_dependency_sha256': hashlib.sha256(dependency.read_bytes()).hexdigest(),
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded three-parameter theorem with complete positive identities. Six specified support/integer-determinant/Sturm controls, including a neighboring-boundary limitation. No exponent scan, finite exponent base, expanded vertex graph, floating eigensolver, historical finite-base rerun or Lean. General single-pair and fully unequal four-prime classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
