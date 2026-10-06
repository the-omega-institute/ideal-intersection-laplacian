import hashlib
import json
from math import isqrt
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def sylvester_matrix(polynomial, variable):
    coefficients = sympy.Poly(polynomial, variable).all_coeffs()
    derivative = sympy.Poly(sympy.diff(polynomial, variable), variable).all_coeffs()
    size = len(coefficients) + len(derivative) - 2
    rows = []
    for shift in range(len(derivative) - 1):
        rows.append([0] * shift + coefficients + [0] * (size - shift - len(coefficients)))
    for shift in range(len(coefficients) - 1):
        rows.append([0] * shift + derivative + [0] * (size - shift - len(derivative)))
    return rows


def symbolic_checks():
    exponent, middle, maximum, variable, growth, excess, other_excess = sympy.symbols('a b c x v u w')
    matrix = operator(exponent, middle, maximum)
    characteristic = sympy.Matrix(matrix).charpoly(variable).as_expr()
    direct = integer_determinant([[(variable if row == column else 0) - matrix[row][column]
                                  for column in range(4)] for row in range(4)])
    assert sympy.expand(characteristic - direct) == 0
    endpoint = sympy.expand(characteristic.subs(variable, 2))
    leading = -(2 * exponent + 1) * middle ** 2 + 2 * exponent * (exponent ** 2 - 1) * middle - (exponent ** 2 - 1)
    linear = (exponent - 1) * (2 * exponent * (exponent + 1) * middle ** 2
                              + (4 * exponent ** 3 + 6 * exponent ** 2 - 3 * exponent - 2) * middle
                              + (exponent - 1) * (2 * exponent ** 2 + exponent - 2))
    constant = (exponent - 1) * ((exponent - 1) * (2 * exponent - 1) - middle) * ((exponent + 1) * middle + exponent - 1)
    assert sympy.expand(endpoint - leading * maximum ** 2 - linear * maximum - constant) == 0
    discriminant = sympy.expand(linear ** 2 - 4 * leading * constant)
    written_coefficients = [
        4 * (exponent - 1) * (exponent + 1) * (exponent ** 2 - exponent - 1) * (exponent ** 2 + exponent + 1),
        4 * (exponent - 1) ** 2 * (exponent ** 2 + exponent + 1) * (4 * exponent ** 3 + 6 * exponent ** 2 - exponent - 2),
        (exponent - 1) ** 2 * (16 * exponent ** 6 + 40 * exponent ** 5 + 8 * exponent ** 4 - 20 * exponent ** 3 - 31 * exponent ** 2 - 8 * exponent + 4),
        2 * exponent * (exponent - 1) ** 3 * (2 * exponent + 1) * (4 * exponent ** 3 + 2 * exponent ** 2 - exponent - 2),
        exponent ** 2 * (exponent - 1) ** 4 * (2 * exponent + 1) ** 2]
    quartic = sympy.Poly(discriminant, middle)
    assert quartic.degree() == 4
    assert all(sympy.expand(actual - written) == 0 for actual, written in zip(quartic.all_coeffs(), written_coefficients))
    fourth, third, second, first, zeroth = written_coefficients
    invariant_first = 12 * fourth * zeroth - 3 * third * first + second ** 2
    invariant_second = 72 * fourth * second * zeroth + 9 * third * second * first - 27 * fourth * first ** 2 - 27 * third ** 2 * zeroth - 2 * second ** 3
    positive = (64 * exponent ** 9 + 128 * exponent ** 8 + 48 * exponent ** 7 - 192 * exponent ** 6
                - 196 * exponent ** 5 - 44 * exponent ** 4 + 119 * exponent ** 3 + 58 * exponent ** 2 + 4 * exponent + 8)
    expected_discriminant = (-4096 * exponent ** 8 * (exponent - 1) ** 15 * (exponent + 1) ** 2
                             * (2 * exponent + 1) ** 6 * (exponent ** 2 + exponent + 1) ** 2 * positive)
    actual_discriminant = sympy.discriminant(discriminant, middle)
    assert sympy.expand(actual_discriminant - expected_discriminant) == 0
    assert sympy.expand((4 * invariant_first ** 3 - invariant_second ** 2) / 27 - expected_discriminant) == 0
    positive_coefficients = [int(value) for value in sympy.Poly(sympy.expand(positive.subs(exponent, growth + 2)), growth).all_coeffs()]
    assert positive_coefficients == [64, 1280, 11312, 57824, 187900, 401324, 561527, 494500, 247744, 53616]
    assert all(value > 0 for value in positive_coefficients)
    assert sympy.expand((2 * leading * maximum + linear) ** 2 - discriminant - 4 * leading * endpoint) == 0
    special_tail = (exponent - 1) * (2 * exponent - 1)
    numerator = (exponent - 1) * (2 * exponent + 1) * (2 * exponent ** 3 - exponent ** 2 + exponent - 1)
    base_height = 2 * exponent * (exponent - 1) * numerator
    assert sympy.expand(linear.subs(middle, special_tail) - base_height) == 0
    assert sympy.expand(discriminant.subs(middle, special_tail) - base_height ** 2) == 0
    third_linear = (exponent - 2) * ((exponent ** 2 - 1) * middle ** 2
                                   + (4 * exponent ** 3 + 3 * exponent ** 2 - 8 * exponent - 2) * middle
                                   + (exponent - 2) * (2 * exponent ** 2 - exponent - 4))
    assert sympy.expand(sympy.Poly(characteristic.subs(variable, 3), maximum).coeff_monomial(maximum) - third_linear) == 0
    for polynomial, minimum in ((linear, 2), (third_linear, 3)):
        coefficients = sympy.Poly(sympy.expand(polynomial.subs({exponent: growth + minimum, middle: excess + 1})), growth, excess).coeffs()
        assert all(value > 0 for value in coefficients)
    minor_third = (matrix[0][0] - 3) * (matrix[3][3] - 3) - matrix[0][3] * matrix[3][0]
    cutoff_third = -(exponent + 2) * excess * other_excess - (exponent ** 2 + 3 * exponent - 2) * (excess + other_excess) - 2 * (exponent - 1) * (3 * exponent + 2)
    assert sympy.expand(minor_third.subs({middle: 2 * exponent - 2 + excess, maximum: 2 * exponent - 2 + other_excess}) - cutoff_third) == 0
    minor_fourth = (matrix[0][0] - 4) * (matrix[3][3] - 4) - matrix[0][3] * matrix[3][0]
    cutoff_fourth = -(2 * exponent + 3) * excess * other_excess - (exponent ** 2 + 5 * exponent + 3) * (excess + other_excess) - 5 * exponent ** 2 - 15 * exponent + 9
    assert sympy.expand(minor_fourth.subs({middle: exponent + excess, maximum: exponent + other_excess}) - cutoff_fourth) == 0
    sixth_quartic = 8729 * middle ** 4 + 230480 * middle ** 3 + 1328030 * middle ** 2 + 904800 * middle + 190125
    assert sympy.expand(discriminant.subs(exponent, 6) - 20 * sixth_quartic) == 0
    assert int(sixth_quartic.subs(middle, 55)) == 5 * 156390 ** 2
    return {'independent_symbolic_permutation_determinant': 'passed',
            'endpoint_two_coefficients_descending': [str(value) for value in (leading, linear, constant)],
            'tail_discriminant_quartic_coefficients_descending': [str(value) for value in written_coefficients],
            'quartic_discriminant_factorization': str(expected_discriminant),
            'positive_factor_H': str(positive), 'H_after_a_v_plus_two_coefficients_descending': positive_coefficients,
            'binary_quartic_invariant_identity': 'disc=(4I^3-J^2)/27; I=12LT-3MR+Q^2; J=72LQT+9MQR-27LR^2-27M^2T-2Q^3',
            'inverse_identity': '(2Ac+B)^2-F=4A*p(2)',
            'rational_base_point': {'b': str(special_tail), 'y': str(base_height), 'original_tail_c': 0},
            'endpoint_three_linear_coefficient': str(third_linear),
            'endpoint_two_and_three_positive_linear_terms': 'checked by complete positive expansions at a>=2 and a>=3,b>=1',
            'prior_cutoff_minors_verified': True, 'strip_b_count': 'a-2', 'strip_candidate_bound': '4(a-2)',
            'a6_integral_model': '5z^2=8729b^4+230480b^3+1328030b^2+904800b+190125',
            'a6_base_point_b_z': [55, 156390]}, discriminant, expected_discriminant


def fixed_control(exponent, middle, maximum, discriminant, expected_discriminant):
    tail = sympy.Symbol('c')
    variable = sympy.Symbol('x')
    symbolic_exponent, symbolic_middle = sympy.symbols('a b')
    matrix = operator(exponent, middle, maximum)
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    determinants = [integer_determinant([[argument * (row == column) - matrix[row][column]
                                         for column in range(4)] for row in range(4)]) for argument in range(5)]
    assert sympy.Poly(sympy.interpolate(list(enumerate(determinants)), variable), variable) == polynomial
    tail_values = []
    for argument in range(4):
        tail_matrix = operator(exponent, middle, argument)
        tail_values.append(integer_determinant([[2 * (row == column) - tail_matrix[row][column]
                                                for column in range(4)] for row in range(4)]))
    difference = tail_values[2] - 2 * tail_values[1] + tail_values[0]
    assert difference % 2 == 0
    leading = difference // 2
    coefficients = [leading, tail_values[1] - tail_values[0] - leading, tail_values[0]]
    quadratic = sympy.Poly(sympy.Matrix(operator(exponent, middle, tail)).charpoly(variable).as_expr().subs(variable, 2), tail)
    assert coefficients == [int(value) for value in quadratic.all_coeffs()]
    assert int(quadratic.eval(3)) == tail_values[3]
    tail_discriminant = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
    assert tail_discriminant == int(discriminant.subs({symbolic_exponent: exponent, symbolic_middle: middle}))
    height = 2 * coefficients[0] * maximum + coefficients[1]
    assert height ** 2 - tail_discriminant == 4 * coefficients[0] * determinants[2]
    specialized = discriminant.subs(symbolic_exponent, exponent)
    sylvester = sylvester_matrix(specialized, symbolic_middle)
    resultant = integer_determinant([[int(entry) for entry in row] for row in sylvester])
    leading_quartic = int(sympy.Poly(specialized, symbolic_middle).LC())
    assert resultant == leading_quartic * int(expected_discriminant.subs(symbolic_exponent, exponent))
    assert resultant != 0 and int(polynomial.count_roots(1, 4)) == 1
    control = support_embedding(exponent, middle, maximum)
    control.update({'four_tail_determinants_at_c_zero_through_three': tail_values,
                    'tail_quadratic_coefficients_descending': coefficients, 'tail_discriminant': tail_discriminant,
                    'height_y': height, 'inverse_identity_verified': True,
                    'five_quartic_determinants_at_x_zero_through_four': determinants,
                    'quartic_coefficients_descending': [int(value) for value in polynomial.all_coeffs()],
                    'integer_sylvester_resultant': resultant, 'nonzero_quartic_discriminant': resultant // leading_quartic,
                    'exact_sturm_count_in_one_four': 1})
    return control


def comparison_example(control):
    assert control['exponents'] == (6, 6, 105, 75)
    assert 3 * 105 ** 2 * 75 ** 2 % 5 == 0 and 20 * 105 ** 2 * 75 ** 2 % 4 == 0
    assert 105 % 25 == 5 and 75 % 125 == 75
    assert (21 - 2 * 15 - 1) % 5 == 0 and (2 * 21 - 15 + 1) % 5 != 0
    assert 110 % 5 == 0 and 110 % 25 != 0
    variable = sympy.Symbol('x')
    for tail, roots in ((105, (0, 1)), (75, (4, 4))):
        assert sympy.Poly(variable ** 2 - variable - tail, variable, modulus=7) == sympy.Poly(
            (variable - roots[0]) * (variable - roots[1]), variable, modulus=7)
    assert control['tail_quadratic_coefficients_descending'] == [-99260, 5188900, -185000]
    delta = control['tail_discriminant']
    floor = isqrt(delta)
    assert delta == 26851230810000 and floor == 5181817
    assert floor ** 2 < delta < (floor + 1) ** 2
    assert control['five_quartic_determinants_at_x_zero_through_four'][2:4] == [-169355000, -6225682400]
    return {'exponents': control['exponents'], 'both_coarse_divisibilities_pass': True,
            'root_two_valuation_branch': 'e=r=1<t=2', 'simple_cubic_resonance_passes': True,
            'prior_double_resonance_hypothesis': False,
            'modular_factors_at_only_prime7': ['x(x-1)', '(x-4)^2'],
            'tail_discriminant': delta, 'square_root_floor': floor,
            'all_integer_tails_excluded_at_fixed_a_b': True,
            'comparison_scope': 'named local tests only; not every previous sufficient spectral region'}


def main():
    symbolic, discriminant, expected_discriminant = symbolic_checks()
    controls = [fixed_control(*fixture, discriminant, expected_discriminant)
                for fixture in ((2, 2, 2), (5, 5, 5), (6, 105, 75))]
    dependencies = ('check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py')
    report = {'written_theorem': 'For every fixed integer a>=2, p(2;a,b,c)=0 has finitely many positive integer tail pairs; its normalization is a geometrically irreducible genus-one curve with a rational point.',
              'graph_corollary': 'For each fixed a>=5, only finitely many b,c>=a can give integer Laplacian spectrum for (a,a,b,c). No effective bound or list is supplied.',
              'symbolic': symbolic, 'fixed_controls': controls, 'comparison_example': comparison_example(controls[2]),
              'classical_theorems_used': ['Riemann-Hurwitz for a degree-two cover with four simple branch points', 'Siegel finiteness of integral points on an affine curve of positive genus'],
              'classical_theorems_formally_verified': False, 'effective_integral_point_enumeration': False,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in dependencies},
              'sympy_version': sympy.__version__, 'requires_finite_exponent_base': False,
              'validation_counts': {'support_column_actions': 168, 'tail_matrix_determinants': 12,
                                    'quartic_matrix_determinants': 15, 'integer_sylvester_determinants': 3,
                                    'total_exact_determinants': 30, 'exact_sturm_counts_in_one_four': 3},
              'scope': 'Written geometric and fixed-minimum finiteness deductions from generic exact identities plus classical Riemann-Hurwitz and Siegel theorems. Three specified implementation controls. No elliptic rank, effective bound, integral-point list or emptiness assertion; integer root two is necessary only for the large-tail spectral region. No scan, expanded graph, historical finite-base rerun, floats or Lean. All previous results and joint manuscript decisions retain their scopes.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
