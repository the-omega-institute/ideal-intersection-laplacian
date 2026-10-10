import hashlib
import json
from pathlib import Path

import sympy

from check_aa_b import cubic_coeffs, cubic_poly


parameter, third, variable, offset = sympy.symbols('a b x offset')
quotient = sympy.Matrix([
    [parameter ** 2 + parameter * third, 0, -parameter ** 2, -parameter * third],
    [0, 2 * parameter * third, 0, -2 * parameter * third],
    [-2 * parameter, 0, 2 * parameter + 2 * parameter * third, -2 * parameter * third],
    [-parameter, -third, -parameter ** 2, parameter ** 2 + parameter + third],
])
first, second, constant = cubic_coeffs(parameter, third)
cubic = variable ** 3 - first * variable ** 2 + second * variable - constant


def equal(first_expression, second_expression):
    assert sympy.expand(first_expression - second_expression) == 0


equal(quotient.charpoly(variable).as_expr(), variable * cubic)
equal(cubic.subs(variable, 2 * parameter * third), 2 * parameter ** 2 * third ** 2)
sign_numerator = parameter ** 3 + 2 * parameter ** 2 + 2 * parameter + 1
equal(cubic.subs(variable, 2 * parameter * third - 1),
      -(parameter + third + 1) * (sign_numerator - parameter * (2 * parameter + 1) * third))
threshold = 4 * parameter + 5
product = parameter ** 3 * (2 * parameter + 1)
bound_numerator = (parameter - 5) * (2 * parameter - 5)
equal(product + threshold ** 2 - parameter * (3 * parameter + 1) * threshold,
      (parameter + 1) ** 2 * bound_numerator)
gap_numerator = 41 * parameter ** 3 - 17 * parameter ** 2 - 11 * parameter + 5
equal(sign_numerator * threshold - parameter * (2 * parameter + 1) * bound_numerator,
      gap_numerator)
equal(gap_numerator.subs(parameter, offset + 2),
      41 * offset ** 3 + 229 * offset ** 2 + 413 * offset + 243)

expected = {1: {(4, 2): 5, (6, 5): 7, (10, 12): 13, (22, 35): 17},
            2: {(12, 7): 13},
            3: {(12, 4): 5, (20, 9): 7, (52, 30): 7}}
index_records = []
for factor_index, expected_pairs in expected.items():
    index_constant = (factor_index + 1) ** 3 * (factor_index + 2)
    records = []
    actual_pairs = []
    for divisor in sympy.divisors(index_constant):
        divisor = int(divisor)
        record = {'divisor': divisor, 'admissible': False}
        if (divisor - 1) % factor_index:
            record['reason'] = 'Wrong factor-index residue'
            records.append(record)
            continue
        repeated = (divisor - 1) // factor_index - 1
        record['repeated_exponent'] = repeated
        if repeated < 2:
            record['reason'] = 'a below2'
            records.append(record)
            continue
        constant_product = repeated ** 3 * (2 * repeated + 1)
        assert constant_product % divisor == 0
        second_factor = constant_product // divisor
        assert (second_factor - 1) % (repeated + 1) == 0
        second_index = (second_factor - 1) // (repeated + 1)
        final_exponent = (repeated - 1) * (2 * repeated - 1) - factor_index * second_index
        record.update({'factor_pair': [divisor, second_factor],
                       'second_index': second_index, 'third_exponent': final_exponent})
        if divisor > second_factor or final_exponent < 1:
            record['reason'] = 'Not the smaller factor' if divisor > second_factor else 'b not positive'
            records.append(record)
            continue
        pair = (repeated, final_exponent)
        assert pair in expected_pairs
        discriminant = ((repeated + 1) ** 2 * final_exponent ** 2
                        + 2 * repeated * (3 * repeated + 1) * final_exponent + repeated ** 2)
        assert discriminant == (second_index - factor_index) ** 2
        assert divisor + second_factor == ((repeated + 1) ** 2 * final_exponent
                                          + repeated * (3 * repeated + 1))
        polynomial = cubic_poly(*pair)
        evaluated_quotient = quotient.subs({parameter: repeated, third: final_exponent})
        equal(evaluated_quotient.charpoly(variable).as_expr(), variable * polynomial.as_expr())
        prime = expected_pairs[pair]
        assert sympy.isprime(prime)
        residues = [int(polynomial.eval(residue)) % prime for residue in range(prime)]
        horner_residues = []
        for residue in range(prime):
            value = 0
            for coefficient in polynomial.all_coeffs():
                value = (value * residue + int(coefficient)) % prime
            horner_residues.append(value)
        assert residues == horner_residues and all(residues)
        record.update({'admissible': True, 'square_root_discriminant': second_index - factor_index,
                       'polynomial': str(polynomial.as_expr()), 'prime': prime,
                       'values_modulo_prime': residues, 'independent_horner': 'passed'})
        actual_pairs.append(pair)
        records.append(record)
    assert set(actual_pairs) == set(expected_pairs)
    index_records.append({'index': factor_index, 'index_constant': index_constant,
                          'all_divisors': records, 'complete_positive_pairs': actual_pairs})

source_paths = [Path(__file__), Path(__file__).with_name('check_aa_b.py')]
print(json.dumps({'symbolic_quotient_and_endpoint_identities': 'passed',
                  'fourth_cutoff_identity': 'passed', 'strict_gap_identity': 'passed',
                  'positive_gap_in_a_minus_2': '41*offset**3 + 229*offset**2 + 413*offset + 243',
                  'complete_fixed_index_certificates': index_records,
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                                    for source in source_paths},
                  'scope': 'General quotient, endpoint, cutoff and positive-gap identities; complete divisors24,108,320 for indices1,2,3; eight root-free modular cubic certificates checked by independent Horner arithmetic. Infinite-family conclusion uses the written proof and prior boundary proof. No parameter-range scan or Lean; fully unequal triples and fullQ3 remain open.'}, indent=2))
