import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable = sympy.symbols('a b c x')
minimum_shift, interval, tail = sympy.symbols('m t v')
parameters = (first, middle, last)
matrix = support_quotient(parameters, complement=True)
quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
endpoint = quintic.eval(2)
cutoff = sympy.Rational(9, 4) * first - 8
middle_substitution = (first + (2 * first - 2) * interval) / (1 + interval)
inverse = (middle - first) / (2 * first - 2 - middle)
assert sympy.cancel(middle_substitution.subs(interval, inverse) - middle) == 0
assert sympy.expand(3 * first - 4 - cutoff) == sympy.Rational(3, 4) * first + 4
transformed = sympy.cancel(64 * (1 + interval) ** 3
                          * endpoint.subs({middle: middle_substitution, last: cutoff + tail}))
expression = sympy.expand(transformed.subs(first, 8 + minimum_shift))
first_nonnegative = 9 * minimum_shift ** 6 * (1 + 2 * interval) * (14 * (1 - interval) ** 2 + 5 * interval + interval ** 2)
second_nonnegative = 308 * minimum_shift ** 5 * interval * (interval - 1) ** 2
residual = sympy.Poly(expression - first_nonnegative - second_nonnegative, minimum_shift, interval, tail)
assert len(residual.terms()) == 84
assert all(coefficient > 0 for coefficient in residual.coeffs())
assert residual.eval({minimum_shift: 0, interval: 0, tail: 0}) == 3014656
vectors = [[list(reversed(list(map(int, sympy.Poly(residual.as_expr().coeff(interval, power)
                                                 .coeff(tail, tail_power), minimum_shift).all_coeffs()))))
            for tail_power in range(4)] for power in range(4)]
reconstruction = sum(coefficient * interval ** power * tail ** tail_power * minimum_shift ** degree
                     for power, row in enumerate(vectors) for tail_power, vector in enumerate(row)
                     for degree, coefficient in enumerate(vector))
assert sympy.expand(reconstruction - residual.as_expr()) == 0
assert sympy.expand(expression - first_nonnegative - second_nonnegative - reconstruction) == 0
boundary = endpoint.subs({middle: 2 * first - 2, last: cutoff + tail}).subs(first, 8 + minimum_shift)
assert sympy.expand(expression.coeff(interval, 3) - 64 * boundary) == 0
assert sympy.expand(quintic.eval(0) + first * middle * last * (first + middle + last)
                    * (first + middle + last + first * middle + first * last + middle * last)) == 0


def integer_horner(coefficients, point):
    value = 0
    for coefficient in coefficients:
        value = value * point + coefficient
    return value


fixtures = []
for exponents in ((8, 8, 10), (9, 10, 13), (20, 30, 38), (40, 58, 84),
                  (64, 80, 136), (100, 140, 218), (20, 38, 38), (20, 40, 40)):
    minimum, second, third = exponents
    assert minimum >= 8 and minimum <= second <= third and third >= sympy.Rational(9, 4) * minimum - 8
    direct = support_quotient(exponents, complement=True)
    polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
    assert polynomial == sympy.Poly(quintic.as_expr().subs(dict(zip(parameters, exponents))), variable)
    coefficients = list(map(int, polynomial.all_coeffs()))
    values = [integer_horner(coefficients, point) for point in (0, 1, 2)]
    assert values == [int(polynomial.eval(point)) for point in (0, 1, 2)]
    assert values[0] < 0 < values[2]
    count = int(polynomial.count_roots(0, 2))
    assert count >= 1
    record = {'exponents': exponents, 'quintic_coefficients': coefficients,
              'integer_Horner_at_0_1_2': values, 'positive_roots_strictly_between_0_and_2': count,
              'sharp_cutoff': str(sympy.Rational(9, 4) * minimum - 8), 'preceding_cutoff': 3 * minimum - 4}
    if second < 2 * minimum - 2:
        interval_value = sympy.Rational(second - minimum, 2 * minimum - 2 - second)
        tail_value = third - (sympy.Rational(9, 4) * minimum - 8)
        scaled = expression.subs({minimum_shift: minimum - 8, interval: interval_value, tail: tail_value})
        assert scaled == 64 * (1 + interval_value) ** 3 * values[2]
        record['positive_identity_matches_direct_quotient'] = True
    else:
        record['branch'] = 'Preserved middle-tail theorem covers b>=2a-2.'
    fixtures.append(record)
controls = []
for exponents in ((20, 22, 32), (10, 10, 12)):
    polynomial = sympy.Poly(sympy.cancel(support_quotient(exponents, complement=True).charpoly(variable).as_expr()
                                        / variable), variable)
    value = int(polynomial.eval(2))
    assert exponents[2] < sympy.Rational(9, 4) * exponents[0] - 8
    controls.append({'exponents': exponents, 'h_C_at_two': value, 'below_new_cutoff': True})
assert controls[0]['h_C_at_two'] < 0 and controls[1]['h_C_at_two'] == 0
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'written_result': 'For ordered real8<=a<=b<=c, c>=9a/4-8implies h_C(2)>0. Every endpoint-two zero in this domain requires c<9a/4-8.',
                  'strict_improvement_over_3a_minus_4': '3a-4-(9a/4-8)=3a/4+4>0.',
                  'transformation': 'a=8+m,b=(a+(2a-2)t)/(1+t),c=9a/4-8+v; m,t,v>=0, covers a<=b<2a-2.',
                  'nonnegative_terms': [str(first_nonnegative), str(second_nonnegative)],
                  'residual_positive_terms': 84, 'residual_constant': 3014656,
                  'residual_vectors_ascending_in_m_by_t_power_and_v_power': vectors,
                  'nonintegrality_consequence': 'All-even triples and permutations(1,3,2)/(3,3,0)mod4 at a>=8,c>=9a/4-8 are nonintegral using a positive root in(0,2)and prior conditional exclusion of1.',
                  'remaining_fully_distinct_integer_endpoint_two_region': 'a>=8,d=b-a>=5,a<2d^2+20,b<beta(a)<2a-2,b<c<9a/4-8. Necessary conditions, not a characterization of integer points.',
                  'direct_quotient_fixtures': fixtures, 'below_cutoff_controls': controls,
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Written unbounded positivity proof from two nonnegative square expressions and a complete84term positive residual, plus preserved middle-tail theorem. No finite base or parameter scan required. Exact generic6x6quotient/transform/inverse/coefficient reconstruction/boundary identities; eight fixed direct quotient/integer-Horner/Sturm fixtures and two below-cutoff controls. No floats or Lean. Previous scripts/results and manuscript files unchanged. General endpoint-two feasibility, other endpoint-one cases and fullQ3open.'}, indent=2))
