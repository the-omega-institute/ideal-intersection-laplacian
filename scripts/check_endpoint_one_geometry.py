import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable = sympy.symbols('a b c x')
minimum_shift, increment = sympy.symbols('m v')
parameters = (first, middle, last)
matrix = support_quotient(parameters, complement=True)
quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
endpoint = quintic.eval(1)
leading = first ** 2 + middle ** 2 - 1
quadratic = (first ** 3 - 4 * first ** 2 * middle ** 2 + 2 * first ** 2 * middle - first ** 2
             + 2 * first * middle ** 2 + first * middle - 3 * first + middle ** 3 - middle ** 2 - 3 * middle + 3)
linear = (first - 1) * (middle - 1) * (2 * first * middle + 3 * first + 3 * middle - 3)
constant = (first - 1) * (middle - 1) * (first + middle - 1) * (first * middle + first + middle - 1)
cubic = leading * last ** 3 + quadratic * last ** 2 + linear * last + constant
assert sympy.expand(endpoint - cubic) == 0
threshold = 2 * first ** 2 - first - 1
factor = first - 2 * middle ** 2 + 3 * middle - 1
test = -middle ** 3 + threshold * middle ** 2 - 3 * (first - 1) * middle - (first - 1) ** 2
diagonal = sympy.expand(endpoint.subs(last, middle))
assert sympy.expand(diagonal - factor * test) == 0
shifted = sympy.Poly(endpoint.subs(last, middle + increment), increment)
assert sympy.expand(2 * shifted.nth(1) - sympy.diff(diagonal, middle)) == 0
normalized_derivative = -1 + 3 * (first - 1) / middle ** 2 + 2 * (first - 1) ** 2 / middle ** 3
assert sympy.cancel(sympy.diff(test / middle ** 2, middle) - normalized_derivative) == 0
assert sympy.expand(test.subs(middle, first)
                    - (first ** 2 + first - 1) * (2 * first ** 2 - 4 * first + 1)) == 0
assert sympy.expand(test.subs(middle, threshold) + 2 * (first - 1) ** 2 * (3 * first + 2)) == 0
lower_threshold_value = 4 * first ** 4 - 10 * first ** 3 + first ** 2 + 9 * first - 3
assert sympy.expand(test.subs(middle, threshold - 1) - lower_threshold_value) == 0
positive_shifted_quadratic = (middle ** 2 * (4 * middle - 4 * first ** 2 + 2 * first - 1)
                              + (5 * first ** 2 + first - 6) * middle + (first - 1) * (first ** 2 - 3))
assert sympy.expand(shifted.nth(2) - positive_shifted_quadratic) == 0
assert sympy.expand(threshold - 1 - first ** 2 - (first - 2) * (first + 1)) == 0
sum_cutoff = 4 * first ** 2 - 2 * first
remainder = 4 * first ** 4 - first ** 3 - 5 * first ** 2 - first + 3
concave = -middle ** 2 + (first ** 2 + first - 2) * middle + remainder
assert sympy.expand(leading * (sum_cutoff - middle) + quadratic - concave) == 0
assert sympy.diff(concave, middle, 2) == -2
first_boundary = 4 * first ** 4 - 5 * first ** 2 - 3 * first + 3
second_boundary = 2 * (first - 1) * (first ** 3 + 3 * first ** 2 - first - 2)
assert sympy.expand(concave.subs(middle, first) - first_boundary) == 0
assert sympy.expand(concave.subs(middle, threshold) - second_boundary) == 0
positive_vectors = {}
for label, expression in (('test_at_B_minus_one', lower_threshold_value),
                          ('concave_at_a', first_boundary), ('concave_at_B', second_boundary)):
    polynomial = sympy.Poly(expression.subs(first, 8 + minimum_shift).expand(), minimum_shift)
    assert all(coefficient > 0 for coefficient in polynomial.all_coeffs())
    positive_vectors[label] = list(map(int, polynomial.all_coeffs()))


def integer_horner(coefficients, point):
    value = 0
    for coefficient in coefficients:
        value = value * point + coefficient
    return value


pair_fixtures = []
for minimum, second in ((8, 9), (8, 118), (8, 119), (9, 9), (9, 151), (9, 152), (20, 22), (20, 779)):
    substitutions = {first: minimum, middle: second}
    polynomial = sympy.Poly(endpoint.subs(substitutions), last)
    coefficients = list(map(int, polynomial.all_coeffs()))
    diagonal_value = integer_horner(coefficients, second)
    test_value = int(test.subs(substitutions))
    assert diagonal_value == polynomial.eval(second) == factor.subs(substitutions) * test_value
    count = int(polynomial.count_roots(second, sympy.oo)) - int(polynomial.eval(second) == 0)
    assert count == int(test_value > 0)
    record = {'pair': [minimum, second], 'exponent_cubic_coefficients': coefficients,
              'test_R1_value': test_value, 'h_C_at_one_on_diagonal': diagonal_value,
              'real_exponent_roots_strictly_above_b': count}
    if test_value > 0:
        upper = 4 * minimum ** 2 - 2 * minimum - second
        assert polynomial.eval(upper) > 0
        assert polynomial.count_roots(second, upper) == 1
        assert polynomial.count_roots(0, second) == 1
        assert polynomial.count_roots(-sympy.oo, 0) == 1
        record['unique_root_bracket'] = [second, upper]
    else:
        assert second >= 2 * minimum ** 2 - minimum - 1
    pair_fixtures.append(record)
fixtures = []
for exponents in ((8, 9, 231), (8, 118, 122), (8, 119, 120), (9, 9, 136),
                  (9, 151, 155), (20, 22, 1538), (20, 779, 780)):
    direct = support_quotient(exponents, complement=True)
    polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
    assert polynomial == sympy.Poly(quintic.as_expr().subs(dict(zip(parameters, exponents))), variable)
    coefficients = list(map(int, polynomial.all_coeffs()))
    values = [integer_horner(coefficients, point) for point in (0, 1)]
    assert values == [int(polynomial.eval(point)) for point in (0, 1)]
    record = {'exponents': exponents, 'quintic_coefficients': coefficients,
              'integer_Horner_at_0_1': values,
              'positive_roots_strictly_between_0_and_1': int(polynomial.count_roots(0, 1))
              - int(polynomial.eval(1) == 0)}
    if exponents != (9, 9, 136):
        assert values[0] < 0 < values[1]
        assert record['positive_roots_strictly_between_0_and_1'] >= 1
    else:
        assert values[1] == 0
        assert sympy.factor_list(polynomial)[1] != [(polynomial, 1)]
        record['scope'] = 'Preserved repeated endpoint-one zero below sum cutoff; already nonintegral, not a root-free claim.'
    fixtures.append(record)
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'written_geometry': 'For fixed reala>=8,b>=a, h_C(1)=0has a real c>b solution iff R1_a(b)>0; then solution unique and simple as exponent root. Threshold gamma(a)lies strictly between2a^2-a-2and2a^2-a-1.',
                  'integer_middle_consequence': 'For integera>=8,b>=a, c>b real endpoint-one feasibility holds exactly when b<=2a^2-a-2. Integer feasibility of c remains separate.',
                  'written_sum_tail': 'For ordered real8<=a<=b<=c, b+c>=4a^2-2aimplies h_C(1)>0. Thus every ordered endpoint-one zero with c>b requires b+c<4a^2-2a; a positive quotient root in(0,1)proves nonintegrality in the integer sum tail without parity assumptions.',
                  'diagonal_factor_L1': str(factor), 'diagonal_test_R1': str(test),
                  'normalized_derivative': str(normalized_derivative),
                  'positive_vectors_descending_in_m_at_a_8_plus_m': positive_vectors,
                  'fixed_pair_cubic_fixtures': pair_fixtures, 'direct_quotient_fixtures': fixtures,
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Written unbounded real feasibility/uniqueness, precise quadratic middle threshold and b+c sum cutoff, no finite base or parameter scan. Exact generic6x6quotient/endpoint cubic/diagonal/symmetry derivative/threshold/concavity endpoint identities; eight chosen exponent cubics with complete exact Sturm counts, seven direct quotient/integer-Horner/Sturm fixtures including preserved repeated endpoint-one control. Simplicity concerns exponent polynomial, not spectral multiplicity. No floats or Lean. General endpoint-one integer feasibility, its other quotient roots, fullQ3 and higher-prime nonsquarefree vectors open; previous results/manuscript unchanged.'}, indent=2))
