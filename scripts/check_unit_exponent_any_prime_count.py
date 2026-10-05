from fractions import Fraction
import hashlib
import json
from math import prod
from pathlib import Path


def support_data(exponents):
    full_support = (1 << len(exponents)) - 1
    supports = list(range(1, full_support))
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
    assert len(exponents) >= 3 and exponents[-1] == 1
    supports, weights, adjacency = support_data(exponents)
    old_full = (1 << (len(exponents) - 1)) - 1
    hub = old_full + 1
    leaves = prod(exponents[:-1])
    half_remainder = prod(exponent + 1 for exponent in exponents[:-1]) - 1 - leaves
    assert half_remainder > 0 and weights[hub] == 1 and weights[old_full] == leaves
    assert adjacency[old_full] == [hub]
    nonhub_neighbors = sum(weights[support] for support in adjacency[hub] if support != old_full)
    assert nonhub_neighbors == half_remainder
    values = {support: 2 * half_remainder if support == old_full else
              0 if support == hub else -leaves for support in supports}
    assert sum(weights[support] * values[support] for support in supports) == 0
    numerator = sum(weights[support] * weights[neighbor] * (values[support] - values[neighbor]) ** 2
                    for support in supports for neighbor in adjacency[support] if support < neighbor)
    denominator = sum(weights[support] * values[support] ** 2 for support in supports)
    assert numerator == leaves * half_remainder * (4 * half_remainder + leaves)
    assert denominator == 2 * leaves * half_remainder * (2 * half_remainder + leaves)
    quotient = Fraction(numerator, denominator)
    assert quotient == Fraction(4 * half_remainder + leaves, 4 * half_remainder + 2 * leaves) < 1
    vertices = sum(weights.values()) + prod(exponents) - 1
    assert vertices == prod(exponent + 1 for exponent in exponents) - 2
    assert vertices == 2 * leaves + 2 * half_remainder
    return {'exponents': exponents, 'support_classes': len(supports), 'leaves': leaves,
            'half_remainder': half_remainder, 'complement_vertices': sum(weights.values()),
            'graph_vertices': vertices, 'trial_energy': numerator, 'trial_norm_squared': denominator,
            'rayleigh_quotient': str(quotient), 'connected_and_identities': 'passed'}


def full_graph_control(exponents):
    supports, weights, adjacency = support_data(exponents)
    old_full = (1 << (len(exponents) - 1)) - 1
    hub = old_full + 1
    leaves = prod(exponents[:-1])
    half_remainder = prod(exponent + 1 for exponent in exponents[:-1]) - 1 - leaves
    vertices = [support for support in supports for repeat in range(weights[support])]
    values = [2 * half_remainder if support == old_full else 0 if support == hub else -leaves
              for support in vertices]
    assert sum(values) == 0
    complement_energy = sum((values[first] - values[second]) ** 2
                            for first in range(len(vertices)) for second in range(first + 1, len(vertices))
                            if not vertices[first] & vertices[second])
    original_energy = sum((values[first] - values[second]) ** 2
                          for first in range(len(vertices)) for second in range(first + 1, len(vertices))
                          if vertices[first] & vertices[second])
    norm_squared = sum(value ** 2 for value in values)
    assert complement_energy + original_energy == len(vertices) * norm_squared
    assert Fraction(complement_energy, norm_squared) < 1
    return {'exponents': exponents, 'full_complement_vertices': len(vertices),
            'rayleigh_quotient': str(Fraction(complement_energy, norm_squared)),
            'complement_identity_on_trial_vector': 'passed'}


def main():
    controls = [(1, 1, 1), (1, 2, 1), (2, 3, 1), (9, 136, 1),
                (1, 1, 1, 1), (2, 3, 4, 1), (7, 11, 13, 1),
                (1, 1, 1, 1, 1), (2, 3, 4, 5, 1)]
    records = [check_control(exponents) for exponents in controls]
    report = {'written_theorem': 'Any t>=3 positive integer prime-exponent vector with a unit exponent is Laplacian nonintegral, with a graph eigenvalue in (V-1,V).',
              'written_rayleigh_bound': '0<mu<= (4B+A)/(4B+2A)<1; A=product of other exponents, B=product of (other exponent+1)-1-A>0.',
              'support_controls': records,
              'independent_full_graph_controls': [full_graph_control(exponents) for exponents in ((1, 1, 1), (2, 3, 1))],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Written unbounded support-counting and Rayleigh proof; nine specified quotient controls and two small full graphs verify implementation. Controls are not the proof and no parameter scan or finite base is required. No floating eigenvalues or Lean. Higher-prime nonsquarefree all-exponents>=2 and original orthogonality n=7 remain open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
