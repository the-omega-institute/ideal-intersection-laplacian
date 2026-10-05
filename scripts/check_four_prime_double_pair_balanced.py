import hashlib
import json
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding


def cubic_block(first, second):
    return sympy.Matrix([[(first + 1) * (second + 1) ** 2 + first, 2 * first * second, first * second ** 2],
                         [first, (2 * first + 1) * second + first + 1, 0],
                         [first, 0, first + 1]])


def symbolic_checks():
    first, second, variable, gap, slack = sympy.symbols('a b x d u')
    full = sympy.Matrix(operator(first, second, second))
    block = cubic_block(first, second)
    embedding = sympy.Matrix([[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]])
    antisymmetric = sympy.Matrix([0, 1, -1, 0])
    assert (full * embedding - embedding * block).applyfunc(sympy.expand) == sympy.zeros(4, 3)
    assert (full * antisymmetric - (first + second + 1) * antisymmetric).applyfunc(sympy.expand) == sympy.zeros(4, 1)
    diagonal = sympy.diag(1, 2 * second, second ** 2)
    assert diagonal * block == block.T * diagonal
    polynomial = block.charpoly(variable).as_expr()
    assert sympy.expand(full.charpoly(variable).as_expr() - (variable - first - second - 1) * polynomial) == 0
    expressions = [(block - 3 * sympy.eye(3))[:size, :size].det() for size in (1, 2, 3)]
    expressions.append(polynomial.subs(variable, 4))
    first_minor = (first + 1) * (second + 1) ** 2 + first - 3
    assert sympy.expand(expressions[0] - first_minor) == 0
    assert sympy.expand(expressions[1] - first_minor * ((2 * first + 1) * second + first - 2) + 2 * first ** 2 * second) == 0
    assert sympy.expand(expressions[2] + polynomial.subs(variable, 3)) == 0
    expected = {2: [8, 4, 24, 180, 138, 26, 375, 1534, 1314, 12, 255, 1894, 5542, 4636, 2, 56, 602, 3052, 7060, 5488],
                3: [16, 48, 376, 52, 852, 3354, 24, 644, 5370, 14193, 4, 180, 2533, 14385, 28728, 12, 322, 3201, 13941, 22437]}
    expansions = []
    for index, expression in enumerate(expressions):
        transformed = sympy.Poly(sympy.expand(expression.subs({first: gap + slack + 6, second: 2 * gap + slack + 6})), gap, slack)
        assert all(coefficient > 0 for coefficient in transformed.coeffs())
        assert len(transformed.terms()) == (10, 21, 20, 20)[index]
        if index in expected:
            assert transformed.coeffs() == expected[index]
        expansions.append({'identity': 'leading_minor_' + str(index + 1) + '_at_three' if index < 3 else 'cubic_at_four',
                           'terms_d_power_u_power_coefficient': [list(monomial) + [int(coefficient)] for monomial, coefficient in transformed.terms()]})
    pair_margins = [2 * (first ** 2 - 1) * second + (first - 1) * (2 * first - 1) - second ** 2,
                    2 * (second ** 2 - 1) * first + (second - 1) * (2 * second - 1) - first ** 2]
    assert sympy.expand((full - 2 * sympy.eye(4)).extract([0, 3], [0, 3]).det() - pair_margins[0]) == 0
    swapped = sympy.Matrix(operator(second, first, first))
    assert sympy.expand((swapped - 2 * sympy.eye(4)).extract([0, 3], [0, 3]).det() - pair_margins[1]) == 0
    first_failure = ((first ** 2 - first - 1) * second ** 2 + 2 * (first ** 2 - 1) * (first + 1) * second
                     + first * (first ** 2 - 1) - (first - 1))
    second_failure = (second ** 2 - 1) * ((2 * first + 1) * second + 2 * first) + first ** 2 * (second ** 2 - second - 1) - (second - 1)
    assert sympy.expand(first_failure - ((first ** 2 - 1) * (second ** 2 + 2 * (first + 1) * second + first) - (first - 1) - first * second ** 2)) == 0
    assert sympy.expand(second_failure - ((second ** 2 - 1) * ((2 * first + 1) * second + first ** 2 + 2 * first) - (second - 1) - first ** 2 * second)) == 0
    comparisons = []
    for expression in pair_margins + [first_failure, second_failure]:
        transformed = sympy.Poly(sympy.expand(expression.subs({first: gap + slack + 6, second: 2 * gap + slack + 6})), gap, slack)
        assert all(coefficient > 0 for coefficient in transformed.coeffs())
        comparisons.append({'failure_margin': str(sympy.expand(expression)), 'transformed_coefficient_count': len(transformed.coeffs()),
                            'all_transformed_coefficients_strictly_positive': True})
    return {'invariant_embedding_scalar_symmetry_characteristic_factorization': 'passed',
            'cubic_coefficients_in_a_b': [str(sympy.factor(value)) for value in sympy.Poly(polynomial, variable).all_coeffs()],
            'positive_expansions': expansions, 'positive_minor_endpoint_coefficients_checked': 71,
            'criterion_failure_margins': comparisons}


def fixed_control(first, second):
    control = support_embedding(first, second, second)
    block = cubic_block(first, second)
    variable = sympy.Symbol('x')
    values = [(endpoint, int((endpoint * sympy.eye(3) - block).det(method='bareiss'))) for endpoint in (0, 1, 2, 3, 4)]
    interpolated = sympy.Poly(sympy.interpolate(values[:4], variable), variable)
    polynomial = sympy.Poly(block.charpoly(variable).as_expr(), variable)
    assert interpolated == polynomial and polynomial.eval(4) == values[-1][1]
    in_region = first <= second <= 2 * first - 6
    endpoint = 3 if in_region else 2
    leading = [int((block - endpoint * sympy.eye(3))[:size, :size].det(method='bareiss')) for size in (1, 2, 3)]
    assert all(value > 0 for value in leading)
    assert polynomial.eval(endpoint) < 0 < polynomial.eval(endpoint + 1)
    assert polynomial.count_roots(endpoint, endpoint + 1) == 1
    if not in_region:
        assert (first, second) == (20, 35)
        assert second == 2 * first - 5
        assert [polynomial.eval(value) for value in (2, 3, 4)] == [-39374484, 222118, 39761312]
    control.update({'a': first, 'b': second, 'in_balanced_theorem_region': in_region,
                    'cubic_coefficients': [int(value) for value in polynomial.all_coeffs()],
                    'five_direct_bareiss_values': values, 'leading_minor_endpoint': endpoint, 'leading_minors': leading,
                    'smallest_restricted_root_interval': [endpoint, endpoint + 1], 'sturm_roots_in_interval': 1})
    return control


def main():
    dependency = Path(__file__).with_name('check_four_prime_pair_three.py')
    report = {'written_theorem': 'Every four-prime vector(a,a,b,b),a<=b<=2a-6,has 3<kappa_min(K)<4 and a noninteger graph eigenvalue in(V-3,V-2). This is an unbounded sufficient region, not a full double-pair classification.',
              'symbolic': symbolic_checks(), 'fixed_controls': [fixed_control(*pair) for pair in ((6, 6), (7, 8), (10, 14), (30, 54), (20, 35))],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'support_embedding_dependency_sha256': hashlib.sha256(dependency.read_bytes()).hexdigest(),
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded two-parameter region with complete positive identities; five specified exact support/Bareiss/Sturm controls, including an offset-five limitation. No finite exponent base, expanded graph, exponent scan, floating eigensolver, historical finite rerun or Lean. General higher-prime Q3 remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
