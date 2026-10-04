import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable = sympy.symbols('a b c x')
offset, gap, minimum_shift = sympy.symbols('u v m')
parameters = (first, middle, last)
matrix = support_quotient(parameters, complement=True)
quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
endpoint = quintic.eval(2)
diagonal = [sum(parameters) - 2 - 2 * sympy.prod(parameters) / (entry * (entry - 2))
            for entry in parameters]
schur = sympy.diag(*(entry / parameter for entry, parameter in zip(diagonal, parameters))) - sympy.ones(3)
assert sympy.cancel(2 * endpoint - sympy.prod(entry - 2 for entry in parameters)
                    * sympy.prod(parameters) * schur.det()) == 0
assert sympy.expand(endpoint - endpoint.xreplace({middle: last, last: middle})) == 0

first_factor = 2 * offset ** 2 + 7 * (first - 2) * offset + 2 * (3 * first ** 2 - 14 * first + 12)
second_factor = ((first + 2) * offset ** 3 + (4 * first ** 2 + 10 * first - 12) * offset ** 2
                 + (4 * first ** 3 + 25 * first ** 2 - 48 * first + 12) * offset
                 + 2 * (13 * first ** 3 - 28 * first ** 2 + 8 * first + 8))
quadratic_coefficient = (2 * (first - 2) * (9 * first ** 3 + 24 * first ** 2 - 56 * first + 16)
                         + (33 * first ** 3 + 20 * first ** 2 - 208 * first + 136) * offset
                         + (20 * first ** 2 + 23 * first - 62) * offset ** 2
                         + 4 * (first + 2) * offset ** 3)
cubic_coefficient = (2 * (3 * first ** 3 - first ** 2 - 8 * first + 4)
                     + (5 * first ** 2 + 3 * first - 10) * offset
                     + (first + 2) * offset ** 2)
linear_coefficient = sympy.diff(first_factor * second_factor, offset) / 2
expected = (first_factor * second_factor + linear_coefficient * gap
            + quadratic_coefficient * gap ** 2 + cubic_coefficient * gap ** 3)
shifted_endpoint = sympy.expand(endpoint.subs({middle: 2 * first - 2 + offset,
                                               last: 2 * first - 2 + offset + gap}))
assert sympy.expand(shifted_endpoint - expected) == 0
positive_certificates = []
for name, expression in (('A', first_factor), ('B', second_factor),
                         ('coefficient_of_v_squared', quadratic_coefficient),
                         ('coefficient_of_v_cubed', cubic_coefficient)):
    for power in range(sympy.Poly(expression, offset).degree() + 1):
        coefficient = sympy.Poly(expression, offset).nth(power)
        shifted = sympy.Poly(sympy.expand(coefficient.subs(first, 4 + minimum_shift)), minimum_shift)
        assert shifted.eval(0) > 0
        assert all(value > 0 for value in shifted.all_coeffs())
        positive_certificates.append({'expression': name, 'u_power': power,
                                      'coefficient_in_a': str(sympy.expand(coefficient)),
                                      'coefficient_at_a_4_plus_m': str(shifted.as_expr()),
                                      'coefficients_descending_in_m': list(map(int, shifted.all_coeffs()))})
full_shift = sympy.Poly(shifted_endpoint.subs(first, 4 + minimum_shift), minimum_shift, offset, gap)
assert len(full_shift.terms()) == 69
assert all(coefficient > 0 for _, coefficient in full_shift.terms())
assert full_shift.coeff_monomial(1) == 6784

fixtures = []
for exponents in ((4, 6, 6), (20, 38, 46), (20, 42, 46), (19, 39, 44), (20, 22, 32)):
    direct = support_quotient(exponents, complement=True)
    polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
    substitutions = dict(zip(parameters, exponents))
    assert polynomial == sympy.Poly(quintic.as_expr().subs(substitutions), variable)
    coefficients = list(map(int, polynomial.all_coeffs()))
    endpoints = []
    for point in (0, 1, 2):
        value = 0
        for coefficient in coefficients:
            value = value * point + coefficient
        assert value == polynomial.eval(point)
        endpoints.append(value)
    schur_values = [sympy.cancel(entry.subs(substitutions)) for entry in diagonal]
    principal_value = sympy.cancel(schur_values[0] * schur_values[1]
                                   - exponents[0] * schur_values[1] - exponents[1] * schur_values[0])
    applies = exponents[1] >= 2 * exponents[0] - 2
    root_count = int(polynomial.count_roots(0, 2)) - int(polynomial.eval(2) == 0)
    if applies:
        assert endpoints[0] < 0 < endpoints[2]
        assert root_count >= 1
    if exponents in ((20, 38, 46), (20, 42, 46), (19, 39, 44)):
        assert schur_values[1] > 0 and principal_value < 0
        assert exponents[2] < 7 * exponents[0] - 16 + sympy.Rational(40, exponents[0] + 2)
    if exponents == (20, 22, 32):
        assert not applies and endpoints[2] < 0 and root_count == 0
    covered = (all(entry % 2 == 0 for entry in exponents)
               or sorted(entry % 4 for entry in exponents) in ([0, 3, 3], [1, 2, 3]))
    fixtures.append({'exponents': exponents, 'middle_tail_applies': applies,
                     'covered_nonintegral_class': covered,
                     'schur_diagonal_at_two': list(map(str, schur_values)),
                     'principal_ab_determinant': str(principal_value),
                     'prior_middle_diagonal_test': bool(schur_values[1] <= 0),
                     'prior_principal_ab_test': bool(schur_values[0] < 0 and principal_value > 0),
                     'quintic_coefficients': coefficients, 'integer_Horner_at_0_1_2': endpoints,
                     'positive_roots_strictly_between_0_and_2': root_count})

repeated = support_quotient((10, 10, 12), complement=True)
repeated_polynomial = sympy.Poly(sympy.cancel(repeated.charpoly(variable).as_expr() / variable), variable)
assert repeated_polynomial.eval(2) == 0
assert 10 < 2 * 10 - 2
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'written_result': 'For4<=a<=b<=c and b>=2a-2, h_C(2)>0 and a positive quotient root lies in(0,2).',
                  'endpoint_two_necessary_condition': 'h_C(2)=0 implies b<2a-2 for ordered minimum>=4.',
                  'nonintegral_classes': ['all-even', 'permutation(1,3,2)mod4', 'permutation(3,3,0)mod4'],
                  'positive_expansion': {'substitution': 'a=4+m,b=2a-2+u,c=b+v; m,u,v>=0',
                                         'nonzero_terms': len(full_shift.terms()), 'constant': 6784,
                                         'all_nonzero_coefficients_strictly_positive': True,
                                         'factored_v_coefficients': {'constant': 'A(u)B(u)', 'linear': '(A*B)prime/2',
                                                                    'quadratic': str(quadratic_coefficient),
                                                                    'cubic': str(cubic_coefficient)},
                                         'component_coefficient_certificates': positive_certificates},
                  'generic_checks': ['direct6x6quotient/Schur determinant at2', 'symmetry in b,c',
                                     'factored positive expansion in u,v', 'all component coefficients at a=4+m'],
                  'direct_exact_fixtures': fixtures,
                  'repeated_endpoint_two_control': {'exponents': [10, 10, 12], 'h_C_at_two': 0,
                                                    'below_middle_tail': True, 'integrality_not_claimed': True},
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Unbounded written polynomial-positivity proof; symbolic exact identities plus five selected direct quotient/integer-Horner/Sturm fixtures and a retained endpoint-zero control. No exponent/modulus scan, floats or Lean. No manuscript integration yet; fullQ3 and mixed-parity endpoint-one surface remain open.'}, indent=2))
