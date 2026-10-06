import hashlib
import json
from math import gcd
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def symbolic_checks():
    exponent, middle, maximum, root, variable, excess, growth = sympy.symbols('a b c s x u v')
    matrix = operator(exponent, middle, maximum)
    expression = sympy.Matrix(matrix).charpoly(variable).as_expr().subs(variable, root)
    direct = integer_determinant([[(root if row == column else 0) - matrix[row][column]
                                  for column in range(4)] for row in range(4)])
    assert sympy.expand(expression - direct) == 0
    difference = exponent + 1 - root
    first_factor = (exponent + 1) * middle + difference
    second_factor = middle * ((root - 1) ** 2 + (root - 2) * difference) - difference * (2 * difference + root - 1)
    assert sympy.expand(expression.subs(maximum, 0) + difference * first_factor * second_factor) == 0
    special_tail = (exponent - 1) * (2 * exponent - 1)
    numerator = (exponent - 1) * (2 * exponent + 1) * (2 * exponent ** 3 - exponent ** 2 + exponent - 1)
    denominator = 2 * exponent ** 3 - 5 * exponent ** 2 + 3 * exponent + 1
    specialized = expression.subs({root: 2, middle: special_tail})
    factored = 2 * exponent * (exponent - 1) * maximum * (numerator - denominator * maximum)
    assert sympy.expand(specialized - factored) == 0
    numerator_multiplier = 3 * exponent ** 2 - 9 * exponent + 7
    denominator_multiplier = -6 * exponent ** 4 + 9 * exponent ** 3 - 2 * exponent ** 2 + 6 * exponent + 1
    assert sympy.expand(numerator_multiplier * numerator + denominator_multiplier * denominator - 8) == 0
    assert sympy.expand(denominator - 1 - exponent * (exponent - 1) * (2 * exponent - 3)) == 0
    restriction = sympy.Matrix(operator(exponent, special_tail, maximum))
    minor = (restriction[0, 0] - 3) * (restriction[3, 3] - 3) - restriction[0, 3] * restriction[3, 0]
    negative = -(2 * exponent ** 3 - 4 * exponent + 4) * excess - (5 * exponent ** 3 - 6 * exponent ** 2 + 5 * exponent - 2)
    assert sympy.expand(minor.subs(maximum, exponent + excess) - negative) == 0
    expected = {'tail_above_a': [2, 4, 1], 'denominator': [2, 7, 7, 3],
                'negative_minor_slope': [2, 12, 20, 12], 'negative_minor_constant': [5, 24, 41, 24]}
    expansions = {}
    for name, polynomial in (('tail_above_a', special_tail - exponent), ('denominator', denominator),
                             ('negative_minor_slope', 2 * exponent ** 3 - 4 * exponent + 4),
                             ('negative_minor_constant', 5 * exponent ** 3 - 6 * exponent ** 2 + 5 * exponent - 2)):
        coefficients = [int(value) for value in sympy.Poly(sympy.expand(polynomial.subs(exponent, growth + 2)), growth).all_coeffs()]
        assert coefficients == expected[name] and all(value > 0 for value in coefficients)
        expansions[name] = coefficients
    return {'independent_symbolic_permutation_determinant': 'passed',
            'generic_constant_factorization': str(-difference * first_factor * second_factor),
            'special_tail': str(special_tail), 'endpoint_two_factorization': str(factored),
            'numerator_N': str(sympy.expand(numerator)), 'denominator_D': str(denominator),
            'bezout_N_multiplier': str(numerator_multiplier), 'bezout_D_multiplier': str(denominator_multiplier),
            'bezout_constant': 8, 'odd_denominator_identity': 'D=1+a(a-1)(2a-3)',
            'negative_minor_at_c_a_plus_u': str(negative),
            'complete_positive_coefficients_after_a_v_plus_two': expansions,
            'rational_tail_candidate': 'N/D>0 with gcd(N,D)=1 and odd D>=3 for all integer a>=2'}


def fixed_control(exponent, maximum):
    middle = (exponent - 1) * (2 * exponent - 1)
    assert exponent >= 2 and maximum >= exponent
    numerator = (exponent - 1) * (2 * exponent + 1) * (2 * exponent ** 3 - exponent ** 2 + exponent - 1)
    denominator = 2 * exponent ** 3 - 5 * exponent ** 2 + 3 * exponent + 1
    assert numerator > 0 and denominator >= 3 and denominator % 2 == 1
    assert gcd(numerator, denominator) == 1
    tail = sympy.Symbol('c')
    variable = sympy.Symbol('x')
    quadratic = sympy.Poly(sympy.Matrix(operator(exponent, middle, tail)).charpoly(variable).as_expr().subs(variable, 2), tail)
    coefficients = [-2 * exponent * (exponent - 1) * denominator, 2 * exponent * (exponent - 1) * numerator, 0]
    assert coefficients == [int(value) for value in quadratic.all_coeffs()]
    values = []
    for argument in range(4):
        matrix = operator(exponent, middle, argument)
        values.append(integer_determinant([[2 * (row == column) - matrix[row][column]
                                           for column in range(4)] for row in range(4)]))
    difference = values[2] - 2 * values[1] + values[0]
    assert difference % 2 == 0
    leading = difference // 2
    assert coefficients == [leading, values[1] - values[0] - leading, values[0]]
    assert int(quadratic.eval(3)) == values[3]
    matrix = operator(exponent, middle, maximum)
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    determinants = [integer_determinant([[argument * (row == column) - matrix[row][column]
                                         for column in range(4)] for row in range(4)])
                    for argument in range(5)]
    assert sympy.Poly(sympy.interpolate(list(enumerate(determinants)), variable), variable) == polynomial
    assert determinants[2] == 2 * exponent * (exponent - 1) * maximum * (numerator - denominator * maximum) != 0
    assert int(polynomial.count_roots(1, 3)) == 1
    embedding = support_embedding(exponent, middle, maximum)
    embedding.update({'tail_gcd': gcd(middle, maximum), 'tail_quadratic_coefficients_descending': coefficients,
                      'four_direct_tail_determinants_at_c_zero_through_three': values,
                      'rational_tail_candidate': {'numerator': numerator, 'denominator': denominator, 'gcd': 1,
                                                  'floor': numerator // denominator, 'integer': False},
                      'quartic_coefficients_descending': [int(value) for value in polynomial.all_coeffs()],
                      'five_direct_integer_determinants_at_x_zero_through_four': determinants,
                      'exact_low_window_sturm_count': 1, 'boundary_c_equals_a': maximum == exponent})
    return embedding


def comparison_example(control):
    assert control['exponents'] == (6, 6, 55, 75)
    assert control['tail_gcd'] == 5
    assert 3 * 55 ** 2 * 75 ** 2 % 5 == 0 and 20 * 55 ** 2 * 75 ** 2 % 4 == 0
    assert 55 % 25 == 5 and 75 % 125 == 75
    assert (11 - 2 * 15 - 1) % 5 == 0 and (2 * 11 - 15 + 1) % 5 != 0
    assert (55 + 5) % 5 == 0 and (55 + 5) % 25 != 0
    variable = sympy.Symbol('x')
    for tail, roots in ((55, (3, -2)), (75, (4, 4))):
        assert sympy.Poly(variable ** 2 - variable - tail, variable, modulus=7) == sympy.Poly(
            (variable - roots[0]) * (variable - roots[1]), variable, modulus=7)
    assert control['rational_tail_candidate']['numerator'] == 26065
    assert control['rational_tail_candidate']['denominator'] == 271
    assert control['five_direct_integer_determinants_at_x_zero_through_four'][2:4] == [25830000, -1681145000]
    return {'exponents': control['exponents'], 'both_coarse_divisibilities_pass': True,
            'root_two_valuation_branch': 'e=r=1<t=2', 'simple_cubic_resonance_passes': True,
            'prior_double_resonance_discriminant_hypothesis': False,
            'modular_factors_at_only_prime7': ['(x-3)(x+2)', '(x-4)^2'],
            'new_global_obstruction': 'only positive root-two tail candidate26065/271is noninteger'}


def main():
    controls = [fixed_control(*fixture) for fixture in ((2, 2), (5, 5), (6, 75), (7, 125), (8, 157), (20, 865))]
    dependencies = ('check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py')
    report = {'written_theorem': 'Every positive four-prime vector(a,a,(a-1)(2a-1),c),a>=2,c>=a has a noninteger restricted root in(1,3)and hence noninteger graph spectrum. No tail ordering or coprimality hypothesis.',
              'symbolic': symbolic_checks(), 'fixed_controls': controls,
              'extra_coverage_example': comparison_example(controls[2]),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in dependencies},
              'sympy_version': sympy.__version__, 'requires_finite_base': False,
              'validation_counts': {'support_column_actions': 336, 'direct_integer_determinants': 54,
                                    'tail_quadratic_determinants': 24, 'control_quartic_determinants': 30,
                                    'exact_low_window_sturm_counts': 6},
              'scope': 'Written unbounded zero-constant family proved by integer Bezout8 identity,odd denominator and strict minor. Six specified support/determinant/Sturm controls include two c=a boundaries and tails on both sides of the rational candidate. No exponent scan,expanded graph,historical finite-base rerun,floating eigenvalues or Lean. Zero tail in polynomial identities is not a graph exponent. General other resonances,four-/higher-prime classification remain open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
