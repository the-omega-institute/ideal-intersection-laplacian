import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def symbolic_checks():
    exponent, middle, maximum, variable, left, right = sympy.symbols('a b c x u v')
    restriction = sympy.Matrix(operator(exponent, middle, maximum))
    minor = (restriction[0, 0] - 3) * (restriction[3, 3] - 3) - restriction[0, 3] * restriction[3, 0]
    expected = -(exponent + 2) * middle * maximum + (exponent + 1) * (exponent - 2) * (middle + maximum) + 2 * (exponent - 1) * (exponent - 2)
    assert sympy.expand(minor - expected) == 0
    shifted = -(exponent + 2) * left * right - (exponent ** 2 + 3 * exponent - 2) * (left + right) - 2 * (exponent - 1) * (3 * exponent + 2)
    assert sympy.expand(minor.subs({middle: 2 * exponent - 2 + left, maximum: 2 * exponent - 2 + right}) - shifted) == 0
    polynomial = restriction.charpoly(variable).as_expr()
    for endpoint, multiplier in ((2, 3), (3, 20)):
        assert sympy.expand(sympy.rem(polynomial.subs(variable, endpoint), exponent - endpoint + 1, exponent) + multiplier * middle ** 2 * maximum ** 2) == 0
    exceptional = [value + 2 for value in sympy.divisors(20) if value >= 3]
    assert exceptional == [6, 7, 12, 22]
    seventh = sympy.Poly(polynomial.subs({exponent: 7, middle: 1, maximum: 1}), variable, modulus=2)
    expected_binary = sympy.Poly((variable + 1) ** 2 * (variable ** 2 + variable + 1), variable, modulus=2)
    assert seventh == expected_binary
    necessary_tails = {value: [tail for tail in range(value, 2 * value - 2) if gcd((value - 1) * (value - 2), tail) == 1]
                       for value in (6, 12, 22)}
    assert necessary_tails == {6: [7, 9], 12: [13, 17, 19, 21], 22: [23, 29, 31, 37, 41]}
    return {'minor_at_three': str(expected), 'negative_minor_above_tail_cutoff': str(shifted),
            'tail_cutoff': 'min(b,c)>=2a-2 implies1<kappa_min<3',
            'coprime_exceptional_a_from_previous_reduction': exceptional,
            'a_seven_all_odd_modular_factorization': '(x+1)^2(x^2+x+1)mod2',
            'complete_necessary_finite_b_lists': {str(key): value for key, value in necessary_tails.items()}}


def finite_row(exponent, middle, expected):
    maximum, variable = sympy.symbols('c x')
    quadratic = sympy.Poly(sympy.Matrix(operator(exponent, middle, maximum)).charpoly(variable).as_expr().subs(variable, 3), maximum)
    content, primitive = quadratic.primitive()
    coefficients = [int(value) for value in primitive.all_coeffs()]
    discriminant = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
    anchor = isqrt(discriminant)
    assert (int(content), coefficients, discriminant, anchor) == expected
    assert anchor ** 2 < discriminant < (anchor + 1) ** 2
    assert int(sympy.discriminant(primitive.as_expr(), maximum)) == discriminant
    values = []
    for tail in (0, 1, 2, 3):
        matrix = operator(exponent, middle, tail)
        values.append(integer_determinant([[3 * (row == column) - matrix[row][column] for column in range(4)] for row in range(4)]))
    difference = values[2] - 2 * values[1] + values[0]
    assert difference % 2 == 0
    leading = difference // 2
    assert [int(value) for value in quadratic.all_coeffs()] == [leading, values[1] - values[0] - leading, values[0]]
    assert quadratic.eval(3) == values[3]
    return {'a': exponent, 'b': middle, 'content': int(content), 'primitive_coefficients_descending': coefficients,
            'primitive_discriminant': discriminant, 'strict_square_anchor': anchor,
            'four_independent_integer_determinants_at_c_zero_through_three': values,
            'no_rational_tail_root': True}


def fixed_control(exponent, middle, maximum):
    assert exponent >= 5 and middle >= exponent and maximum >= exponent
    assert gcd((exponent - 1) * (exponent - 2), middle * maximum) == 1
    embedding = support_embedding(exponent, middle, maximum)
    variable = sympy.Symbol('x')
    matrix = operator(exponent, middle, maximum)
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    values = []
    for argument in range(5):
        value = integer_determinant([[argument * (row == column) - matrix[row][column] for column in range(4)] for row in range(4)])
        assert value == polynomial.eval(argument)
        values.append(value)
    cutoff = min(middle, maximum) >= 2 * exponent - 2
    upper = 3 if cutoff else 4
    count = int(polynomial.count_roots(1, upper))
    assert count == 1
    assert polynomial.eval(2) != 0
    if exponent != 7:
        assert polynomial.eval(3) != 0
    else:
        reduced = sympy.Poly(polynomial.as_expr(), variable, modulus=2)
        assert any(factor.degree() > 1 for factor, multiplicity in reduced.factor_list()[1])
    return {'exponents': [exponent, exponent, middle, maximum], 'support_embedding': embedding,
            'five_independent_integer_determinants_at_zero_through_four': values,
            'tail_cutoff_holds': cutoff, 'exact_low_root_window': [1, upper], 'exact_low_window_sturm_count': count,
            'a_seven_modular_branch': exponent == 7}


def main():
    expected = {
        (6, 7): (4, [-1085, 8417, -848], 67165569, 8195),
        (6, 9): (4, [-1847, 11381, -2144], 113687289, 10662),
        (12, 13): (10, [-4238, 121085, 6802], 14776884729, 121560),
        (12, 17): (90, [-874, 18581, -462], 343638409, 18537),
        (12, 19): (10, [-10100, 192017, -11822], 36392919489, 190769),
        (12, 21): (10, [-12614, 217949, -20942], 46445117049, 215511),
        (22, 23): (180, [-2001, 142585, 17568], 20471096497, 143077),
        (22, 29): (180, [-3551, 188573, 10992], 35715906697, 188986),
        (22, 31): (60, [-12491, 614283, 23456], 378515559673, 615236),
        (22, 37): (60, [-18869, 767703, -13936], 588316062673, 767017),
        (22, 41): (180, [-7947, 292141, -15408], 84856574377, 291301)}
    symbolic = symbolic_checks()
    complete_pairs = {(int(exponent), tail) for exponent, tails in symbolic['complete_necessary_finite_b_lists'].items() for tail in tails}
    assert set(expected) == complete_pairs
    controls = [(6, 7, 49), (12, 13, 169), (22, 23, 529), (7, 11, 121), (6, 11, 13), (12, 23, 29)]
    directory = Path(__file__).parent
    helpers = ['check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py']
    report = {'written_theorem': 'Every positive four-prime vector(a,a,b,c),a>=5,b,c>=a,gcd((a-1)(a-2),bc)=1,is nonintegral,with no exceptional a. Previous4exceptions are settled by a7modular obstruction and complete11necessary nonsquare-discriminant quadratics for a6,12,22,after min-tail cutoff2a-2.',
              'symbolic': symbolic, 'complete_eleven_finite_rows': [finite_row(*pair, values) for pair, values in expected.items()],
              'fixed_controls': [fixed_control(*control) for control in controls],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256((directory / name).read_bytes()).hexdigest() for name in helpers},
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded reduction with complete11-row exact finite arithmetic,not an arbitrary exponent base.44independent integer determinants reconstruct finite tail quadratics; six support controls verify336column actions,30more integer determinants and6exact Sturm counts;74determinants total. Algebraic c0 solely interpolation. No tail scan,expanded graph,historical finite-base rerun or Lean. General noncoprime repeated-minimum/single-pair,fully unequal four-prime,higher-prime classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
