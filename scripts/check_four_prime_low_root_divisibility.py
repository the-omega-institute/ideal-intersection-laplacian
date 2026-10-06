import hashlib
import json
from math import gcd, prod
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def symbolic_checks():
    exponent, middle, maximum, variable, growth, left, right = sympy.symbols('a b c x z v w')
    restriction = sympy.Matrix(operator(exponent, middle, maximum))
    polynomial = restriction.charpoly(variable).as_expr()
    anchor = -exponent ** 2 * middle ** 2 * maximum ** 2 * (2 * exponent + 1)
    assert sympy.expand(polynomial.subs(variable, exponent + 1) - anchor) == 0
    remainders = []
    for endpoint, multiplier in ((2, 3), (3, 20)):
        expected = -multiplier * middle ** 2 * maximum ** 2
        actual = sympy.rem(polynomial.subs(variable, endpoint), exponent - endpoint + 1, exponent)
        assert sympy.expand(actual - expected) == 0
        quotient = sympy.cancel((polynomial.subs(variable, endpoint) - expected) / (exponent - endpoint + 1))
        assert sympy.Poly(quotient, exponent, middle, maximum).domain == sympy.ZZ
        remainders.append({'endpoint': endpoint, 'divisor': str(exponent - endpoint + 1),
                           'polynomial_remainder': str(expected), 'quotient_has_integer_coefficients': True})
    minor = (restriction[0, 0] - 4) * (restriction[3, 3] - 4) - restriction[0, 3] * restriction[3, 0]
    expected_minor = -(2 * exponent + 3) * middle * maximum + (exponent ** 2 - 2 * exponent - 3) * (middle + maximum) + 2 * exponent ** 2 - 9 * exponent + 9
    assert sympy.expand(minor - expected_minor) == 0
    shifted = -(2 * exponent + 3) * left * right - (exponent ** 2 + 5 * exponent + 3) * (left + right) - 5 * exponent ** 2 - 15 * exponent + 9
    assert sympy.expand(minor.subs({middle: exponent + left, maximum: exponent + right}) - shifted) == 0
    assert all(value > 0 for value in sympy.Poly(sympy.expand(-shifted.subs(exponent, growth + 5)), growth, left, right).coeffs())
    exceptional = [value + 2 for value in sympy.divisors(20) if value >= 3]
    assert exceptional == [6, 7, 12, 22]
    tails = (exponent + 1, (exponent + 1) ** 2)
    assert sympy.rem(tails[0], exponent + 1, exponent) == 0
    assert sympy.rem(tails[1], exponent + 1, exponent) == 0
    product_failure = (exponent ** 2 - 1) * sum(tails) + (exponent - 1) * (2 * exponent - 1) - prod(tails)
    gap = tails[1] - tails[0]
    weighted_failure = (2 * exponent + 1) * gap ** 2 - 8 * exponent * tails[0]
    comparisons = []
    for label, expression in (('product_tail_failure', product_failure), ('even_gap_weighted_failure', weighted_failure)):
        coefficients = sympy.Poly(sympy.expand(expression.subs(exponent, growth + 18)), growth).all_coeffs()
        assert all(value > 0 for value in coefficients)
        comparisons.append({'criterion': label, 'failure_margin': str(sympy.expand(expression)),
                            'positive_coefficients_after_a_equals_z_plus_eighteen': [int(value) for value in coefficients]})
    for distinguished, others in ((exponent, (exponent, *tails)), (tails[0], (exponent, exponent, tails[1])),
                                  (tails[1], (exponent, exponent, tails[0]))):
        product = prod(others)
        proper_weight = prod(entry + 1 for entry in others) - 1 - product
        margin = (distinguished ** 2 - 1) * proper_weight - (distinguished - 1) - product
        coefficients = sympy.Poly(sympy.expand(margin.subs(exponent, growth + 18)), growth).all_coeffs()
        assert all(value > 0 for value in coefficients)
        comparisons.append({'criterion': 'small_exponent_failure', 'distinguished_exponent': str(distinguished),
                            'failure_margin': str(sympy.expand(margin)),
                            'positive_coefficients_after_a_equals_z_plus_eighteen': [int(value) for value in coefficients]})
    return {'generic_anchor_value': str(anchor), 'low_endpoint_remainders': remainders,
            'upper_principal_minor_at_four': str(expected_minor), 'negative_minor_at_b_a_plus_v_c_a_plus_w': str(shifted),
            'coprime_corollary_exceptional_a': exceptional,
            'new_family': '(a,a,a+1,(a+1)^2),a=6s,s>=3',
            'new_family_passes_all_p_dividing_a_plus_one': 'Both tails are0modp; x^2-x-k reduces to x(x-1).',
            'coverage_comparisons': comparisons}


def fixed_control(exponent, middle, maximum):
    assert exponent >= 5 and middle >= exponent and maximum >= exponent
    embedding = support_embedding(exponent, middle, maximum)
    variable = sympy.Symbol('x')
    matrix = operator(exponent, middle, maximum)
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    determinants = []
    for argument in range(5):
        determinant = integer_determinant([[argument * (row == column) - matrix[row][column] for column in range(4)] for row in range(4)])
        assert determinant == polynomial.eval(argument)
        determinants.append(determinant)
    product_square = (middle * maximum) ** 2
    second_divides = (3 * product_square) % (exponent - 1) == 0
    third_divides = (20 * product_square) % (exponent - 2) == 0
    assert int(polynomial.eval(2)) % (exponent - 1) == (-3 * product_square) % (exponent - 1)
    assert int(polynomial.eval(3)) % (exponent - 2) == (-20 * product_square) % (exponent - 2)
    witness_count = int(polynomial.count_roots(1, 4))
    assert witness_count == 1
    condition = not second_divides and not third_divides
    if condition:
        assert polynomial.eval(2) != 0 and polynomial.eval(3) != 0
    minor = (matrix[0][0] - 4) * (matrix[3][3] - 4) - matrix[0][3] * matrix[3][0]
    assert minor < 0
    return {'exponents': [exponent, exponent, middle, maximum], 'support_embedding': embedding,
            'five_independent_integer_determinants_at_zero_through_four': determinants,
            'endpoint_two_divisibility': second_divides,
            'endpoint_three_divisibility': third_divides,
            'arithmetic_nonintegrality_condition_holds': condition,
            'coprime_to_both_endpoint_divisors': gcd((exponent - 1) * (exponent - 2), middle * maximum) == 1,
            'exact_distinct_restricted_roots_between_one_and_four': witness_count,
            'negative_upper_principal_minor': minor,
            'passing_one_divisibility_is_not_integrality_claim': True}


def main():
    controls = [(18, 19, 361), (24, 25, 625), (30, 31, 961), (11, 14, 26), (6, 7, 49), (22, 23, 529)]
    directory = Path(__file__).parent
    helpers = ['check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py']
    report = {'written_theorem': 'For positive(a,a,b,c),a>=5,b,c>=a,integrality requires (a-1)|3b^2c^2 or (a-2)|20b^2c^2. If neither holds,the smallest genuine restricted root in(1,4)is noninteger. Coprime tails exclude all a except6,7,12,22. In particular every(a,a,a+1,(a+1)^2),a=6s,s>=3,is nonintegral despite passing all p|a+1 modular splitting tests.',
              'symbolic': symbolic_checks(), 'fixed_controls': [fixed_control(*control) for control in controls],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256((directory / name).read_bytes()).hexdigest() for name in helpers},
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded endpoint-divisibility theorem and new modular-compatible infinite family. Six specified support controls,336support-column actions,30independent integer determinants and6exact Sturm root counts. Two controls illustrate arithmetic-test limits,not integrality. No exponent/tail scan,expanded graph,historical finite-base rerun or Lean. General classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
