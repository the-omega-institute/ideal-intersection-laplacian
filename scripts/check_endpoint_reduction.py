import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, middle, last, variable = sympy.symbols('a b c x')
quotient = support_quotient((first, middle, last), complement=True)
quintic = sympy.Poly(sympy.cancel(quotient.charpoly(variable).as_expr() / variable), variable)
leading = first * last * (first + last - 1) + 2 * first * (first - 1) + 2 * last * (last - 1) - 4
quadratic = (last ** 2 * ((first + 2) * last - (7 * first ** 2 - 2 * first + 8))
             + (first ** 3 + 2 * first ** 2 - 6 * first - 4) * last
             + 2 * (first - 2) * (first ** 2 - 2 * first - 6))
linear = ((first - 2) * (last - 2)
          * (first ** 2 * last + first ** 2 + first * last ** 2 + 6 * first * last
             + 4 * first + last ** 2 + 4 * last - 12))
constant = 2 * (first - 2) * (last - 2) * (first + last - 2) * (first * last + first + last - 2)
assert sympy.Poly(quintic.eval(2), middle).all_coeffs() == [sympy.expand(expression)
                                                         for expression in (leading, quadratic, linear, constant)]
cutoff = (7 * first ** 2 - 2 * first + 8) / (first + 2)
assert sympy.cancel(cutoff - (7 * first - 16 + 40 / (first + 2))) == 0
assert sympy.cancel((7 * first - 12) - cutoff - 4 * (first - 8) / (first + 2)) == 0

positive_rows = []
for name, expression, variables in (
        ('leading', leading, (first, last)),
        ('linear', linear, (first, last)),
        ('constant', constant, (first, last)),
        ('quadratic_remainder_linear', first ** 3 + 2 * first ** 2 - 6 * first - 4, (first,)),
        ('quadratic_remainder_constant', 2 * (first - 2) * (first ** 2 - 2 * first - 6), (first,))):
    shifted = sympy.Poly(sympy.expand(expression.subs({parameter: parameter + 4 for parameter in variables})), *variables)
    assert all(coefficient > 0 for coefficient in shifted.coeffs())
    assert shifted.TC() > 0
    positive_rows.append({'expression': name, 'shifted_polynomial': str(shifted.as_expr()),
                          'strictly_positive_coefficients': len(shifted.coeffs())})

endpoint_constants = {
    1: (first - 1) * (middle - 1) * (first + middle - 1) * (first * middle + first + middle - 1),
    2: 2 * (first - 2) * (middle - 2) * (first + middle - 2) * (first * middle + first + middle - 2),
}
for endpoint, expected in endpoint_constants.items():
    polynomial = sympy.Poly(quintic.eval(endpoint), last)
    assert polynomial.degree() == 3
    assert sympy.expand(polynomial.TC() - expected) == 0


def integer_horner(coefficients, argument):
    value = 0
    for coefficient in coefficients:
        value = value * argument + int(coefficient)
    return value


fixture_rows = []
for exponents in ((8, 10, 44), (10, 14, 58), (40, 42, 266)):
    matrix = support_quotient(exponents, complement=True)
    assert all(entry % 2 == 0 for entry in matrix)
    polynomial = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    assert polynomial == sympy.Poly(quintic.as_expr().subs(dict(zip((first, middle, last), exponents))), variable)
    values = [integer_horner(polynomial.all_coeffs(), endpoint) for endpoint in (0, 1, 2)]
    assert values == [int(polynomial.eval(endpoint)) for endpoint in (0, 1, 2)]
    assert values[0] < 0 < values[2] and values[1] != 0
    root_count = int(polynomial.count_roots(0, 2))
    assert root_count >= 1
    minimum, second, maximum = exponents
    exact_cutoff = cutoff.subs(first, minimum)
    assert maximum >= exact_cutoff and maximum < 4 * minimum ** 2 - 2 * minimum
    assert sympy.gcd_list(exponents) == 2
    assert (minimum - 2) * (sum(exponents) - 2) <= 2 * second * maximum
    assert maximum - minimum > 4
    fixture_rows.append({'exponents': exponents, 'cutoff': str(exact_cutoff),
                          'endpoint_values_at_0_1_2': values,
                          'exact_roots_in_open_interval_0_2': root_count,
                          'even_integer_quotient_entries': True,
                          'outside_prior_quadratic_tail_and_balanced_region': True})

boundary_rows = []
for exponents, endpoint in (((9, 9, 136), 1), ((10, 10, 12), 2)):
    matrix = support_quotient(exponents, complement=True)
    polynomial = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    assert integer_horner(polynomial.all_coeffs(), endpoint) == 0
    divisor_constant = int(endpoint_constants[endpoint].subs({first: exponents[0], middle: exponents[1]}))
    assert divisor_constant % exponents[2] == 0
    assert any(factor.degree() > 1 for factor, multiplicity in polynomial.factor_list()[1])
    if endpoint == 2:
        assert exponents[2] < cutoff.subs(first, exponents[0])
    boundary_rows.append({'exponents': exponents, 'endpoint': endpoint,
                          'divisor_constant': divisor_constant,
                          'nonlinear_rational_factor': True,
                          'scope': 'Existing repeated-exponent case, not a new family'})

sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'endpoint_two_coefficients_in_middle_exponent': [str(expression) for expression in (leading, quadratic, linear, constant)],
                  'strict_cutoff': 'h_C(2)=0 implies c<7a-16+40/(a+2), for4<=a<=b<=c',
                  'all_even_tail': 'c>=7a-16+40/(a+2) is nonintegral for all-even triples with minimum>=4; c>=7a-12 suffices at minimum>=8',
                  'positive_shift_certificates': positive_rows,
                  'endpoint_constant_terms_in_largest_exponent': {str(endpoint): str(expression) for endpoint, expression in endpoint_constants.items()},
                  'direct_quotient_fixtures': fixture_rows, 'existing_endpoint_zero_fixtures': boundary_rows,
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Written positivity and divisibility proofs; exact general endpoint-cubic, cutoff and constant-term identities, five positive shifted-coefficient checks, three selected integer quotient/Horner/Sturm fixtures and two existing endpoint-zero cases. No new exponent range or divisor-set enumeration, no floating-point spectrum, no Lean. FullQ3 remains open.'}, indent=2))
