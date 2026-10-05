import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable = sympy.symbols('a b c x')
parameters = (first, middle, last)
total = sum(parameters)
product = sympy.prod(parameters)
diagonal = [total - 2 - 2 * product / (entry * (entry - 2)) for entry in parameters]
schur_congruence = sympy.diag(*(entry / parameter for entry, parameter in zip(diagonal, parameters))) - sympy.ones(3)
quotient = support_quotient(parameters, complement=True)
quintic = sympy.Poly(sympy.cancel(quotient.charpoly(variable).as_expr() / variable), variable)
assert sympy.cancel(2 * quintic.eval(2) - sympy.prod(entry - 2 for entry in parameters)
                    * product * schur_congruence.det()) == 0
principal_determinant = schur_congruence[:2, :2].det()
cleared_principal = sympy.cancel((first - 2) * (middle - 2)
                                * (diagonal[0] * diagonal[1] - first * diagonal[1] - middle * diagonal[0]))
assert sympy.expand(cleared_principal.subs({first: 20, middle: 22})
                    - 40 * (13 * last ** 2 - 414 * last - 720)) == 0
assert sympy.expand((13 * last ** 2 - 414 * last - 720).subs(last, sympy.Symbol('shift') + 34)) == sympy.Symbol('shift') ** 2 * 13 + 470 * sympy.Symbol('shift') + 232
assert sympy.cancel(product / last * principal_determinant
                    - (diagonal[0] * diagonal[1] - first * diagonal[1] - middle * diagonal[0])) == 0
middle_numerator = (middle - 2) * (total - 2) - 2 * first * last
assert sympy.cancel(diagonal[1] * (middle - 2) - middle_numerator) == 0
assert sympy.expand(middle_numerator - ((middle - 2) * (first + middle - 2)
                                       - (2 * first - middle + 2) * last)) == 0
zero_first = sympy.Symbol('zero_first')
second_diagonal, third_diagonal = sympy.symbols('second_diagonal third_diagonal')
boundary_congruence = sympy.diag(zero_first / first, second_diagonal / middle, third_diagonal / last) - sympy.ones(3)
assert sympy.expand(product * boundary_congruence.det().subs(zero_first, 0)
                    + first * second_diagonal * third_diagonal) == 0

fixtures = []
for exponents in ((20, 22, 40), (20, 22, 46), (19, 23, 52), (20, 22, 38),
                  (20, 22, 34), (20, 22, 33), (17, 19, 50)):
    substitutions = dict(zip(parameters, exponents))
    matrix = support_quotient(exponents, complement=True)
    polynomial = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    assert polynomial == sympy.Poly(quintic.as_expr().subs(substitutions), variable)
    coefficients = [int(coefficient) for coefficient in polynomial.all_coeffs()]
    values = []
    for endpoint in (0, 1, 2):
        value = 0
        for coefficient in coefficients:
            value = value * endpoint + coefficient
        assert value == polynomial.eval(endpoint)
        values.append(value)
    schur_values = [sympy.cancel(entry.subs(substitutions)) for entry in diagonal]
    rational_matrix = schur_congruence.subs(substitutions)
    principal = rational_matrix[:2, :2]
    root_count = int(polynomial.count_roots(0, 2)) - int(polynomial.eval(2) == 0)
    satisfies_criterion = schur_values[1] <= 0
    stronger_criterion = schur_values[0] < 0 and principal.det() > 0
    if satisfies_criterion:
        assert principal.trace() < 0 and principal.det() > 0
        assert root_count >= 1
    if stronger_criterion:
        assert principal.trace() < 0 and root_count >= 1
    assert polynomial.eval(1) != 0
    if exponents == (20, 22, 33):
        assert not satisfies_criterion and not stronger_criterion and root_count == 1
    if exponents == (17, 19, 50):
        assert tuple(entry % 8 for entry in exponents) == (1, 3, 2)
        assert schur_values[1] == -16
    minimum, second, maximum = exponents
    new_bound = sympy.Rational((second - 2) * (minimum + second - 2), 2 * minimum - second + 2)
    old_bound = 7 * minimum - 16 + sympy.Rational(40, minimum + 2)
    assert maximum < old_bound
    assert (minimum - 2) * (sum(exponents) - 2) <= 2 * second * maximum
    assert minimum > 7 and second > 15 and maximum - minimum > 4
    assert sympy.gcd_list(exponents) in (1, 2)
    if all(entry % 2 == 0 for entry in exponents):
        assert all(entry % 2 == 0 for entry in matrix)
    fixtures.append({'exponents': exponents, 'schur_diagonal_at_two': list(map(str, schur_values)),
                     'middle_criterion_applies': bool(satisfies_criterion),
                     'stronger_principal_block_criterion_applies': bool(stronger_criterion),
                     'covered_nonintegral_class': all(entry % 2 == 0 for entry in exponents)
                     or sorted(entry % 4 for entry in exponents) in ([0, 3, 3], [1, 2, 3]),
                     'principal_trace': str(principal.trace()), 'principal_determinant': str(principal.det()),
                     'characteristic_quintic_coefficients': coefficients,
                     'endpoint_values_at_0_1_2': values, 'positive_roots_strictly_between_0_and_2': root_count,
                     'middle_tail': str(new_bound), 'prior_linear_tail': str(old_bound),
                     'below_prior_linear_tail_and_outside_sufficient_balanced_region': True})

control = support_quotient((10, 10, 12), complement=True)
control_polynomial = sympy.Poly(sympy.cancel(control.charpoly(variable).as_expr() / variable), variable)
assert control_polynomial.eval(2) == 0
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'written_result': 'For4<=a<b<c, (b-2)(a+b+c-2)<=2ac gives a positive quotient root in(0,2).',
                  'nonintegral_classes': ['all-even', 'permutation(1,3,2)mod4', 'permutation(3,3,0)mod4'],
                  'necessary_integer_spectrum_conditions': ['(a-2)(a+b+c-2)<2bc', '(b-2)(a+b+c-2)>2ac',
                                                           'h_C(2)=0; two is smallest positive and simple'],
                  'symbolic_identities': ['generic direct quotient/Schur determinant at2',
                                          'principal2x2determinant', 'middle-diagonal numerator and tail',
                                          'minimum-diagonal-zero determinant', '20,22stronger principal quadratic and positive shift at34'],
                  'strengthened_fixed_pair': 'For a20,b22, all c>=34 have a quotient root in(0,2); even c>=34 nonintegral.',
                  'direct_exact_fixtures': fixtures,
                  'repeated_endpoint_two_control': {'exponents': [10, 10, 12], 'endpoint_two': 0,
                                                   'scope': 'Existing repeated-exponent example, outside distinct hypothesis'},
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Written Schur/principal-submatrix proof; generic rational identities, seven fixed direct integer quotient/Horner/Sturm fixtures and one existing repeated control. Includes strengthened boundary at34, outside both tests at33 and explicit modulo8overlap. No exponent/modulus scan, no floating spectra, no Lean. Consolidated manuscript unchanged; fullQ3 and higher-prime vectors open.'}, indent=2))
