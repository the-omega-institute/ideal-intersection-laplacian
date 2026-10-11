import hashlib
import json
from itertools import product
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, second, third, scale = sympy.symbols('a b c d', positive=True)
variable = sympy.Symbol('x')
exponents = (first, second, third)
quotient = support_quotient(exponents, complement=True)
scaled_quotient = quotient.subs(dict(zip(exponents, (scale * first, scale * second, scale * third)))) / scale
for entry in scaled_quotient:
    assert sympy.Poly(sympy.expand(entry), first, second, third, scale).domain == sympy.ZZ
quintic = sympy.Poly(sympy.cancel(quotient.charpoly(variable).as_expr() / variable), variable)
equal_factor = ((variable - first ** 2 - first)
                * (variable ** 2 - (first ** 2 + 4 * first) * variable + 3 * first ** 2) ** 2)
assert sympy.expand(quintic.as_expr().subs({second: first, third: first}) - equal_factor) == 0
quadratic = sympy.Poly(variable ** 2 - (first ** 2 + 4 * first) * variable + 3 * first ** 2, variable)
assert sympy.expand(quadratic.discriminant() - first ** 2 * (first ** 2 + 8 * first + 4)) == 0

parity_rows = []
for residues in product(range(2), repeat=3):
    representatives = tuple(residue or 2 for residue in residues)
    direct = support_quotient(representatives, complement=True)
    polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable, modulus=2)
    specialized = sympy.Poly(quintic.as_expr().subs(dict(zip(exponents, residues))), variable, modulus=2)
    assert polynomial == specialized
    odd_count = sum(residues)
    expected = {0: variable ** 5, 1: variable ** 2 * (variable + 1) ** 3,
                2: variable ** 2 * (variable + 1) ** 3,
                3: variable * (variable ** 2 + variable + 1) ** 2}[odd_count]
    assert polynomial == sympy.Poly(expected, variable, modulus=2)
    factors = polynomial.factor_list()[1]
    nonlinear = any(factor.degree() > 1 for factor, multiplicity in factors)
    assert nonlinear == (odd_count == 3)
    parity_rows.append({'residues': residues, 'quintic_modulo_two': str(polynomial.as_expr()),
                        'nonlinear_irreducible_factor': nonlinear})
binary_quadratic_values = [(argument ** 2 + argument + 1) % 2 for argument in range(2)]
assert binary_quadratic_values == [1, 1]

prime_rows = []
for prime in (3, 5, 7):
    squares = {argument ** 2 % prime for argument in range(prime)}
    for residue in range(1, prime):
        direct = support_quotient((residue, residue, residue), complement=True)
        polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable, modulus=prime)
        specialized = sympy.Poly(equal_factor.subs(first, residue), variable, modulus=prime)
        assert polynomial == specialized
        reduced_quadratic = sympy.Poly(quadratic.as_expr().subs(first, residue), variable, modulus=prime)
        discriminant_factor = (residue ** 2 + 8 * residue + 4) % prime
        root_values = []
        coefficients = [int(coefficient) for coefficient in reduced_quadratic.all_coeffs()]
        for argument in range(prime):
            value = 0
            for coefficient in coefficients:
                value = (value * argument + coefficient) % prime
            assert value == int(reduced_quadratic.eval(argument)) % prime
            root_values.append(value)
        irreducible = discriminant_factor not in squares
        assert irreducible == all(root_values)
        assert irreducible == reduced_quadratic.is_irreducible
        assert any(factor.degree() > 1 for factor, multiplicity in polynomial.factor_list()[1]) == irreducible
        prime_rows.append({'prime': prime, 'common_nonzero_residue': residue,
                           'discriminant_factor': discriminant_factor,
                           'quadratic': str(reduced_quadratic.as_expr()),
                           'all_residue_values': root_values,
                           'irreducible': irreducible})
assert [row['common_nonzero_residue'] for row in prime_rows if row['prime'] == 5 and row['irreducible']] == [1, 3, 4]
assert [row['common_nonzero_residue'] for row in prime_rows if row['prime'] == 7 and row['irreducible']] == [1, 2, 4, 5]

fixture_rows = []
fixtures = [((8, 16, 24), 'common_divisor'), ((12, 24, 60), 'common_divisor'),
            ((9, 11, 13), 'all_odd'), ((11, 16, 21), 'residue_one_mod5'),
            ((13, 18, 23), 'residue_three_mod5'), ((14, 19, 24), 'residue_four_mod5')]
for triple, reason in fixtures:
    matrix = support_quotient(triple, complement=True)
    polynomial = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    if reason == 'common_divisor':
        divisor = sympy.gcd_list(triple)
        assert divisor >= 3
        divided = matrix / divisor
        assert all(entry.is_Integer for entry in divided)
        divided_polynomial = sympy.Poly(sympy.cancel(divided.charpoly(variable).as_expr() / variable), variable)
        assert sympy.expand(polynomial.as_expr() - divisor ** 5 * divided_polynomial.as_expr().subs(variable, variable / divisor)) == 0
        assert polynomial.eval(0) != 0 and polynomial.eval(3) != 0
        assert polynomial.count_roots(0, 3) >= 1
        assert polynomial.eval(1) != 0 and polynomial.eval(2) != 0
        evidence = {'common_divisor': int(divisor), 'positive_roots_below_three': int(polynomial.count_roots(0, 3)),
                    'scaled_integer_matrix_and_characteristic_identity': 'passed'}
    else:
        prime = 2 if reason == 'all_odd' else 5
        reduction = sympy.Poly(polynomial.as_expr(), variable, modulus=prime)
        assert any(factor.degree() > 1 for factor, multiplicity in reduction.factor_list()[1])
        evidence = {'prime': prime, 'reduced_quintic': str(reduction.as_expr()),
                    'nonlinear_irreducible_factor': True}
    fixture_rows.append({'exponents': triple, 'reason': reason, 'evidence': evidence})

boundary = support_quotient((9, 9, 136), complement=True)
boundary_polynomial = sympy.Poly(sympy.cancel(boundary.charpoly(variable).as_expr() / variable), variable)
assert boundary_polynomial.eval(1) == 0
assert any(factor.degree() > 1 for factor, multiplicity in boundary_polynomial.factor_list()[1])

source_paths = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
modular_evaluations = 2 + sum(row['prime'] for row in prime_rows)
assert modular_evaluations == 70
print(json.dumps({'symbolic_integer_scaled_quotient': 'passed',
                  'equal_exponent_factorization': str(equal_factor),
                  'quadratic_discriminant': 'a^2*(a^2+8a+4)',
                  'common_divisor_theorem': 'Every positive triple with gcd(a,b,c)>=3 is nonintegral, using the written uniform low-root bound and rational-root theorem; minimum3 uses the prior theorem',
                  'all_odd_theorem': 'h_C(x) mod2 = x*(x^2+x+1)^2, so all odd triples are nonintegral',
                  'general_prime_theorem': 'For odd primep and common nonzero residuer, r^2+8r+4 nonsquare modp implies nonintegrality',
                  'parity_table': parity_rows, 'binary_quadratic_root_values': binary_quadratic_values,
                  'common_residue_checks': prime_rows,
                  'modular_root_values_checked': modular_evaluations,
                  'direct_quotient_fixtures': fixture_rows,
                  'endpoint_zero_example': {'exponents': [9, 9, 136], 'h_C_at_one': 0,
                                            'other_nonlinear_rational_factor': True,
                                            'scope': 'Existing Reza boundary family, not a new family; confirms the necessary endpoint condition is not sufficient'},
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in source_paths},
                  'scope': 'Written common-divisor and congruence-class proofs. Exact symbolic integer-scaling/equal-factor/discriminant identities, complete8parity table, complete nonzero common residues for primes3,5,7 with all70quadratic residue evaluations including the binary factor, six selected direct quotient fixtures and one existing endpoint-zero boundary example. No exponent scan, numerical spectrum or Lean. FullQ3 remains open.'}, indent=2))
