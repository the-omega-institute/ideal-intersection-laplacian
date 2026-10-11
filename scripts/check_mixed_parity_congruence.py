import hashlib
from itertools import combinations_with_replacement, permutations
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


first, second, third, variable = sympy.symbols('a b c x')
left_shift, right_shift, even_shift, argument = sympy.symbols('u v w y')
exponents = (first, second, third)
quotient = support_quotient(exponents, complement=True)
quintic = sympy.Poly(sympy.cancel(quotient.charpoly(variable).as_expr() / variable), variable)


def integer_horner(coefficients, value):
    result = 0
    for coefficient in coefficients:
        result = result * value + int(coefficient)
    return result


def independent_endpoint(triple, value):
    left, right, even = triple
    matrix = [
        [right + even + right * even, -right, -even, 0, 0, -right * even],
        [-left, left + even + left * even, -even, 0, -left * even, 0],
        [-left, -right, left + right + left * right, -left * right, 0, 0],
        [0, 0, -even, even, 0, 0],
        [0, -right, 0, 0, right, 0],
        [-left, 0, 0, 0, 0, left],
    ]
    assert sympy.Matrix(matrix) == support_quotient(triple, complement=True)
    total = 0
    for permutation in permutations(range(6)):
        inversions = sum(permutation[left_index] > permutation[right_index]
                         for left_index in range(6) for right_index in range(left_index + 1, 6))
        term = (-1) ** inversions
        for row, column in enumerate(permutation):
            term *= value * int(row == column) - matrix[row][column]
        total += term
    assert total % value == 0
    return total // value


parity_checks = []
for parity in ((1, 0, 0), (1, 1, 0)):
    reduced = sympy.Poly(quintic.as_expr().subs(dict(zip(exponents, parity))), variable, modulus=2)
    assert reduced == sympy.Poly(variable ** 2 * (variable + 1) ** 3, variable, modulus=2)
    substituted = quintic.as_expr().subs(dict(zip(exponents, (2 * left_shift + parity[0],
                                                            2 * right_shift + parity[1],
                                                            2 * even_shift + parity[2]))))
    for offset, divisor in ((0, 4), (1, 8)):
        polynomial = sympy.Poly(sympy.expand(substituted.subs(variable, 2 * argument + offset)),
                                left_shift, right_shift, even_shift, argument)
        assert all(int(coefficient) % divisor == 0 for coefficient in polynomial.coeffs())
        parity_checks.append({'exponent_parity': parity, 'argument_parity': offset,
                              'required_divisor': divisor, 'coefficient_count': len(polynomial.terms()),
                              'result': 'All coefficients divisible; this first necessary condition gives no obstruction'})


def linear_product_signature(roots, modulus):
    coefficients = [1]
    for root in roots:
        updated = [0] * (len(coefficients) + 1)
        for index, coefficient in enumerate(coefficients):
            updated[index] = (updated[index] + coefficient) % modulus
            updated[index + 1] = (updated[index + 1] - root * coefficient) % modulus
        coefficients = updated
    return tuple(coefficients)


splitting_checks = []
for modulus in (4, 8):
    signatures = {linear_product_signature(roots, modulus): roots
                  for roots in combinations_with_replacement(range(modulus), 5)}
    witnesses = []
    for residues in combinations_with_replacement(range(modulus), 3):
        if sum(residue % 2 for residue in residues) not in (1, 2):
            continue
        signature = tuple(int(coefficient.subs(dict(zip(exponents, residues)))) % modulus
                          for coefficient in quintic.all_coeffs())
        assert signature in signatures
        roots = signatures[signature]
        assert signature == linear_product_signature(roots, modulus)
        assert sum(root % 2 == 0 for root in roots) == 2
        witnesses.append({'exponent_residues': residues, 'coefficient_signature': signature,
                          'linear_root_residues': roots})
    assert len(witnesses) == {4: 12, 8: 80}[modulus]
    splitting_checks.append({'modulus': modulus, 'root_multisets': sympy.binomial(modulus + 4, 5),
                             'mixed_parity_unordered_classes': len(witnesses),
                             'excluded_classes': [], 'compatible_factorizations': witnesses})

rows = []
coefficient_checks = 0
for residues, expected_values in (
    ((1, 3, 2), (8, 16)), ((1, 7, 2), (24, 16)), ((3, 7, 2), (16, 8)),
    ((3, 5, 6), (8, 16)), ((3, 7, 6), (16, 24)), ((5, 7, 6), (24, 16)),
):
    substitutions = dict(zip(exponents, (8 * left_shift + residues[0],
                                         8 * right_shift + residues[1],
                                         8 * even_shift + residues[2])))
    checks = []
    for value, expected in zip((1, 3), expected_values):
        polynomial = sympy.Poly(sympy.expand(quintic.eval(value).subs(substitutions)),
                                left_shift, right_shift, even_shift)
        assert int(polynomial.TC()) % 32 == expected
        assert all(int(coefficient) % 32 == 0 for monomial, coefficient in polynomial.terms() if any(monomial))
        coefficient_checks += len(polynomial.terms())
        exact = independent_endpoint(residues, value)
        coefficients = [int(coefficient.subs(dict(zip(exponents, residues))))
                        for coefficient in quintic.all_coeffs()]
        assert exact == integer_horner(coefficients, value)
        assert exact % 32 == expected
        checks.append({'argument': value, 'residue_modulo_32': expected,
                       'symbolic_coefficient_count': len(polynomial.terms()),
                       'all_nonconstant_coefficients_divisible_by_32': True,
                       'independent_integer_determinant': exact})
    rows.append({'odd_odd_even_residues_modulo_8': residues, 'checks': checks})
assert coefficient_checks == 558

fixtures = []
for triple in ((10, 17, 19), (14, 19, 21)):
    direct = support_quotient(triple, complement=True)
    polynomial = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
    coefficients = [int(coefficient) for coefficient in polynomial.all_coeffs()]
    values = [independent_endpoint(triple, value) for value in (1, 3)]
    assert values == [integer_horner(coefficients, value) for value in (1, 3)]
    assert all(value % 32 for value in values)
    assert any(factor.degree() > 1 for factor, multiplicity in polynomial.factor_list()[1])
    fixtures.append({'exponents': triple, 'h_C_at_one_and_three': values,
                     'values_modulo_32': [value % 32 for value in values],
                     'nonlinear_rational_factor': True})

source = Path(__file__)
print(json.dumps({'mixed_parity_quintic_modulo_two': 'x^2*(x+1)^3',
                  'written_necessary_condition': 'An integral mixed-parity quotient has three odd roots; two share a residue modulo4. Therefore32divides h_C(1) or32divides h_C(3).',
                  'first_coefficient_divisibility_checks': parity_checks,
                  'complete_lower_modulus_splitting_checks': splitting_checks,
                  'infinite_congruence_classes': rows, 'symbolic_coefficient_checks': coefficient_checks,
                  'independent_integer_determinants': 16, 'direct_integer_fixtures': fixtures,
                  'sympy': sympy.__version__, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                  'scope': 'Written pigeonhole/divisibility proof for six residue patterns and all permutations, without exponent-size bounds. Twelve symbolic substitutions verify558coefficients;16independent720term integer determinant expansions agree with Horner. Lower-modulus finite checks record only splitting compatibility, not integrality. No exponent scan, numerical spectrum or Lean. FullQ3 remains open.'}, default=int, indent=2))
