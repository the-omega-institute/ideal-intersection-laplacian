import hashlib
from itertools import permutations, product
import json
from pathlib import Path

import sympy

import check_modular_endpoints as diagnostic


first, second, third, variable = sympy.symbols('a b c x')
complement = sympy.Matrix([
    [second + third + second * third, -second, -third, 0, 0, -second * third],
    [-first, first + third + first * third, -third, 0, -first * third, 0],
    [-first, -second, first + second + first * second, -first * second, 0, 0],
    [0, 0, -third, third, 0, 0],
    [0, -second, 0, 0, second, 0],
    [-first, 0, 0, 0, 0, first],
])
quintic = sympy.Poly(sympy.cancel(complement.charpoly(variable).as_expr() / variable), variable)
original, total = diagnostic.build_B_and_N()
weights = sympy.Matrix([[first, second, third, first * second, first * third, second * third]])
assert original + complement == total * sympy.eye(6) - sympy.ones(6, 1) * weights
reflected = {endpoint: diagnostic.build_h_C_endpoint(endpoint, original, total) for endpoint in (1, 2)}
for endpoint in (1, 2):
    assert sympy.expand(reflected[endpoint] - quintic.eval(endpoint)) == 0
assert [int(quintic.eval(endpoint).subs({first: 4, second: 5, third: 6}))
        for endpoint in (1, 2)] == [-23520, 1656]
endpoint_functions = {endpoint: sympy.lambdify((first, second, third), quintic.eval(endpoint), 'math')
                      for endpoint in (1, 2)}


def modular_determinant(matrix, prime):
    values = [[int(value) % prime for value in row] for row in matrix]
    determinant = 1
    for column in range(len(values)):
        pivot = next((row for row in range(column, len(values)) if values[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            values[column], values[pivot] = values[pivot], values[column]
            determinant = -determinant
        entry = values[column][column]
        determinant = determinant * entry % prime
        inverse = pow(entry, -1, prime)
        for row in range(column + 1, len(values)):
            multiplier = values[row][column] * inverse % prime
            for index in range(column, len(values)):
                values[row][index] = (values[row][index] - multiplier * values[column][index]) % prime
    return determinant % prime


def integer_determinant(matrix):
    result = 0
    for permutation in permutations(range(6)):
        inversions = sum(permutation[left] > permutation[right]
                         for left in range(6) for right in range(left + 1, 6))
        term = (-1) ** inversions
        for row, column in enumerate(permutation):
            term *= int(matrix[row][column])
        result += term
    return result


summary = []
determinant_checks = 0
for prime in (2, 3, 5, 7, 11, 13):
    table = diagnostic.modular_analysis(reflected[1], reflected[2], prime)
    independent_roots = {endpoint: {(left, right): [] for left, right in product(range(prime), repeat=2)}
                         for endpoint in (1, 2)}
    for triple in product(range(prime), repeat=3):
        direct = complement.subs(dict(zip((first, second, third), triple)))
        for endpoint in (1, 2):
            expected = int(endpoint_functions[endpoint](*triple)) % prime
            shifted = (endpoint * sympy.eye(6) - direct).tolist()
            if prime == endpoint:
                determinant = integer_determinant(shifted)
                assert determinant % endpoint == 0
                reconstructed = determinant // endpoint % prime
            else:
                reconstructed = modular_determinant(shifted, prime) * pow(endpoint, -1, prime) % prime
            assert reconstructed == expected
            determinant_checks += 1
            if reconstructed == 0:
                independent_roots[endpoint][triple[:2]].append(triple[2])
    for row in table['pairs']:
        pair = (row['a'], row['b'])
        assert row['c_roots_endpoint_one'] == independent_roots[1][pair]
        assert row['c_roots_endpoint_two'] == independent_roots[2][pair]
        assert row['c_roots_either_endpoint'] == sorted(set(independent_roots[1][pair]) | set(independent_roots[2][pair]))
    if prime == 2:
        assert table['surviving_union_count'] == 8 and table['both_zero_intersection_count'] == 6
    if prime == 3:
        assert table['surviving_union_count'] == 22 and table['both_zero_intersection_count'] == 15
    for triple, endpoint in (((9, 9, 136), 1), ((10, 10, 12), 2)):
        residues = tuple(value % prime for value in triple)
        assert residues[2] in independent_roots[endpoint][residues[:2]]
    summary.append({key: table[key] for key in ('prime', 'surviving_union_count',
                                               'excluded_both_nonzero_count', 'both_zero_intersection_count')})
assert determinant_checks == 8062
assert int(endpoint_functions[1](9, 9, 136)) == 0
assert int(endpoint_functions[2](10, 10, 12)) == 0
counterexample = {endpoint: int(endpoint_functions[endpoint](9, 9, 136)) for endpoint in (1, 2)}
assert counterexample[1] == 0 and counterexample[2] != 0
source = Path(__file__)
print(json.dumps({'necessary_condition': 'h_C(1)=0 OR h_C(2)=0', 'generic_reflection_identity': 'passed',
                  'complete_prime_summaries': summary, 'independent_determinant_endpoint_checks': determinant_checks,
                  'modular_gaussian_determinants': 8054, 'integer_determinants_for_endpoint_two_mod_two': 8,
                  'intersection_counterexample': {'exponents': [9, 9, 136], 'endpoint_values': counterexample,
                                                   'scope': 'Already settled repeated family; endpoint-one zero does not require endpoint-two zero'},
                  'sympy': sympy.__version__,
                  'source_sha256': {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                                    for path in (source, source.with_name('check_modular_endpoints.py'))},
                  'scope': 'Complete8062endpoint checks over all4031residue triples at six fixed coauthor primes;377pair rootsets on both surfaces agree with corrected reflected-H script. No bound on positive exponents or integrality asserted for surviving residues. No exponent scan, numerical spectrum or Lean.'}, indent=2))
