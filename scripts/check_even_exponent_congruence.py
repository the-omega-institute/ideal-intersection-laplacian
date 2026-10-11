import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, second, third, variable, shift = sympy.symbols('u v w x y')
odd_halves = (2 * first + 1, 2 * second + 1, 2 * third + 1)
exponents = tuple(2 * half for half in odd_halves)
complement = support_quotient(exponents, complement=True)
scaled = complement / 2
assert all(sympy.Poly(entry, first, second, third).domain == sympy.ZZ for entry in scaled)
scaled_quintic = sympy.Poly(sympy.cancel(scaled.charpoly(variable).as_expr() / variable), variable)
complement_quintic = sympy.Poly(sympy.cancel(complement.charpoly(variable).as_expr() / variable), variable)
assert sympy.expand(complement_quintic.as_expr() - 32 * scaled_quintic.as_expr().subs(variable, variable / 2)) == 0

binary_matrix = scaled.applyfunc(lambda entry: sympy.Poly(entry, first, second, third, modulus=2).as_expr())
expected_top = sympy.ones(3) - sympy.eye(3)
assert binary_matrix[:3, :3] == expected_top
assert binary_matrix[:3, 3:] == sympy.zeros(3)
assert binary_matrix[3:, 3:] == sympy.eye(3)
binary_characteristic = sympy.Poly(binary_matrix.charpoly(variable).as_expr(), variable, modulus=2)
assert binary_characteristic == sympy.Poly(variable * (variable + 1) ** 5, variable, modulus=2)
binary_remainder = sympy.Poly(sympy.expand(scaled_quintic.as_expr() - (variable + 1) ** 5), first, second, third, variable)
assert all(coefficient % 2 == 0 for coefficient in binary_remainder.coeffs())

shifted = sympy.expand(scaled_quintic.as_expr().subs(variable, 2 * shift + 1))
expected_residue = 8 * (first + second + third + shift - 1)
residue_remainder = sympy.Poly(sympy.expand(shifted - expected_residue), first, second, third, shift)
assert all(coefficient % 32 == 0 for coefficient in residue_remainder.coeffs())
difference = sympy.Poly(sympy.expand(scaled_quintic.eval(3) - scaled_quintic.eval(1) - 8), first, second, third)
assert all(coefficient % 32 == 0 for coefficient in difference.coeffs())


def integer_horner(coefficients, argument):
    value = 0
    for coefficient in coefficients:
        value = value * argument + int(coefficient)
    return value


fixtures = []
for triple in ((10, 14, 18), (14, 22, 34), (18, 26, 42)):
    direct_complement = support_quotient(triple, complement=True)
    direct_scaled = direct_complement / 2
    assert all(entry.is_Integer for entry in direct_scaled)
    direct_quintic = sympy.Poly(sympy.cancel(direct_scaled.charpoly(variable).as_expr() / variable), variable)
    substitution = dict(zip((first, second, third), ((exponent - 2) // 4 for exponent in triple)))
    assert direct_quintic == sympy.Poly(scaled_quintic.as_expr().subs(substitution), variable)
    values = [integer_horner(direct_quintic.all_coeffs(), argument) for argument in (1, 3)]
    assert values == [int(direct_quintic.eval(argument)) for argument in (1, 3)]
    assert (values[1] - values[0]) % 32 == 8
    assert any(value % 32 != 0 for value in values)
    assert sympy.Poly(direct_quintic.as_expr(), variable, modulus=2) == sympy.Poly((variable + 1) ** 5, variable, modulus=2)
    factors = direct_quintic.factor_list()[1]
    assert any(factor.degree() > 1 for factor, multiplicity in factors)
    minimum, middle, maximum = triple
    assert sympy.gcd_list(triple) == 2
    cutoff = sympy.Rational(7 * minimum ** 2 - 2 * minimum + 8, minimum + 2)
    assert maximum < cutoff and maximum < 4 * minimum ** 2 - 2 * minimum
    assert (minimum - 2) * (sum(triple) - 2) <= 2 * middle * maximum
    fixtures.append({'exponents': triple, 'scaled_quintic': str(direct_quintic.as_expr()),
                     'integer_horner_values_at_1_3': values,
                     'residues_modulo_32': [value % 32 for value in values],
                     'difference_modulo_32': 8,
                     'rational_factor_degrees': [factor.degree() for factor, multiplicity in factors],
                     'gcd': 2, 'inside_previous_even_linear_bound': True,
                     'outside_prior_balanced_region': True})

sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'written_theorem': 'Every positive three-prime triple with all exponents congruent2mod4 is nonintegral, regardless of ratios or minimum',
                  'written_corollary': 'Every triple whose exponents have the same2adic valuation is nonintegral: valuation0 uses prior all-odd proof, valuation1 the new theorem, valuation>=2 prior common-divisor proof',
                  'symbolic_integer_scaled_quotient': True,
                  'characteristic_scaling': 'h_C(x)=32*f(x/2)',
                  'binary_block_matrix': str(binary_matrix),
                  'binary_scaled_quintic': '(x+1)^5',
                  'modulo_two_coefficients_checked': len(binary_remainder.coeffs()),
                  'shifted_polynomial_congruence': 'f(2y+1)=8*(u+v+w+y-1) mod32 for exponents(4u+2,4v+2,4w+2)',
                  'modulo_32_coefficients_checked': len(residue_remainder.coeffs()),
                  'difference_congruence': 'f(3)-f(1)=8 mod32',
                  'direct_integer_quotient_fixtures': fixtures,
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
                  'scope': 'Written rational-root/parity/divisibility contradiction and valuation corollary. Exact symbolic integer scaling, binary block/characteristic and coefficientwise modulo2/modulo32 identities; three selected direct quotient/rational factor/integer Horner fixtures. No exponent scan, numerical spectrum or Lean. FullQ3 and mixed-valuation endpoint-zero cases remain open.'}, indent=2))
