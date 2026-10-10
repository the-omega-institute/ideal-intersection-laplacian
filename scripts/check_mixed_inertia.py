import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, second, third = sympy.symbols('a b c', positive=True)
variable, span, middle_offset, extra = sympy.symbols('x r d u')
exponents = (first, second, third)
total = sum(exponents)
product = sympy.prod(exponents)
column = sympy.Matrix(exponents)
diagonal = [total - 3 * product / exponent ** 2 for exponent in exponents]
comparison_congruence = (sympy.diag(*(exponent * value for exponent, value in zip(exponents, diagonal)))
                         - column * column.T)
sum_of_squares = (third * (first - second) ** 2
                  + second * (first - third) ** 2
                  + first * (second - third) ** 2)
assert sympy.cancel(comparison_congruence.det() - 6 * product * sum_of_squares) == 0
assert sympy.cancel((sympy.ones(1, 3) * comparison_congruence * sympy.ones(3, 1))[0]
                    + 3 * product * sum(1 / exponent for exponent in exponents)) == 0
schur_values = [total - variable - variable * product / (exponent * (exponent - variable))
                for exponent in exponents]
schur_congruence = (sympy.diag(*(exponent * value for exponent, value in zip(exponents, schur_values)))
                   - column * column.T)
comparison_gap = sympy.diag(*(3 * exponent + 9 * product / (exponent * (exponent - 3))
                             for exponent in exponents))
assert (comparison_congruence - schur_congruence.subs(variable, 3)
        - comparison_gap).applyfunc(sympy.cancel) == sympy.zeros(3)
assert comparison_congruence.subs({second: first, third: first}) == -first ** 2 * sympy.ones(3)
lower_condition = (first - 2) * (total - 2) - 2 * second * third
lower_at_span = sympy.expand(lower_condition.subs({second: first + middle_offset, third: first + span}))
worst_lower = first ** 2 - 2 * first * span - 8 * first - 2 * span ** 2 - 4 * span + 4
assert sympy.expand(lower_at_span - worst_lower - (span - middle_offset) * (first + 2 * span + 2)) == 0
shifted_lower = sympy.expand(worst_lower.subs(first, 3 * span + 8 + extra))
assert sympy.expand(shifted_lower - (span + 2) ** 2 - (4 * span + 8) * extra - extra ** 2) == 0

secular_rows = []
secular_fixtures = [((20, 21, 24), 2), ((20, 21, 30), 2), ((8, 100, 10000), 3),
                    ((20, 21, 30), 3), ((100, 102, 104), 3), ((4, 5, 6), 3)]
for triple, endpoint in secular_fixtures:
    values = [sympy.cancel(value.subs(dict(zip(exponents, triple))).subs(variable, endpoint))
              for value in schur_values]
    assert all(value != 0 for value in values)
    negative_diagonal = sum(1 for value in values if value < 0)
    secular = sympy.cancel(1 - sum(sympy.Rational(exponent, 1) / value
                                  for exponent, value in zip(triple, values)))
    assert secular != 0
    predicted_count = negative_diagonal + int(bool(secular < 0)) - 1
    quotient = support_quotient(triple, complement=True)
    polynomial = sympy.Poly(sympy.cancel(quotient.charpoly(variable).as_expr() / variable), variable)
    assert polynomial.eval(0) != 0 and polynomial.eval(endpoint) != 0
    actual_count = int(polynomial.count_roots(0, endpoint))
    assert actual_count == predicted_count
    secular_rows.append({'exponents': triple, 'endpoint': endpoint,
                         'schur_diagonal': [str(value) for value in values],
                         'negative_diagonal_entries': negative_diagonal,
                         'secular_factor': str(secular),
                         'positive_root_count_below_endpoint': actual_count})
assert {(row['negative_diagonal_entries'], sympy.sign(sympy.Rational(row['secular_factor'])))
        for row in secular_rows} == {(0, -1), (1, 1), (1, -1), (2, 1), (2, -1), (3, 1)}

root_rows = []
fixtures = [(4, 5, 6), (8, 8, 8), (8, 8, 11), (8, 15, 20),
            (8, 100, 10000), (20, 21, 24), (38, 43, 48),
            (308, 350, 408), (3008, 3600, 4008)]
for triple in fixtures:
    quotient = support_quotient(triple, complement=True)
    polynomial = sympy.Poly(sympy.cancel(quotient.charpoly(variable).as_expr() / variable), variable)
    assert polynomial.eval(0) != 0 and polynomial.eval(3) != 0
    below_three = int(polynomial.count_roots(0, 3))
    assert below_three >= 1
    lower = (triple[0] - 2) * (sum(triple) - 2) - 2 * triple[1] * triple[2]
    below_two = None
    between_two_and_three = None
    if lower > 0:
        assert polynomial.eval(2) != 0
        below_two = int(polynomial.count_roots(0, 2))
        between_two_and_three = int(polynomial.count_roots(2, 3))
        assert below_two == 0 and between_two_and_three >= 1
    root_rows.append({'exponents': triple, 'quintic': str(polynomial.as_expr()),
                      'positive_roots_below_three': below_three,
                      'lower_condition': lower, 'positive_roots_below_two': below_two,
                      'roots_between_two_and_three': between_two_and_three,
                      'zero_schur_diagonal_entries_at_three': sum(
                          sympy.cancel(value.subs(dict(zip(exponents, triple))).subs(variable, 3)) == 0
                          for value in schur_values)})
assert sum(row['zero_schur_diagonal_entries_at_three'] > 0 for row in root_rows) == 2

source_paths = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'comparison_determinant': '6*(c*(a-b)^2+b*(a-c)^2+a*(b-c)^2)',
                  'comparison_negative_rayleigh': '-3abc*(1/a+1/b+1/c)',
                  'schur_comparison_gap': 'diag(3+9abc/[t^2*(t-3)]) is positive definite for a>3',
                  'general_symbolic_identities': 'passed',
                  'general_low_root_bound': 'Every ordered4<=a<=b<=c has a nonzero complement quotient root in(0,3)',
                  'mixed_inertia_formula': 'For0<x<a and all k_t(x) nonzero: n_minus(K)=number_of_negative_k_t+indicator(1-sum(t/k_t)<0)',
                  'interval_criterion': '(a-2)(a+b+c-2)>2bc implies a complement root in(2,3)',
                  'span_threshold': 'minimum a>=3r+8, r=maximum-minus-minimum, implies nonintegrality',
                  'threshold_positive_expansion': str(shifted_lower),
                  'secular_formula_sturm_representatives': secular_rows,
                  'independent_quotient_sturm_representatives': root_rows,
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                                    for source in source_paths},
                  'scope': 'Written general comparison/inertia proof and balanced-region theorem. Exact symbolic3x3determinant, negative Rayleigh, comparison-gap and span identities; six secular/Sturm fixtures and nine direct quotient/Sturm fixtures, including equal exponents, two zero-diagonal boundaries and arbitrarily large selected spans. Fixtures validate formulas, not infinite quantifiers. No scan, numerical eigenvalues or Lean. FullQ3 remains open.'}, indent=2))
