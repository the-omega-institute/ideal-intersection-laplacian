import hashlib
from itertools import permutations
import json
from pathlib import Path

import sympy

from check_higher_derivatives import a, b, c, x, build_h_C_derivatives
from check_six_support_quotient import support_quotient


exponents = (a, b, c)
left_shift, middle_shift, right_shift, argument = sympy.symbols('u v w y')
shifts = (left_shift, middle_shift, right_shift)
quintic = sympy.Poly(sympy.cancel(
    support_quotient(exponents, complement=True).charpoly(x).as_expr() / x), x)
assert sympy.expand(quintic.as_expr() - build_h_C_derivatives(0)[0]) == 0
for ordering in permutations(exponents):
    assert sympy.expand(quintic.as_expr().subs(dict(zip(exponents, ordering)), simultaneous=True)
                        - quintic.as_expr()) == 0

identities = []
for residues in ((3, 0, 0), (1, 3, 2), (3, 3, 0)):
    substitution = dict(zip(exponents, (4 * shift + residue
                                       for shift, residue in zip(shifts, residues))))
    specialized = sympy.expand(quintic.as_expr().subs(substitution, simultaneous=True))
    binary_difference = sympy.Poly(specialized - x ** 2 * (x + 1) ** 3,
                                   *shifts, x, domain=sympy.ZZ)
    assert all(int(value) % 2 == 0 for value in binary_difference.coeffs())
    shifted = sympy.Poly(sympy.expand(specialized.subs(x, 2 * argument + 1)),
                         *shifts, argument, domain=sympy.ZZ)
    assert all(int(value) % 8 == 0 for value in shifted.coeffs())
    difference = sympy.Poly(sympy.expand(shifted.as_expr() / 8 - (argument + 1) ** 3),
                            *shifts, argument, domain=sympy.ZZ)
    assert all(int(value) % 2 == 0 for value in difference.coeffs())
    row = {'residue_roles_modulo_four': residues,
           'binary_quintic_difference_coefficients': len(binary_difference.terms()),
           'integer_shift_divisibility_coefficients': len(shifted.terms()),
           'shifted_binary_identity': '(y+1)^3',
           'shifted_binary_difference_coefficients': len(difference.terms())}
    if residues == (3, 0, 0):
        endpoint = sympy.Poly(specialized.subs(x, 2) - 4, *shifts, domain=sympy.ZZ)
        assert all(int(value) % 8 == 0 for value in endpoint.coeffs())
        row['endpoint_two_modulo_eight'] = 4
        row['endpoint_difference_coefficients'] = len(endpoint.terms())
    identities.append(row)


def independent_matrix(triple):
    left, middle, right = triple
    return [
        [middle + right + middle * right, -middle, -right, 0, 0, -middle * right],
        [-left, left + right + left * right, -right, 0, -left * right, 0],
        [-left, -middle, left + middle + left * middle, -left * middle, 0, 0],
        [0, 0, -right, right, 0, 0],
        [0, -middle, 0, 0, middle, 0],
        [-left, 0, 0, 0, 0, left],
    ]


def integer_determinant(matrix):
    total = 0
    size = len(matrix)
    for ordering in permutations(range(size)):
        inversions = sum(ordering[left_index] > ordering[right_index]
                         for left_index in range(size) for right_index in range(left_index + 1, size))
        term = (-1) ** inversions
        for row, column in enumerate(ordering):
            term *= matrix[row][column]
        total += term
    return total


fixtures = []
for triple, kind in (((19, 36, 100), 'complete_class'), ((35, 52, 120), 'complete_class'),
                    ((3, 4, 8), 'small_minimum_already_proved'),
                    ((25, 27, 758), 'mixed_linear_tail'), ((29, 27, 882), 'mixed_linear_tail'),
                    ((19, 27, 140), 'mixed_linear_tail'),
                    ((9, 9, 136), 'endpoint_one_control'), ((10, 10, 12), 'endpoint_two_control')):
    matrix = independent_matrix(triple)
    assert sympy.Matrix(matrix) == support_quotient(triple, complement=True)
    assert integer_determinant(matrix) == 0
    values = []
    for endpoint in range(1, 7):
        determinant = integer_determinant([[endpoint * int(row == column) - matrix[row][column]
                                           for column in range(6)] for row in range(6)])
        assert determinant % endpoint == 0
        values.append((endpoint, determinant // endpoint))
    independent = sympy.Poly(sympy.interpolate(values, x), x, domain=sympy.ZZ)
    assert independent == sympy.Poly(quintic.as_expr().subs(dict(zip(exponents, triple))), x)
    minimum, middle, maximum = sorted(triple)
    cutoff = sympy.Rational(7 * minimum ** 2 - 2 * minimum + 8, minimum + 2)
    if kind == 'complete_class' or kind == 'small_minimum_already_proved':
        assert independent.eval(2) % 8 == 4
        assert sorted(value % 4 for value in triple) == [0, 0, 3]
    if kind == 'mixed_linear_tail':
        assert minimum >= 4 and maximum >= cutoff and independent.eval(2) > 0
    if kind == 'endpoint_one_control':
        assert independent.eval(1) == 0
    if kind == 'endpoint_two_control':
        assert independent.eval(2) == 0 and maximum < cutoff
    assert independent.eval(0) != 0 and independent.eval(3) != 0
    if minimum >= 4:
        assert independent.count_roots(0, 3) >= 1
    assert any(factor.degree() > 1 for factor, multiplicity in independent.factor_list()[1])
    row = {'exponents': triple, 'kind': kind,
           'independent_coefficients': [int(value) for value in independent.all_coeffs()],
           'integer_determinant_interpolation_points': values,
           'h_at_one': int(independent.eval(1)), 'h_at_two': int(independent.eval(2)),
           'positive_roots_in_open_interval_zero_three': int(independent.count_roots(0, 3)),
           'ordered_minimum': minimum, 'ordered_maximum': maximum,
           'linear_cutoff': str(cutoff), 'nonlinear_rational_factor': True}
    if triple in ((25, 27, 758), (29, 27, 882)):
        left, odd_exponent, even_exponent = triple
        left_parameter = (left - 1) // 4
        total_parameter = (left + even_exponent - odd_exponent * (odd_exponent + 2)) // 128
        assert (left + even_exponent - odd_exponent * (odd_exponent + 2)) % 128 == 0
        odd_parameter = (odd_exponent - 11) // 16
        assert odd_exponent % 16 == 11
        assert (total_parameter + left_parameter + odd_parameter) % 2 == 1
        row['passes_all_previous_clustered_root_conditions'] = True
    fixtures.append(row)

print(json.dumps({
    'base_commit': '51ca2e372ba1d51b30142c388a65920bb5b3d72e',
    'written_results': [
        'Every positive permutation of (3,0,0)mod4 is nonintegral, with no size or ratio bound.',
        'For residue patterns (1,3,2) or (3,3,0)mod4, all permutations, an integral spectrum with minimum m>=4 requires maximum M<7m-16+40/(m+2).'],
    'generic_direct_reflected_quintic_and_six_symmetry_checks': 'passed',
    'coefficientwise_identities': identities,
    'fixtures': fixtures,
    'independent_six_by_six_integer_determinants': 56,
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy': sympy.__version__,
    'scope': 'Written infinite-family results combine shifted integer-root distributions with the proved uniform low root and linear endpoint-two bound. Three arbitrary-shift polynomial identities and one endpoint congruence are checked coefficientwise; eight independently reconstructed quintics and exact Sturm counts check selected fixtures. No exponent or modulus range scan, floating spectrum or Lean. Full Q3 and nonsquarefree higher-prime vectors remain open.'
}, indent=2))
