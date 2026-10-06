import hashlib
import itertools
import json
from math import prod
from pathlib import Path

import sympy

from check_four_prime_single_pair_midpoint import integer_determinant


def tensor_operator(exponent, tails):
    diagonal = sympy.ones(1, 1)
    disjoint = sympy.ones(1, 1)
    for entry in tails:
        diagonal = sympy.kronecker_product(diagonal, sympy.diag(entry + 1, 1))
        disjoint = sympy.kronecker_product(disjoint, sympy.Matrix([[1, entry], [1, 0]]))
    return (exponent + 1) * diagonal + exponent * disjoint, diagonal, disjoint


def splits(polynomial):
    return all(factor.degree() == 1 for factor, multiplicity in polynomial.factor_list()[1])


def splits_by_integer_division(coefficients, prime):
    remaining = [value % prime for value in coefficients]
    for root in range(prime):
        while len(remaining) > 1:
            quotient = [remaining[0]]
            for coefficient in remaining[1:-1]:
                quotient.append((coefficient + root * quotient[-1]) % prime)
            if (remaining[-1] + root * quotient[-1]) % prime:
                break
            remaining = quotient
    return len(remaining) == 1


def symbolic_checks():
    exponent, middle, maximum, variable = sympy.symbols('a b c x')
    restriction, diagonal, disjoint = tensor_operator(exponent, (middle, maximum))
    assert all(sympy.expand(value) == 0 for value in restriction + disjoint - (exponent + 1) * (diagonal + disjoint))
    weight = sympy.Symbol('k')
    factor = sympy.Matrix([[1, weight], [1, 0]])
    assert sympy.expand(factor.charpoly(variable).as_expr() - (variable ** 2 - variable - weight)) == 0
    binary = []
    expected = {(0, 0): variable ** 3 * (variable + 1),
                (0, 1): variable ** 2 * (variable ** 2 + variable + 1),
                (1, 0): variable ** 2 * (variable ** 2 + variable + 1),
                (1, 1): (variable + 1) ** 2 * (variable ** 2 + variable + 1)}
    for residues, expression in expected.items():
        polynomial = sympy.Poly((-disjoint.subs({middle: residues[0], maximum: residues[1]})).charpoly(variable).as_expr(), variable, modulus=2)
        assert polynomial == sympy.Poly(expression, variable, modulus=2)
        assert splits(polynomial) == (residues == (0, 0))
        binary.append({'tail_parities': list(residues), 'characteristic_modulo_two': str(expression),
                       'splits_into_linear_factors': splits(polynomial)})
    residue_table = []
    for prime, excluded in ((2, [1]), (3, [1]), (5, [3, 4])):
        actual = []
        for residue in range(prime):
            polynomial = sympy.Poly(variable ** 2 - variable - residue, variable, modulus=prime)
            linear = splits(polynomial)
            assert linear == splits_by_integer_division([1, -1, -residue], prime)
            if prime == 2:
                assert linear == (residue == 0)
            else:
                square = (1 + 4 * residue) % prime in {value * value % prime for value in range(prime)}
                assert linear == square
            if not linear:
                actual.append(residue)
            residue_table.append({'prime': prime, 'tail_residue': residue, 'splits': linear})
        assert actual == excluded
    shift = sympy.Symbol('z')
    tails = (2 * exponent, 2 * exponent ** 2 + 1)
    product_failure = (exponent ** 2 - 1) * sum(tails) + (exponent - 1) * (2 * exponent - 1) - prod(tails)
    gap = tails[1] - tails[0]
    weighted_failure = (2 * exponent + 1) * gap ** 2 - 4 * exponent * tails[0]
    comparisons = []
    for label, expression in (('product_tail_failure', product_failure), ('odd_gap_weighted_failure', weighted_failure)):
        coefficients = sympy.Poly(sympy.expand(expression.subs(exponent, shift + 5)), shift).all_coeffs()
        assert all(value > 0 for value in coefficients)
        comparisons.append({'criterion': label, 'failure_margin': str(sympy.expand(expression)),
                            'positive_coefficients_after_a_equals_z_plus_five': [int(value) for value in coefficients]})
    for distinguished, others in ((exponent, (exponent, *tails)), (tails[0], (exponent, exponent, tails[1])),
                                  (tails[1], (exponent, exponent, tails[0]))):
        product = prod(others)
        proper_weight = prod(entry + 1 for entry in others) - 1 - product
        margin = (distinguished ** 2 - 1) * proper_weight - (distinguished - 1) - product
        coefficients = sympy.Poly(sympy.expand(margin.subs(exponent, shift + 5)), shift).all_coeffs()
        assert all(value > 0 for value in coefficients)
        comparisons.append({'criterion': 'small_exponent_failure', 'distinguished_exponent': str(distinguished),
                            'failure_margin': str(sympy.expand(margin)),
                            'positive_coefficients_after_a_equals_z_plus_five': [int(value) for value in coefficients]})
    return {'tensor_reduction_identity': 'K+tensor(F)=(a+1)(tensor(E)+tensor(F))',
            'factor_characteristic': 'x^2-x-k', 'binary_four_prime_table': binary,
            'complete_tail_residue_table_for_primes_2_3_5': residue_table,
            'additional_coverage_family': '(a,a,2a,2a^2+1),odd a>=5', 'coverage_comparisons': comparisons}


def fixed_control(exponent, tails, prime):
    assert (exponent + 1) % prime == 0 and sympy.isprime(prime)
    exponents = (exponent, exponent, *tails)
    supports = tuple(range(1, (1 << len(exponents)) - 1))
    subsets = [sum(bit << (index + 2) for index, bit in enumerate(bits)) for bits in itertools.product((0, 1), repeat=len(tails))]
    weights = {support: prod(entry for index, entry in enumerate(exponents) if support & (1 << index)) for support in supports}
    basis = [{support: int(support == (1 | subset)) - int(support == (2 | subset)) for support in supports} for subset in subsets]
    restriction, diagonal, disjoint = tensor_operator(exponent, tails)
    dimension = len(subsets)
    vertices = prod(entry + 1 for entry in exponents) - 2
    universals = prod(exponents) - 1
    assert vertices == sum(weights.values()) + universals
    for column, values in enumerate(basis):
        assert sum(weights[support] * values[support] for support in supports) == 0
        for support in supports:
            action = sum(weights[neighbor] * (values[support] - values[neighbor]) for neighbor in supports if not support & neighbor)
            expected = sum(basis[row][support] * (restriction[row, column] - (row == column)) for row in range(dimension))
            assert action == expected
            original = sum(weights[neighbor] * (values[support] - values[neighbor]) for neighbor in supports if support & neighbor)
            assert original + action == sum(weights.values()) * values[support]
            assert original + universals * values[support] == (vertices + 1) * values[support] - sum(basis[row][support] * restriction[row, column] for row in range(dimension))
    symmetrizer = sympy.diag(*[prod(entry for index, entry in enumerate(tails) if subset & (1 << (index + 2))) for subset in subsets])
    assert symmetrizer * restriction == restriction.T * symmetrizer
    assert all(int(value) % prime == 0 for value in restriction + disjoint)
    variable = sympy.Symbol('x')
    characteristic = sympy.Poly(restriction.charpoly(variable).as_expr(), variable)
    determinants = []
    for argument in range(dimension + 1):
        determinant = integer_determinant([[argument * (row == column) - int(restriction[row, column]) for column in range(dimension)] for row in range(dimension)])
        assert determinant == characteristic.eval(argument)
        determinants.append(determinant)
    reduced = sympy.Poly(characteristic.as_expr(), variable, modulus=prime)
    tensor_reduced = sympy.Poly((-disjoint).charpoly(variable).as_expr(), variable, modulus=prime)
    assert reduced == tensor_reduced
    assert splits(reduced) == splits_by_integer_division([int(value) for value in characteristic.all_coeffs()], prime)
    tail_splitting = [splits(sympy.Poly(variable ** 2 - variable - entry, variable, modulus=prime)) for entry in tails]
    assert splits(reduced) == all(tail_splitting)
    return {'exponents': list(exponents), 'prime': prime, 'dimension': dimension,
            'support_column_actions_checked': len(supports) * dimension,
            'weighted_zero_sum_symmetry_complement_graph_lift': 'passed',
            'characteristic_coefficients': [int(value) for value in characteristic.all_coeffs()],
            'direct_integer_determinants_at_0_through_dimension': determinants,
            'reduced_factorization': [[str(factor.as_expr()), multiplicity] for factor, multiplicity in reduced.factor_list()[1]],
            'tail_quadratics_split': tail_splitting, 'full_restriction_splits': splits(reduced),
            'modular_nonintegrality_proved_for_control': not splits(reduced)}


def main():
    controls = [(5, (10, 51), 2), (5, (10, 52), 2), (8, (10, 11), 3),
                (8, (11, 14), 3), (9, (13, 20, 22), 5), (9, (10, 11, 12), 5)]
    helper = Path(__file__).parent / 'check_four_prime_single_pair_midpoint.py'
    report = {'written_theorem': 'For any positive repeated-pair vector(a,a,k3,...,kt),t>=3,and prime p dividing a+1,the characteristic polynomial of the genuine tensor restriction splits over F_p iff every x^2-x-k_i splits. Integrality therefore requires each tail even at p=2,or each 1+4k_i a quadratic residue(including0)at odd p.',
              'symbolic': symbolic_checks(), 'fixed_controls': [fixed_control(*control) for control in controls],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {helper.name: hashlib.sha256(helper.read_bytes()).hexdigest()},
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded tensor-splitting proof for arbitrary prime count. Complete10tail-residue rows for primes2,3,5and4binary four-prime rows. Six specified4/5-prime controls,704support-column actions and38independent integer determinants. Passing split controls are not integrality claims. No exponent/tail scan,expanded graph,Sturm count,historical finite-base rerun or Lean. General classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
