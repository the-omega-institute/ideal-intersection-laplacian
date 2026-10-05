import argparse
import csv
import hashlib
import io
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable = sympy.symbols('a b c x')
minimum_shift, middle_shift, last_shift = sympy.symbols('m t u')
parameters = (first, middle, last)
matrix = support_quotient(parameters, complement=True)
quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
endpoint = quintic.eval(2)
four_difference = sympy.expand(quintic.eval(4) - 3 * endpoint)
five_difference = sympy.expand(4 * endpoint - quintic.eval(5))
positive_five = sympy.Poly(five_difference.subs({first: 8 + minimum_shift, middle: 8 + middle_shift,
                                               last: 8 + last_shift}).expand(), minimum_shift, middle_shift, last_shift)
assert len(positive_five.terms()) == 44
assert all(coefficient > 0 for coefficient in positive_five.coeffs())
assert positive_five.eval({minimum_shift: 0, middle_shift: 0, last_shift: 0}) == 4629843
middle_substitution = first * (1 + 2 * middle_shift) / (1 + middle_shift)
last_substitution = first * (4 + 9 * last_shift) / (4 * (1 + last_shift))
assert sympy.cancel(middle_substitution.subs(middle_shift, (middle - first) / (2 * first - middle)) - middle) == 0
assert sympy.cancel(last_substitution.subs(last_shift, 4 * (last - first) / (9 * first - 4 * last)) - last) == 0
transformed = sympy.cancel(64 * (1 + middle_shift) ** 3 * (1 + last_shift) ** 3
                          * four_difference.subs({middle: middle_substitution, last: last_substitution}))
positive_four = sympy.Poly(transformed.subs(first, 40 + minimum_shift).expand(), minimum_shift, middle_shift, last_shift)
assert len(positive_four.terms()) == 112
assert all(coefficient > 0 for coefficient in positive_four.coeffs())
assert positive_four.eval({minimum_shift: 0, middle_shift: 0, last_shift: 0}) == 611305472


def coefficient_vectors(polynomial):
    vectors = [[list(reversed(list(map(int, sympy.Poly(polynomial.as_expr().coeff(middle_shift, middle_power)
                                                     .coeff(last_shift, last_power), minimum_shift).all_coeffs()))))
                for last_power in range(4)] for middle_power in range(4)]
    reconstructed = sum(coefficient * minimum_shift ** degree * middle_shift ** middle_power * last_shift ** last_power
                        for middle_power, row in enumerate(vectors) for last_power, vector in enumerate(row)
                        for degree, coefficient in enumerate(vector))
    assert sympy.expand(reconstructed - polynomial.as_expr()) == 0
    return vectors


four_vectors = coefficient_vectors(positive_four)
five_vectors = coefficient_vectors(positive_five)


def integer_horner(coefficients, point):
    value = 0
    for coefficient in coefficients:
        value = value * point + coefficient
    return value


def integer_shift_matrix(exponents):
    minimum, second, third = exponents
    complement = [[second + third + second * third, -second, -third, 0, 0, -second * third],
                  [-minimum, minimum + third + minimum * third, -third, 0, -minimum * third, 0],
                  [-minimum, -second, minimum + second + minimum * second, -minimum * second, 0, 0],
                  [0, 0, -third, third, 0, 0], [0, -second, 0, 0, second, 0],
                  [-minimum, 0, 0, 0, 0, minimum]]
    return [[(2 if row_index == column_index else 0) - entry
             for column_index, entry in enumerate(row)] for row_index, row in enumerate(complement)]


def bareiss_determinant(entries):
    working = [row[:] for row in entries]
    previous_pivot = 1
    sign = 1
    size = len(working)
    for pivot_index in range(size - 1):
        if working[pivot_index][pivot_index] == 0:
            swap_index = next((index for index in range(pivot_index + 1, size)
                               if working[index][pivot_index] != 0), None)
            if swap_index is None:
                return 0
            working[pivot_index], working[swap_index] = working[swap_index], working[pivot_index]
            sign = -sign
        pivot = working[pivot_index][pivot_index]
        for row_index in range(pivot_index + 1, size):
            for column_index in range(pivot_index + 1, size):
                numerator = (working[row_index][column_index] * pivot
                             - working[row_index][pivot_index] * working[pivot_index][column_index])
                assert numerator % previous_pivot == 0
                working[row_index][column_index] = numerator // previous_pivot
        for row_index in range(pivot_index + 1, size):
            working[row_index][pivot_index] = 0
        previous_pivot = pivot
    return sign * working[-1][-1]


cubic = sympy.Poly(endpoint, last)
evaluate_coefficients = sympy.lambdify((first, middle), cubic.all_coeffs(), modules='math')
csv_output = io.StringIO()
writer = csv.writer(csv_output, lineterminator='\n')
writer.writerow(['a', 'b', 'c', 'h_C_at_two_integer_Horner', 'det_two_I_minus_C_integer_Bareiss'])
base_counts = []
total = 0
for minimum in range(8, 40):
    maximum = (9 * minimum - 33) // 4
    count = 0
    least_absolute = None
    for second in range(minimum + 1, 2 * minimum - 2):
        coefficients = evaluate_coefficients(minimum, second)
        assert all(isinstance(coefficient, int) for coefficient in coefficients)
        for third in range(second + 1, maximum + 1):
            value = integer_horner(coefficients, third)
            determinant = bareiss_determinant(integer_shift_matrix((minimum, second, third)))
            assert determinant == 2 * value
            assert value != 0
            writer.writerow([minimum, second, third, value, determinant])
            count += 1
            least_absolute = abs(value) if least_absolute is None else min(least_absolute, abs(value))
    base_counts.append({'minimum': minimum, 'largest_integer_c_below_strict_cutoff': maximum,
                        'complete_triples_checked': count, 'least_absolute_h_C_at_two': least_absolute,
                        'endpoint_two_zeros': 0})
    total += count
assert total == 8658
csv_text = csv_output.getvalue()

fixtures = []
for exponents in ((40, 50, 75), (40, 60, 78), (64, 80, 128), (100, 140, 215),
                  (8, 9, 10), (20, 30, 37), (39, 60, 79)):
    direct = support_quotient(exponents, complement=True)
    assert sympy.Matrix(integer_shift_matrix(exponents)) == 2 * sympy.eye(6) - direct
    polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
    assert polynomial == sympy.Poly(quintic.as_expr().subs(dict(zip(parameters, exponents))), variable)
    coefficients = list(map(int, polynomial.all_coeffs()))
    values = [integer_horner(coefficients, point) for point in (2, 4, 5)]
    assert values == [int(polynomial.eval(point)) for point in (2, 4, 5)]
    assert bareiss_determinant(integer_shift_matrix(exponents)) == 2 * values[0]
    assert 4 * values[0] - values[2] > 0
    record = {'exponents': exponents, 'quintic_coefficients': coefficients, 'integer_Horner_at_2_4_5': values,
              'roots_strictly_between_4_and_5': int(polynomial.count_roots(4, 5))
              - int(polynomial.eval(4) == 0) - int(polynomial.eval(5) == 0)}
    if exponents[0] >= 40:
        assert values[1] - 3 * values[0] > 0
        record['positive_four_difference_checked'] = True
    fixtures.append(record)
control = sympy.Poly(sympy.cancel(support_quotient((10, 10, 12), complement=True).charpoly(variable).as_expr()
                                  / variable), variable)
assert control.eval(2) == 0 and control.eval(4) < 0 and control.eval(5) < 0
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
certificate = {'written_tail': 'For ordered reala>=40 and h_C(2)=0, h_C(4)>0>h_C(5), so another quotient root lies strictly in(4,5). Uses preceding middle/maximum bounds; no parity assumption or finite base for this tail.',
               'complete_integer_result': 'Every positive integer three-exponent vector with h_C(2)=0 has a nonintegral quotient spectrum: written taila>=40; complete8658triple finite base excludes fully distinct endpoint-two zeros at8<=a<=39; earlier repeated and minimum<=7nonintegrality results handle the other cases.',
               'parity_class_completion': 'Every all-even triple and every permutation(1,3,2)/(3,3,0)mod4 triple is Laplacian nonintegral, combining uniform low root, conditional exclusion of1, endpoint-two obstruction and earlier repeated/minimum<=7results. Global statement depends on finite computations.',
               'positive_four_difference': {'terms': 112, 'constant': 611305472,
                                            'transformation': 'a=40+m,b=a(1+2t)/(1+t),c=a(4+9u)/(4(1+u));m,t,u>=0.',
                                            'vectors_ascending_in_m_by_t_power_and_u_power': four_vectors},
               'positive_five_difference': {'terms': 44, 'constant': 4629843,
                                            'transformation': 'a=8+m,b=8+t,c=8+u;m,t,u>=0.',
                                            'vectors_ascending_in_m_by_t_power_and_u_power': five_vectors},
               'finite_base_scope': 'Exactly all8658integer triples8<=a<=39,a<b<2a-2,b<c<9a/4-8. No small-gap or growing-gap exclusions needed to reduce this base. Every endpoint value checked by integer cubic Horner and an independent integer6x6Bareiss determinant. No zeros; repeated triples excluded from this base.',
               'finite_base_counts': base_counts, 'finite_base_triples': total,
               'finite_base_csv_sha256': hashlib.sha256(csv_text.encode()).hexdigest(),
               'direct_quotient_fixtures': fixtures,
               'repeated_control': {'exponents': [10, 10, 12], 'h_C_at_two': 0,
                                    'scope': 'Below written-tail threshold and outside fully distinct base. Existing repeated nonintegrality theorem retained; h_C(4)negative here, so no all-minima(4,5)bracket claimed.'},
               'sympy': sympy.__version__,
               'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
               'scope': 'Written unbounded endpoint-two nonintegrality tail and two full positive identities. Global parity-class completion relies on necessary8658triple finite base plus earlier repeated/minimum<=7results; not a purely written all-triples theorem. Seven direct quotient/Horner/Sturm fixtures and repeated control. No arbitrary c cutoff, unrelated search/modulus expansion, floats or Lean. General endpoint-two integer-point emptiness at unbounded minima is not proved or needed. Remaining endpoint-one classes, fullQ3 and higher-prime nonsquarefree vectors open; manuscript unchanged.'}
parser = argparse.ArgumentParser()
parser.add_argument('--csv', action='store_true')
arguments = parser.parse_args()
print(csv_text if arguments.csv else json.dumps(certificate, indent=2), end='' if arguments.csv else '\n')
