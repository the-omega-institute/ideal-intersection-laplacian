import hashlib
import json
from math import isqrt, prod
from pathlib import Path

import sympy


def operator(exponent, middle, maximum):
    return [[(exponent + 1) * (middle + 1) * (maximum + 1) + exponent,
             exponent * maximum, exponent * middle, exponent * middle * maximum],
            [exponent, (exponent + 1) * (middle + 1), exponent * middle, 0],
            [exponent, exponent * maximum, (exponent + 1) * (maximum + 1), 0],
            [exponent, 0, 0, exponent + 1]]


def symbolic_check():
    exponent, middle, maximum, weight, variable = sympy.symbols('a b c k x')
    diagonal = lambda entry: sympy.diag(entry + 1, 1)
    disjoint = lambda entry: sympy.Matrix([[1, entry], [1, 0]])
    matrix = sympy.Matrix(operator(exponent, middle, maximum))
    tensor = ((exponent + 1) * sympy.kronecker_product(diagonal(middle), diagonal(maximum))
              + exponent * sympy.kronecker_product(disjoint(middle), disjoint(maximum)))
    assert matrix == tensor
    normalized = diagonal(weight).inv() * disjoint(weight)
    assert sympy.factor((variable * sympy.eye(2) - normalized).det()
                        - (variable - 1) * (variable + weight / (weight + 1))) == 0
    specific = matrix.subs(exponent, 3)
    second = (-7 * middle ** 2 * maximum ** 2 + 48 * middle ** 2 * maximum - 8 * middle ** 2
              + 48 * middle * maximum ** 2 + 302 * middle * maximum + 76 * middle
              - 8 * maximum ** 2 + 76 * maximum + 40)
    third = (-35 * middle ** 2 * maximum ** 2 + 8 * middle ** 2 * maximum - 20 * middle ** 2
             + 8 * middle * maximum ** 2 + 109 * middle * maximum + 11 * middle
             - 20 * maximum ** 2 + 11 * maximum + 4)
    assert sympy.expand((specific - 2 * sympy.eye(4)).det() - second) == 0
    assert sympy.expand((specific - 3 * sympy.eye(4)).det() - third) == 0
    expansions = {}
    expected_coefficients = {2: [35, 132, 144, 132, 387, 315, 144, 315, 108],
                             17: [7, 190, 1215, 190, 4526, 22228, 1215, 22228, 27721]}
    for endpoint, shift in ((third, 2), (second, 17)):
        polynomial = sympy.Poly(sympy.expand(-endpoint.subs({middle: middle + shift, maximum: maximum + shift})), middle, maximum)
        assert polynomial.coeffs() == expected_coefficients[shift]
        assert all(coefficient > 0 for coefficient in polynomial.coeffs())
        expansions[str(shift)] = [list(monomial) + [int(coefficient)] for monomial, coefficient in polynomial.terms()]
    leading = -7 * middle ** 2 + 48 * middle - 8
    linear = 48 * middle ** 2 + 302 * middle + 76
    constant = -8 * middle ** 2 + 76 * middle + 40
    assert sympy.expand(second - (leading * maximum ** 2 + linear * maximum + constant)) == 0
    expected_discriminants = {7: (20640564, 4543), 8: (30997264, 5567), 9: (44692596, 6685),
                              11: (84630100, 9199), 12: (112262544, 10595), 13: (146014164, 12083),
                              15: (235204596, 15336), 16: (292433040, 17100)}
    fixed_rows = []
    for value in range(2, 17):
        coefficients = [int(expression.subs(middle, value)) for expression in (leading, linear, constant)]
        polynomial = sympy.Poly(second.subs(middle, value), maximum)
        assert polynomial.all_coeffs() == coefficients
        record = {'b': value, 'coefficients': coefficients}
        if value <= 6:
            assert all(coefficient > 0 for coefficient in coefficients)
            record['obstruction'] = 'positive coefficients'
        elif value in (10, 14):
            expected = -12 * maximum * (19 * maximum - 658) if value == 10 else -4 * (3 * maximum - 58) * (59 * maximum - 2)
            assert sympy.expand(polynomial.as_expr() - expected) == 0
            roots = [sympy.Rational(658, 19)] if value == 10 else [sympy.Rational(58, 3), sympy.Rational(2, 59)]
            assert all(root.q != 1 and polynomial.eval(root) == 0 for root in roots)
            record.update({'obstruction': 'rational noninteger positive roots', 'positive_roots': [str(root) for root in roots]})
        else:
            discriminant = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
            anchor = isqrt(discriminant)
            assert (discriminant, anchor) == expected_discriminants[value]
            assert anchor ** 2 < discriminant < (anchor + 1) ** 2
            assert int(sympy.discriminant(polynomial.as_expr(), maximum)) == discriminant
            record.update({'obstruction': 'nonsquare discriminant', 'discriminant': discriminant, 'square_anchor': anchor})
        fixed_rows.append(record)
    assert sum(row['obstruction'] == 'nonsquare discriminant' for row in fixed_rows) == 8
    return {'normalized_two_dimensional_eigenvalues': ['1', '-k/(k+1)'],
            'general_lower_bound': 'kappa_min(K_a)>1 for every a,b,c>=1',
            'generic_second_endpoint': str(second), 'generic_third_endpoint': str(third),
            'complete_positive_expansions': expansions, 'all_fifteen_fixed_b_rows': fixed_rows,
            'integer_endpoint_pairs': [], 'generic_identities': 'passed'}


def support_embedding(exponent, middle, maximum, expand=False):
    exponents = (exponent, exponent, middle, maximum)
    supports = list(range(1, 15))
    weights = {support: prod(entry for index, entry in enumerate(exponents) if support & (1 << index))
               for support in supports}
    adjacency = {support: [neighbor for neighbor in supports if not support & neighbor] for support in supports}
    basis = [{support: 1 if support == (1 | tail) else -1 if support == (2 | tail) else 0
              for support in supports} for tail in (0, 8, 4, 12)]
    restriction = operator(exponent, middle, maximum)
    complement_vertices = sum(weights.values())
    universals = exponent ** 2 * middle * maximum - 1
    graph_vertices = (exponent + 1) ** 2 * (middle + 1) * (maximum + 1) - 2
    assert graph_vertices == complement_vertices + universals
    for column, values in enumerate(basis):
        assert sum(weights[support] * values[support] for support in supports) == 0
        for support in supports:
            action = sum(weights[neighbor] * (values[support] - values[neighbor]) for neighbor in adjacency[support])
            expected = sum(basis[row][support] * (restriction[row][column] - (row == column)) for row in range(4))
            assert action == expected
            original = sum(weights[neighbor] * (values[support] - values[neighbor]) for neighbor in supports if support & neighbor)
            assert original + action == complement_vertices * values[support]
            assert original + universals * values[support] == graph_vertices * values[support] - expected
        if expand:
            vertices = [support for support in supports for repeat in range(weights[support])]
            for index, support in enumerate(vertices):
                action = sum(values[support] - values[neighbor] for other, neighbor in enumerate(vertices)
                             if index != other and not support & neighbor)
                assert action == sum(basis[row][support] * (restriction[row][column] - (row == column)) for row in range(4))
    symmetrizer = [1, maximum, middle, middle * maximum]
    assert all(symmetrizer[row] * restriction[row][column] == symmetrizer[column] * restriction[column][row]
               for row in range(4) for column in range(4))
    return {'exponents': exponents, 'graph_vertices': graph_vertices, 'complement_vertices': complement_vertices,
            'embedding_columns_checked': 4, 'expanded_graph_checked': expand,
            'weighted_symmetry_zero_sum_complement_join': 'passed'}


def main():
    controls = [(3, 2, 2), (3, 3, 7), (3, 6, 100), (3, 7, 304),
                (3, 10, 35), (3, 14, 19), (3, 17, 17), (3, 19, 100), (4, 2, 5), (7, 11, 13)]
    report = {'written_theorem': 'Every four-prime vector(3,3,b,c),b,c>=2 has a noninteger graph eigenvalue in(V-2,V), different fromV-1.',
              'symbolic': symbolic_check(),
              'support_controls': [support_embedding(*control) for control in controls],
              'independent_expanded_graph_controls': [support_embedding(*control, expand=True) for control in ((3, 2, 2), (3, 2, 3))],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'sympy_version': sympy.__version__,
              'scope': 'Written unbounded invariant-subspace/tensor positivity proof with eight fixed nonsquare discriminants and two rational factorizations; no finite two-parameter exponent base, modular search, floating eigenvalues or Lean. Ten specified support controls and two expanded graphs validate implementation; general higher-prime nonsquarefreeQ3 remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
