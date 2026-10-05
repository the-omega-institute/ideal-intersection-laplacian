import argparse
import csv
import hashlib
import io
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def integer_horner(coefficients, point):
    value = 0
    for coefficient in coefficients:
        value = value * point + coefficient
    return value


def integer_shift_matrix(exponents, spectral_point):
    minimum, middle, last = exponents
    complement = [[middle + last + middle * last, -middle, -last, 0, 0, -middle * last],
                  [-minimum, minimum + last + minimum * last, -last, 0, -minimum * last, 0],
                  [-minimum, -middle, minimum + middle + minimum * middle, -minimum * middle, 0, 0],
                  [0, 0, -last, last, 0, 0], [0, -middle, 0, 0, middle, 0],
                  [-minimum, 0, 0, 0, 0, minimum]]
    return [[(spectral_point if row_index == column_index else 0) - entry
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


def certificate():
    middle, last, variable = sympy.symbols('b c x')
    matrix = support_quotient((8, middle, last), complement=True)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    endpoint = quintic.eval(1)
    coefficients = [middle ** 2 + 63, middle ** 3 - 241 * middle ** 2 + 133 * middle + 427,
                    7 * (middle - 1) * (19 * middle + 21),
                    7 * (middle - 1) * (middle + 7) * (9 * middle + 7)]
    cubic = sum(coefficient * last ** (3 - degree) for degree, coefficient in enumerate(coefficients))
    assert sympy.expand(endpoint - cubic) == 0
    test = -middle ** 3 + 119 * middle ** 2 - 21 * middle - 49
    assert sympy.expand(endpoint.subs(last, middle) - (7 - 2 * middle ** 2 + 3 * middle) * test) == 0
    assert sympy.Matrix(integer_shift_matrix((8, middle, last), 1)) == sympy.eye(6) - matrix
    csv_output = io.StringIO()
    writer = csv.writer(csv_output, lineterminator='\n')
    fields = ['minimum', 'middle', 'lower_c', 'upper_c', 'Horner_lower', 'Horner_upper',
              'Bareiss_lower', 'Bareiss_upper', 'Sturm_roots_above_middle', 'Sturm_roots_in_bracket']
    writer.writerow(fields)
    rows = []
    for second in range(11, 119):
        fixed_coefficients = [int(coefficient.subs(middle, second)) for coefficient in coefficients]
        fixed_cubic = sympy.Poly(endpoint.subs(middle, second), last)
        lower, upper = second, 240 - second
        assert integer_horner(fixed_coefficients, lower) < 0 < integer_horner(fixed_coefficients, upper)
        while upper - lower > 1:
            midpoint = (lower + upper) // 2
            value = integer_horner(fixed_coefficients, midpoint)
            assert value != 0
            if value < 0:
                lower = midpoint
            else:
                upper = midpoint
        horner_values = [integer_horner(fixed_coefficients, point) for point in (lower, upper)]
        assert lower > second and upper == lower + 1 and horner_values[0] < 0 < horner_values[1]
        determinants = [bareiss_determinant(integer_shift_matrix((8, second, point), 1))
                        for point in (lower, upper)]
        assert determinants == horner_values
        root_counts = [int(fixed_cubic.count_roots(second, sympy.oo)), int(fixed_cubic.count_roots(lower, upper))]
        assert root_counts == [1, 1]
        assert sympy.gcd(fixed_cubic, fixed_cubic.diff()).degree() == 0
        row = [8, second, lower, upper, *horner_values, *determinants, *root_counts]
        writer.writerow(row)
        rows.append(dict(zip(fields, row)))
    assert len(rows) == 108 and [row['middle'] for row in rows] == list(range(11, 119))
    controls = []
    for exponents, spectral_point in [((8, 9, 10), 2), ((8, 8, 105), 1), ((9, 9, 136), 1)]:
        direct = support_quotient(exponents, complement=True)
        direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        value = int(direct_quintic.eval(spectral_point))
        determinant = bareiss_determinant(integer_shift_matrix(exponents, spectral_point))
        assert determinant == spectral_point * value
        assert (value > 0) if spectral_point == 2 else (value == 0)
        controls.append({'exponents': exponents, 'spectral_point': spectral_point,
                         'endpoint_value': value, 'Bareiss_determinant': determinant})
    csv_text = csv_output.getvalue()
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
    result = {'minimum_eight_result': 'Every positive integer three-exponent vector with minimum exactly8 is Laplacian nonintegral. Repeated exponents use existing written theorem. Fully distinct vectors use written uniform low root, written endpoint-two maximum cutoff, written endpoint-one geometry/gaps1/2 and complete108pair finite unit-bracket certificate. The result requires finite computation, not a purely written minimum-eight theorem.',
              'cumulative_consequence': 'Together with existing minimum<=7results, every triple with minimum<=8is nonintegral. This cumulative conclusion retains the earlier27562triple finite certificate. The global8658triple endpoint-two completion base is not needed for the new minimum-eight proof.',
              'complete_finite_base': {'minimum': 8, 'middle_minimum': 11, 'middle_maximum': 118,
                                       'pairs': 108, 'all_integer_c_strictly_above_middle_covered': True,
                                       'endpoint_one_integer_zeros': 0, 'unit_brackets': 108,
                                       'independent_Bareiss_boundary_determinants': 216,
                                       'exact_Sturm_counts': 216,
                                       'csv_file': 'minimum-eight-base.csv',
                                       'csv_sha256': hashlib.sha256(csv_text.encode()).hexdigest()},
              'endpoint_two_written_reduction': 'Fully distinct ordered minimum8has b>=9,c>=10. Written c>=9a/4-8=10implies h_C(2)>0. No finite endpoint-two base needed here.',
              'endpoint_one_written_reduction': 'Gaps1/2exclude middle9/10. Real feasibility excludes everymiddle>=119. Remainingmiddle11through118have unique real c>middle; the full108pair finite certificate brackets each between consecutive integers.',
              'generic_endpoint_one_cubic_coefficients': list(map(str, coefficients)),
              'selected_base_rows': [rows[index] for index in (0, 11, 53, 107)],
              'preserved_controls': controls, 'sympy': sympy.__version__,
              'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
              'scope': 'Complete minimum-eight necessary fixed-pair base, not an arbitrary exponent range: all108middlevalues11through118with unboundedccoverage from written uniqueness and exact unit brackets; every boundary independently integer-Horner/6x6Bareisschecked and both fullc>b/bracketSturmcounts1. Finite certificate essential. No newdiscriminantcertificate, higherminimumscan, floats or Lean. Oldresults/manuscriptunchanged; repeated endpoint-one zeros preserved. FullQ3/higher-prime nonsquarefreevectorsopen; remainingminimum>=9.'}
    return result, csv_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', action='store_true')
    arguments = parser.parse_args()
    result, csv_text = certificate()
    if arguments.csv:
        print(csv_text, end='')
    else:
        print(json.dumps(result, indent=2))
