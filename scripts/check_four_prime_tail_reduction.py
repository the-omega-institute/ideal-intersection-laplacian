import hashlib
import json
from math import isqrt
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def refined_bound(first, tail):
    width = (first + 1) * tail
    product_bound = width ** 2 // 4
    return product_bound * (product_bound + first * (width - 1) + first ** 2 * tail)


def symbolic_checks():
    first, tail, maximum, variable, offset, growth = sympy.symbols('a b c x t u')
    matrix = sympy.Matrix(operator(first, tail, maximum))
    polynomial = matrix.charpoly(variable).as_expr()
    endpoint = (first + 1) * (tail + 1)
    width = (first + 1) * tail
    endpoint_positive = first ** 2 * tail * maximum * (
        (maximum - 1) * (endpoint ** 2 - tail * (2 * first + 1))
        + (first + 1) ** 2 * (tail ** 2 + 1) - first * tail)
    assert sympy.expand(polynomial.subs(variable, endpoint) - endpoint_positive) == 0
    constant = sympy.Poly(polynomial.subs(variable, first + 1 + offset), maximum).nth(0)
    positive_constant = offset * (width - offset) * (offset * (width - offset) + first * offset + first ** 2 * tail)
    assert sympy.expand(constant - positive_constant) == 0
    factor = (variable ** 2 - (first * tail + 3 * first + tail + 2) * variable
              + 2 * first ** 2 + 2 * first * tail + 3 * first + tail + 1)
    assert sympy.expand(sympy.Poly(polynomial, maximum).nth(0)
                        - (variable - first - 1) * (variable - endpoint) * factor) == 0
    fixed = sympy.Poly(polynomial.subs({first: 5, tail: 5, variable: 6 + offset}), maximum)
    expected = [216 * offset ** 2 - 1080 * offset - 6875,
                offset * (-42 * offset ** 2 + 1195 * offset + 575),
                offset * (30 - offset) * (offset * (30 - offset) + 5 * offset + 125)]
    assert all(sympy.expand(fixed.nth(degree) - expression) == 0
               for degree, expression in zip((2, 1, 0), expected))
    assert sympy.expand(expected[0].subs(offset, 9 + growth)
                        - (216 * growth ** 2 + 2808 * growth + 901)) == 0
    assert sympy.expand(expected[1] / offset
                        - (7928 - 359 * (offset - 9) + 42 * (offset - 9) * (28 - offset))) == 0
    assert sympy.expand(fixed.as_expr().subs(offset, 5) + 6875 * (maximum - 5) * (maximum + 1)) == 0
    exceptional = polynomial.subs({first: 5, tail: 5, maximum: 5})
    cubic = variable ** 3 - 288 * variable ** 2 + 14298 * variable - 41261
    assert sympy.expand(exceptional - (variable - 11) * cubic) == 0
    assert cubic.subs(variable, 3) == -932 and cubic.subs(variable, 4) == 11387
    return {'strict_second_root_upper_endpoint_identity': str(endpoint_positive),
            'strict_second_root_interval': 'a+1<kappa_2<(a+1)(b+1)',
            'constant_coefficient_positive_identity': str(positive_constant),
            'constant_coefficient_factorization': str((variable - first - 1) * (variable - endpoint) * factor),
            'integer_second_root_candidate_domain': 'k=a+1+t,1<=t<=(a+1)b-1',
            'candidate_tail_divisibility': 'c divides t(d-t)[t(d-t)+at+a^2b],d=(a+1)b',
            'candidate_tail_count_bound': '2((a+1)b-1)',
            'refined_tail_cutoff': 'U[U+a(d-1)+a^2b],U=floor(d^2/4),d=(a+1)b',
            'fixed_a_b_5_tail_polynomial_coefficients_descending': [str(value) for value in expected],
            'fixed_a_b_5_positive_coefficient_region': '9<=t<=28; A=216(t-9)^2+2808(t-9)+901>0; B/t=7928-359(t-9)+42(t-9)(28-t)>=1107',
            'fixed_a_b_5_only_integer_second_root_tail': {'t': 5, 'k': 11, 'c': 5},
            'exceptional_quartic_factorization': str((variable - 11) * cubic),
            'exceptional_cubic_endpoint_values': [-932, 11387]}


def fixed_pair_candidate_rows():
    maximum, variable = sympy.symbols('c x')
    polynomial = sympy.Matrix(operator(5, 5, maximum)).charpoly(variable).as_expr()
    expected_anchors = {1: 12071, 2: 19516, 3: 26717, 4: 33948, 6: 48574, 7: 55828, 8: 62890}
    rows = []
    all_candidates = []
    for offset in range(1, 30):
        anchor = 6 + offset
        quadratic = sympy.Poly(polynomial.subs(variable, anchor), maximum)
        coefficients = [int(quadratic.nth(degree)) for degree in (2, 1, 0)]
        values = []
        for tail_value in (0, 1, 2, 3):
            matrix = operator(5, 5, tail_value)
            values.append(integer_determinant([[anchor * (row == column) - matrix[row][column]
                                                for column in range(4)] for row in range(4)]))
        direct_leading = (values[2] - 2 * values[1] + values[0]) // 2
        assert (values[2] - 2 * values[1] + values[0]) % 2 == 0
        direct_linear = values[1] - values[0] - direct_leading
        assert coefficients == [direct_leading, direct_linear, values[0]]
        assert quadratic.eval(3) == values[3]
        leading, linear, constant = coefficients
        assert leading != 0 and constant > 0
        discriminant = linear ** 2 - 4 * leading * constant
        candidates = []
        if 9 <= offset <= 28:
            assert all(value > 0 for value in coefficients)
            obstruction = 'all three coefficients positive'
        elif offset == 29:
            assert discriminant == -4968683100
            obstruction = 'negative discriminant'
        elif offset == 5:
            assert coefficients == [-6875, 27500, 34375] and discriminant == 41250 ** 2
            numerators = [-linear - 41250, -linear + 41250]
            integer_roots = [value // (2 * leading) for value in numerators if value % (2 * leading) == 0]
            assert sorted(integer_roots) == [-1, 5]
            candidates = [5]
            obstruction = '-6875(c-5)(c+1)'
        else:
            square_anchor = isqrt(discriminant)
            assert square_anchor == expected_anchors[offset]
            assert square_anchor ** 2 < discriminant < (square_anchor + 1) ** 2
            obstruction = 'nonsquare discriminant'
        all_candidates.extend(candidates)
        row = {'t': offset, 'k': anchor, 'quadratic_coefficients_descending': coefficients,
               'four_direct_integer_determinants_at_c_0_1_2_3': values,
               'discriminant': discriminant, 'obstruction': obstruction,
               'positive_integer_tail_candidates': candidates}
        if offset in expected_anchors:
            row['consecutive_square_anchor'] = expected_anchors[offset]
        rows.append(row)
    assert all_candidates == [5]
    return rows


def fixed_control(first, tail, maximum=None):
    bound = refined_bound(first, tail)
    in_region = maximum is None
    maximum = bound + 1 if in_region else maximum
    endpoint = (first + 1) * (tail + 1)
    matrix = operator(first, tail, maximum)
    control = support_embedding(first, tail, maximum)
    variable = sympy.Symbol('x')
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    values = [(anchor, integer_determinant([[anchor * (row == column) - matrix[row][column]
                                            for column in range(4)] for row in range(4)]))
              for anchor in range(6)]
    assert sympy.Poly(sympy.interpolate(values[:5], variable), variable) == polynomial
    assert polynomial.eval(5) == values[-1][1]
    assert polynomial.count_roots(1, first + 1) == 1
    assert polynomial.count_roots(first + 1, endpoint) == 1
    assert polynomial.eval(endpoint) > 0
    precision = sympy.Rational(1, 4)
    witness = None
    index = 1 if in_region else 0
    while witness is None:
        low_intervals = polynomial.intervals(eps=precision)[:2]
        lower, upper = low_intervals[index][0]
        anchor = int(sympy.floor(lower))
        if lower != upper and upper <= anchor + 1 and polynomial.eval(anchor) != 0 and polynomial.eval(anchor + 1) != 0:
            witness = [anchor, anchor + 1]
        precision /= 2
    endpoint_values = [integer_determinant([[anchor * (row == column) - matrix[row][column]
                                           for column in range(4)] for row in range(4)]) for anchor in witness]
    assert endpoint_values == [polynomial.eval(anchor) for anchor in witness]
    assert endpoint_values[0] * endpoint_values[1] < 0 and polynomial.count_roots(*witness) == 1
    if not in_region:
        assert (first, tail, maximum) == (5, 5, 5) and polynomial.eval(11) == 0 and witness == [3, 4]
    vertices = control['graph_vertices']
    old_bound = 24 * (endpoint + first) ** 3 * (3 * endpoint + first)
    assert old_bound > 128 * bound
    control.update({'a': first, 'b': tail, 'c': maximum, 'refined_tail_bound': bound,
                    'old_tail_bound': old_bound, 'in_refined_large_tail_region': in_region,
                    'two_low_root_isolating_intervals': [[str(value) for value in interval] for interval, multiplicity in low_intervals],
                    'root_counts_below_and_above_a_plus_1': [1, 1],
                    'quartic_coefficients': [int(value) for value in polynomial.all_coeffs()],
                    'six_direct_integer_determinant_values': values,
                    'two_direct_witness_endpoint_determinants': endpoint_values,
                    'witness_root_index': index + 1, 'restricted_noninteger_witness_interval': witness,
                    'graph_noninteger_witness_interval': [vertices + 1 - anchor for anchor in reversed(witness)],
                    'sturm_roots_in_witness_interval': 1})
    return control


def main():
    directory = Path(__file__).parent
    helpers = ['check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py']
    report = {'written_uniform_theorem': 'For all positive(a,a,b,c),integrality requires c to be a positive integer root of one of at most d-1 nonzero quadratics p(a+1+t),1<=t<=d-1,d=(a+1)b; at most2(d-1)tail candidates; c divides positive H(t). Nonintegral for c>U[U+a(d-1)+a^2b],U=floor(d^2/4). No ordering between a,b.',
              'fixed_pair_corollary': 'Every positive(5,5,5,c)is nonintegral. Complete29candidate-quadratic arithmetic leaves only c=5,kappa_2=11; its remaining cubic has a root in(3,4).',
              'symbolic': symbolic_checks(), 'all_29_fixed_pair_candidate_quadratics': fixed_pair_candidate_rows(),
              'fixed_controls': [fixed_control(1, 1), fixed_control(5, 5), fixed_control(5, 6),
                                 fixed_control(5, 11), fixed_control(10, 20), fixed_control(30, 5), fixed_control(5, 5, 5)],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256((directory / name).read_bytes()).hexdigest() for name in helpers},
              'sympy_version': sympy.__version__,
              'scope': 'Written uniform divisor/quadratic tail reduction and refined cutoff; fixed triple-five corollary uses complete29candidate-quadratic arithmetic plus an explicit cubic interval. 116 independent determinants reconstruct/cross-check all29quadratics; seven support/quartic/root-isolation/Sturm controls add56integer determinants. No exponent rectangle,tail scan,expanded graph,floating eigensolver,historical finite-base rerun or Lean. General single-pair and fully unequal four-prime classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
