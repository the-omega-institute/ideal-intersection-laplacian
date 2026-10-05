import hashlib
import itertools
import json
from math import prod
from pathlib import Path

import sympy


def symbolic_checks():
    exponent, product, total, middle, maximum, weight, variable, first, second = sympy.symbols('a A B b c k x u v')
    determinant = ((exponent + 1) * total + exponent - 2) * (exponent - 1) - exponent ** 2 * product
    expected = (exponent ** 2 - 1) * total + (exponent - 1) * (exponent - 2) - exponent ** 2 * product
    assert sympy.expand(determinant - expected) == 0
    four_prime = -middle * maximum + (exponent ** 2 - 1) * (middle + maximum) + (exponent - 1) * (2 * exponent - 1)
    assert sympy.expand(determinant.subs({product: middle * maximum, total: (middle + 1) * (maximum + 1)}) - four_prime) == 0
    limit = 2 * exponent ** 2 - 1
    tail = first * second + exponent ** 2 * (first + second) + 3 * exponent - 2
    assert sympy.expand(-four_prime.subs({middle: limit + first, maximum: limit + second}) - tail) == 0
    assert sympy.expand(four_prime.subs({middle: exponent ** 2, maximum: exponent ** 4 + exponent ** 2 - 3 * exponent + 1})) == 0
    normalized = sympy.diag(1 / (weight + 1), 1) * sympy.Matrix([[1, weight], [1, 0]])
    assert sympy.factor((variable * sympy.eye(2) - normalized).det() - (variable - 1) * (variable + weight / (weight + 1))) == 0
    comparison = []
    expected_coefficients = ([4, 48, 236, 607, 857, 623, 180], [16, 236, 1472, 5022, 10096, 11923, 7628, 2030])
    for distinguished, others, coefficients in zip((exponent, limit), ((exponent, limit, limit), (exponent, exponent, limit)), expected_coefficients):
        other_product = prod(others)
        proper_weight = prod(entry + 1 for entry in others) - 1 - other_product
        margin = sympy.expand((distinguished ** 2 - 1) * proper_weight - (distinguished - 1) - other_product)
        shifted = sympy.Poly(sympy.expand(margin.subs(exponent, variable + 2)), variable)
        assert shifted.all_coeffs() == list(coefficients)
        assert all(entry > 0 for entry in coefficients)
        comparison.append({'distinguished_exponent': str(distinguished), 'failure_margin': str(margin), 'coefficients_after_a_equals_z_plus_two': list(coefficients)})
    return {'product_minor': str(expected), 'four_prime_minor': str(four_prime),
            'strict_tail_identity': str(tail), 'boundary_family': ['a^2', 'a^4+a^2-3a+1'],
            'comparison_with_small_exponent_criterion': comparison, 'identities': 'passed'}


def tensor_operator(exponent, tails):
    diagonal = sympy.ones(1, 1)
    disjoint = sympy.ones(1, 1)
    for entry in tails:
        diagonal = sympy.kronecker_product(diagonal, sympy.diag(entry + 1, 1))
        disjoint = sympy.kronecker_product(disjoint, sympy.Matrix([[1, entry], [1, 0]]))
    return (exponent + 1) * diagonal + exponent * disjoint


def variations(polynomial, endpoint):
    signs = [sympy.sign(entry.subs(polynomial.gen, endpoint)) for entry in sympy.sturm(polynomial.as_expr(), polynomial.gen)]
    nonzero = [entry for entry in signs if entry]
    return sum(left != right for left, right in zip(nonzero, nonzero[1:]))


def support_control(exponent, tails):
    exponents = (exponent, exponent, *tails)
    supports = tuple(range(1, (1 << len(exponents)) - 1))
    weights = {support: prod(entry for index, entry in enumerate(exponents) if support & (1 << index)) for support in supports}
    subsets = [sum(bit << (index + 2) for index, bit in enumerate(bits)) for bits in itertools.product((0, 1), repeat=len(tails))]
    basis = sympy.Matrix([[int(support == (1 | tail)) - int(support == (2 | tail)) for tail in subsets] for support in supports])
    complement = sympy.zeros(len(supports))
    original = sympy.zeros(len(supports))
    for row, support in enumerate(supports):
        for column, neighbor in enumerate(supports):
            if row == column:
                continue
            target = original if support & neighbor else complement
            target[row, row] += weights[neighbor]
            target[row, column] -= weights[neighbor]
    restriction = tensor_operator(exponent, tails)
    dimension = len(subsets)
    assert complement * basis == basis * (restriction - sympy.eye(dimension))
    assert sympy.Matrix([[weights[support] for support in supports]]) * basis == sympy.zeros(1, dimension)
    complement_vertices = sum(weights.values())
    universals = prod(exponents) - 1
    vertices = prod(entry + 1 for entry in exponents) - 2
    assert vertices == complement_vertices + universals
    assert (original + complement) * basis == complement_vertices * basis
    assert (original + universals * sympy.eye(len(supports))) * basis == basis * ((vertices + 1) * sympy.eye(dimension) - restriction)
    diagonal = sympy.diag(*[prod(entry for index, entry in enumerate(tails) if subset & (1 << (index + 2))) for subset in subsets])
    assert diagonal * restriction == restriction.T * diagonal
    shifted = diagonal * (restriction - sympy.eye(dimension))
    leading_minors = [int(shifted[:size, :size].det()) for size in range(1, dimension + 1)]
    assert all(value > 0 for value in leading_minors)
    product = prod(tails)
    total = prod(entry + 1 for entry in tails)
    minor = (exponent ** 2 - 1) * total + (exponent - 1) * (exponent - 2) - exponent ** 2 * product
    variable = sympy.Symbol('x')
    characteristic = sympy.Poly(restriction.charpoly(variable).as_expr(), variable)
    interior_count = variations(characteristic, 1) - variations(characteristic, 2) - int(characteristic.eval(2) == 0)
    if minor <= 0:
        assert interior_count >= 1
    record = {'exponents': list(exponents), 'graph_vertices': vertices,
              'proper_supports_checked': len(supports), 'embedding_columns_checked': dimension,
              'weighted_symmetry_zero_sum_complement_join': 'passed',
              'leading_minors_at_one': leading_minors, 'endpoint_principal_minor_at_two': minor,
              'sufficient_condition_holds': minor <= 0, 'characteristic_coefficients': [int(entry) for entry in characteristic.all_coeffs()],
              'distinct_roots_strictly_between_one_and_two': int(interior_count)}
    if minor == 0:
        trial = sympy.zeros(dimension, 1)
        trial[0] = exponent - 1
        trial[-1] = -exponent
        residual = (restriction - 2 * sympy.eye(dimension)) * trial
        assert residual[0] == residual[-1] == 0
        assert all(value == exponent * (exponent - 1) for value in residual[1:-1])
        assert (trial.T * diagonal * residual)[0] == 0
        intermediate = 1
        local_diagonal = restriction[intermediate, intermediate] - 2
        trial[intermediate] = -sympy.Rational(exponent * (exponent - 1), local_diagonal)
        energy = (trial.T * diagonal * (restriction - 2 * sympy.eye(dimension)) * trial)[0]
        expected_energy = -sympy.Rational(diagonal[intermediate, intermediate] * exponent ** 2 * (exponent - 1) ** 2, local_diagonal)
        assert energy == expected_energy < 0
        record['boundary_negative_trial_energy_minus_twice_norm'] = str(energy)
    return record


def three_prime_boundary():
    exponent, variable = sympy.symbols('a x')
    remaining = (exponent - 1) * (2 * exponent - 1)
    restriction = tensor_operator(exponent, (remaining,))
    upper = sympy.expand(sympy.trace(restriction) - 2)
    assert sympy.expand(restriction.charpoly(variable).as_expr() - (variable - 2) * (variable - upper)) == 0
    assert sympy.Poly(sympy.expand((upper - 2).subs(exponent, variable + 2)), variable).all_coeffs() == [2, 11, 21, 13]
    return {'family': '(a,a,(a-1)(2a-1)),a>=2', 'restricted_eigenvalues': ['2', str(upper)], 'equality_strictness_does_not_extend_to_t_equals_three': True}


def main():
    controls = [(1, (1, 1)), (5, (49, 49)), (2, (4, 15)), (5, (25, 636)),
                (5, (25, 635)), (5, (99, 99, 99)), (2, (7, 7, 48))]
    report = {'written_theorem': 'For t>=4 and exponents(a,a,k3,...,kt),a^2*A>=(a^2-1)*B+(a-1)*(a-2) gives a noninteger graph eigenvalue in(V-1,V),including equality.',
              'symbolic': symbolic_checks(), 'support_controls': [support_control(exponent, tails) for exponent, tails in controls],
              'three_prime_boundary': three_prime_boundary(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'sympy_version': sympy.__version__,
              'scope': 'Written unbounded sufficient condition; seven fixed support controls, exact symbolic identities, leading minors and Sturm counts. No expanded vertex graph, exponent scan, floating eigenvalues, finite classification base or Lean run. Higher-prime Q3 remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
