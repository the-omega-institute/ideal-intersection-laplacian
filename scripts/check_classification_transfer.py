import json
import sympy


first, second, third = sympy.symbols('a b c', positive=True)
weights = [first, second, third, first * second, first * third, second * third]
supports = [{1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}]


def quotient(complement):
    matrix = sympy.zeros(6)
    for row, source in enumerate(supports):
        for column, target in enumerate(supports):
            if row != column and (bool(source.intersection(target)) != complement):
                matrix[row, row] += weights[column]
                matrix[row, column] = -weights[column]
    return matrix


complement = quotient(True)
original = quotient(False)
weight_matrix = sympy.diag(*weights)
weighted = weight_matrix * complement
assert weighted == weighted.T
assert complement * sympy.ones(6, 1) == sympy.zeros(6, 1)
assert (sympy.ones(1, 6) * weighted).applyfunc(sympy.expand) == sympy.zeros(1, 6)
total = sum(weights)
assert (original + complement - total * sympy.eye(6) + sympy.ones(6, 1) * sympy.Matrix([weights])).applyfunc(sympy.expand) == sympy.zeros(6)
coordinates = sympy.Matrix(sympy.symbols('z1:7'))
edge_energy = 0
edges = []
for row in range(6):
    for column in range(row + 1, 6):
        if not supports[row].intersection(supports[column]):
            edges.append([row + 1, column + 1])
            edge_energy += weights[row] * weights[column] * (coordinates[row] - coordinates[column]) ** 2
assert sympy.expand((coordinates.T * weighted * coordinates)[0] - edge_energy) == 0
symmetric_embedding = sympy.Matrix([[1, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0],
                                   [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 1]])
antisymmetric_embedding = sympy.Matrix([[1, 0], [-1, 0], [0, 0], [0, 0], [0, 1], [0, -1]])
repeated = original.subs({second: first, third: second}, simultaneous=True)
symmetric_block = sympy.Matrix([[first ** 2 + first * second, 0, -first ** 2, -first * second],
                               [0, 2 * first * second, 0, -2 * first * second],
                               [-2 * first, 0, 2 * first + 2 * first * second, -2 * first * second],
                               [-first, -second, -first ** 2, first ** 2 + first + second]])
antisymmetric_block = sympy.Matrix([[first ** 2 + first * second, -first * second],
                                   [-first, first ** 2 + first + second + 2 * first * second]])
assert (repeated * symmetric_embedding - symmetric_embedding * symmetric_block).applyfunc(sympy.expand) == sympy.zeros(6, 4)
assert (repeated * antisymmetric_embedding - antisymmetric_embedding * antisymmetric_block).applyfunc(sympy.expand) == sympy.zeros(6, 2)
print(json.dumps({'sympy': sympy.__version__, 'scope': 'Fresh coefficientwise symbolic checks for added explanatory transfer and positive-real-weight paragraphs; no finite-domain rerun.',
                  'weighted_symmetry_and_zero_sums': True, 'complement_identity': True,
                  'positive_energy_identity': True, 'support_disjointness_edges': edges,
                  'repeated_symmetric_embedding': True, 'repeated_antisymmetric_embedding': True,
                  'lean_run': False}, indent=2))
