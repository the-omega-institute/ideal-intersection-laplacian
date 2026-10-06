import hashlib
import json
from math import gcd
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def valuation(value, prime):
    assert value != 0
    value = abs(int(value))
    power = 0
    while value % prime == 0:
        power += 1
        value //= prime
    return power


def symbolic_checks():
    root, middle, maximum, difference, variable, normalized, first, second, excess = sympy.symbols('s b c h x z n m v')
    matrix = operator(root - 1 + difference, middle, maximum)
    expression = sympy.Matrix(matrix).charpoly(variable).as_expr().subs(variable, root)
    direct = integer_determinant([[(root if row == column else 0) - matrix[row][column]
                                  for column in range(4)] for row in range(4)])
    assert sympy.expand(expression - direct) == 0
    quadratic = sympy.Poly(expression, maximum)
    leading, linear, constant = quadratic.all_coeffs()
    discriminant = sympy.expand(linear ** 2 - 4 * leading * constant)
    assert sympy.expand(discriminant - sympy.discriminant(expression, maximum)) == 0
    local = (2 * root - 1) ** 2 * normalized ** 2 + 2 * root ** 2 * (2 * root - 1) ** 2 * normalized + root ** 4
    shifted = sympy.expand(discriminant.subs(middle, -difference + difference ** 2 * normalized))
    quotient = sympy.cancel((shifted - difference ** 6 * (root - 1) ** 2 * local) / difference ** 7)
    error = sympy.Poly(quotient, difference, normalized, root, domain=sympy.ZZ)
    assert sympy.expand(shifted - difference ** 6 * (root - 1) ** 2 * local - difference ** 7 * error.as_expr()) == 0
    exponent = 6 + 25 * first
    tail = 20 + 100 * first + 125 * second
    assert sympy.expand(exponent - 1 - 5 * (1 + 5 * first)) == 0
    assert sympy.expand(tail + exponent - 1 - 25 * (1 + 5 * first + 5 * second)) == 0
    assert sympy.expand(tail - (2 * exponent - 2) - (10 + 50 * first + 125 * second)) == 0
    generic_a, generic_b, generic_c = sympy.symbols('a B C')
    restriction = sympy.Matrix(operator(generic_a, generic_b, generic_c))
    minor = (restriction[0, 0] - 3) * (restriction[3, 3] - 3) - restriction[0, 3] * restriction[3, 0]
    written = -(generic_a + 2) * generic_b * generic_c + (generic_a + 1) * (generic_a - 2) * (generic_b + generic_c) + 2 * (generic_a - 1) * (generic_a - 2)
    assert sympy.expand(minor - written) == 0
    right = sympy.Symbol('w')
    negative = -(generic_a + 2) * excess * right - (generic_a ** 2 + 3 * generic_a - 2) * (excess + right) - 2 * (generic_a - 1) * (3 * generic_a + 2)
    assert sympy.expand(minor.subs({generic_b: 2 * generic_a - 2 + excess,
                                  generic_c: 2 * generic_a - 2 + right}) - negative) == 0
    return {'independent_symbolic_permutation_determinant': 'passed',
            'generic_discriminant_identity': 'Delta_c(s;s-1+h,-h+h^2z)=h^6(s-1)^2D_s(z)+h^7E_s(h,z)',
            'local_polynomial': str(local), 'integer_error_polynomial': str(error.as_expr()),
            'integer_error_polynomial_terms': len(error.terms()),
            'unbounded_family': 'a=6+25n,b=20+100n+125m,n,m>=0,c>=2a-2',
            'family_h_identity': 'h=a-1=5(1+5n)',
            'family_b_plus_h_identity': 'b+h=25(1+5n+5m)',
            'family_b_tail_cutoff_margin': 'b-(2a-2)=10+50n+125m',
            'strict_root_three_minor_at_cutoff': str(negative)}


def residue_table(endpoint, prime):
    rows = []
    squares = {value * value % prime for value in range(prime)}
    for normalized in range(prime):
        residue = ((2 * endpoint - 1) ** 2 * normalized ** 2
                   + 2 * endpoint ** 2 * (2 * endpoint - 1) ** 2 * normalized + endpoint ** 4) % prime
        symbol = int(sympy.legendre_symbol(residue, prime))
        assert (symbol >= 0) == (residue in squares)
        rows.append({'z': normalized, 'D_residue': residue, 'quadratic_character': symbol})
    excluded = [row['z'] for row in rows if row['quadratic_character'] == -1]
    assert excluded == ([1, 3, 4] if endpoint == 2 else [1, 2, 4, 6])
    return {'s': endpoint, 'prime': prime, 'complete_rows': rows, 'excluded_z': excluded}


def fixed_control(exponent, middle, maximum, endpoint, prime):
    assert exponent >= 5 and min(middle, maximum) >= 2 * exponent - 2
    difference = exponent + 1 - endpoint
    power = valuation(difference, prime)
    assert endpoint * (endpoint - 1) * (2 * endpoint - 1) % prime != 0
    assert (middle + difference) % prime ** (2 * power) == 0
    unit_h = difference // prime ** power
    normalized = ((middle + difference) // prime ** (2 * power)) * pow(unit_h ** 2, -1, prime) % prime
    local_residue = ((2 * endpoint - 1) ** 2 * normalized ** 2
                     + 2 * endpoint ** 2 * (2 * endpoint - 1) ** 2 * normalized + endpoint ** 4) % prime
    tail = sympy.Symbol('c')
    variable = sympy.Symbol('x')
    quadratic = sympy.Poly(sympy.Matrix(operator(exponent, middle, tail)).charpoly(variable).as_expr().subs(variable, endpoint), tail)
    values = []
    for argument in range(4):
        matrix = operator(exponent, middle, argument)
        values.append(integer_determinant([[endpoint * (row == column) - matrix[row][column]
                                           for column in range(4)] for row in range(4)]))
    second_difference = values[2] - 2 * values[1] + values[0]
    assert second_difference % 2 == 0
    leading = second_difference // 2
    coefficients = [leading, values[1] - values[0] - leading, values[0]]
    assert coefficients == [int(value) for value in quadratic.all_coeffs()]
    assert int(quadratic.eval(3)) == values[3]
    discriminant = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
    assert discriminant == int(sympy.discriminant(quadratic.as_expr(), tail))
    assert discriminant % prime ** (6 * power) == 0
    assert discriminant // prime ** (6 * power) % prime == (endpoint - 1) ** 2 * pow(unit_h, 6, prime) * local_residue % prime
    character = int(sympy.legendre_symbol(local_residue, prime))
    if character == -1:
        assert valuation(discriminant, prime) == 6 * power
    matrix = operator(exponent, middle, maximum)
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    determinants = [integer_determinant([[argument * (row == column) - matrix[row][column]
                                         for column in range(4)] for row in range(4)])
                    for argument in range(5)]
    assert sympy.Poly(sympy.interpolate(list(enumerate(determinants)), variable), variable) == polynomial
    assert int(polynomial.count_roots(1, 3)) == 1
    in_family = (exponent >= 6 and (exponent - 6) % 25 == 0
                 and middle >= 20 + 4 * (exponent - 6) and (middle - 20 - 4 * (exponent - 6)) % 125 == 0)
    embedding = support_embedding(exponent, middle, maximum)
    embedding.update({'tail_gcd': gcd(middle, maximum), 'endpoint': endpoint, 'good_prime': prime,
                      'h_valuation': power, 'normalized_z_mod_prime': normalized,
                      'D_residue': local_residue, 'quadratic_character': character,
                      'endpoint_excluded_by_new_discriminant': character == -1,
                      'tail_quadratic_coefficients_descending': coefficients,
                      'four_direct_tail_determinants_at_c_zero_through_three': values,
                      'tail_discriminant': discriminant,
                      'tail_discriminant_divided_by_prime_to_6e_residue': discriminant // prime ** (6 * power) % prime,
                      'five_direct_integer_determinants_at_x_zero_through_four': determinants,
                      'quartic_coefficients_descending': [int(value) for value in polynomial.all_coeffs()],
                      'exact_low_window_sturm_count': 1, 'in_new_family': in_family})
    return embedding


def comparison_example(control):
    assert control['exponents'] == (6, 6, 145, 20)
    assert control['tail_gcd'] == 5
    assert 3 * 145 ** 2 * 20 ** 2 % 5 == 0 and 20 * 145 ** 2 * 20 ** 2 % 4 == 0
    assert valuation(145, 5) == valuation(20, 5) == 1
    scaled_h, scaled_b, scaled_c = 1, 29, 4
    assert (scaled_b - 2 * scaled_c - scaled_h) % 5 == 0
    assert (2 * scaled_b - scaled_c + scaled_h) % 5 == 0
    variable = sympy.Symbol('x')
    for tail, roots in ((145, (4, 4)), (20, (3, -2))):
        assert sympy.Poly(variable ** 2 - variable - tail, variable, modulus=7) == sympy.Poly(
            (variable - roots[0]) * (variable - roots[1]), variable, modulus=7)
    assert control['tail_quadratic_coefficients_descending'] == [-212460, 9600900, -459000]
    assert control['five_direct_integer_determinants_at_x_zero_through_four'][2:4] == [106575000, -801589680]
    return {'exponents': control['exponents'], 'both_coarse_divisibilities_pass': True,
            'all_available_good_prime_valuation_ranges_pass': True,
            'root_two_both_cubic_resonance_factors_vanish_mod5': True,
            'modular_factors_at_only_prime7': ['(x-4)^2', '(x-3)(x+2)'],
            'new_obstruction': 'Delta_c(p(2))/5^6=2mod5 is nonsquare',
            'root_three_excluded_by_prior_cutoff_minor': True}


def main():
    symbolic = symbolic_checks()
    fixtures = ((6, 145, 20, 2, 5), (6, 520, 70, 2, 5), (31, 120, 60, 2, 5),
                (56, 220, 110, 2, 5), (9, 42, 91, 3, 7), (6, 45, 20, 2, 5))
    controls = [fixed_control(*fixture) for fixture in fixtures]
    assert [control['in_new_family'] for control in controls] == [True, True, True, True, False, False]
    assert [control['endpoint_excluded_by_new_discriminant'] for control in controls] == [True, True, True, True, True, False]
    dependencies = ('check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py')
    report = {'written_theorem': 'For integer root s>=2,h=a+1-s and good prime ell|h,if v_ell(b+h)>=2v_ell(h),the rational z=(b+h)/h^2 is ell-integral and D_s(z) must be a square or zero modulo ell,where D_s=(2s-1)^2z^2+2s^2(2s-1)^2z+s^4. No tail coprimality assumption.',
              'written_nonintegrality_family': 'Every positive(a,a,b,c)with a=6+25n,b=20+100n+125m,n,m>=0,c>=2a-2 is nonintegral. No ordering between b,c.',
              'symbolic': symbolic, 'complete_local_residue_tables': [residue_table(2, 5), residue_table(3, 7)],
              'fixed_controls': controls, 'extra_coverage_example': comparison_example(controls[0]),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in dependencies},
              'sympy_version': sympy.__version__, 'requires_finite_base': False,
              'validation_counts': {'support_column_actions': 336, 'direct_integer_determinants': 54,
                                    'tail_quadratic_determinants': 24, 'control_quartic_determinants': 30,
                                    'exact_low_window_sturm_counts': 6},
              'scope': 'Written unbounded resonant discriminant obstruction and three-parameter nonintegrality family. Two complete local residue tables and six specified symbolic/support/determinant/Sturm controls,including a passing discriminant test. The criterion is necessary only. No parameter scan,expanded graph,historical finite-base rerun,floating eigenvalues or Lean. Remaining resonances,bad primes and general four-/higher-prime classification stay open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
