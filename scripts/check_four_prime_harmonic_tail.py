import hashlib
import json
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def symbolic_checks():
    first, tail, maximum, variable = sympy.symbols('a b c x')
    matrix = sympy.Matrix(operator(first, tail, maximum))
    polynomial = matrix.charpoly(variable).as_expr()
    harmonic = first + 1 + 2 * tail * maximum / (tail + maximum)
    positive = sympy.Poly(sympy.cancel(polynomial.subs(variable, harmonic) * (tail + maximum) ** 4
                                     / (tail * maximum * (tail - maximum) ** 2)), first, tail, maximum)
    assert len(positive.terms()) == 22 and all(value > 0 for value in positive.coeffs())
    lower_identity = first * tail * (tail - maximum) * (first + tail + 1) * (
        first * tail * maximum + first * tail - first * maximum + tail * maximum)
    assert sympy.expand(polynomial.subs(variable, first + tail + 1) - lower_identity) == 0
    endpoint = (first + 1) * (tail + 1)
    top_diagonal = endpoint * (maximum + 1) + first
    assert sympy.expand(top_diagonal - first - 1 - 2 * tail
                        - ((maximum - 1) * endpoint + 2 * first * tail + 2 * first + 1)) == 0
    offset = 2 * tail - 1
    width = (first + 1) * tail
    product = offset * (width - offset)
    bound = sympy.expand(product * (product + first * offset + first ** 2 * tail))
    return {'harmonic_endpoint': 'a+1+2bc/(b+c)',
            'positive_harmonic_bracket': str(positive.as_expr()),
            'positive_harmonic_bracket_terms': 22,
            'generic_lower_endpoint_identity': str(lower_identity),
            'second_root_window_for_b_less_than_c': 'a+b+1<kappa_2<a+1+2bc/(b+c)<a+2b+1',
            'integer_offset_domain_for_unequal_ordered_tails': 'b+1<=t<=2b-1',
            'quadratic_tail_candidate_count': 'at most2(b-1),independent of repeated a',
            'refined_cutoff_for_a_at_least_3': str(bound),
            'refined_cutoff_formula': 'T=(2b-1),d=(a+1)b,J=T(d-T),c<=J[J+aT+a^2b]',
            'scope': 'b<c; tail permutation permits this order; no ordering between a and b. Cutoff refinement uses a>=3.'}


def fixed_control(first, tail, maximum):
    assert tail < maximum
    matrix = operator(first, tail, maximum)
    variable = sympy.Symbol('x')
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    control = support_embedding(first, tail, maximum)
    lower = first + tail + 1
    harmonic = first + 1 + sympy.Rational(2 * tail * maximum, tail + maximum)
    values = [(anchor, integer_determinant([[anchor * (row == column) - matrix[row][column]
                                            for column in range(4)] for row in range(4)])) for anchor in range(6)]
    assert sympy.Poly(sympy.interpolate(values[:5], variable), variable) == polynomial
    assert polynomial.eval(5) == values[-1][1]
    assert polynomial.eval(lower) < 0 < polynomial.eval(harmonic)
    assert polynomial.count_roots(1, lower) == 1
    assert polynomial.count_roots(lower, harmonic) == 1
    assert polynomial.count_roots(harmonic, sympy.oo) == 2
    control.update({'a': first, 'b': tail, 'c': maximum,
                    'quartic_coefficients': [int(value) for value in polynomial.all_coeffs()],
                    'six_independent_integer_determinants': values,
                    'second_root_window': [str(lower), str(harmonic)],
                    'exact_endpoint_values': [str(polynomial.eval(lower)), str(polynomial.eval(harmonic))],
                    'exact_sturm_root_counts_below_inside_above': [1, 1, 2],
                    'window_integer_free': bool(harmonic - lower <= 1)})
    return control


def main():
    directory = Path(__file__).parent
    helpers = ['check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py']
    report = {'written_theorem': 'For positive(a,a,b,c),b<c,the second genuine restricted root lies in(a+b+1,a+1+2bc/(b+c)). Any integral graph has t=kappa_2-a-1 in[b+1,2b-1],leaving at most2(b-1)quadratic tail candidates per fixed(a,b). For a>=3,the positive constant-term bound sharpens to H_(2b-1).',
              'symbolic': symbolic_checks(),
              'fixed_controls': [fixed_control(1, 1, 4), fixed_control(5, 5, 6), fixed_control(5, 5, 11),
                                 fixed_control(5, 6, 20), fixed_control(5, 11, 100), fixed_control(30, 5, 100)],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256((directory / name).read_bytes()).hexdigest() for name in helpers},
              'sympy_version': sympy.__version__,
              'scope': 'Written harmonic root-location and uniform quadratic candidate reduction,not full classification. Six exact support/determinant/Sturm controls; some windows contain integers and do not themselves prove nonintegrality. No exponent scan,expanded graph,historical finite-base rerun or Lean.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
