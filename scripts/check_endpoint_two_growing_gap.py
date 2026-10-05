import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable = sympy.symbols('a b c x')
gap, gap_shift, minimum_shift = sympy.symbols('d r u')
parameters = (first, middle, last)
matrix = support_quotient(parameters, complement=True)
quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
endpoint = quintic.eval(2)
leading = first * middle * (first + middle - 1) + 2 * first * (first - 1) + 2 * middle * (middle - 1) - 4
quadratic = (middle ** 2 * ((first + 2) * middle - (7 * first ** 2 - 2 * first + 8))
             + (first ** 3 + 2 * first ** 2 - 6 * first - 4) * middle
             + 2 * (first - 2) * (first ** 2 - 2 * first - 6))
linear = ((first - 2) * (middle - 2)
          * (first ** 2 * middle + first ** 2 + first * middle ** 2 + 6 * first * middle
             + 4 * first + middle ** 2 + 4 * middle - 12))
constant = 2 * (first - 2) * (middle - 2) * (first + middle - 2) * (first * middle + first + middle - 2)
cubic = leading * last ** 3 + quadratic * last ** 2 + linear * last + constant
assert sympy.expand(endpoint - cubic) == 0
lower = 2 * first + gap - 11
upper = lower + 1
family = sympy.expand(cubic.subs(middle, first + gap))
lower_value = sympy.expand(family.subs(last, lower))
upper_value = sympy.expand(family.subs(last, upper))
shifted = {}
for label, value in (('negative_lower', -lower_value), ('positive_upper', upper_value)):
    expression = sympy.expand(value.subs(first, 2 * gap ** 2 + 20 + minimum_shift).subs(gap, 5 + gap_shift))
    polynomial = sympy.Poly(expression, minimum_shift, gap_shift)
    assert all(coefficient > 0 for coefficient in polynomial.coeffs())
    vectors = [list(reversed(list(map(int, sympy.Poly(expression.coeff(minimum_shift, power), gap_shift).all_coeffs()))))
               for power in range(6)]
    reconstruction = sum(coefficient * minimum_shift ** power * gap_shift ** index
                         for power, vector in enumerate(vectors) for index, coefficient in enumerate(vector))
    assert sympy.expand(reconstruction - expression) == 0
    shifted[label] = {'nonzero_terms': len(polynomial.terms()),
                      'constant': int(expression.subs({minimum_shift: 0, gap_shift: 0})),
                      'vectors_ascending_in_r_by_u_power': vectors}
assert shifted['negative_lower']['constant'] == 8176563072
assert shifted['positive_upper']['constant'] == 1722564592
assert sympy.expand(lower - (first + gap)) == first - 11


def integer_horner(coefficients, point):
    value = 0
    for coefficient in coefficients:
        value = value * point + coefficient
    return value


fixtures = []
for minimum, difference in ((70, 5), (92, 6), (148, 8), (100, 5), (182, 9)):
    second = minimum + difference
    left = 2 * minimum + difference - 11
    right = left + 1
    exponent_polynomial = sympy.Poly(family.subs({first: minimum, gap: difference}), last)
    assert minimum >= 2 * difference ** 2 + 20 and difference >= 5 and left > second
    assert exponent_polynomial.eval(left) < 0 < exponent_polynomial.eval(right)
    assert exponent_polynomial.count_roots(left, right) == 1
    assert exponent_polynomial.count_roots(second, sympy.oo) == 1
    direct_records = []
    for third in (left, right):
        exponents = (minimum, second, third)
        direct = support_quotient(exponents, complement=True)
        polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        assert polynomial == sympy.Poly(quintic.as_expr().subs(dict(zip(parameters, exponents))), variable)
        coefficients = list(map(int, polynomial.all_coeffs()))
        endpoints = [integer_horner(coefficients, point) for point in (0, 1, 2)]
        assert endpoints == [int(polynomial.eval(point)) for point in (0, 1, 2)]
        assert endpoints[2] == exponent_polynomial.eval(third)
        direct_records.append({'exponents': exponents, 'quintic_coefficients': coefficients,
                               'integer_Horner_at_0_1_2': endpoints,
                               'positive_roots_strictly_between_0_and_3': int(polynomial.count_roots(0, 3))
                               - int(polynomial.eval(3) == 0)})
    fixtures.append({'pair': [minimum, second], 'gap': difference, 'unique_exponent_root_bracket': [left, right],
                     'exponent_cubic_coefficients': list(map(int, exponent_polynomial.all_coeffs())),
                     'direct_quotients': direct_records})
controls = []
for exponents in ((20, 22, 32), (20, 22, 33), (10, 10, 12)):
    direct = support_quotient(exponents, complement=True)
    polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
    value = int(polynomial.eval(2))
    assert value == int(endpoint.subs(dict(zip(parameters, exponents))))
    controls.append({'exponents': exponents, 'h_C_at_two': value, 'growing_gap_hypotheses_hold': False})
assert controls[0]['h_C_at_two'] < 0 < controls[1]['h_C_at_two']
assert controls[2]['h_C_at_two'] == 0
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'written_result': 'For real d>=5,a>=2d^2+20,b=a+d, the unique real endpoint-two solution c>b lies strictly in(2a+d-11,2a+d-10). Thus no integer endpoint-two solution for integer a,d and c>b.',
                  'endpoint_values_coefficients_descending_in_a': {
                      'lower': list(map(str, sympy.Poly(lower_value, first).all_coeffs())),
                      'upper': list(map(str, sympy.Poly(upper_value, first).all_coeffs()))},
                  'positive_expansions_at_d_5_plus_r_a_2d_squared_20_plus_u': shifted,
                  'nonintegrality_consequence': 'All-even triples and permutations(1,3,2)/(3,3,0)mod4 satisfying the size-ordered hypotheses, using the uniform low root and prior conditional exclusion of1.',
                  'fixed_pair_fixtures': fixtures, 'outside_hypothesis_controls': controls,
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Unbounded written proof from complete positive coefficient identities and prior real-root uniqueness. No finite base or exponent scan needed. Five selected exponent cubics: exact Sturm counts in bracket and entire c>b tail. Ten direct6x6quotient/Horner/Sturm fixtures and three outside-hypothesis controls. No floats or Lean. General integer endpoint-two feasibility, other endpoint-one cases, fullQ3 and higher-prime nonsquarefree vectors remain open. Manuscript unchanged.'}, indent=2))
