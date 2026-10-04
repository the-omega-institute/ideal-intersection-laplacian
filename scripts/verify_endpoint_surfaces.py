import hashlib
import json
from math import isqrt
from pathlib import Path

import sympy

import check_endpoint_surfaces as diagnostic


first, second, third, variable = sympy.symbols('a b c x')
complement = sympy.Matrix([
    [second + third + second * third, -second, -third, 0, 0, -second * third],
    [-first, first + third + first * third, -third, 0, -first * third, 0],
    [-first, -second, first + second + first * second, -first * second, 0, 0],
    [0, 0, -third, third, 0, 0],
    [0, -second, 0, 0, second, 0],
    [-first, 0, 0, 0, 0, first],
])
quintic = sympy.Poly(sympy.cancel(complement.charpoly(variable).as_expr() / variable), variable)
endpoint_cubics = {endpoint: sympy.Poly(quintic.eval(endpoint), third) for endpoint in (1, 2)}
constant_terms = {
    1: (first - 1) * (second - 1) * (first + second - 1) * (first * second + first + second - 1),
    2: 2 * (first - 2) * (second - 2) * (first + second - 2) * (first * second + first + second - 2),
}
for endpoint, polynomial in endpoint_cubics.items():
    assert polynomial.degree() == 3
    assert sympy.expand(polynomial.TC() - constant_terms[endpoint]) == 0


def integer_horner(coefficients, argument):
    value = 0
    for coefficient in coefficients:
        value = value * argument + int(coefficient)
    return value


def positive_divisors(number):
    result = []
    for candidate in range(1, isqrt(number) + 1):
        if number % candidate == 0:
            result.append(candidate)
            partner = number // candidate
            if partner != candidate:
                result.append(partner)
    return sorted(result)


rows = []
total_divisors = 0
total_evaluations = 0
for minimum in range(4, 15):
    for middle in range(minimum + 1, 16):
        weights = sympy.Matrix([minimum, middle, third, minimum * middle, minimum * third, middle * third])
        direct = complement.subs({first: minimum, second: middle})
        original = diagnostic.quotient_matrix_H(minimum, middle).subs(diagnostic.c, third)
        assert original + direct == sum(weights) * sympy.eye(6) - sympy.ones(6, 1) * weights.T
        for endpoint in (1, 2):
            polynomial = sympy.Poly(endpoint_cubics[endpoint].as_expr().subs({first: minimum, second: middle}), third)
            reconstructed = diagnostic.h_C_at_x(minimum, middle, endpoint).subs(diagnostic.c, third)
            assert sympy.expand(polynomial.as_expr() - reconstructed) == 0
            coefficients = [int(coefficient) for coefficient in polynomial.all_coeffs()]
            constant = coefficients[-1]
            assert constant > 0
            divisors = positive_divisors(constant)
            eligible = [int(divisor) for divisor in divisors if divisor > middle]
            candidates = [divisor for divisor in eligible if integer_horner(coefficients, divisor) == 0]
            assert candidates == diagnostic.integer_roots_in_c(reconstructed.subs(third, diagnostic.c), middle + 1)
            assert candidates == []
            total_divisors += len(divisors)
            total_evaluations += len(eligible)
            rows.append({'a': minimum, 'b': middle, 'endpoint': endpoint,
                         'cubic_coefficients_descending': coefficients,
                         'positive_divisors_of_constant': len(divisors),
                         'divisors_above_b_evaluated': len(eligible), 'integer_roots_above_b': candidates})
assert len(rows) == 132
assert len({(row['a'], row['b']) for row in rows}) == 66
assert len({(row['a'], row['b']) for row in rows if row['a'] >= 8}) == 28

positive_controls = []
for minimum, middle, endpoint, expected_root in ((9, 9, 1, 136), (10, 10, 2, 12)):
    polynomial = diagnostic.h_C_at_x(minimum, middle, endpoint)
    roots = diagnostic.integer_roots_in_c(polynomial, middle + 1)
    assert expected_root in roots
    direct = complement.subs({first: minimum, second: middle, third: expected_root})
    direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
    reported, factors, all_integer = diagnostic.factor_check(minimum, middle, expected_root)
    assert sympy.expand(reported.as_expr().subs(diagnostic.x, variable) - direct_quintic.as_expr()) == 0
    assert direct_quintic.eval(endpoint) == 0
    assert not all_integer and any(factor.degree() > 1 for factor, multiplicity in factors[1])
    positive_controls.append({'exponents': [minimum, middle, expected_root], 'endpoint': endpoint,
                              'integer_roots_above_b': roots, 'all_roots_integer': all_integer,
                              'scope': 'Previously settled repeated-exponent family; outside the fully distinct requested domain'})

regression = []
for endpoint in (1, 2):
    original = diagnostic.quotient_matrix_H(4, 5)
    original_quintic = sympy.cancel(original.charpoly(diagnostic.x).as_expr() / diagnostic.x)
    full_vertex_count = 5 * 6 * (diagnostic.c + 1) - 2
    flawed_endpoint = sympy.expand(-original_quintic.subs(diagnostic.x, full_vertex_count - endpoint))
    corrected = diagnostic.h_C_at_x(4, 5, endpoint)
    assert sympy.Poly(flawed_endpoint, diagnostic.c).degree() == 5
    assert sympy.Poly(corrected, diagnostic.c).degree() == 3
    regression.append({'exponents': [4, 5, 6], 'endpoint': endpoint,
                       'original_value_using_full_vertex_count': int(flawed_endpoint.subs(diagnostic.c, 6)),
                       'corrected_complement_value': int(corrected.subs(diagnostic.c, 6))})

sources = [Path(__file__), Path(__file__).with_name('check_endpoint_surfaces.py')]
print(json.dumps({'requested_domain': '4<=a<b<=15, integer c>b with no upper bound on c',
                  'pair_count': 66, 'endpoint_cubic_count': 132,
                  'positive_divisors_considered': total_divisors,
                  'integer_horner_divisors_above_b_evaluated': total_evaluations,
                  'candidate_triples': [], 'pairs_with_minimum_at_least_eight': 28,
                  'independent_method': 'Direct disjoint-support complement matrix, generic endpoint cubics and positive-divisor exhaustion of their nonzero constant terms; independent integer Horner evaluation. Cross-checks corrected reflected-H script and exact rational linear-factor extraction for every pair.',
                  'pairs': rows, 'positive_controls': positive_controls,
                  'reflection_regression': regression,
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Complete finite certificate over66pairs and132cubics, with unbounded integer c handled by exact divisor reduction. With the previously proved uniform low root in(0,3), proves nonintegrality for every fully distinct4<=a<b<=15,c>b. Does not prove the endpoint surfaces globally empty or fullQ3. No floating-point spectrum, no Lean; no unrelated exponent range.'}, indent=2))
