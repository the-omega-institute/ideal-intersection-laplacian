import json

import sympy

from verify_minimum_three import complement_quotient


def main():
    minimum, middle, maximum, variable, gap, inverse, scaled = sympy.symbols("a b c x d t y")
    matrix = sympy.Matrix(complement_quotient((minimum, middle, maximum)))
    determinant = sympy.expand((variable * sympy.eye(6) - matrix).det(method="domain-ge"))
    quintic, remainder = sympy.div(determinant, variable, variable)
    assert remainder == 0
    quadratic = variable ** 2 - (minimum ** 2 + 4 * minimum) * variable + 3 * minimum ** 2
    balanced = (variable - minimum ** 2 - minimum) * quadratic ** 2
    assert sympy.expand(quintic.subs({middle: minimum, maximum: minimum}) - balanced) == 0
    assert sympy.expand(quadratic.subs(variable, minimum)) == -minimum ** 3
    assert sympy.expand(quadratic.subs(variable, 3)) == 9 - 12 * minimum
    lower = 3 * minimum / (minimum + 4)
    assert sympy.factor(quadratic.subs(variable, lower)) == 9 * minimum ** 2 / (minimum + 4) ** 2
    sharp_root = 6 / (1 + 4 / minimum + sympy.sqrt((1 + 4 / minimum) ** 2 - 12 / minimum ** 2))
    assert sympy.simplify(quadratic.subs(variable, sharp_root)) == 0
    assert sympy.limit(sharp_root, minimum, sympy.oo) == 3

    endpoint = sympy.expand(quintic.subs({variable: 1, middle: minimum + gap}))
    cubic = sympy.Poly(endpoint, maximum)
    assert cubic.degree() == 3
    assert cubic.LC() == 2 * minimum ** 2 + 2 * minimum * gap + gap ** 2 - 1
    constant = ((minimum - 1) * (minimum + gap - 1) * (2 * minimum + gap - 1)
                * (minimum * (minimum + gap) + 2 * minimum + gap - 1))
    assert sympy.expand(cubic.TC() - constant) == 0
    middle_value = sympy.Poly(cubic.eval(minimum + gap), minimum)
    assert middle_value.degree() == 6 and middle_value.LC() == -4

    rescaled = sympy.Poly(sympy.expand(inverse ** 8 * endpoint.subs(
        {minimum: 1 / inverse, maximum: scaled / inverse ** 2})), inverse, scaled)
    leading = rescaled.as_expr().subs(inverse, 0)
    assert sympy.expand(leading - 2 * scaled ** 2 * (scaled - 2)) == 0
    assert sympy.diff(leading, scaled).subs(scaled, 2) == 8
    unknown = sympy.symbols("coefficient0:3")
    ansatz = 2 + (2 * gap - 3) * inverse + sum(
        coefficient * inverse ** degree for degree, coefficient in enumerate(unknown, start=2))
    substitution = sympy.Poly(sympy.expand(rescaled.as_expr().subs(scaled, ansatz)), inverse)
    solved = {}
    for degree, coefficient in enumerate(unknown, start=2):
        equation = substitution.nth(degree).subs(solved)
        solved[coefficient] = sympy.factor(sympy.solve(equation, coefficient)[0])
    expected = [-(gap + 2) * (2 * gap - 1) / 2, gap ** 2 / 2,
                gap ** 2 * (gap + 1) * (2 * gap - 3) / 4]
    assert all(sympy.expand(solved[coefficient] - value) == 0
               for coefficient, value in zip(unknown, expected))
    residual = sympy.Poly(sympy.expand(substitution.as_expr().subs(solved)), inverse)
    assert all(residual.nth(degree) == 0 for degree in range(5))
    assert sympy.expand(residual.nth(5) - gap ** 2 * (4 * gap ** 3 - 6 * gap + 7)) == 0
    print(json.dumps({
        "balanced_direct_determinant_factorization": "passed",
        "smallest_root_anchor_signs_and_limit": "passed exactly; written ordering for m>=1",
        "endpoint_one_direct_determinant_cubic": "passed",
        "rescaled_polynomial_at_zero": str(sympy.factor(leading)),
        "implicit_function_derivative_at_zero_two": 8,
        "fixed_gap_coefficients_constant_inverse_inverse_squared": list(map(str, expected)),
        "rescaled_residual_coefficients_zero_through_degree_four": True,
        "rescaled_degree_five_residual": str(sympy.factor(residual.nth(5))),
        "middle_anchor_leading_coefficient": -4,
        "scope": "Generic exact determinant and coefficient identities supporting the written fixed-d analytic implicit-function proof. O_d(a^-3) has no effective constant, minimum or uniform growing-gap bound. Shared set-disjointness constructor and SymPy; no exponent scan, numerical experiments, historical finite-base rerun or Lean.",
        "sympy": sympy.__version__,
        "status": "passed",
    }, indent=2))


if __name__ == "__main__":
    main()
