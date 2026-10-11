import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, second, third, variable, first_offset, gap_offset = sympy.symbols('a b c x u v')
quotient = support_quotient((first, second, third), complement=True)
quintic = sympy.Poly(sympy.cancel(quotient.charpoly(variable).as_expr() / variable), variable)
total = first + second + third + first * second + first * third + second * third
assert sympy.expand(quintic.eval(0) + first * second * third * (first + second + third) * total) == 0
leading = first ** 2 + second ** 2 - 1
quadratic = (first ** 3 - 4 * first ** 2 * second ** 2 + 2 * first ** 2 * second
             - first ** 2 + 2 * first * second ** 2 + first * second - 3 * first
             + second ** 3 - second ** 2 - 3 * second + 3)
linear = (first - 1) * (second - 1) * (2 * first * second + 3 * first + 3 * second - 3)
constant = ((first - 1) * (second - 1) * (first + second - 1)
            * (first * second + first + second - 1))
endpoint = leading * third ** 3 + quadratic * third ** 2 + linear * third + constant
assert sympy.expand(quintic.eval(1) - endpoint) == 0
cutoff = 4 * first ** 2 - 2 * first
remainder = 4 * first ** 4 - first ** 3 - 5 * first ** 2 - first + 3
assert sympy.expand(quadratic + cutoff * leading
                    - (second ** 2 * (second - 1) + (2 * first ** 2 + first - 3) * second
                       + remainder)) == 0
positive_remainder = (4 * first_offset ** 4 + 31 * first_offset ** 3
                      + 85 * first_offset ** 2 + 95 * first_offset + 37)
assert sympy.expand(remainder.subs(first, first_offset + 2) - positive_remainder) == 0
assert all(value > 0 for value in sympy.Poly(positive_remainder, first_offset).all_coeffs())

minimum_three_quintic = sympy.Poly(quintic.as_expr().subs(first, 3), variable)
minimum_three_endpoint = ((second ** 2 + 8) * third ** 3
                          + (second - 1) * (second ** 2 - 30 * second - 12) * third ** 2
                          + 6 * (second - 1) * (3 * second + 2) * third
                          + 4 * (second - 1) * (second + 2) * (2 * second + 1))
assert sympy.expand(minimum_three_quintic.eval(1) - minimum_three_endpoint) == 0
second_endpoint = minimum_three_quintic.eval(2)
first_region = 104 * gap_offset ** 3 + 1238 * gap_offset ** 2 + 4018 * gap_offset + 2344
second_region = ((5 * first_offset ** 2 + 54 * first_offset + 153) * gap_offset ** 3
                 + (20 * first_offset ** 3 + 262 * first_offset ** 2 + 1179 * first_offset + 1863)
                 * gap_offset ** 2
                 + (25 * first_offset ** 4 + 426 * first_offset ** 3 + 2642 * first_offset ** 2
                    + 7011 * first_offset + 6624) * gap_offset
                 + 10 * first_offset ** 5 + 218 * first_offset ** 4 + 1828 * first_offset ** 3
                 + 7200 * first_offset ** 2 + 12600 * first_offset + 6480)
assert sympy.expand(second_endpoint.subs({second: 4, third: gap_offset + 6}) - first_region) == 0
assert sympy.expand(second_endpoint.subs({second: first_offset + 5, third: first_offset + gap_offset + 6})
                    - second_region) == 0
assert all(value > 0 for region in (first_region, second_region)
           for value in sympy.Poly(region, first_offset, gap_offset).coeffs())


def horner(coefficients, argument):
    value = Fraction(0)
    for coefficient in coefficients:
        value = value * argument + int(coefficient)
    return value


cases = []
negative_ranges = {}
for lower in range(4, int(cutoff.subs(first, 3))):
    for upper in range(lower + 1, int(cutoff.subs(first, 3))):
        exponents = (3, lower, upper)
        evaluated = support_quotient(exponents, complement=True)
        polynomial = sympy.Poly(sympy.cancel(evaluated.charpoly(variable).as_expr() / variable), variable)
        assert polynomial == sympy.Poly(minimum_three_quintic.as_expr().subs({second: lower, third: upper}), variable)
        coefficients = [int(value) for value in polynomial.all_coeffs()]
        at_one = horner(coefficients, 1)
        at_two = horner(coefficients, 2)
        endpoint_coefficients = [int(value) for value in
                                 sympy.Poly(minimum_three_endpoint.subs(second, lower), third).all_coeffs()]
        assert at_one == horner(endpoint_coefficients, upper) == polynomial.eval(1)
        assert at_two == polynomial.eval(2)
        assert at_one != 0
        if at_one > 0:
            interval = (Fraction(0), Fraction(1))
        elif exponents == (3, 4, 5):
            interval = (Fraction(1), Fraction(3, 2))
        else:
            assert at_two > 0
            interval = (Fraction(1), Fraction(2))
        endpoint_values = [horner(coefficients, argument) for argument in interval]
        assert endpoint_values[0] * endpoint_values[1] < 0
        assert all(value == polynomial.eval(sympy.Rational(argument.numerator, argument.denominator))
                   for argument, value in zip(interval, endpoint_values))
        vertex_count = 4 * (lower + 1) * (upper + 1) - 2
        assert interval[1] <= 2 < sum([3, lower, upper, 3 * lower, 3 * upper, lower * upper])
        cases.append({'exponents': exponents, 'quintic_coefficients': coefficients,
                      'h1': int(at_one), 'h2': int(at_two),
                      'complement_interval': [str(argument) for argument in interval],
                      'endpoint_values': [str(value) for value in endpoint_values],
                      'graph_vertex_count': vertex_count,
                      'graph_eigenvalue_interval': [str(vertex_count - interval[1]), str(vertex_count - interval[0])],
                      'independent_quotient_and_horner_checks': 'passed'})
        if at_one < 0:
            negative_ranges.setdefault(lower, []).append(upper)

assert len(cases) == 325
assert sum(case['h1'] > 0 for case in cases) == 257
assert sum(case['h1'] < 0 for case in cases) == 68
for lower, upper_values in negative_ranges.items():
    assert upper_values == list(range(min(upper_values), max(upper_values) + 1))
exception = next(case for case in cases if case['exponents'] == (3, 4, 5))
assert exception['quintic_coefficients'] == [1, -83, 2327, -24133, 60576, -42480]
assert exception['h1'] == -3792 and exception['h2'] == -540
assert exception['endpoint_values'] == ['-3792', '48825/32']
exception_polynomial = sympy.Poly.from_list(exception['quintic_coefficients'], variable)
assert exception_polynomial.count_roots(1, sympy.Rational(3, 2)) == 1

source_paths = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'symbolic_identities': 'passed',
                  'general_h1_cubic_coefficients': [str(expression) for expression in (leading, quadratic, linear, constant)],
                  'uniform_cutoff': str(cutoff),
                  'cutoff_positive_remainder_at_a2_plus_u': str(positive_remainder),
                  'minimum_three_h1': str(minimum_three_endpoint),
                  'minimum_three_h2_positive_regions': [str(first_region), str(second_region)],
                  'finite_domain_derived_from_cutoff': 'a=3, 4<=b<c<4*a^2-2*a=30',
                  'counts': {'total': len(cases), 'h1_positive': 257, 'h1_negative': 68, 'h1_zero': 0},
                  'negative_h1_ranges': [{'b': lower, 'c_min': min(upper_values), 'c_max': max(upper_values)}
                                         for lower, upper_values in negative_ranges.items()],
                  'exception_sturm_count_between_1_and_3_over_2': 1,
                  'cases': cases, 'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                                    for source in source_paths},
                  'scope': 'Written general endpoint cutoff for all a,b>=2, c>=4a^2-2a; positive expansions for minimum-three h2; exact quotient/Horner sign certificates for every one of the 325 pairs in the theorem-derived minimum-three finite domain, with one rational-endpoint/Sturm exception. Combined with prior proofs, every triple with minimum exponent<=3 is settled. Pairwise distinct a>=4 with c<4a^2-2a and nonsquarefree higher-prime vectors remain open. No Lean or floating-point spectra.'}, indent=2))
