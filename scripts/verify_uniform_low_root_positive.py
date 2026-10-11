import json
from pathlib import Path

import sympy

from verify_minimum_three import complement_quotient


ROOT = Path(__file__).resolve().parents[1]


def main():
    minimum, middle, maximum = sympy.symbols("a b c", positive=True)
    variable, trial_scale = sympy.symbols("x t")
    exponents = (minimum, middle, maximum)
    total, product = sum(exponents), sympy.prod(exponents)
    matrix = sympy.Matrix(complement_quotient(exponents))
    weights = (*exponents, minimum * middle, minimum * maximum, middle * maximum)
    square_weights = sympy.diag(*(sympy.sqrt(weight) for weight in weights))
    symmetric = (square_weights * matrix * square_weights.inv()).applyfunc(sympy.simplify)
    ordering = [0, 1, 2, 5, 4, 3]
    reordered = symmetric.extract(ordering, ordering)
    column = sympy.Matrix([sympy.sqrt(exponent) for exponent in exponents])
    singleton = sympy.diag(*(total + product / exponent for exponent in exponents)) - column * column.T
    paired = sympy.diag(*exponents)
    coupling = -sympy.sqrt(product) * sympy.eye(3)
    expected = singleton.row_join(coupling).col_join(coupling.row_join(paired))
    assert (reordered - expected).applyfunc(sympy.simplify) == sympy.zeros(6)
    shifted = reordered - 3 * sympy.eye(6)
    principal = shifted.extract([0, 1, 3, 4], [0, 1, 3, 4])
    trial = sympy.eye(2).col_join(trial_scale * sympy.eye(2))
    trial_identity = (principal[:2, :2] - 2 * trial_scale * sympy.sqrt(product) * sympy.eye(2)
                      + trial_scale ** 2 * sympy.diag(minimum - 3, middle - 3))
    assert (trial.T * principal * trial - trial_identity).applyfunc(sympy.simplify) == sympy.zeros(2)
    remaining = [0, 1, 2, 3]
    eliminated = [4, 5]
    reduced = (shifted.extract(remaining, remaining)
               - shifted.extract(remaining, eliminated)
               * shifted.extract(eliminated, eliminated).inv()
               * shifted.extract(eliminated, remaining))
    compression = sympy.Matrix([[1, 0, 0], [0, 0, sympy.sqrt(middle)],
                                [0, 0, sympy.sqrt(maximum)], [0, 1, 0]])
    compressed = (compression.T * reduced * compression).applyfunc(sympy.simplify)
    diagonal = middle * maximum + middle + maximum - 3
    cross = -sympy.sqrt(minimum) * (middle + maximum)
    rayleigh = ((minimum - 3) * (middle + maximum)
                - 3 * product * (1 / (middle - 3) + 1 / (maximum - 3)))
    expected_compression = sympy.Matrix([[diagonal, -sympy.sqrt(product), cross],
                                         [-sympy.sqrt(product), minimum - 3, 0],
                                         [cross, 0, rayleigh]])
    assert (compressed - expected_compression).applyfunc(sympy.simplify) == sympy.zeros(3)
    compressed_determinant = (diagonal * (minimum - 3) * rayleigh
                              - product * rayleigh - (minimum - 3) * cross ** 2)
    assert sympy.cancel(compressed.det() - compressed_determinant) == 0
    comparison = sympy.diag(*(total - 3 * product / exponent ** 2 for exponent in exponents)) - column * column.T
    squares = maximum * (minimum - middle) ** 2 + middle * (minimum - maximum) ** 2 + minimum * (middle - maximum) ** 2
    assert sympy.cancel(comparison.det() - 6 * squares) == 0
    assert sympy.cancel((column.T * comparison * column)[0]
                        + 3 * product * sum(1 / exponent for exponent in exponents)) == 0
    schur = (singleton - 3 * sympy.eye(3)
              - product * sympy.diag(*(1 / (exponent - 3) for exponent in exponents)))
    gap = sympy.diag(*(3 + 9 * product / (exponent ** 2 * (exponent - 3)) for exponent in exponents))
    assert (comparison - schur - gap).applyfunc(sympy.cancel) == sympy.zeros(3)
    determinant = sympy.expand((variable * sympy.eye(6) - matrix).det(method="domain-ge"))
    quintic, remainder = sympy.div(determinant, variable, variable)
    assert remainder == 0
    controls = []
    fixtures = ((sympy.Rational(1, 2), 1, 2), (1, 3, 4), (2, 4, 5),
                (3, 4, 5), (3, 6, 9), (sympy.Rational(7, 2), 4, 5), (4, 4, 4))
    for exponents_value in fixtures:
        control_matrix = sympy.Matrix(complement_quotient(exponents_value))
        direct = sympy.expand((variable * sympy.eye(6) - control_matrix).det())
        specialized = sympy.expand(quintic.subs(dict(zip(exponents, exponents_value))))
        assert sympy.expand(direct - variable * specialized) == 0
        polynomial = sympy.Poly(specialized, variable)
        assert polynomial.eval(0) != 0
        boundary_multiplicity = 0
        while polynomial.eval(3) == 0:
            polynomial, remainder = polynomial.div(sympy.Poly(variable - 3, variable))
            assert remainder.is_zero
            boundary_multiplicity += 1
        count = sum(multiplicity * factor.count_roots(0, 3)
                    for factor, multiplicity in polynomial.sqf_list()[1])
        assert count >= 1
        controls.append({"parameters": list(map(str, exponents_value)),
                         "positive_roots_strictly_below_three": int(count),
                         "root_three_multiplicity_excluded": boundary_multiplicity})
    equal_quadratic = variable ** 2 - (minimum ** 2 + 4 * minimum) * variable + 3 * minimum ** 2
    equal_factor = (variable - minimum ** 2 - minimum) * equal_quadratic ** 2
    assert sympy.expand(quintic.subs({middle: minimum, maximum: minimum}) - equal_factor) == 0
    assert sympy.expand(equal_quadratic.subs(variable, minimum)) == -minimum ** 3
    sharp_root = 6 / (1 + 4 / minimum + sympy.sqrt((1 + 4 / minimum) ** 2 - 12 / minimum ** 2))
    assert sympy.simplify(equal_quadratic.subs(variable, sharp_root)) == 0
    assert sympy.limit(sharp_root, minimum, sympy.oo) == 3
    assert r"For every ordered real triple $0<a\leq b\leq c$" in (ROOT / "paper/sections/mixed-inertia.tex").read_text()
    print(json.dumps({
        "statement": "For every ordered positive real triple0<a<=b<=c, the complement quotient has a positive root strictly below3",
        "direct_weighted_symmetry_and_block_identity": "passed",
        "two_small_parameters_negative_trial_subspace": "passed generically",
        "one_small_parameter_compression_rayleigh_and_determinant": "passed generically,including a=3 without division by a-3",
        "retained_a_greater_than_three_comparison_identities": "passed",
        "fixed_exact_root_counts": controls,
        "sharp_uniform_constant": 3,
        "equal_parameter_factorization_and_lowest_root_limit": "passed generically and exactly",
        "current_manuscript_statement": "passed",
        "sympy": sympy.__version__,
        "scope": "Written three-case inertia proof covers all positive reals; principal trial and compressed determinant identities include singular a=3. Seven fixed exact rational/integer controls count multiplicities and exclude roots exactly3. Equal-parameter family proves constant3optimal by its lowest-root limit. Shared set-disjointness support constructor and SymPy,no original characteristic helper. No parameter scan,new finite base,historical finite-base rerun,floats or Lean. Classification finite inputs and balanced-interval corollary retain their scopes.",
        "status": "passed",
    }, indent=2))


if __name__ == "__main__":
    main()
