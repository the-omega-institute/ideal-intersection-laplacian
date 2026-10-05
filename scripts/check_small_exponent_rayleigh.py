from fractions import Fraction
import hashlib
import json
from math import prod
from pathlib import Path

import sympy


def symbolic_check():
    leaves, remainder, exponent, variable = sympy.symbols('A B m u', positive=True)
    compression = sympy.Matrix([[exponent, -exponent, 0],
                                [-leaves, leaves + remainder, -remainder],
                                [0, -exponent / (exponent + 1), exponent / (exponent + 1)]])
    polynomial = (variable ** 2 - (leaves + remainder + exponent + exponent / (exponent + 1)) * variable
                  + exponent * (leaves + (exponent + 1) * remainder + exponent) / (exponent + 1))
    assert sympy.simplify((variable * sympy.eye(3) - compression).det() - variable * polynomial) == 0
    endpoint = ((exponent ** 2 - 1) * remainder - leaves - (exponent - 1)) / (exponent + 1)
    assert sympy.simplify(polynomial.subs(variable, 1) - endpoint) == 0
    boundary = (exponent ** 2 - 1) * remainder - (exponent - 1)
    vector = sympy.Matrix([exponent, exponent - 1, -exponent * (exponent - 1)])
    assert all(sympy.simplify(entry.subs(leaves, boundary)) == 0
               for entry in compression * vector - vector)
    assert sympy.simplify((leaves * vector[0] + exponent * vector[1]
                           + (exponent + 1) * remainder * vector[2]).subs(leaves, boundary)) == 0
    last = -exponent * (leaves + exponent - 1) / ((exponent + 1) * remainder)
    energy = exponent * leaves + exponent * remainder * (exponent - 1 - last) ** 2
    norm = leaves * exponent ** 2 + exponent * (exponent - 1) ** 2 + (exponent + 1) * remainder * last ** 2
    difference = (exponent * ((exponent ** 2 - 1) * remainder - leaves - exponent + 1)
                  * (exponent * leaves + (exponent ** 2 - 1) * remainder + exponent * (exponent - 1))
                  / (remainder * (exponent + 1) ** 2))
    assert sympy.factor(energy - norm - difference) == 0
    return {'characteristic_polynomial': 'u*(u^2-(A+B+m+m/(m+1))*u+m*(A+(m+1)*B+m)/(m+1))',
            'endpoint': '((m^2-1)*B-A-(m-1))/(m+1)',
            'boundary_vector': ['m', 'm-1', '-m*(m-1)'],
            'trial_energy_minus_norm': 'm*((m^2-1)*B-A-(m-1))*(m*A+(m^2-1)*B+m*(m-1))/(B*(m+1)^2)',
            'generic_identities': 'passed'}


def support_data(exponents):
    full = (1 << len(exponents)) - 1
    supports = list(range(1, full))
    weights = {support: prod(exponent for index, exponent in enumerate(exponents)
                             if support & (1 << index)) for support in supports}
    adjacency = {support: [neighbor for neighbor in supports if not support & neighbor]
                 for support in supports}
    reached = {supports[0]}
    pending = list(reached)
    while pending:
        support = pending.pop()
        for neighbor in adjacency[support]:
            if neighbor not in reached:
                reached.add(neighbor)
                pending.append(neighbor)
    assert reached == set(supports)
    return supports, weights, adjacency


def check_control(exponents):
    supports, weights, adjacency = support_data(exponents)
    old_full = (1 << (len(exponents) - 1)) - 1
    hub = old_full + 1
    leaves = prod(exponents[:-1])
    remainder = prod(exponent + 1 for exponent in exponents[:-1]) - 1 - leaves
    exponent = exponents[-1]
    groups = {support: 0 if support == old_full else 1 if support == hub else 2
              for support in supports}
    masses = [sum(weights[support] for support in supports if groups[support] == group)
              for group in range(3)]
    assert masses == [leaves, exponent, (exponent + 1) * remainder]
    assert adjacency[old_full] == [hub]
    energy_matrix = [[0 for column in range(3)] for row in range(3)]
    for support in supports:
        for neighbor in adjacency[support]:
            if support >= neighbor or groups[support] == groups[neighbor]:
                continue
            first, second = groups[support], groups[neighbor]
            edge_weight = weights[support] * weights[neighbor]
            energy_matrix[first][first] += edge_weight
            energy_matrix[second][second] += edge_weight
            energy_matrix[first][second] -= edge_weight
            energy_matrix[second][first] -= edge_weight
    expected = [[exponent * leaves, -exponent * leaves, 0],
                [-exponent * leaves, exponent * (leaves + remainder), -exponent * remainder],
                [0, -exponent * remainder, exponent * remainder]]
    assert energy_matrix == expected
    endpoint = Fraction((exponent ** 2 - 1) * remainder - leaves - (exponent - 1), exponent + 1)
    values = {support: Fraction(exponent) if support == old_full else
              Fraction(exponent - 1) if support == hub else
              -Fraction(exponent * (leaves + exponent - 1), (exponent + 1) * remainder)
              for support in supports}
    assert sum(weights[support] * values[support] for support in supports) == 0
    energy = sum(weights[support] * weights[neighbor] * (values[support] - values[neighbor]) ** 2
                 for support in supports for neighbor in adjacency[support] if support < neighbor)
    norm = sum(weights[support] * values[support] ** 2 for support in supports)
    expected_difference = (Fraction(exponent, remainder * (exponent + 1) ** 2)
                           * ((exponent ** 2 - 1) * remainder - leaves - exponent + 1)
                           * (exponent * leaves + (exponent ** 2 - 1) * remainder + exponent * (exponent - 1)))
    assert energy - norm == expected_difference
    assert (energy <= norm) == (endpoint <= 0)
    complement_size = sum(weights.values())
    original_size = prod(exponent + 1 for exponent in exponents) - 2
    universals = prod(exponents) - 1
    assert original_size == complement_size + universals
    residual = {support: sum(weights[neighbor] * (values[support] - values[neighbor])
                             for neighbor in adjacency[support]) - values[support]
                for support in supports}
    if endpoint == 0:
        assert exponent >= 2 and energy == norm
        assert values[hub] == exponent - 1
        assert all(values[support] == -exponent * (exponent - 1)
                   for support in supports if groups[support] == 2)
        assert any(residual[support] != 0 for support in supports if groups[support] == 2)
        assert all(residual[support] == exponent * (exponent - 1)
                   for support in supports if groups[support] == 2 and support & hub)
    for support in supports:
        complement_action = sum(weights[neighbor] * (values[support] - values[neighbor])
                                for neighbor in adjacency[support])
        original_action = sum(weights[neighbor] * (values[support] - values[neighbor])
                              for neighbor in supports if support & neighbor)
        assert complement_action + original_action == complement_size * values[support]
        assert original_action + universals * values[support] == original_size * values[support] - complement_action
    reciprocal_sum = sum(Fraction(1, other) for other in exponents[:-1])
    sufficient = exponent >= 2 and reciprocal_sum <= Fraction(1, exponent ** 2)
    if sufficient:
        assert leaves > (exponent ** 2 - 1) * remainder
    return {'exponents': exponents, 'A': leaves, 'B': remainder,
            'complement_vertices': complement_size, 'graph_vertices': original_size,
            'support_classes': len(supports), 'p_at_one': str(endpoint),
            'rational_trial_rayleigh_quotient': str(energy / norm),
            'criterion_applies': endpoint <= 0,
            'boundary_strictness_checked': endpoint == 0,
            'reciprocal_sufficient_condition': sufficient,
            'support_energy_complement_join_checks': 'passed'}


def full_graph_check(exponents):
    supports, weights, adjacency = support_data(exponents)
    old_full = (1 << (len(exponents) - 1)) - 1
    hub = old_full + 1
    leaves = prod(exponents[:-1])
    remainder = prod(exponent + 1 for exponent in exponents[:-1]) - 1 - leaves
    exponent = exponents[-1]
    vertices = [support for support in supports for repeat in range(weights[support])]
    values = [Fraction(exponent) if support == old_full else Fraction(exponent - 1) if support == hub else
              -Fraction(exponent * (leaves + exponent - 1), (exponent + 1) * remainder)
              for support in vertices]
    energy = sum((values[first] - values[second]) ** 2
                 for first in range(len(vertices)) for second in range(first + 1, len(vertices))
                 if not vertices[first] & vertices[second])
    expected = exponent * leaves + exponent * remainder * (Fraction(exponent - 1)
                + Fraction(exponent * (leaves + exponent - 1), (exponent + 1) * remainder)) ** 2
    assert energy == expected and sum(values) == 0
    return {'exponents': exponents, 'vertices': len(vertices), 'exact_trial_energy': str(energy),
            'expanded_graph_energy_check': 'passed'}


def main():
    controls = [(2, 3, 1), (4, 11, 2), (10, 39, 3),
                (10, 10, 10, 2), (4, 19, 74, 2), (12, 12, 12, 2),
                (36, 36, 36, 36, 3), (2, 2, 2, 2), (9, 9, 9, 2)]
    records = [check_control(exponents) for exponents in controls]
    assert sum(record['boundary_strictness_checked'] for record in records) == 3
    assert sum(not record['criterion_applies'] for record in records) == 2
    report = {'written_theorem': 'For t>=3, A>= (m^2-1)*B-(m-1) gives a graph eigenvalue in (V-1,V), including equality.',
              'symbolic': symbolic_check(), 'support_controls': records,
              'independent_expanded_graph_controls': [full_graph_check(exponents) for exponents in ((1, 1, 2), (4, 11, 2))],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded variational proof with a non-equitable compression and strict boundary argument, no finite base. Nine specified exact support controls, three boundary and two negative controls; two expanded graphs. No parameter scan, floating eigenvalues or Lean; higher-prime nonsquarefree Q3 remains open outside the sufficient criterion.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
