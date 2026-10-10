import json
from pathlib import Path

import sympy

from verify_minimum_three import complement_quotient


ROOT = Path(__file__).resolve().parents[1]


def symmetric_blocks(exponents, endpoint):
    matrix = sympy.Matrix(complement_quotient(exponents))
    first, second, third = exponents
    weights = (*exponents, first * second, first * third, second * third)
    scaling = sympy.diag(*(sympy.sqrt(weight) for weight in weights))
    symmetric = (scaling * matrix * scaling.inv()).applyfunc(sympy.simplify)
    order = [0, 1, 2, 5, 4, 3]
    shifted = symmetric.extract(order, order) - endpoint * sympy.eye(6)
    schur = (shifted[:3, :3] - shifted[:3, 3:] * shifted[3:, 3:].inv() * shifted[3:, :3])
    product = sympy.prod(exponents)
    values = [sympy.simplify(sum(exponents) - endpoint
              - endpoint * product / (exponent * (exponent - endpoint))) for exponent in exponents]
    column = sympy.Matrix([sympy.sqrt(exponent) for exponent in exponents])
    assert (schur - sympy.diag(*values) + column * column.T).applyfunc(sympy.simplify) == sympy.zeros(3)
    return matrix, values


def main():
    first_weight, second_weight, third_weight = sympy.symbols('v1 v2 v3', positive=True)
    second_diagonal, third_diagonal = sympy.symbols('k2 k3', real=True)
    column = sympy.Matrix([first_weight, second_weight, third_weight])
    matrix = sympy.diag(0, second_diagonal, third_diagonal) - column * column.T
    transform = sympy.Matrix([[1 / first_weight, -second_weight / first_weight,
                               -third_weight / first_weight], [0, 1, 0], [0, 0, 1]])
    assert (transform.T * matrix * transform).applyfunc(sympy.simplify) == sympy.diag(-1, second_diagonal, third_diagonal)
    variable = sympy.Symbol('u')
    controls = []
    fixtures = (((10, sympy.Rational(76, 7), 11), 2), ((8, 15, 20), 3),
                ((8, 8, 11), 3), ((8, 8, sympy.Rational(42, 5)), 2), ((5, 6, 6), 2))
    for exponents, endpoint in fixtures:
        exponents = tuple(map(sympy.sympify, exponents))
        assert 0 < endpoint < min(exponents)
        quotient, values = symmetric_blocks(exponents, endpoint)
        negative_count = sum(int(bool(value < 0)) for value in values)
        zero_count = sum(value == 0 for value in values)
        assert zero_count > 0
        direct = sympy.expand((variable * sympy.eye(6) - quotient).det())
        quintic, remainder = sympy.div(direct, variable, variable)
        assert remainder == 0
        polynomial = sympy.Poly(quintic, variable)
        assert polynomial.eval(0) != 0
        endpoint_multiplicity = 0
        while polynomial.eval(endpoint) == 0:
            polynomial, remainder = polynomial.div(sympy.Poly(variable - endpoint, variable))
            assert remainder.is_zero
            endpoint_multiplicity += 1
        strict_count = sum(multiplicity * factor.count_roots(0, endpoint)
                           for factor, multiplicity in polynomial.sqf_list()[1])
        assert strict_count == negative_count and endpoint_multiplicity == zero_count - 1
        controls.append({'parameters': list(map(str, exponents)), 'endpoint': endpoint,
            'schur_diagonal': list(map(str, values)), 'negative_diagonal_count': int(negative_count),
            'zero_diagonal_count': int(zero_count), 'positive_roots_strictly_below_endpoint': int(strict_count),
            'endpoint_multiplicity': endpoint_multiplicity})
    assert {(row['zero_diagonal_count'], row['negative_diagonal_count']) for row in controls} == {(1, 0), (1, 1), (1, 2), (2, 0), (2, 1)}
    endpoint = 48 - 8 * sympy.sqrt(33)
    assert endpoint.is_positive and (8 - endpoint).is_positive
    quotient, values = symmetric_blocks((sympy.Integer(8),) * 3, endpoint)
    assert values == [0, 0, 0]
    direct = sympy.expand((variable * sympy.eye(6) - quotient).det())
    factorization = (variable - 72) * (variable ** 2 - 96 * variable + 192) ** 2
    assert sympy.expand(direct - variable * factorization) == 0
    assert sympy.simplify((variable ** 2 - 96 * variable + 192).subs(variable, endpoint)) == 0
    assert (72 - endpoint).is_positive and (16 * sympy.sqrt(33)).is_positive
    assert sympy.simplify(sympy.diff(factorization, variable).subs(variable, endpoint)) == 0
    assert sympy.simplify(sympy.diff(factorization, variable, 2).subs(variable, endpoint)) != 0
    assert r'\operatorname{nullity}K(x)=z-1' in (ROOT / 'paper/sections/mixed-inertia.tex').read_text()
    print(json.dumps({'statement': 'For0<x<a and z>0 zero Schur diagonals,q negative diagonals,the complement quotient has q positive roots strictly below x and multiplicity z-1 at x',
        'generic_zero_diagonal_congruence': 'passed;K congruent to diag(-1,k2,k3) after choosing one zero diagonal',
        'direct_weighted_symmetry_and_schur_blocks': 'passed for all six controls',
        'fixed_rational_endpoint_controls': controls,
        'fixed_algebraic_endpoint_control': {'parameters': [8, 8, 8], 'endpoint': str(endpoint),
            'zero_diagonal_count': 3, 'negative_diagonal_count': 0,
            'positive_roots_strictly_below_endpoint': 0, 'endpoint_multiplicity': 2,
            'quintic_factorization': str(factorization), 'exact_factorization_and_root_ordering': 'passed'},
        'supporting_manuscript_statement': 'passed', 'sympy': sympy.__version__,
        'scope': 'Written zero-diagonal coordinate congruence completes supporting inertia lemma,retaining0<x<a and original nonsingular formula. Shared set-disjointness support constructor/SymPy,no original characteristic helper. Five fixed rational endpoint controls remove endpoint factors before strict root counts with multiplicities; one algebraic endpoint uses exact factorization/ordering. No scan,new finite base,historical finite-base rerun,floats or Lean. Selected main classification retained.',
        'status': 'passed'}, indent=2))


if __name__ == '__main__':
    main()
