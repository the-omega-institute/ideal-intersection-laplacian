import hashlib
import json
from math import isqrt, prod
from pathlib import Path

import sympy


def operator(middle, maximum):
    return [[3 * (middle + 1) * (maximum + 1) + 2, 2 * maximum, 2 * middle, 2 * middle * maximum],
            [2, 3 * (middle + 1), 2 * middle, 0],
            [2, 2 * maximum, 3 * (maximum + 1), 0],
            [2, 0, 0, 3]]


def symbolic_check():
    middle, maximum, variable = sympy.symbols('b c x')
    matrix = sympy.Matrix(operator(middle, maximum))
    minors = [3 * middle * maximum + 3 * middle + 3 * maximum + 4,
              9 * middle ** 2 * maximum + 9 * middle ** 2 + 15 * middle * maximum + 18 * middle + 2 * maximum + 8,
              15 * middle ** 2 * maximum ** 2 + 33 * middle ** 2 * maximum + 6 * middle ** 2
              + 33 * middle * maximum ** 2 + 84 * middle * maximum + 28 * middle + 6 * maximum ** 2 + 28 * maximum + 16,
              2 * (5 * middle ** 2 * maximum ** 2 + 21 * middle ** 2 * maximum + 6 * middle ** 2
                   + 21 * middle * maximum ** 2 + 76 * middle * maximum + 28 * middle + 6 * maximum ** 2 + 28 * maximum + 16)]
    for size, expected in enumerate(minors, 1):
        assert sympy.expand((matrix - sympy.eye(4))[:size, :size].det() - expected) == 0
        assert all(coefficient > 0 for coefficient in sympy.Poly(expected, middle, maximum).coeffs())
    assert sympy.expand((matrix - 3 * sympy.eye(4)).extract([0, 3], [0, 3]).det() + 4 * middle * maximum) == 0
    endpoint = (-5 * middle ** 2 * maximum ** 2 + 12 * middle ** 2 * maximum - 3 * middle ** 2
                + 12 * middle * maximum ** 2 + 48 * middle * maximum + 8 * middle - 3 * maximum ** 2 + 8 * maximum + 3)
    assert sympy.expand((matrix - 2 * sympy.eye(4)).det() - endpoint) == 0
    tail = (5 * middle ** 2 * maximum ** 2 + 58 * middle ** 2 * maximum + 164 * middle ** 2
            + 58 * middle * maximum ** 2 + 596 * middle * maximum + 1364 * middle
            + 164 * maximum ** 2 + 1364 * maximum + 1600)
    assert sympy.expand(-endpoint.subs({middle: middle + 7, maximum: maximum + 7}) - tail) == 0
    low_rows = {2: maximum ** 2 + 152 * maximum + 7,
                3: 4 * maximum * (65 - 3 * maximum),
                4: -35 * maximum ** 2 + 392 * maximum - 13,
                5: -4 * (maximum - 8) * (17 * maximum - 1),
                6: -111 * maximum ** 2 + 728 * maximum - 57}
    for value, expected in low_rows.items():
        assert sympy.expand(endpoint.subs(middle, value) - expected) == 0
    discriminants = {}
    for value, expected in ((4, 151844), (6, 504676)):
        actual = int(sympy.discriminant(low_rows[value], maximum))
        anchor = isqrt(actual)
        assert actual == expected and anchor ** 2 < actual < (anchor + 1) ** 2
        discriminants[str(value)] = {'discriminant': actual, 'lower_square_anchor': anchor}
    cubic = variable ** 3 - 210 * variable ** 2 + 7701 * variable - 53240
    exceptional = sympy.Matrix(operator(5, 8))
    assert sympy.expand((variable * sympy.eye(4) - exceptional).det() - (variable - 2) * cubic) == 0
    values = [(entry ** 3 - 210 * entry ** 2 + 7701 * entry - 53240) % 17 for entry in range(17)]
    assert values == [4, 16, 5, 11, 6, 13, 4, 2, 13, 9, 13, 14, 1, 14, 8, 6, 14]
    assert 0 not in values
    assert [int(coefficient) % 17 for coefficient in sympy.Poly(cubic, variable).all_coeffs()] == [1, 11, 0, 4]
    return {'generic_principal_minors': [str(sympy.expand(expression)) for expression in minors],
            'generic_endpoint_polynomial': str(endpoint),
            'tail_positive_coefficients': [list(monomial) + [int(coefficient)]
                                           for monomial, coefficient in sympy.Poly(tail, middle, maximum).terms()],
            'low_b_symbolic_rows': {str(value): str(expression) for value, expression in low_rows.items()},
            'nonsquare_discriminants': discriminants,
            'unique_integer_endpoint_pair': [5, 8], 'exceptional_cubic': str(cubic),
            'mod17_values_at_0_through_16': values, 'all_generic_identities': 'passed'}


def support_embedding(middle, maximum, expand=False):
    exponents = (2, 2, middle, maximum)
    supports = list(range(1, 15))
    weights = {support: prod(exponent for index, exponent in enumerate(exponents)
                             if support & (1 << index)) for support in supports}
    adjacency = {support: [neighbor for neighbor in supports if not support & neighbor]
                 for support in supports}
    trial_basis = []
    for tail in (0, 8, 4, 12):
        trial_basis.append({support: 1 if support == (1 | tail) else -1 if support == (2 | tail) else 0
                            for support in supports})
    expected_operator = operator(middle, maximum)
    complement_vertices = sum(weights.values())
    universals = 4 * middle * maximum - 1
    graph_vertices = 9 * (middle + 1) * (maximum + 1) - 2
    assert graph_vertices == complement_vertices + universals
    for column, values in enumerate(trial_basis):
        assert sum(weights[support] * values[support] for support in supports) == 0
        for support in supports:
            complement_action = sum(weights[neighbor] * (values[support] - values[neighbor])
                                    for neighbor in adjacency[support])
            expected_action = sum(trial_basis[row][support] * (expected_operator[row][column] - (row == column))
                                  for row in range(4))
            assert complement_action == expected_action
            original_action = sum(weights[neighbor] * (values[support] - values[neighbor])
                                  for neighbor in supports if support & neighbor)
            assert original_action + complement_action == complement_vertices * values[support]
            assert original_action + universals * values[support] == graph_vertices * values[support] - expected_action
        if expand:
            vertices = [support for support in supports for repeat in range(weights[support])]
            for index, support in enumerate(vertices):
                action = sum(values[support] - values[neighbor] for other, neighbor in enumerate(vertices)
                             if index != other and not support & neighbor)
                assert action == sum(trial_basis[row][support] * (expected_operator[row][column] - (row == column))
                                     for row in range(4))
    symmetrizer = [1, maximum, middle, middle * maximum]
    assert all(symmetrizer[row] * expected_operator[row][column] == symmetrizer[column] * expected_operator[column][row]
               for row in range(4) for column in range(4))
    return {'b': middle, 'c': maximum, 'graph_vertices': graph_vertices,
            'complement_vertices': complement_vertices, 'support_classes': len(supports),
            'embedding_columns_checked': 4, 'expanded_graph_checked': expand,
            'weighted_symmetry_zero_sum_complement_join': 'passed'}


def main():
    controls = [(2, 2), (2, 11), (3, 22), (4, 11), (5, 8), (6, 7), (7, 7), (19, 100)]
    report = {'written_theorem': 'Every four-prime positive exponent vector (2,2,b,c), b,c>=2, is Laplacian nonintegral.',
              'symbolic': symbolic_check(),
              'support_controls': [support_embedding(middle, maximum) for middle, maximum in controls],
              'independent_expanded_graph_controls': [support_embedding(middle, maximum, expand=True)
                                                       for middle, maximum in ((2, 2), (2, 3))],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'sympy_version': sympy.__version__,
              'scope': 'Written infinite invariant-subspace and positive-minor proof; five symbolic low-b polynomials and one explicit17-residue irreducibility certificate, no finite exponent base or range scan. Eight specified support controls and two expanded graphs validate the implementation. No floating-point eigenvalues or Lean; full higher-prime nonsquarefree Q3 remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
