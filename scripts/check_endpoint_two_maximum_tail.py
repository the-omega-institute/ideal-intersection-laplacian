import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable = sympy.symbols('a b c x')
ratio, tail, minimum_shift = sympy.symbols('t v m')
parameters = (first, middle, last)
matrix = support_quotient(parameters, complement=True)
quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
endpoint = quintic.eval(2)
leading = first * last * (first + last - 1) + 2 * first * (first - 1) + 2 * last * (last - 1) - 4
quadratic = (last ** 2 * ((first + 2) * last - (7 * first ** 2 - 2 * first + 8))
             + (first ** 3 + 2 * first ** 2 - 6 * first - 4) * last
             + 2 * (first - 2) * (first ** 2 - 2 * first - 6))
linear = (first - 2) * (last - 2) * (first ** 2 * last + first ** 2 + first * last ** 2
                                    + 6 * first * last + 4 * first + last ** 2 + 4 * last - 12)
constant = 2 * (first - 2) * (last - 2) * (first + last - 2) * (first * last + first + last - 2)
assert sympy.expand(endpoint - (leading * middle ** 3 + quadratic * middle ** 2
                                + linear * middle + constant)) == 0
assert sympy.expand(quintic.eval(0) + sympy.prod(parameters) * sum(parameters)
                    * (sum(parameters) + first * middle + first * last + middle * last)) == 0
substituted_middle = (first + (2 * first - 2) * ratio) / (1 + ratio)
transformed = sympy.Poly(sympy.cancel((1 + ratio) ** 3
                                     * endpoint.subs({middle: substituted_middle, last: 3 * first - 4 + tail}))
                         .subs(first, 4 + minimum_shift).expand(), ratio, tail, minimum_shift)
assert transformed.degree(ratio) == 3 and transformed.degree(tail) == 3
assert len(transformed.terms()) == 88
assert all(coefficient > 0 for _, coefficient in transformed.terms())
assert transformed.coeff_monomial(1) == 17568
coefficient_vectors = []
for ratio_power in range(4):
    row = []
    for tail_power in range(4):
        expression = sum(coefficient * minimum_shift ** powers[2]
                         for powers, coefficient in transformed.terms()
                         if powers[:2] == (ratio_power, tail_power))
        polynomial = sympy.Poly(expression, minimum_shift)
        row.append(list(map(int, reversed(polynomial.all_coeffs()))))
    coefficient_vectors.append(row)
inverse_ratio = (middle - first) / (2 * first - 2 - middle)
assert sympy.cancel(substituted_middle.subs(ratio, inverse_ratio) - middle) == 0
assert sympy.cancel((1 + inverse_ratio) - (first - 2) / (2 * first - 2 - middle)) == 0
boundary = sympy.Poly(transformed.as_expr(), ratio).nth(3)
assert sympy.expand(boundary - endpoint.subs({middle: 2 * first - 2,
                                             last: 3 * first - 4 + tail})
                    .subs(first, 4 + minimum_shift)) == 0
old_bound = 7 * first - 16 + 40 / (first + 2)
assert sympy.cancel(old_bound - (3 * first - 4) - 4 * (first ** 2 - first + 4) / (first + 2)) == 0

fixtures = []
for exponents in ((4, 4, 8), (20, 34, 56), (20, 34, 58), (19, 31, 56), (20, 22, 32)):
    direct = support_quotient(exponents, complement=True)
    polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
    substitutions = dict(zip(parameters, exponents))
    assert polynomial == sympy.Poly(quintic.as_expr().subs(substitutions), variable)
    coefficients = list(map(int, polynomial.all_coeffs()))
    values = []
    for point in (0, 1, 2):
        value = 0
        for coefficient in coefficients:
            value = value * point + coefficient
        assert value == polynomial.eval(point)
        values.append(value)
    smallest, second, maximum = exponents
    diagonal = [sympy.Rational(sum(exponents) - 2) - sympy.Rational(2 * sympy.prod(exponents), entry * (entry - 2))
                for entry in exponents]
    principal = diagonal[0] * diagonal[1] - smallest * diagonal[1] - second * diagonal[0]
    applies = maximum >= 3 * smallest - 4
    root_count = int(polynomial.count_roots(0, 2)) - int(polynomial.eval(2) == 0)
    if applies:
        assert values[0] < 0 < values[2] and root_count >= 1
    if exponents in ((20, 34, 56), (20, 34, 58), (19, 31, 56)):
        assert second < 2 * smallest - 2
        assert maximum < old_bound.subs(first, smallest)
        assert diagonal[1] > 0 and principal < 0
    if exponents == (20, 22, 32):
        assert not applies and values[2] < 0 and root_count == 0
    covered = (all(entry % 2 == 0 for entry in exponents)
               or sorted(entry % 4 for entry in exponents) in ([0, 3, 3], [1, 2, 3]))
    fixtures.append({'exponents': exponents, 'new_maximum_tail_applies': applies,
                     'covered_nonintegral_class': covered,
                     'prior_middle_tail_applies': second >= 2 * smallest - 2,
                     'prior_minimum_only_tail': str(old_bound.subs(first, smallest)),
                     'schur_diagonal_at_two': list(map(str, diagonal)),
                     'principal_ab_determinant': str(principal),
                     'prior_middle_diagonal_test': bool(diagonal[1] <= 0),
                     'prior_principal_ab_test': bool(diagonal[0] < 0 and principal > 0),
                     'quintic_coefficients': coefficients, 'integer_Horner_at_0_1_2': values,
                     'positive_roots_strictly_between_0_and_2': root_count})

control = support_quotient((10, 10, 12), complement=True)
control_polynomial = sympy.Poly(sympy.cancel(control.charpoly(variable).as_expr() / variable), variable)
assert control_polynomial.eval(2) == 0 and 12 < 3 * 10 - 4
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'written_result': 'For4<=a<=b<=c,c>=3a-4 implies h_C(2)>0 and a positive quotient root in(0,2).',
                  'endpoint_two_necessary_conditions': ['b<2a-2', 'c<3a-4'],
                  'nonintegral_classes': ['all-even', 'permutation(1,3,2)mod4', 'permutation(3,3,0)mod4'],
                  'positive_expansion': {'substitution': 'a=4+m,c=3a-4+v,b=(a+(2a-2)t)/(1+t)',
                                         'domain': 'm,v,t>=0 covers a>=4,c>=3a-4,a<=b<2a-2; b>=2a-2 handled by prior middle-tail theorem',
                                         'polynomial': '(1+t)^3*h_C(2)', 'nonzero_terms': 88,
                                         'constant': 17568, 'all_nonzero_coefficients_strictly_positive': True,
                                         'coefficient_vectors_ascending_in_m_rows_t_columns_v': coefficient_vectors},
                  'generic_checks': ['direct6x6quotient endpoint cubic coefficients and h_C(0)',
                                     'rational interval transformation and inverse', 'full positive expansion',
                                     't_cubic_coefficient_equals_b_2a_minus_2_boundary', 'strict improvement over prior maximum bound'],
                  'direct_exact_fixtures': fixtures,
                  'repeated_endpoint_two_control': {'exponents': [10, 10, 12], 'h_C_at_two': 0,
                                                    'below_new_maximum_tail': True, 'integrality_not_claimed': True},
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Written unbounded polynomial positivity proof with explicit coefficient certificate, using prior full determinant middle-tail theorem. Five fixed direct quotient/integer-Horner/Sturm checks and retained endpoint-zero control. No exponent/modulus scan, floats or Lean. Manuscript unchanged; surviving endpoint-two region, other mixed-parity endpoint-one cases, fullQ3 and higher-prime nonsquarefree vectors open.'}, indent=2))
