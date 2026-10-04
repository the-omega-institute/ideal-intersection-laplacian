import hashlib
import itertools
import json
from math import isqrt
from pathlib import Path


def ideal_graph(exponents):
    zero_ideal = tuple(exponents)
    whole_ring = (0,) * len(exponents)
    vertices = [
        coordinates
        for coordinates in itertools.product(*(range(bound + 1) for bound in exponents))
        if coordinates not in (zero_ideal, whole_ring)
    ]
    neighbors = [[] for coordinates in vertices]
    pairs_checked = 0
    edges_checked = 0
    for first, coordinates in enumerate(vertices):
        for second in range(first + 1, len(vertices)):
            pairs_checked += 1
            other = vertices[second]
            if any(max(left, right) < bound for left, right, bound in zip(coordinates, other, exponents)):
                neighbors[first].append(second)
                neighbors[second].append(first)
                edges_checked += 1
    return vertices, neighbors, pairs_checked, edges_checked


def support(coordinates, exponents):
    return sum(1 << index for index, (value, bound) in enumerate(zip(coordinates, exponents)) if value < bound)


def check_invariant_block(neighbors, embedding, block):
    dimension = len(block)
    if any(not any(row[column] for row in embedding) for column in range(dimension)):
        raise AssertionError("A proposed basis vector is zero")
    if any(sum(row[first] * row[second] for row in embedding) != 0
           for first in range(dimension) for second in range(first)):
        raise AssertionError("The proposed basis vectors are not independent and orthogonal")
    for vertex, row in enumerate(embedding):
        for column in range(dimension):
            direct = sum(row[column] - embedding[other][column] for other in neighbors[vertex])
            reduced = sum(row[index] * block[index][column] for index in range(dimension))
            if direct != reduced:
                raise AssertionError((vertex, column, direct, reduced))


def squarefree_check(prime_count):
    exponents = (1,) * prime_count
    vertices, neighbors, pairs, edges = ideal_graph(exponents)
    pair_count = prime_count // 2 if prime_count % 2 else prime_count // 2 - 1
    scale = 2 ** pair_count
    sign = (-1) ** pair_count
    offset = 2 ** prime_count - 1
    dimension = 2 if prime_count % 2 else 3
    embedding = []
    for coordinates in vertices:
        mask = support(coordinates, exponents)
        coefficient = 1
        for pair in range(pair_count):
            first = bool(mask & (1 << (2 * pair)))
            second = bool(mask & (1 << (2 * pair + 1)))
            if first == second:
                coefficient = 0
            elif first:
                coefficient *= -1
        residual_size = (mask >> (2 * pair_count)).bit_count()
        embedding.append([coefficient if residual_size == column else 0 for column in range(dimension)])
    if dimension == 2:
        block = [[offset - 2 * scale + sign, sign], [sign, offset - scale]]
        gap = scale - sign
        discriminant = gap * gap + 4
        if not gap * gap < discriminant < (gap + 1) ** 2:
            raise AssertionError("Odd squarefree discriminant is not strictly between consecutive squares")
        witness = {"discriminant": discriminant, "between_squares": [gap * gap, (gap + 1) ** 2]}
    else:
        block = [
            [offset - 4 * scale + sign, 2 * sign, sign],
            [sign, offset - 2 * scale + sign, 0],
            [sign, 0, offset - scale],
        ]
        leading_minors = [
            3 * scale + 1 - sign,
            (3 * scale + 1 - sign) * (scale + 1 - sign) - 2,
            (3 * scale - sign) * (scale + 1 - sign) - 2,
        ]
        if not all(value > 0 for value in leading_minors):
            raise AssertionError("Even squarefree positive-definiteness witness fails")
        witness = {
            "positive_leading_minors_of_K_minus_scale_minus_one_I": leading_minors,
            "negative_principal_minor_of_K_minus_scale_I": -1,
            "noninteger_eigenvalue_interval": [offset - scale, offset - scale + 1],
        }
    check_invariant_block(neighbors, embedding, block)
    return {"exponents": list(exponents), "vertices": len(vertices), "pairs_checked": pairs,
            "edges_checked": edges, "block": block, "witness": witness, "invariance": "passed"}


def two_unit_exponents_check(exponent):
    exponents = (1, 1, exponent)
    vertices, neighbors, pairs, edges = ideal_graph(exponents)
    embedding = []
    for coordinates in vertices:
        mask = support(coordinates, exponents)
        embedding.append([int(mask == 1) - int(mask == 2), int(mask == 5) - int(mask == 6)])
    block = [[2 * exponent, -exponent], [-1, 4 * exponent + 1]]
    check_invariant_block(neighbors, embedding, block)
    discriminant = (2 * exponent + 2) ** 2 - 3
    if isqrt(discriminant) ** 2 == discriminant:
        raise AssertionError("Mixed-exponent discriminant unexpectedly square")
    if not (2 * exponent + 1) ** 2 < discriminant < (2 * exponent + 2) ** 2:
        raise AssertionError("Mixed-exponent square bounds fail")
    return {"exponents": list(exponents), "vertices": len(vertices), "pairs_checked": pairs,
            "edges_checked": edges, "block": block, "discriminant": discriminant,
            "invariance": "passed"}


def main():
    record = {
        "status": "passed",
        "method": "Integer invariant-block checks against direct coordinatewise ideal intersections",
        "squarefree": [squarefree_check(prime_count) for prime_count in range(3, 9)],
        "two_unit_exponents": [two_unit_exponents_check(exponent) for exponent in range(1, 9)],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Finite independent checks of the embeddings and obstruction inequalities; the infinite-family conclusions use the written proofs. No floating-point spectrum or Lean run.",
    }
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
