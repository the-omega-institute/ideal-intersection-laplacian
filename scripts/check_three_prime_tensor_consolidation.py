import hashlib
import json
from pathlib import Path

import sympy


def complement_quotient(exponents):
    supports = list(range(1, 7))
    weights = {support: sympy.prod(entry for index, entry in enumerate(exponents)
                                   if support & (1 << index)) for support in supports}
    matrix = sympy.zeros(6)
    for row, support in enumerate(supports):
        for column, neighbor in enumerate(supports):
            if not support & neighbor:
                matrix[row, row] += weights[neighbor]
                matrix[row, column] -= weights[neighbor]
    return matrix, weights


def repeated_operator(exponent, remaining):
    return sympy.Matrix([[(exponent + 1) * (remaining + 1) + exponent,
                          exponent * remaining], [exponent, exponent + 1]])


def zero_matrix(matrix):
    return all(sympy.expand(entry) == 0 for entry in matrix)


def symbolic_check():
    exponent, unequal, remaining, variable, shift = sympy.symbols('a d b x u')
    diagonal = lambda entry: sympy.diag(entry + 1, 1)
    disjoint = lambda entry: sympy.Matrix([[1, entry], [1, 0]])
    quotient, weights = complement_quotient((exponent, unequal, remaining))
    tensor = (sympy.kronecker_product(diagonal(remaining), diagonal(unequal), diagonal(exponent))
              - sympy.kronecker_product(disjoint(remaining), disjoint(unequal), disjoint(exponent)))
    assert zero_matrix(tensor.extract(list(range(1, 7)), list(range(1, 7))) - quotient - sympy.eye(6))
    assert zero_matrix(quotient * sympy.ones(6, 1))
    weight_matrix = sympy.diag(*[weights[support] for support in range(1, 7)])
    assert zero_matrix(weight_matrix * quotient - quotient.T * weight_matrix)
    matrix = repeated_operator(exponent, remaining)
    expected_characteristic = (variable ** 2 - ((exponent + 1) * (remaining + 2) + exponent) * variable
                               + (2 * exponent + 1) * remaining + (exponent + 1) * (2 * exponent + 1))
    assert sympy.expand((variable * sympy.eye(2) - matrix).det() - expected_characteristic) == 0
    assert sympy.expand((matrix - 2 * sympy.eye(2)).det()
                        - ((exponent - 1) * (2 * exponent - 1) - remaining)) == 0
    assert sympy.expand((matrix - 3 * sympy.eye(2)).det()
                        - (2 * (exponent - 2) * (exponent - 1) - (exponent + 2) * remaining)) == 0
    boundary = (exponent - 1) * (2 * exponent - 1)
    assert sympy.expand(expected_characteristic.subs(remaining, boundary)
                        - (variable - 2) * (variable - (2 * exponent ** 3 - exponent ** 2 + exponent + 1))) == 0
    assert sympy.expand(boundary - exponent - (2 * (exponent - 1) ** 2 - 1)) == 0
    balanced = matrix.subs(remaining, exponent)
    assert sympy.expand((balanced - 3 * sympy.eye(2)).det() - (exponent ** 2 - 8 * exponent + 4)) == 0
    assert sympy.expand((balanced - 4 * sympy.eye(2)).det() - (9 - 12 * exponent)) == 0
    assert sympy.expand((balanced - 3 * sympy.eye(2)).det().subs(exponent, 8 + shift)
                        - (shift ** 2 + 8 * shift + 4)) == 0
    embedding = sympy.Matrix([[1, 0], [-1, 0], [0, 0], [0, 0], [0, 1], [0, -1]])
    equal_quotient = quotient.subs(unequal, exponent)
    assert zero_matrix(equal_quotient * embedding - embedding * (matrix - sympy.eye(2)))
    weighted = sympy.Matrix([[unequal, 0], [-exponent, 0], [0, 0], [0, 0],
                             [0, unequal], [0, -exponent]])
    assert zero_matrix(sympy.ones(1, 6) * weight_matrix * weighted)
    action = quotient * weighted
    singleton_residual = action.row(0) / unequal + action.row(1) / exponent
    pair_residual = action.row(4) / unequal + action.row(5) / exponent
    assert zero_matrix(singleton_residual - sympy.Matrix([[remaining * (unequal - exponent),
                                                          -remaining * (unequal - exponent)]]))
    assert zero_matrix(pair_residual - sympy.Matrix([[exponent - unequal, unequal - exponent]]))
    constant_line = action * sympy.ones(2, 1)
    assert sympy.expand(constant_line[0] / unequal
                        - (remaining * (exponent + unequal + 1) + exponent + unequal)) == 0
    assert sympy.expand(constant_line[4] / unequal - (exponent + unequal)) == 0
    normalized = diagonal(remaining).inv() * disjoint(remaining)
    assert sympy.factor((variable * sympy.eye(2) - normalized).det()
                        - (variable - 1) * (variable + remaining / (remaining + 1))) == 0
    return {'full_six_support_tensor_identity': 'passed', 'weighted_symmetry_constant_kernel': 'passed',
            'generic_repeated_pair_embedding': 'passed', 'generic_unequal_pair_residuals': 'passed',
            'normalized_characteristic_identity': 'passed', 'generic_repeated_characteristic': str(expected_characteristic),
            'endpoint_two': str((exponent - 1) * (2 * exponent - 1) - remaining),
            'boundary_K_eigenvalues': ['2', '2*a**3-a**2+a+1'],
            'boundary_attribution': 'Existing boundary family supplied by Reza Nikandish; manuscript Theorem 5.1.',
            'balanced_a_at_least_eight': '3<kappa_min<4, equivalently 2<mu_min<3',
            'balanced_third_endpoint_positive_expansion': 'u**2+8*u+4',
            'balanced_fourth_endpoint': '9-12*a'}


def support_control(exponent, remaining):
    quotient, weights = complement_quotient((exponent, exponent, remaining))
    embedding = sympy.Matrix([[1, 0], [-1, 0], [0, 0], [0, 0], [0, 1], [0, -1]])
    restriction = repeated_operator(exponent, remaining)
    vertices = (exponent + 1) ** 2 * (remaining + 1) - 2
    universals = exponent ** 2 * remaining - 1
    nonuniversals = sum(weights.values())
    assert vertices == universals + nonuniversals
    assert zero_matrix(quotient * embedding - embedding * (restriction - sympy.eye(2)))
    assert zero_matrix(sympy.Matrix([[weights[support] for support in range(1, 7)]]) * embedding)
    original = nonuniversals * sympy.eye(6) - sympy.ones(6, 1) * sympy.Matrix([[weights[support] for support in range(1, 7)]]) - quotient
    assert zero_matrix((original + universals * sympy.eye(6)) * embedding
                       - embedding * ((vertices + 1) * sympy.eye(2) - restriction))
    return {'exponents': [exponent, exponent, remaining], 'graph_vertices': vertices,
            'embedding_columns_checked': 2, 'zero_sum_complement_and_graph_lift': 'passed'}


def main():
    controls = [(2, 3), (3, 10), (8, 8), (8, 105), (12, 253), (3, 7)]
    report = {'purpose': 'Exact response to three-prime tensor consolidation question; no new classification theorem.',
              'symbolic': symbolic_check(), 'specified_support_controls': [support_control(*control) for control in controls],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'sympy_version': sympy.__version__,
              'classification_source': '7be84599097fdff320b196cb4f84a2dfe505bd77',
              'retained_finite_dependencies': [27562, 8658],
              'scope': 'Generic symbolic tensor/embedding/endpoint identities and six specified support controls. Existing boundary result and classification retained; no exponent scan, numerical spectrum, Lean or rerun of historical certificates.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
