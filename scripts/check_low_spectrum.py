import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient, support_weights


first, second, third = sympy.symbols('a b c', positive=True)
variable, offset = sympy.symbols('x u')
total_exponent = first + second + third
product_exponent = first * second * third
quotient = support_quotient((first, second, third), complement=True)
weights = support_weights((first, second, third))
scaling = sympy.diag(*(sympy.sqrt(weight) for weight in weights))
symmetric = scaling * quotient * scaling.inv()
permutation = [0, 1, 2, 5, 4, 3]
symmetric = symmetric.extract(permutation, permutation).applyfunc(sympy.simplify)
central = sympy.Matrix([
    [second + third + second * third, -sympy.sqrt(first * second), -sympy.sqrt(first * third)],
    [-sympy.sqrt(first * second), first + third + first * third, -sympy.sqrt(second * third)],
    [-sympy.sqrt(first * third), -sympy.sqrt(second * third), first + second + first * second],
])
leaves = sympy.diag(first, second, third)
coupling = -sympy.sqrt(product_exponent) * sympy.eye(3)
expected = central.row_join(coupling).col_join(coupling.row_join(leaves))
assert (symmetric - expected).applyfunc(sympy.simplify) == sympy.zeros(6)
schur = central - variable * sympy.eye(3) - product_exponent * (leaves - variable * sympy.eye(3)).inv()
diagonal_values = [total_exponent - variable - variable * product_exponent / (exponent * (exponent - variable))
                   for exponent in (first, second, third)]
root_vector = sympy.Matrix([sympy.sqrt(first), sympy.sqrt(second), sympy.sqrt(third)])
assert (schur - (sympy.diag(*diagonal_values) - root_vector * root_vector.T)).applyfunc(sympy.simplify) == sympy.zeros(3)
for exponent, diagonal_value in zip((first, second, third), diagonal_values):
    assert sympy.cancel((exponent - variable) * diagonal_value
                        - ((exponent - variable) * (total_exponent - variable)
                           - variable * product_exponent / exponent)) == 0
ordered_parameter = sympy.Symbol('t', positive=True)
diagonal_function = total_exponent - variable - variable * product_exponent / (ordered_parameter * (ordered_parameter - variable))
derivative = variable * product_exponent * (2 * ordered_parameter - variable) / (ordered_parameter ** 2 * (ordered_parameter - variable) ** 2)
assert sympy.cancel(sympy.diff(diagonal_function, ordered_parameter) - derivative) == 0
characteristic = quotient.charpoly(variable).as_expr()
schur_determinant = (sympy.prod(diagonal_values)
                     - first * diagonal_values[1] * diagonal_values[2]
                     - second * diagonal_values[0] * diagonal_values[2]
                     - third * diagonal_values[0] * diagonal_values[1])
assert sympy.cancel(characteristic
                    - (first - variable) * (second - variable) * (third - variable)
                    * schur_determinant) == 0
quintic = sympy.Poly(sympy.cancel(characteristic / variable), variable)
equal_exponent_factorization = ((variable - first ** 2 - first)
                                * (variable ** 2 - (first ** 2 + 4 * first) * variable + 3 * first ** 2) ** 2)
assert sympy.expand(quintic.as_expr().subs({second: first, third: first}) - equal_exponent_factorization) == 0
assert sympy.expand(quintic.eval(0)
                    + product_exponent * total_exponent * (total_exponent + first * second + first * third + second * third)) == 0

families = [
    {'gaps': (1, 2), 'h1_multiplier': -4 * first * (first + 1),
     'positive_factor': first ** 4 + 2 * first ** 3 - 4 * first ** 2 - 6 * first - 2,
     'h2_multiplier': -first,
     'integer_root_factor': first ** 5 - 9 * first ** 4 - 14 * first ** 3 + 93 * first ** 2 + 67 * first + 6,
     'prime': 7, 'expected_residues': [6, 4, 1, 5, 6, 5, 1]},
    {'gaps': (1, 3), 'h1_multiplier': -4 * first * (first + 1) * (first + 3),
     'positive_factor': first ** 3 + first ** 2 - 5 * first - 3,
     'h2_multiplier': -(first - 2) * (first + 1),
     'integer_root_factor': first ** 4 - 6 * first ** 3 - 42 * first ** 2 - 39 * first - 10,
     'prime': 11, 'expected_residues': [1, 3, 9, 8, 2, 6, 4, 4, 5, 8, 5]},
    {'gaps': (2, 3), 'h1_multiplier': -4 * (first + 2),
     'positive_factor': first ** 5 + 5 * first ** 4 + 2 * first ** 3 - 18 * first ** 2 - 28 * first - 10,
     'h2_multiplier': -first,
     'integer_root_factor': first ** 5 - 5 * first ** 4 - 48 * first ** 3 - 59 * first ** 2 - 39 * first - 54,
     'prime': 7, 'expected_residues': [2, 6, 5, 3, 5, 4, 3]},
    {'gaps': (3, 4), 'h1_multiplier': -4 * (first + 3),
     'positive_factor': first ** 5 + 8 * first ** 4 + 14 * first ** 3 - 26 * first ** 2 - 93 * first - 54,
     'h2_multiplier': -1,
     'integer_root_factor': first ** 6 - first ** 5 - 74 * first ** 4 - 375 * first ** 3 - 967 * first ** 2 - 1220 * first - 340,
     'prime': 13, 'expected_residues': [11, 1, 3, 4, 3, 1, 9, 9, 11, 11, 6, 1, 8]},
]
records = []
representatives = []
for family in families:
    middle_gap, last_gap = family['gaps']
    substitution = {second: first + middle_gap, third: first + last_gap}
    upper_condition = sympy.expand(((third - 3) * (total_exponent - 3) - 3 * first * second).subs(substitution))
    expected_upper = {(1, 2): -6 * first, (1, 3): -2 * first,
                      (2, 3): -4 * first, (3, 4): 4 - 2 * first}[family['gaps']]
    assert upper_condition == expected_upper
    assert all(value < 0 for value in sympy.Poly(upper_condition.subs(first, offset + 4), offset).all_coeffs())
    assert sympy.expand(quintic.eval(1).subs(substitution)
                        - family['h1_multiplier'] * family['positive_factor']) == 0
    positive_coefficients = [int(value) for value in
                             sympy.Poly(family['positive_factor'].subs(first, offset + 4), offset).all_coeffs()]
    assert all(value > 0 for value in positive_coefficients)
    factor = sympy.Poly(family['integer_root_factor'], first)
    assert sympy.expand(quintic.eval(2).subs(substitution) - family['h2_multiplier'] * factor.as_expr()) == 0
    coefficients = [int(value) for value in factor.all_coeffs()]
    residues = []
    for argument in range(family['prime']):
        value = 0
        for coefficient in coefficients:
            value = (value * argument + coefficient) % family['prime']
        assert value == int(factor.eval(argument)) % family['prime']
        residues.append(value)
    assert residues == family['expected_residues'] and all(residues)
    records.append({'offsets': [0, middle_gap, last_gap],
                    'upper_inertia_condition_at_3': str(upper_condition),
                    'h1_multiplier': str(family['h1_multiplier']),
                    'h1_positive_factor': str(family['positive_factor']),
                    'h1_positive_factor_coefficients_at_a4_plus_u': positive_coefficients,
                    'h2_multiplier': str(family['h2_multiplier']),
                    'h2_integer_root_factor': str(factor.as_expr()),
                    'factor_coefficients': coefficients,
                    'prime': family['prime'], 'residues': residues,
                    'independent_modular_horner': 'passed'})
    for minimum in (4, 20):
        exponents = (minimum, minimum + middle_gap, minimum + last_gap)
        evaluated = support_quotient(exponents, complement=True)
        polynomial = sympy.Poly(sympy.cancel(evaluated.charpoly(variable).as_expr() / variable), variable)
        assert polynomial == sympy.Poly(quintic.as_expr().subs(dict(zip((first, second, third), exponents))), variable)
        assert polynomial.eval(1) != 0 and polynomial.eval(2) != 0
        assert polynomial.count_roots(0, 3) == 2
        lower_condition = ((exponents[0] - 2) * (sum(exponents) - 2) - 2 * exponents[1] * exponents[2])
        root_count_between_2_and_3 = int(polynomial.count_roots(2, 3))
        if minimum == 20:
            assert lower_condition > 0 and root_count_between_2_and_3 == 2
        representatives.append({'exponents': exponents, 'quintic': str(polynomial.as_expr()),
                                'sturm_count_between_0_and_3': 2,
                                'sturm_count_between_2_and_3': root_count_between_2_and_3,
                                'lower_inertia_condition_at_2': lower_condition})

source_paths = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'symbolic_symmetric_block_and_schur_identities': 'passed',
                  'equal_exponent_factorization': str(equal_exponent_factorization),
                  'schur_diagonal': [str(value) for value in diagonal_values],
                  'ordered_parameter_derivative': str(derivative),
                  'general_upper_condition': '(c-m)(a+b+c-m)<mab, with integer2<=m<a, implies exactly two nonzero complement roots in(0,m)',
                  'general_lower_condition': '(a-m+1)(a+b+c-m+1)>(m-1)bc additionally places both roots in(m-1,m)',
                  'families': records, 'total_modular_residues_checked': sum(record['prime'] for record in records),
                  'representative_sturm_checks': representatives,
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                                    for source in source_paths},
                  'scope': 'General written Sylvester-inertia criterion with exact symbolic block/Schur/determinant/monotonicity checks. Four complete fixed-gap infinite families use written upper-inertia/positive h1 arguments and38root-free modular residues excluding h2=0; eight independently reconstructed representative quotient/Sturm checks at a4/20. No parameter scan or Lean. FullQ3 and other unequal/higher-prime vectors remain open.'}, indent=2))
