import hashlib
import json
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def tail_bound(first, tail):
    endpoint = (first + 1) * (tail + 1)
    return 24 * (endpoint + first) ** 3 * (3 * endpoint + first)


def symbolic_checks():
    first, tail, maximum, variable = sympy.symbols('a b c x')
    matrix = sympy.Matrix(operator(first, tail, maximum))
    diagonal = sympy.diag(1, maximum, tail, tail * maximum)
    assert diagonal * matrix == matrix.T * diagonal
    endpoint = (first + 1) * (tail + 1)
    constant_matrix = sympy.Matrix(operator(first, tail, 0))
    slope_matrix = sympy.Matrix([[endpoint, first, 0, first * tail], [0, 0, 0, 0],
                                [0, first, first + 1, 0], [0, 0, 0, 0]])
    assert (matrix - constant_matrix - maximum * slope_matrix).applyfunc(sympy.expand) == sympy.zeros(4)
    polynomial = matrix.charpoly(variable).as_expr()
    tail_polynomial = sympy.Poly(polynomial, maximum)
    assert tail_polynomial.degree() == 2
    leading = ((first + 1) ** 2 * (tail + 1) * variable ** 2
               - (first + 1) * (tail + 1) * (first ** 2 + 2 * first * tail + 4 * first + tail + 2) * variable
               + (2 * first + 1) * (first + tail + 1) * (2 * first * tail + first + tail + 1))
    assert sympy.expand(tail_polynomial.nth(2) - leading) == 0
    leading_polynomial = sympy.Poly(leading, variable)
    root_sum = sympy.cancel(-leading_polynomial.nth(1) / leading_polynomial.nth(2))
    assert sympy.cancel(root_sum - first - 2 * tail - 3 + (tail + 1) / (first + 1)) == 0
    assert sympy.rem(leading_polynomial.nth(0), first + 1, first) == tail ** 2
    assert sympy.expand(leading.subs(variable, first + 1) + first ** 2 * tail ** 2 * (2 * first + 1)) == 0
    shifted = diagonal * (matrix - (first + 1) * sympy.eye(4))
    inner = shifted.extract([1, 2], [1, 2])
    assert (inner - tail * maximum * sympy.Matrix([[first + 1, first], [first, first + 1]])).applyfunc(sympy.expand) == sympy.zeros(2)
    outer = shifted.extract([0, 3], [0, 3])
    coupling = shifted.extract([0, 3], [1, 2])
    schur = outer - coupling * inner.inv() * coupling.T
    assert sympy.cancel(schur.det() + first ** 2 * tail ** 2 * maximum ** 2) == 0
    assert schur[1, 1] == 0 and schur[0, 1] == first * tail * maximum
    size = endpoint + first
    linear_bound = 48 * endpoint * size ** 3
    constant_bound = 24 * size ** 4
    assert sympy.expand(linear_bound + constant_bound - tail_bound(first, tail)) == 0
    product_failure = ((first ** 2 - 1) * (tail + maximum) + (first - 1) * (2 * first - 1)
                       - tail * maximum)
    family_failure = ((first ** 2 - first - 1) * maximum + first ** 3 + 2 * first ** 2 - 4 * first + 1)
    assert sympy.expand(product_failure.subs(tail, first) - family_failure) == 0
    return {'generic_symmetry_and_linear_tail_matrix': 'passed',
            'tail_quadratic_leading_polynomial': str(leading),
            'tail_quadratic_linear_coefficient': str(tail_polynomial.nth(1)),
            'tail_quadratic_constant_coefficient': str(tail_polynomial.nth(0)),
            'leading_root_sum': str(root_sum),
            'leading_constant_remainder_modulo_a_plus_1': str(tail ** 2),
            'leading_at_a_plus_1': str(sympy.factor(leading.subs(variable, first + 1))),
            'schur_inertia_determinant': '-a^2 b^2 c^2',
            'two_bounded_distinct_roots': '1<=kappa_1<a+1<kappa_2<=(a+1)(b+1)',
            'linear_tail_coefficient_bound': '48 M (M+a)^3',
            'constant_tail_coefficient_bound': '24 (M+a)^4',
            'explicit_tail_cutoff': '24(M+a)^3(3M+a),M=(a+1)(b+1)',
            'triple_minimum_product_tail_failure': str(family_failure)}


def fixed_control(first, tail, maximum=None):
    bound = tail_bound(first, tail)
    in_region = maximum is None
    maximum = bound + 1 if in_region else maximum
    endpoint = (first + 1) * (tail + 1)
    matrix = operator(first, tail, maximum)
    control = support_embedding(first, tail, maximum)
    variable = sympy.Symbol('x')
    values = [(anchor, integer_determinant([[anchor * (row == column) - matrix[row][column]
                                            for column in range(4)] for row in range(4)]))
              for anchor in range(6)]
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    assert sympy.Poly(sympy.interpolate(values[:5], variable), variable) == polynomial
    assert polynomial.eval(5) == values[-1][1]
    assert polynomial.count_roots(1, first + 1) == 1
    assert polynomial.count_roots(first + 1, endpoint) == 1
    assert polynomial.eval(first + 1) != 0
    precision = sympy.Rational(1, 4)
    witness = None
    while witness is None:
        low_intervals = polynomial.intervals(eps=precision)[:2]
        for interval, multiplicity in low_intervals:
            lower, upper = interval
            anchor = int(sympy.floor(lower))
            if lower != upper and upper <= anchor + 1 and polynomial.eval(anchor) != 0 and polynomial.eval(anchor + 1) != 0:
                witness = [anchor, anchor + 1]
                break
        precision /= 2
    endpoint_values = [integer_determinant([[anchor * (row == column) - matrix[row][column]
                                           for column in range(4)] for row in range(4)]) for anchor in witness]
    assert endpoint_values == [polynomial.eval(anchor) for anchor in witness]
    assert endpoint_values[0] * endpoint_values[1] < 0 and polynomial.count_roots(*witness) == 1
    if not in_region:
        assert (first, tail, maximum) == (5, 5, 11) and maximum < bound
    vertices = control['graph_vertices']
    control.update({'a': first, 'b': tail, 'c': maximum, 'tail_bound': bound,
                    'in_large_tail_region': in_region,
                    'bounded_root_upper_endpoint': endpoint,
                    'two_low_root_isolating_intervals': [[str(value) for value in interval] for interval, multiplicity in low_intervals],
                    'root_counts_below_and_above_a_plus_1': [1, 1],
                    'quartic_coefficients': [int(value) for value in polynomial.all_coeffs()],
                    'six_direct_integer_determinant_values': values,
                    'two_direct_witness_endpoint_determinants': endpoint_values,
                    'restricted_noninteger_witness_interval': witness,
                    'graph_noninteger_witness_interval': [vertices + 1 - anchor for anchor in reversed(witness)],
                    'sturm_roots_in_witness_interval': 1})
    return control


def main():
    directory = Path(__file__).parent
    helpers = ['check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py']
    report = {'written_theorem': 'For all positive integers a,b, every four-prime(a,a,b,c)with c>24(M+a)^3(3M+a),M=(a+1)(b+1),is nonintegral. Thus integral tails are finite for each fixed pair(a,b); this conservative cutoff does not complete the unbounded classification.',
              'symbolic': symbolic_checks(),
              'fixed_controls': [fixed_control(1, 1), fixed_control(5, 5), fixed_control(5, 6),
                                 fixed_control(5, 11), fixed_control(10, 20), fixed_control(30, 5),
                                 fixed_control(5, 5, 11)],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256((directory / name).read_bytes()).hexdigest() for name in helpers},
              'sympy_version': sympy.__version__,
              'scope': 'Written uniform effective large-tail theorem using two bounded distinct roots, a nonsplitting leading quadratic, and a determinant coefficient majorant. Seven fixed support/integer-determinant/exact root-isolation/Sturm controls. The below-bound diagnostic has an independently certified noninteger root and does not establish any converse. No exponent scan, finite exponent base, expanded graph, floating eigensolver, historical finite-base rerun or Lean. General single-pair and fully unequal four-prime classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
