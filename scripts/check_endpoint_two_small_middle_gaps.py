import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable, shift = sympy.symbols('a b c x m')
parameters = (first, middle, last)
matrix = support_quotient(parameters, complement=True)
quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
endpoint = quintic.eval(2)


def integer_horner(coefficients, point):
    value = 0
    for coefficient in coefficients:
        value = value * point + coefficient
    return value


def positive_divisors(integer):
    divisors = set()
    for candidate in range(1, isqrt(integer) + 1):
        if integer % candidate == 0:
            divisors.add(candidate)
            divisors.add(integer // candidate)
    return sorted(divisors)


families = []
total_candidates = 0
for gap, threshold in ((1, 20), (3, 16), (4, 64)):
    polynomial = sympy.Poly(endpoint.subs(middle, first + gap), last)
    lower = 2 * first + gap - 10
    upper = lower + 1
    negative_lower = sympy.Poly((-polynomial.eval(lower)).subs(first, threshold + shift).expand(), shift)
    positive_upper = sympy.Poly(polynomial.eval(upper).subs(first, threshold + shift).expand(), shift)
    assert all(coefficient > 0 for coefficient in negative_lower.all_coeffs())
    assert all(coefficient > 0 for coefficient in positive_upper.all_coeffs())
    assert sympy.expand(lower - (first + gap)) == first - 10
    base = []
    candidates_checked = 0
    for minimum in range(8, threshold):
        second = minimum + gap
        specialized = sympy.Poly(polynomial.as_expr().subs(first, minimum), last)
        coefficients = list(map(int, specialized.all_coeffs()))
        content = 0
        for coefficient in coefficients:
            content = gcd(content, abs(coefficient))
        primitive = [coefficient // content for coefficient in coefficients]
        direct_polynomial = sympy.Poly.from_list(primitive, last)
        assert direct_polynomial == specialized.primitive()[1]
        assert primitive[-1] != 0
        candidates = [candidate for candidate in positive_divisors(abs(primitive[-1])) if candidate > second]
        values = [integer_horner(primitive, candidate) for candidate in candidates]
        integer_roots = [candidate for candidate, value in zip(candidates, values) if value == 0]
        rational_roots = direct_polynomial.ground_roots()
        extracted = sorted(int(root) for root in rational_roots if root.is_Integer and root > second)
        assert integer_roots == extracted == []
        base.append({'pair': [minimum, second], 'primitive_cubic_coefficients_descending_in_c': primitive,
                     'constant_divisor_candidates_c_above_b': candidates, 'integer_Horner_at_all_candidates': values,
                     'integer_roots_c_above_b': integer_roots,
                     'all_rational_roots': {str(root): int(multiplicity) for root, multiplicity in rational_roots.items()},
                     'complete_for_all_integer_c_above_b': True})
        candidates_checked += len(candidates)
    families.append({'gap': gap, 'written_tail_minimum': threshold,
                     'family_cubic_coefficients_descending_in_c': list(map(str, polynomial.all_coeffs())),
                     'real_root_bracket': [str(lower), str(upper)],
                     'positive_coefficients_descending_in_m_at_a_threshold_plus_m': {
                         'negative_lower': list(map(int, negative_lower.all_coeffs())),
                         'positive_upper': list(map(int, positive_upper.all_coeffs()))},
                     'complete_finite_base_pairs': len(base), 'constant_divisor_candidates_checked': candidates_checked,
                     'finite_base': base})
    total_candidates += candidates_checked
assert sum(family['complete_finite_base_pairs'] for family in families) == 76

fixtures = []
for minimum, gap in ((20, 1), (40, 1), (16, 3), (32, 3), (64, 4), (128, 4)):
    second = minimum + gap
    left = 2 * minimum + gap - 10
    right = left + 1
    cubic = sympy.Poly(endpoint.subs({first: minimum, middle: second}), last)
    assert left > second and cubic.eval(left) < 0 < cubic.eval(right)
    assert cubic.count_roots(left, right) == 1
    assert cubic.count_roots(second, sympy.oo) == 1
    direct_records = []
    for third in (left, right):
        exponents = (minimum, second, third)
        direct = support_quotient(exponents, complement=True)
        polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        assert polynomial == sympy.Poly(quintic.as_expr().subs(dict(zip(parameters, exponents))), variable)
        coefficients = list(map(int, polynomial.all_coeffs()))
        values = [integer_horner(coefficients, point) for point in (0, 1, 2)]
        assert values == [int(polynomial.eval(point)) for point in (0, 1, 2)]
        assert values[2] == cubic.eval(third)
        direct_records.append({'exponents': exponents, 'quintic_coefficients': coefficients,
                               'integer_Horner_at_0_1_2': values,
                               'positive_roots_strictly_between_0_and_3': int(polynomial.count_roots(0, 3))
                               - int(polynomial.eval(3) == 0)})
    fixtures.append({'pair': [minimum, second], 'gap': gap, 'unique_exponent_root_bracket': [left, right],
                     'direct_quotients': direct_records})
control = support_quotient((10, 10, 12), complement=True)
control_polynomial = sympy.Poly(sympy.cancel(control.charpoly(variable).as_expr() / variable), variable)
assert control_polynomial.eval(2) == 0
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'combined_result': 'For every integer a>=8,1<=d<=4,c>a+d, the ordered triple(a,a+d,c)has h_C(2)!=0. Gap2uses the preceding preserved theorem; new gaps1,3,4use written tails and complete76pair finite base.',
                  'structural_consequence': 'Every fully distinct integer endpoint-two zero at a>=8 must have d=b-a>=5 and a<2d^2+20, combining small-middle-gap exclusion with the preceding growing-gap theorem.',
                  'nonintegrality_consequence': 'All-even triples and permutations(1,3,2)/(3,3,0)mod4 with a>=8,1<=b-a<=4 are nonintegral by prior conditional exclusion of1 and uniform low root. Other endpoint-one cases remain open.',
                  'new_gap_families': families, 'finite_base_pairs': 76,
                  'finite_base_divisor_candidates_checked': total_candidates,
                  'fixed_pair_fixtures': fixtures,
                  'outside_hypothesis_control': {'exponents': [10, 10, 12], 'h_C_at_two': 0,
                                                'scope': 'Repeated minimum, gap0; outside the fully distinct theorem.'},
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Written infinite tails at a>=20,16,64 for gaps1,3,4. Extension down to a8depends on complete76pair finite computation, not a purely written all-a theorem. Every integer c>b reduced to positive divisors of primitive constant, checked by integer Horner and independently by rational-factor extraction. Six selected exponent cubics and twelve direct quotient/Horner/Sturm fixtures. Gap2and growing-gap theorems preserved. No unrelated range or modulus expansion, floats or Lean. Manuscript unchanged; general endpoint-two feasibility, other endpoint-one cases and fullQ3open.'}, indent=2))
