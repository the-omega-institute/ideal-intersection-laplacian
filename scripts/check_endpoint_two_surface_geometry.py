import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable = sympy.symbols('a b c x')
gap, minimum_shift, middle_shift = sympy.symbols('v m d')
parameters = (first, middle, last)
matrix = support_quotient(parameters, complement=True)
quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
endpoint = quintic.eval(2)
diagonal_first = first * middle + 2 * first - 2 * middle ** 2 + 6 * middle - 4
diagonal_second = (-(first + 2) * middle ** 3 + 2 * first * (first - 2) * middle ** 2
                   - (first + 6) * (first - 2) * middle - 2 * (first - 2) ** 2)
shifted = sympy.Poly(endpoint.subs(last, middle + gap).expand(), gap)
assert sympy.expand(shifted.nth(0) - diagonal_first * diagonal_second) == 0
assert sympy.expand(2 * shifted.nth(1) - sympy.diff(diagonal_first * diagonal_second, middle)) == 0
assert sympy.expand(diagonal_second.subs(middle, first)
                    - (first - 1) * (first + 2) * (first ** 2 - 8 * first + 4)) == 0
assert sympy.expand(diagonal_second.subs(middle, 2 * first - 2)
                    + 2 * (13 * first ** 3 - 28 * first ** 2 + 8 * first + 8)) == 0
normalized_derivative = sympy.diff(diagonal_second / middle ** 2, middle)
assert sympy.cancel(normalized_derivative + first + 2
                    - (first + 6) * (first - 2) / middle ** 2
                    - 4 * (first - 2) ** 2 / middle ** 3) == 0
assert sympy.cancel(sympy.diff(diagonal_second, middle)
                    - middle ** 2 * normalized_derivative - 2 * diagonal_second / middle) == 0
derivative_bound = -first - 1 + 8 / first
bound_shift = sympy.Poly(sympy.cancel(-first * derivative_bound).subs(first, 8 + minimum_shift).expand(), minimum_shift)
assert all(coefficient > 0 for coefficient in bound_shift.all_coeffs())
negative_diagonal = sympy.Poly((-diagonal_first).subs(middle, first + middle_shift)
                               .subs(first, 8 + minimum_shift).expand(), minimum_shift, middle_shift)
assert all(coefficient > 0 for _, coefficient in negative_diagonal.terms())
assert negative_diagonal.coeff_monomial(1) == 4
assert sympy.expand(sympy.diff(diagonal_first, middle).subs(middle, first + middle_shift)
                    - (-3 * first + 6 - 4 * middle_shift)) == 0

positive_coefficients = []
for power in (2, 3):
    expression = shifted.nth(power).subs(middle, first + middle_shift).subs(first, 8 + minimum_shift).expand()
    polynomial = sympy.Poly(expression, minimum_shift, middle_shift)
    assert all(coefficient > 0 for _, coefficient in polynomial.terms())
    vectors = [list(map(int, reversed(sympy.Poly(sympy.Poly(expression, middle_shift).nth(degree),
                                                minimum_shift).all_coeffs())))
               for degree in range(polynomial.degree(middle_shift) + 1)]
    positive_coefficients.append({'power_of_c_minus_b': power, 'coefficient_vectors_ascending_in_m_by_d_power': vectors,
                                  'nonzero_terms': len(polynomial.terms()),
                                  'constant': int(polynomial.coeff_monomial(1))})

pairs = []
for minimum, second in ((8, 9), (20, 22), (20, 32), (20, 33), (10, 10)):
    substitutions = {first: minimum, middle: second}
    polynomial = sympy.Poly(endpoint.subs(substitutions), last)
    gap_polynomial = sympy.Poly(polynomial.as_expr().subs(last, second + gap), gap)
    diagonal_value = int(diagonal_second.subs(substitutions))
    real_roots_in_tail = int(gap_polynomial.count_roots(0, sympy.oo)) - int(gap_polynomial.eval(0) == 0)
    assert real_roots_in_tail == int(diagonal_value > 0)
    record = {'pair': [minimum, second], 'R_value': diagonal_value,
              'endpoint_cubic_coefficients_descending_in_c': list(map(int, polynomial.all_coeffs())),
              'real_roots_strictly_above_b': real_roots_in_tail}
    if (minimum, second) in ((20, 22), (20, 32)):
        assert polynomial.eval(32) < 0 < polynomial.eval(33)
        assert polynomial.count_roots(32, 33) == 1
        record.update({'unique_real_root_bracket': [32, 33], 'integer_endpoint_two_solution_c_above_b': False})
    if (minimum, second) == (10, 10):
        assert polynomial.eval(12) == 0
        assert sympy.diff(polynomial.as_expr(), last).subs(last, 12) > 0
        record.update({'unique_endpoint_two_solution': 12, 'integrality_not_claimed': True})
    pairs.append(record)
assert diagonal_second.subs({first: 8, middle: 8}) == 280
assert diagonal_second.subs({first: 8, middle: 9}) == -342
assert diagonal_second.subs({first: 20, middle: 32}) == 760
assert diagonal_second.subs({first: 20, middle: 33}) == -22626

fixtures = []
for exponents in ((8, 9, 10), (20, 22, 32), (20, 22, 33), (20, 32, 32),
                  (20, 32, 33), (20, 33, 34), (10, 10, 12)):
    direct = support_quotient(exponents, complement=True)
    polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
    assert polynomial == sympy.Poly(quintic.as_expr().subs(dict(zip(parameters, exponents))), variable)
    coefficients = list(map(int, polynomial.all_coeffs()))
    endpoint_values = []
    for point in (0, 1, 2):
        value = 0
        for coefficient in coefficients:
            value = value * point + coefficient
        assert value == polynomial.eval(point)
        endpoint_values.append(value)
    fixtures.append({'exponents': exponents, 'quintic_coefficients': coefficients,
                     'integer_Horner_at_0_1_2': endpoint_values,
                     'positive_roots_strictly_between_0_and_2': int(polynomial.count_roots(0, 2))
                     - int(polynomial.eval(2) == 0)})
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'written_result': 'For fixed a>=8,b>=a, h_C(2)=0 has a real solution c>b iff R_a(b)>0; that solution is unique and simple as a root in c.',
                  'R': '-(a+2)b^3+2a(a-2)b^2-(a+6)(a-2)b-2(a-2)^2',
                  'middle_threshold': 'R_a(b)/b^2 strictly decreases on b>=a; unique beta(a) in(a,2a-2); R_a(b)>0 iff b<beta(a).',
                  'diagonal_factorization': 'h_C(2)atc=b=L_a(b)R_a(b),L_a(b)=ab+2a-2b^2+6b-4<0',
                  'generic_checks': ['generic direct6x6quotient', 'diagonal factorization and symmetry derivative',
                                     'positive quadratic/cubic coefficients in c-b', 'normalized R derivative and bounds',
                                     'R at b=a and b=2a-2'],
                  'positive_coefficient_vectors': positive_coefficients,
                  'specific_consequences': ['minimum8: beta(8)in(8,9), no endpoint-two zero for fully distinct ordered triples',
                                            'minimum20: beta(20)in(32,33), integer middle must be at most32',
                                            'fixed(20,22): unique real endpoint-two root in c is between32and33, no integer c>b; all-even triples in this fixed pair nonintegral'],
                  'selected_pair_real_root_checks': pairs, 'direct_quotient_fixtures': fixtures,
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Written unbounded root-geometry theorem, exact polynomial/derivative identities and positive coefficient vectors. Five selected pair cubics checked with exact Sturm counts over c>b; seven direct quotient/Horner fixtures. No enlarged pair range or exponent/modulus scan, floats or Lean. Simplicity is in parameter c, not a new spectral multiplicity claim. Manuscript unchanged; fullQ3, endpoint-one cases and general integer feasibility on endpoint-two surface open.'}, indent=2))
