import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

import sympy

from check_aa_b import cubic_poly


parameter, factor_index = sympy.symbols('a j')
period = parameter + 1
product = parameter ** 3 * (2 * parameter + 1)
boundary = (parameter - 1) * (2 * parameter - 1)
first_factor = period * factor_index + 1
index_constant = (factor_index + 1) ** 3 * (factor_index + 2)
division_quotient = (2 * factor_index ** 3 * parameter ** 3
                     - factor_index ** 2 * (factor_index + 2) * parameter ** 2
                     + factor_index * (factor_index + 1) * (factor_index + 2) * parameter
                     - (factor_index + 1) ** 2 * (factor_index + 2))


def equal(first, second):
    if sympy.expand(first - second) != 0:
        raise AssertionError('Polynomial identity failed')


equal(factor_index ** 4 * product - index_constant, first_factor * division_quotient)
equal(product, 1 + period * (3 * parameter - 2) + period ** 2 * boundary)
threshold = 3 * parameter + 4
numerator = 2 * (parameter - 4) * (parameter - 2)
third_bound = numerator / threshold
equal(product + threshold ** 2 - parameter * (3 * parameter + 1) * threshold,
      period ** 2 * numerator)
equal(9 * numerator, (6 * parameter - 44) * threshold + 320)
gap_numerator = 2 * parameter ** 3 - parameter ** 2 - 5 * parameter - 12
equal((parameter - 3) * (2 * parameter - 3) * threshold
      - numerator * (2 * parameter + 3), gap_numerator)
offset = sympy.Symbol('offset')
equal(gap_numerator.subs(parameter, offset + 3),
      2 * offset ** 3 + 17 * offset ** 2 + 43 * offset + 18)

index_value = 2
constant = (index_value + 1) ** 3 * (index_value + 2)
divisor_records = []
admissible = []
for divisor in sympy.divisors(constant):
    divisor = int(divisor)
    record = {'divisor': divisor, 'admissible': False}
    if (divisor - 1) % index_value:
        record['reason'] = 'Wrong residue for j(a+1)+1'
        divisor_records.append(record)
        continue
    repeated = (divisor - 1) // index_value - 1
    record['repeated_exponent'] = repeated
    if repeated < 2:
        record['reason'] = 'a below2'
        divisor_records.append(record)
        continue
    constant_product = repeated ** 3 * (2 * repeated + 1)
    assert gcd(divisor, index_value) == 1
    assert constant_product % divisor == 0
    second_factor = constant_product // divisor
    record['factor_pair'] = [divisor, second_factor]
    if divisor > second_factor:
        record['reason'] = 'Not the smaller factor'
        divisor_records.append(record)
        continue
    assert (second_factor - 1) % (repeated + 1) == 0
    second_index = (second_factor - 1) // (repeated + 1)
    third = (repeated - 1) * (2 * repeated - 1) - index_value * second_index
    record.update({'second_index': second_index, 'third_exponent': third})
    if third < 1:
        record['reason'] = 'b not positive'
        divisor_records.append(record)
        continue
    record['admissible'] = True
    square_root = second_index - index_value
    discriminant = ((repeated + 1) ** 2 * third ** 2
                    + 2 * repeated * (3 * repeated + 1) * third + repeated ** 2)
    assert discriminant == square_root ** 2
    assert divisor + second_factor == (repeated + 1) ** 2 * third + repeated * (3 * repeated + 1)
    polynomial = cubic_poly(repeated, third)
    prime = 13
    residues = [int(polynomial.eval(residue)) % prime for residue in range(prime)]
    assert all(residues)
    record.update({'square_root_discriminant': square_root,
                   'polynomial': str(polynomial.as_expr()),
                   'prime': prime, 'values_modulo_prime': residues})
    admissible.append([repeated, third])
    divisor_records.append(record)
assert admissible == [[12, 7]]

small_cases = []
for repeated, expected_bound in [(7, sympy.Rational(6, 5)),
                                 (8, sympy.Rational(12, 7)),
                                 (9, sympy.Rational(70, 31))]:
    bound = third_bound.subs(parameter, repeated)
    assert bound == expected_bound
    for third in range(1, int(sympy.floor(bound)) + 1):
        discriminant = ((repeated + 1) ** 2 * third ** 2
                        + 2 * repeated * (3 * repeated + 1) * third + repeated ** 2)
        lower = isqrt(discriminant)
        assert lower ** 2 < discriminant < (lower + 1) ** 2
        small_cases.append({'repeated_exponent': repeated, 'third_exponent': third,
                            'third_bound': str(bound), 'discriminant': discriminant,
                            'consecutive_square_roots': [lower, lower + 1]})
assert len(small_cases) == 4
print(json.dumps({'symbolic_identities': 'passed',
                  'fixed_index': index_value, 'index_constant': constant,
                  'all_divisor_candidates': divisor_records,
                  'complete_positive_exponent_pairs': admissible,
                  'additional_complete_fixed_exponents': small_cases,
                  'third_cutoff': str(third_bound),
                  'sympy': sympy.__version__,
                  'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'cubic_source_sha256': hashlib.sha256(Path(__file__).with_name('check_aa_b.py').read_bytes()).hexdigest(),
                  'scope': 'General fixed-index divisibility identity; complete j2 candidates via divisors108; one cubic modulo13; four remaining discriminants under proved bound for a7,8,9. No unbounded scan or Lean; arbitrary j and fullQ3 remain open.'}, indent=2))
