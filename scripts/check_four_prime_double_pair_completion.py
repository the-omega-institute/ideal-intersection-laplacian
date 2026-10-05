import hashlib
import json
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding


def cubic_block(first, second):
    return sympy.Matrix([[(first + 1) * (second + 1) ** 2 + first, 2 * first * second, first * second ** 2],
                         [first, (2 * first + 1) * second + first + 1, 0],
                         [first, 0, first + 1]])


def endpoint_polynomial(endpoint, first, second):
    if endpoint == 2:
        return ((2 * first + 1) * second ** 3 - (first - 1) * (4 * first ** 2 + 6 * first + 1) * second ** 2
                - (first - 1) * (4 * first ** 2 - 3) * second - (first - 1) ** 2 * (2 * first - 1))
    return ((first + 2) * (2 * first + 1) * second ** 3 - first * (first - 2) * (4 * first + 5) * second ** 2
            - 2 * (first - 2) * (2 * first ** 2 - 2 * first - 3) * second - 2 * (first - 2) ** 2 * (first - 1))


def symbolic_checks():
    first, second, variable, slack, gap = sympy.symbols('a b x u d')
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
    endpoints = {}
    for endpoint in (2, 3):
        expression = endpoint_polynomial(endpoint, first, second)
        assert sympy.expand(polynomial.subs(variable, endpoint) - expression) == 0
        endpoints[str(endpoint)] = [str(sympy.factor(value)) for value in sympy.Poly(expression, second).all_coeffs()]
        shifted = block - endpoint * sympy.eye(3)
        top = (first + 1) * (second + 1) ** 2 + first - endpoint
        middle = (2 * first + 1) * second + first + 1 - endpoint
        assert sympy.expand(shifted[:2, :2].det() - top * middle + 2 * first ** 2 * second) == 0
    unit_minor = (full - 2 * sympy.eye(4)).extract([0, 3], [0, 3]).det().subs(first, 1)
    assert sympy.expand(unit_minor + second ** 2) == 0
    upper = sympy.Poly(sympy.expand(polynomial.subs({variable: 4, first: slack + 2, second: slack + gap + 2})), slack, gap)
    expected_upper = [4, 12, 8, 68, 130, 4, 80, 367, 489, 24, 246, 759, 717, 35, 233, 503, 353]
    assert upper.coeffs() == expected_upper
    assert len(upper.terms()) == 17 and all(value > 0 for value in upper.coeffs())
    expansions = [{'identity': 'p(4),a=2+u,b=a+d',
                   'terms_u_power_d_power_coefficient': [list(monomial) + [int(value)] for monomial, value in upper.terms()]}]
    brackets = [(2, 2 * first ** 2 - 2, 2, -1, [4, 36, 124, 201, 154, 45]),
                (2, 2 * first ** 2 - 1, 2, 1, [4, 48, 220, 483, 504, 200]),
                (3, 2 * first - 6, 13, -1, [4, 250, 5388, 48806, 159264]),
                (3, 2 * first - 5, 13, 1, [4, 146, 1839, 8839, 10452])]
    for endpoint, anchor, threshold, sign, expected in brackets:
        expression = sign * endpoint_polynomial(endpoint, first, anchor)
        shifted = sympy.Poly(sympy.expand(expression.subs(first, slack + threshold)), slack)
        assert shifted.all_coeffs() == expected
        assert all(value > 0 for value in shifted.coeffs())
        expansions.append({'endpoint': endpoint, 'exponent_anchor': str(anchor), 'a_shift': threshold,
                           'sign': sign, 'coefficients_in_descending_u_power': expected})
    assert sympy.expand(endpoint_polynomial(3, 2, second) - 20 * second ** 3) == 0
    return {'generic_embedding_symmetry_characteristic_endpoint_identities': 'passed', 'endpoint_cubic_coefficients': endpoints,
            'unit_empty_full_minor_at_two': '-b^2', 'positive_expansions': expansions, 'positive_coefficients_checked': 39}


def horner(coefficients, argument):
    result = 0
    for coefficient in coefficients:
        result = result * argument + coefficient
    return result


def fixed_endpoint_rows():
    variable = sympy.Symbol('b')
    small = []
    for exponent, expected in ((3, 428), (4, 408)):
        value = int(endpoint_polynomial(3, exponent, exponent))
        independent = -int((cubic_block(exponent, exponent) - 3 * sympy.eye(3)).det(method='bareiss'))
        assert value == independent == expected > 0
        small.append({'a': exponent, 'P3_at_b_equals_a': value, 'unique_positive_b_root_below_a': True})
    rows = []
    expected_rows = [(5, 5, -932, 1728), (6, 7, -1784, 4896), (7, 9, -2730, 11100),
                     (8, 11, -3518, 21816), (9, 13, -3800, 38808), (10, 15, -3132, 64128),
                     (11, 17, -974, 100116), (12, 18, -115600, 3310)]
    for exponent, anchor, lower, upper in expected_rows:
        coefficients = [int(value) for value in sympy.Poly(endpoint_polynomial(3, exponent, variable), variable).all_coeffs()]
        assert coefficients[0] > 0 and all(value < 0 for value in coefficients[1:])
        values = [horner(coefficients, argument) for argument in (anchor, anchor + 1)]
        independent = [-int((cubic_block(exponent, argument) - 3 * sympy.eye(3)).det(method='bareiss')) for argument in (anchor, anchor + 1)]
        assert values == independent == [lower, upper] and lower < 0 < upper
        rows.append({'a': exponent, 'h': anchor, 'coefficients_in_b': coefficients, 'P3_at_h': lower, 'P3_at_h_plus_one': upper})
    return {'a_two_identity': 'P3(2,b)=20b^3', 'two_small_positive_values': small, 'all_eight_bracket_rows': rows,
            'independent_bareiss_determinants': 18}


def witness_interval(first, second):
    if first == 1 or second >= 2 * first ** 2 - 1:
        return 1, 2
    if first <= 4:
        return 2, 3
    anchors = {5: 5, 6: 7, 7: 9, 8: 11, 9: 13, 10: 15, 11: 17, 12: 18}
    third_anchor = anchors[first] if first <= 12 else 2 * first - 6
    return (3, 4) if second <= third_anchor else (2, 3)


def fixed_control(first, second):
    control = support_embedding(first, second, second)
    block = cubic_block(first, second)
    variable = sympy.Symbol('x')
    values = [(endpoint, int((endpoint * sympy.eye(3) - block).det(method='bareiss'))) for endpoint in (0, 1, 2, 3, 4)]
    polynomial = sympy.Poly(block.charpoly(variable).as_expr(), variable)
    assert sympy.Poly(sympy.interpolate(values[:4], variable), variable) == polynomial
    assert polynomial.eval(4) == values[-1][1]
    lower, upper = witness_interval(first, second)
    leading = [int((block - lower * sympy.eye(3))[:size, :size].det(method='bareiss')) for size in (1, 2, 3)]
    assert all(value > 0 for value in leading)
    assert polynomial.eval(lower) < 0 < polynomial.eval(upper)
    assert polynomial.count_roots(lower, upper) == 1
    assert first + second + 1 >= upper
    control.update({'a': first, 'b': second, 'cubic_coefficients': [int(value) for value in polynomial.all_coeffs()],
                    'five_direct_bareiss_values': values, 'leading_minor_endpoint': lower, 'leading_minors': leading,
                    'smallest_restricted_root_interval': [lower, upper], 'sturm_roots_in_interval': 1})
    return control


def main():
    dependency = Path(__file__).with_name('check_four_prime_pair_three.py')
    controls = [(1, 3), (2, 6), (2, 7), (12, 18), (12, 19), (13, 20), (13, 21), (13, 336), (13, 337)]
    report = {'written_theorem': 'Every positive four-prime double-pair exponent vector(a,a,b,b) is Laplacian nonintegral. The smallest repeated-pair witness lies in one of(1,2),(2,3),(3,4),with complete exponent thresholds.',
              'symbolic': symbolic_checks(), 'endpoint_fixed_arithmetic': fixed_endpoint_rows(),
              'fixed_support_controls': [fixed_control(*pair) for pair in controls],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'support_embedding_dependency_sha256': hashlib.sha256(dependency.read_bytes()).hexdigest(), 'sympy_version': sympy.__version__,
              'scope': 'Written unbounded endpoint brackets with ten fixed rows of constant arithmetic, not an exponent rectangle base. Nine specified exact support/Bareiss/Sturm controls. No expanded graph, exponent scan, floating eigensolver, historical finite rerun or Lean. General four-prime and higher-prime Q3 remain open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
