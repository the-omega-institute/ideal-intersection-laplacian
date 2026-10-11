import hashlib
import json
from math import isqrt
from pathlib import Path

import sympy

from check_aa_b import cubic_poly


parameter = sympy.Symbol('a')
product = parameter ** 3 * (2 * parameter + 1)
threshold = 2 * parameter + 3
numerator = (parameter - 3) * (2 * parameter - 3)
second_bound = numerator / threshold
first_bound = 2 * (parameter - 1) * (parameter - 2) / (parameter + 2)


def equal(first, second):
    if sympy.expand(first - second) != 0:
        raise AssertionError('Polynomial identity failed')


equal(product, (parameter + 2)
      * (2 * parameter ** 3 - 3 * parameter ** 2 + 6 * parameter - 12) + 24)
equal(product + threshold ** 2 - parameter * (3 * parameter + 1) * threshold,
      (parameter + 1) ** 2 * numerator)
equal(numerator, (parameter - 6) * threshold + 27)
gap_numerator = 2 * parameter ** 3 - parameter ** 2 - parameter - 6
equal(2 * (parameter - 1) * (parameter - 2) * threshold
      - numerator * (parameter + 2), gap_numerator)
offset = sympy.Symbol('offset')
equal(gap_numerator.subs(parameter, offset + 2),
      2 * offset ** 3 + 11 * offset ** 2 + 19 * offset + 4)

expected = {(4, 2): 5, (6, 5): 7, (10, 12): 13, (22, 35): 17}
certificates = []
candidate_divisors = []
for divisor in sympy.divisors(24):
    repeated = int(divisor) - 2
    record = {'divisor_of_24': int(divisor), 'repeated_exponent': repeated}
    if repeated < 2:
        record['admissible'] = False
        candidate_divisors.append(record)
        continue
    first_factor = repeated + 2
    constant = repeated ** 3 * (2 * repeated + 1)
    assert constant % first_factor == 0
    second_factor = constant // first_factor
    denominator = (repeated + 1) ** 2
    third_numerator = first_factor + second_factor - repeated * (3 * repeated + 1)
    assert third_numerator % denominator == 0
    third = third_numerator // denominator
    record.update({'third_exponent': third, 'admissible': third >= 1})
    candidate_divisors.append(record)
    if third < 1:
        continue
    assert first_factor <= second_factor
    assert (second_factor - first_factor) % (repeated + 1) == 0
    square_root = (second_factor - first_factor) // (repeated + 1)
    discriminant = ((repeated + 1) ** 2 * third ** 2
                    + 2 * repeated * (3 * repeated + 1) * third + repeated ** 2)
    assert discriminant == square_root ** 2
    assert sympy.Rational(third) == first_bound.subs(parameter, repeated)
    polynomial = cubic_poly(repeated, third)
    prime = expected[(repeated, third)]
    residues = [int(polynomial.eval(residue)) % prime for residue in range(prime)]
    assert all(residues)
    certificates.append({'repeated_exponent': repeated, 'third_exponent': third,
                         'factor_pair': [first_factor, second_factor],
                         'square_root_discriminant': square_root,
                         'polynomial': str(polynomial.as_expr()),
                         'prime': prime, 'values_modulo_prime': residues})
assert {(record['repeated_exponent'], record['third_exponent'])
        for record in certificates} == set(expected)

small_cases = []
for repeated in [5, 6]:
    bound = second_bound.subs(parameter, repeated)
    assert 1 <= bound < 2
    discriminant = (repeated + 1) ** 2 + 2 * repeated * (3 * repeated + 1) + repeated ** 2
    lower = isqrt(discriminant)
    assert lower ** 2 < discriminant < (lower + 1) ** 2
    small_cases.append({'repeated_exponent': repeated, 'second_bound': str(bound),
                        'remaining_third_exponent': 1, 'discriminant': discriminant,
                        'consecutive_square_roots': [lower, lower + 1]})

print(json.dumps({'symbolic_identities': 'passed',
                  'all_divisors_of_24': candidate_divisors,
                  'first_nonboundary_factor_certificates': certificates,
                  'additional_complete_fixed_exponents': small_cases,
                  'second_cutoff': str(second_bound),
                  'sympy': sympy.__version__,
                  'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'cubic_source_sha256': hashlib.sha256(Path(__file__).with_name('check_aa_b.py').read_bytes()).hexdigest(),
                  'scope': 'Complete d=a+2 cases via divisors of24; four exact modular witnesses; written all-a second cutoff; two remaining b=1 discriminants for a5,6. No parameter-range scan or Lean; fullQ3open.'}, indent=2))
