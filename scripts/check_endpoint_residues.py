import hashlib
from itertools import permutations, product
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, second, third, variable = sympy.symbols('a b c x')
exponents = (first, second, third)
complement = support_quotient(exponents, complement=True)
quintic = sympy.Poly(sympy.cancel(complement.charpoly(variable).as_expr() / variable), variable)
cubics = {endpoint: sympy.Poly(quintic.eval(endpoint), third) for endpoint in (1, 2)}
assert all(polynomial.degree() == 3 for polynomial in cubics.values())


def integer_complement(triple):
    supports = (1, 2, 4, 3, 5, 6)
    weights = [int(sympy.prod(triple[index] for index in range(3) if support & (1 << index)))
               for support in supports]
    matrix = [[0] * 6 for row in supports]
    for row, left in enumerate(supports):
        for column, right in enumerate(supports):
            if left & right == 0:
                matrix[row][column] = -weights[column]
                matrix[row][row] += weights[column]
    return matrix


def integer_determinant(matrix):
    total = 0
    for permutation in permutations(range(len(matrix))):
        inversions = sum(permutation[left] > permutation[right]
                         for left in range(len(matrix)) for right in range(left + 1, len(matrix)))
        term = (-1) ** inversions
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def determinant_endpoint(triple, endpoint):
    matrix = integer_complement(triple)
    shifted = [[endpoint * int(row == column) - value for column, value in enumerate(entries)]
               for row, entries in enumerate(matrix)]
    determinant = integer_determinant(shifted)
    assert determinant % endpoint == 0
    return determinant // endpoint


def integer_horner(coefficients, argument):
    value = 0
    for coefficient in coefficients:
        value = value * argument + int(coefficient)
    return value


parity_rows = []
pair_rows = []
endpoint_checks = 0
modulo_three_exclusions = []
for prime in (2, 3):
    for left, right in product(range(prime), repeat=2):
        for endpoint in (1, 2):
            coefficients = [int(coefficient.subs({first: left, second: right}))
                            for coefficient in cubics[endpoint].all_coeffs()]
            values = [integer_horner(coefficients, argument) % prime for argument in range(prime)]
            reduced_coefficients = [coefficient % prime for coefficient in coefficients]
            pair_rows.append({'prime': prime, 'a': left, 'b': right, 'endpoint': endpoint,
                              'cubic_coefficients_descending_mod_p': reduced_coefficients,
                              'zero_polynomial': not any(reduced_coefficients),
                              'values_for_all_c_residues': values,
                              'c_roots': [argument for argument, value in enumerate(values) if value == 0]})
    for residues in product(range(prime), repeat=3):
        substitutions = dict(zip(exponents, residues))
        reduced = sympy.Poly(quintic.as_expr().subs(substitutions), variable, modulus=prime)
        representatives = tuple(residue or prime for residue in residues)
        direct = support_quotient(representatives, complement=True)
        assert direct == sympy.Matrix(integer_complement(representatives))
        direct_reduction = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable),
                                      variable, modulus=prime)
        assert reduced == direct_reduction
        values = []
        for endpoint in (1, 2):
            exact = determinant_endpoint(representatives, endpoint)
            expected = int(quintic.eval(endpoint).subs(substitutions)) % prime
            assert exact % prime == expected
            coefficients = [int(coefficient.subs(substitutions))
                            for coefficient in cubics[endpoint].all_coeffs()]
            assert integer_horner(coefficients, residues[2]) % prime == expected
            values.append(expected)
            endpoint_checks += 1
        if prime == 2:
            odd_count = sum(residues)
            expected_polynomial = {0: variable ** 5, 1: variable ** 2 * (variable + 1) ** 3,
                                   2: variable ** 2 * (variable + 1) ** 3,
                                   3: variable * (variable ** 2 + variable + 1) ** 2}[odd_count]
            assert reduced == sympy.Poly(expected_polynomial, variable, modulus=2)
            assert values == [int(odd_count in (0, 3)), 0]
            parity_rows.append({'residues': residues, 'quintic_factorization_mod_two': str(expected_polynomial),
                                'h_C_one_mod_two': values[0], 'h_C_two_mod_two': values[1]})
        elif all(values):
            expected_polynomial = (variable ** 5 if len(set(residues)) == 1
                                   else (variable ** 2 + 1) * (variable ** 3 + variable ** 2 - variable + 1))
            assert reduced == sympy.Poly(expected_polynomial, variable, modulus=3)
            modulo_three_exclusions.append({'residues': residues, 'endpoint_values_mod_three': values,
                                            'quintic_mod_three': str(expected_polynomial)})
assert [tuple(row['residues']) for row in modulo_three_exclusions] == [
    (0, 0, 0), (1, 2, 2), (2, 1, 2), (2, 2, 1), (2, 2, 2)]
assert all(row['c_roots'] for row in pair_rows)
assert endpoint_checks == 70 and len(pair_rows) == 26

fixtures = []
for triple in ((8, 17, 22), (8, 17, 23)):
    polynomial = sympy.Poly(quintic.as_expr().subs(dict(zip(exponents, triple))), variable)
    values = [determinant_endpoint(triple, endpoint) for endpoint in (1, 2)]
    assert values == [int(polynomial.eval(endpoint)) for endpoint in (1, 2)]
    assert all(value % 3 for value in values)
    low_roots = int(polynomial.count_roots(0, 3))
    assert low_roots >= 1
    fixtures.append({'exponents': triple, 'endpoint_values': values, 'positive_roots_in_0_3': low_roots})

controls = []
for triple, endpoint in (((9, 9, 136), 1), ((10, 10, 12), 2)):
    assert determinant_endpoint(triple, endpoint) == 0
    polynomial = sympy.Poly(quintic.as_expr().subs(dict(zip(exponents, triple))), variable)
    assert polynomial.eval(endpoint) == 0
    controls.append({'exponents': triple, 'endpoint': endpoint,
                     'scope': 'Previously settled repeated-exponent case; global endpoint surface is nonempty'})

source = Path(__file__)
print(json.dumps({'primes': [2, 3],
                  'endpoint_cubic_coefficients_descending': {
                      str(endpoint): [str(sympy.factor(coefficient)) for coefficient in polynomial.all_coeffs()]
                      for endpoint, polynomial in cubics.items()},
                  'parity_table': parity_rows, 'pair_root_tables': pair_rows,
                  'pair_endpoint_rows': len(pair_rows), 'independent_integer_determinant_endpoint_checks': endpoint_checks,
                  'modulo_three_simultaneous_exclusions': modulo_three_exclusions,
                  'direct_integer_fixtures': fixtures, 'existing_endpoint_zero_controls': controls,
                  'sympy': sympy.__version__, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                  'scope': 'Complete residue tables for fixed primes2and3; independent720term integer determinants check both endpoints at35positive residue representatives, including endpoint2mod2 without field division. Written low-root argument proves infinite mod3classes. No exponent scan, numerical spectrum or Lean. FullQ3 remains open.'}, indent=2))
