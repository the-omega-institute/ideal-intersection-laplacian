import argparse
import hashlib
from itertools import combinations, product
import json
from pathlib import Path

import sympy


supports = (1, 2, 4, 3, 5, 6)
first, second, third, variable = sympy.symbols('a b c x')


def support_weights(exponents):
    return [sympy.prod(exponents[index] for index in range(3) if support & (1 << index))
            for support in supports]


def support_quotient(exponents, complement=False):
    weights = support_weights(exponents)
    matrix = sympy.zeros(6)
    for row, row_support in enumerate(supports):
        for column, column_support in enumerate(supports):
            if row == column:
                continue
            intersects = bool(row_support & column_support)
            if intersects != complement:
                matrix[row, column] = -weights[column]
                matrix[row, row] += weights[column]
    return matrix


def direct_embedding_check(exponents):
    vertices = [vertex for vertex in product(*(range(bound + 1) for bound in exponents))
                if vertex not in ((0, 0, 0), exponents)]
    labels = [sum(1 << index for index, (value, bound) in enumerate(zip(vertex, exponents))
                  if value < bound) for vertex in vertices]
    reduced_vertices = [(vertex, label) for vertex, label in zip(vertices, labels) if label != 7]
    neighbor_counts = sympy.zeros(6)
    pairs_checked = 0
    for row, row_support in enumerate(supports):
        representative = next(vertex for vertex, label in reduced_vertices if label == row_support)
        for neighbor, neighbor_support in reduced_vertices:
            pairs_checked += 1
            if neighbor == representative:
                continue
            adjacent = any(max(value, other) < bound
                           for value, other, bound in zip(representative, neighbor, exponents))
            if adjacent and neighbor_support != row_support:
                column = supports.index(neighbor_support)
                neighbor_counts[row, column] -= 1
                neighbor_counts[row, row] += 1
    assert neighbor_counts == support_quotient(exponents)
    return {'exponents': exponents, 'vertices': len(vertices),
            'representative_vertex_pairs_checked': pairs_checked}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', action='store_true')
    arguments = parser.parse_args()
    exponents = (first, second, third)
    weights = support_weights(exponents)
    total = sum(weights)
    quotient = support_quotient(exponents)
    complement = support_quotient(exponents, complement=True)
    expected_complement = sympy.Matrix([
        [second + third + second * third, -second, -third, 0, 0, -second * third],
        [-first, first + third + first * third, -third, 0, -first * third, 0],
        [-first, -second, first + second + first * second, -first * second, 0, 0],
        [0, 0, -third, third, 0, 0],
        [0, -second, 0, 0, second, 0],
        [-first, 0, 0, 0, 0, first],
    ])
    assert complement == expected_complement
    assert quotient + complement == total * sympy.eye(6) - sympy.ones(6, 1) * sympy.Matrix([weights])
    for matrix in (quotient, complement):
        weighted = sympy.diag(*weights) * matrix
        assert weighted == weighted.T
        assert matrix * sympy.ones(6, 1) == sympy.zeros(6, 1)
    characteristic = complement.charpoly(variable).as_expr()
    quintic = sympy.Poly(sympy.cancel(characteristic / variable), variable)
    assert sympy.expand(quintic.eval(0) + first * second * third * (first + second + third) * total) == 0
    assert sympy.expand(quintic.eval(first)
                        + first ** 2 * second ** 2 * third ** 2
                        * (first ** 2 + 2 * first - second - third)) == 0
    assert sympy.factor(quintic.eval(1).subs(first, 1)) == second ** 2 * third ** 2 * (second + third - 3)
    reduced_characteristic = quotient.charpoly(variable).as_expr()
    original_quintic = sympy.Poly(sympy.cancel(reduced_characteristic / variable), variable)
    assert sympy.expand(original_quintic.as_expr() + quintic.as_expr().subs(variable, total - variable)) == 0

    cases = []
    for triple in combinations(range(1, 7), 3):
        evaluated = support_quotient(triple)
        polynomial = sympy.Poly(sympy.cancel(evaluated.charpoly(variable).as_expr() / variable), variable)
        factors = sympy.factor_list(polynomial)[1]
        noninteger = any(factor.degree() >= 2 for factor, multiplicity in factors)
        assert noninteger
        prime_witness = None
        for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            if any(factor.degree() >= 2 and sympy.Poly(factor.as_expr(), variable, modulus=prime).is_irreducible
                   for factor, multiplicity in factors):
                prime_witness = prime
                break
        cases.append({'exponents': triple, 'quintic': str(polynomial.as_expr()),
                      'factor_degrees': [int(factor.degree()) for factor, multiplicity in factors],
                      'factorization': str(sympy.factor(polynomial.as_expr())),
                      'has_noninteger_root': noninteger,
                      'smallest_tested_prime_for_nonlinear_factor': prime_witness})
    assert len(cases) == 20
    direct_checks = [direct_embedding_check(triple) for triple in ((1, 2, 3), (2, 3, 4))]
    result = {'origin': 'Independent support-derived checker; not Reza announced but unavailable check_fully_distinct.py.',
              'support_order': ['1', '2', '3', '12', '13', '23'],
              'general_complement_quotient': str(complement),
              'symbolic_identities': 'passed',
              'complement_quintic_at_0': str(sympy.factor(quintic.eval(0))),
              'complement_quintic_at_a': str(sympy.factor(quintic.eval(first))),
              'complement_quintic_at_1_when_a_is_1': str(sympy.factor(quintic.eval(1).subs(first, 1))),
              'complete_requested_independent_range': '1 <= a < b < c <= 6; exactly20triples',
              'cases': cases, 'direct_ideal_embedding_checks': direct_checks,
              'sympy': sympy.__version__,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'General exact six-support and complement identities; two finite direct ideal-graph embedding checks; rational factorization for twenty fully distinct triples. Infinite (1,b,c) theorem uses written endpoint proof and earlier repeated-exponent exceptions. No claim of fullQ3/fullydistinct closure; no Lean or floating-point spectra.'}
    if arguments.json:
        print(json.dumps(result, indent=2))
        return
    print('Independent six-support diagnostic: 1 <= a < b < c <= 6')
    print('a b c | factor degrees | noninteger root | first tested factor witness prime')
    for case in cases:
        print('{} {} {} | {} | {} | {}'.format(*case['exponents'],
              ','.join(map(str, case['factor_degrees'])), case['has_noninteger_root'],
              case['smallest_tested_prime_for_nonlinear_factor']))
    print('20/20 quintics have a nonlinear irreducible factor over Q.')
    print('General complement endpoint identities: passed.')
    print('Direct ideal-graph embeddings: (1,2,3), (2,3,4), passed.')
    print('This is independent output, not a run of the unavailable coauthor script.')
    print('All (1,b,c) are covered by the written proof; fully distinct a>=2 and full Q3 remain open.')


if __name__ == '__main__':
    main()
