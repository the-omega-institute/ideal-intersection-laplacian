import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable = sympy.symbols('a b c x')
minimum_shift = sympy.Symbol('m')
parameters = (first, middle, last)
generic_matrix = support_quotient(parameters, complement=True)
quintic = sympy.Poly(sympy.cancel(generic_matrix.charpoly(variable).as_expr() / variable), variable)
endpoint = quintic.eval(2)
gap_polynomial = ((2 * first ** 2 + 9 * first + 6) * last ** 3
                  - (5 * first ** 3 + 12 * first ** 2 + 14 * first + 12) * last ** 2
                  + (2 * first ** 4 + 10 * first ** 3 - 56 * first) * last
                  + 4 * first ** 4 + 8 * first ** 3 - 32 * first ** 2)
assert sympy.expand(endpoint.subs(middle, first + 2) - first * gap_polynomial) == 0
lower_value = -16 * first * (7 * first ** 3 - 84 * first ** 2 + 148 * first + 240)
upper_value = 3 * first * (2 * first ** 4 - 49 * first ** 3 + 356 * first ** 2 - 427 * first - 882)
assert sympy.expand(first * gap_polynomial.subs(last, 2 * first - 8) - lower_value) == 0
assert sympy.expand(first * gap_polynomial.subs(last, 2 * first - 7) - upper_value) == 0
negative_lower = sympy.Poly((-lower_value).subs(first, 20 + minimum_shift).expand(), minimum_shift)
positive_upper = sympy.Poly(upper_value.subs(first, 20 + minimum_shift).expand(), minimum_shift)
assert all(coefficient > 0 for coefficient in negative_lower.all_coeffs())
assert all(coefficient > 0 for coefficient in positive_upper.all_coeffs())
assert negative_lower.eval(0) == 8192000
assert positive_upper.eval(0) == 3658680


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


finite_base = []
total_candidates = 0
for minimum in range(8, 20):
    second = minimum + 2
    coefficients = list(map(int, sympy.Poly(gap_polynomial.subs(first, minimum), last).all_coeffs()))
    content = 0
    for coefficient in coefficients:
        content = gcd(content, abs(coefficient))
    primitive = [coefficient // content for coefficient in coefficients]
    assert primitive == list(map(int, sympy.Poly(gap_polynomial.subs(first, minimum), last).primitive()[1].all_coeffs()))
    candidates = [candidate for candidate in positive_divisors(abs(primitive[-1])) if candidate > second]
    roots = [candidate for candidate in candidates if integer_horner(primitive, candidate) == 0]
    polynomial = sympy.Poly.from_list(primitive, last)
    rational_roots = polynomial.ground_roots()
    extracted = sorted(int(root) for root in rational_roots if root.is_Integer and root > second)
    assert roots == extracted == []
    if minimum == 10:
        assert rational_roots == {sympy.Integer(10): 1}
        assert polynomial.eval(10) == 0 and 10 < second
    finite_base.append({'pair': [minimum, second], 'primitive_cubic_coefficients_descending_in_c': primitive,
                        'constant_divisor_candidates_c_above_b': candidates,
                        'integer_Horner_at_all_candidates': [integer_horner(primitive, candidate) for candidate in candidates],
                        'integer_roots_c_above_b': roots,
                        'all_rational_roots': {str(root): int(multiplicity) for root, multiplicity in rational_roots.items()},
                        'complete_for_all_integer_c_above_b': True})
    total_candidates += len(candidates)

fixtures = []
for exponents in ((8, 10, 11), (10, 12, 13), (19, 21, 22),
                  (20, 22, 32), (20, 22, 33), (40, 42, 72), (40, 42, 73)):
    direct = support_quotient(exponents, complement=True)
    polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
    substitutions = dict(zip(parameters, exponents))
    assert polynomial == sympy.Poly(quintic.as_expr().subs(substitutions), variable)
    coefficients = list(map(int, polynomial.all_coeffs()))
    endpoints = [integer_horner(coefficients, point) for point in (0, 1, 2)]
    assert endpoints == [int(polynomial.eval(point)) for point in (0, 1, 2)]
    assert endpoints[2] == exponents[0] * gap_polynomial.subs({first: exponents[0], last: exponents[2]})
    record = {'exponents': exponents, 'quintic_coefficients': coefficients,
              'integer_Horner_at_0_1_2': endpoints,
              'positive_roots_strictly_between_0_and_2': int(polynomial.count_roots(0, 2))
              - int(polynomial.eval(2) == 0)}
    if exponents[0] >= 20:
        cubic = sympy.Poly(gap_polynomial.subs(first, exponents[0]), last)
        assert cubic.eval(2 * exponents[0] - 8) < 0 < cubic.eval(2 * exponents[0] - 7)
        assert cubic.count_roots(2 * exponents[0] - 8, 2 * exponents[0] - 7) == 1
        assert cubic.count_roots(exponents[1], sympy.oo) == 1
        record['unique_exponent_root_bracket'] = [2 * exponents[0] - 8, 2 * exponents[0] - 7]
    fixtures.append(record)
control = support_quotient((10, 12, 10), complement=True)
control_polynomial = sympy.Poly(sympy.cancel(control.charpoly(variable).as_expr() / variable), variable)
assert control_polynomial.eval(2) == 0
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'combined_result': 'For every integer a>=8,c>a+2, the gap-two triple(a,a+2,c)has h_C(2)!=0.',
                  'written_tail': 'For a>=20 the unique real endpoint-two root above b=a+2 lies strictly between2a-8and2a-7, so is not an integer.',
                  'tail_endpoint_identities': {'lower': str(lower_value), 'upper': str(upper_value)},
                  'positive_shifted_coefficients_descending_in_m_at_a_20_plus_m': {
                      'negative_lower': list(map(int, negative_lower.all_coeffs())),
                      'positive_upper': list(map(int, positive_upper.all_coeffs()))},
                  'finite_base_scope': 'Exactly12pairs(a,a+2),8<=a<=19; all integer c>b exhaustively reduced to positive divisors of the primitive constant, independently cross-checked by rational-factor extraction.',
                  'finite_base_divisor_candidates_checked': total_candidates, 'finite_base': finite_base,
                  'nonintegrality_consequence': 'All-even gap-two triples and gap-two permutations(1,3,2)mod4, a>=8,c>a+2, using uniform low root and prior conditional exclusion of1. Other mixed endpoint-one cases not settled.',
                  'direct_quotient_fixtures': fixtures,
                  'unordered_endpoint_zero_control': {'exponents': [10, 12, 10], 'h_C_at_two': 0,
                                                      'scope': 'c=10<b=12; permutation of retained repeated control(10,10,12), not a counterexample to ordered gap-two theorem.'},
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Infinite written tail uses previous real-root uniqueness theorem and two exact sign identities. Extension8<=a<=19 relies on the complete12pair finite computation, not an unbounded all-a pure written proof. Seven fixed direct quotient/Horner/Sturm fixtures and an unordered endpoint-zero control. No unrelated range or modulus expansion, floats or Lean. Manuscript unchanged; fullQ3, arbitrary middle gaps, general integer endpoint-two feasibility and other endpoint-one cases open.'}, indent=2))
