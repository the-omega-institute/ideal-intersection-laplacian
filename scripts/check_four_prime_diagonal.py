import hashlib
import json
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding


def cubic_block(exponent):
    return sympy.Matrix([[(exponent + 1) ** 3 + exponent, 2 * exponent ** 2, exponent ** 3],
                         [exponent, 2 * exponent ** 2 + 2 * exponent + 1, 0],
                         [exponent, 0, exponent + 1]])


def symbolic_checks():
    exponent, variable, shift = sympy.symbols('a x u')
    full = sympy.Matrix(operator(exponent, exponent, exponent))
    block = cubic_block(exponent)
    embedding = sympy.Matrix([[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]])
    antisymmetric = sympy.Matrix([0, 1, -1, 0])
    assert (full * embedding - embedding * block).applyfunc(sympy.expand) == sympy.zeros(4, 3)
    assert (full * antisymmetric - (2 * exponent + 1) * antisymmetric).applyfunc(sympy.expand) == sympy.zeros(4, 1)
    diagonal = sympy.diag(1, 2 * exponent, exponent ** 2)
    assert diagonal * block == block.T * diagonal
    polynomial = (variable ** 3 - (exponent + 1) ** 2 * (exponent + 3) * variable ** 2
                  + (exponent + 1) * (2 * exponent ** 4 + 6 * exponent ** 3 + 13 * exponent ** 2 + 11 * exponent + 3) * variable
                  - (2 * exponent + 1) ** 3 * (exponent ** 2 + exponent + 1))
    assert sympy.expand(block.charpoly(variable).as_expr() - polynomial) == 0
    assert sympy.expand(full.charpoly(variable).as_expr() - (variable - (2 * exponent + 1)) * polynomial) == 0
    expected = [[1, 18, 109, 218], [2, 58, 670, 3848, 10968, 12394],
                [2, 46, 398, 1562, 2548, 932], [12, 274, 2307, 8457, 11387],
                [2, 31, 155, 251], [3, 62, 477, 1616, 2031]]
    expressions = [(block - 3 * sympy.eye(3))[:size, :size].det() for size in (1, 2, 3)]
    expressions.extend([polynomial.subs(variable, 4),
                        2 * exponent * (exponent ** 2 - 1) + (exponent - 1) * (2 * exponent - 1) - exponent ** 2,
                        (exponent ** 2 - 1) * (3 * exponent ** 2 + 3 * exponent) - (exponent - 1) - exponent ** 3])
    assert sympy.expand(expressions[2] + polynomial.subs(variable, 3)) == 0
    names = ['leading_minor_1_at_three', 'leading_minor_2_at_three', 'leading_minor_3_at_three',
             'characteristic_value_at_four', 'product_tail_failure_margin', 'small_exponent_failure_margin']
    expansions = []
    for name, expression, coefficients in zip(names, expressions, expected):
        shifted = sympy.Poly(sympy.expand(expression.subs(exponent, shift + 5)), shift)
        assert shifted.all_coeffs() == coefficients
        assert all(coefficient > 0 for coefficient in coefficients)
        expansions.append({'identity': name, 'polynomial_in_a': str(sympy.expand(expression)),
                           'coefficients_after_a_equals_five_plus_u': coefficients})
    return {'invariant_embeddings_weighted_symmetry_characteristic_factorization': 'passed',
            'cubic': str(sympy.expand(polynomial)), 'positive_expansions': expansions,
            'positive_coefficients_checked': sum(len(coefficients) for coefficients in expected)}


def fixed_control(exponent):
    control = support_embedding(exponent, exponent, exponent)
    block = cubic_block(exponent)
    variable = sympy.Symbol('x')
    values = [(endpoint, int((endpoint * sympy.eye(3) - block).det(method='bareiss'))) for endpoint in (0, 1, 2, 3)]
    interpolated = sympy.Poly(sympy.interpolate(values, variable), variable)
    characteristic = sympy.Poly(block.charpoly(variable).as_expr(), variable)
    assert interpolated == characteristic
    assert characteristic.eval(3) < 0 < characteristic.eval(4)
    assert characteristic.count_roots(3, 4) == 1
    leading = [int((block - 3 * sympy.eye(3))[:size, :size].det(method='bareiss')) for size in (1, 2, 3)]
    assert all(value > 0 for value in leading)
    control.update({'cubic_coefficients': [int(value) for value in characteristic.all_coeffs()],
                    'four_independent_bareiss_determinant_values': values, 'leading_minors_at_three': leading,
                    'cubic_at_three': int(characteristic.eval(3)), 'cubic_at_four': int(characteristic.eval(4)),
                    'sturm_roots_in_three_four': 1})
    return control


def main():
    dependency = Path(__file__).with_name('check_four_prime_pair_three.py')
    report = {'written_theorem': 'Every integer a>=5 gives 3<kappa_min(K_a)<4 for four-prime exponents(a,a,a,a), hence a noninteger graph eigenvalue in(V-3,V-2). Earlier unit/pair-two/three/four theorems complete all positive a.',
              'symbolic': symbolic_checks(), 'fixed_controls': [fixed_control(exponent) for exponent in (5, 6, 11)],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'support_embedding_dependency_sha256': hashlib.sha256(dependency.read_bytes()).hexdigest(),
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded proof; complete positive expansions and three fixed exact support/characteristic/Sturm controls. No finite exponent base, expanded vertex graph, exponent-range scan, floating eigensolver or Lean. General higher-prime Q3 remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
