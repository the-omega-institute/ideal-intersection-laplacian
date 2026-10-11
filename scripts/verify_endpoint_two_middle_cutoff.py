import json
from pathlib import Path

import sympy

from verify_minimum_three import complement_quotient


ROOT = Path(__file__).resolve().parents[1]


def main():
    minimum, middle, maximum, variable = sympy.symbols("a b c x")
    minimum_shift, middle_shift, maximum_shift = sympy.symbols("m u v")
    matrix = sympy.Matrix(complement_quotient((minimum, middle, maximum)))
    determinant = sympy.expand((variable * sympy.eye(6) - matrix).det(method="domain-ge"))
    quintic, remainder = sympy.div(determinant, variable, variable)
    assert remainder == 0
    endpoint = quintic.subs(variable, 2)
    boundary = 2 * minimum - 2 + middle_shift
    tail = sympy.Poly(sympy.expand(endpoint.subs(
        {middle: boundary, maximum: boundary + maximum_shift}, simultaneous=True)), maximum_shift)
    assert tail.degree() == 3
    first_factor = (2 * middle_shift ** 2 + 7 * (minimum - 2) * middle_shift
                    + 2 * (3 * minimum ** 2 - 14 * minimum + 12))
    second_factor, remainder = sympy.div(tail.nth(0), first_factor, middle_shift)
    assert sympy.expand(remainder) == 0
    expected_second = ((minimum + 2) * middle_shift ** 3
                       + (4 * minimum ** 2 + 10 * minimum - 12) * middle_shift ** 2
                       + (4 * minimum ** 3 + 25 * minimum ** 2 - 48 * minimum + 12) * middle_shift
                       + 2 * (13 * minimum ** 3 - 28 * minimum ** 2 + 8 * minimum + 8))
    assert sympy.expand(second_factor - expected_second) == 0
    product = first_factor * second_factor
    assert sympy.expand(tail.nth(1) - sympy.diff(product, middle_shift) / 2) == 0
    coefficient_reports = {}
    for name, expression in (("B0", second_factor), ("D0", tail.nth(2)), ("E0", tail.nth(3))):
        shifted = sympy.Poly(sympy.expand(expression.subs(minimum, 3 + minimum_shift)),
                             minimum_shift, middle_shift)
        assert all(coefficient > 0 for coefficient in shifted.coeffs())
        coefficient_reports[name] = {
            "positive_coefficients": len(shifted.terms()),
            "constant": int(shifted.nth(0, 0)),
            "shifted_identity": str(shifted.as_expr()),
        }
    threshold = (7 + sympy.sqrt(13)) / 3
    other_root = (7 - sympy.sqrt(13)) / 3
    assert 3 < threshold < 4
    constant = first_factor.subs(middle_shift, 0)
    assert sympy.expand(constant - 6 * (minimum - threshold) * (minimum - other_root)) == 0
    assert sympy.simplify(first_factor.subs({minimum: threshold, middle_shift: 0})) == 0
    assert sympy.expand(sympy.diff(first_factor, middle_shift) - (4 * middle_shift + 7 * (minimum - 2))) == 0
    boundary_triple = (threshold, 2 * threshold - 2, 2 * threshold - 2)
    assert sympy.simplify(endpoint.subs(dict(zip((minimum, middle, maximum), boundary_triple)))) == 0
    assert sympy.simplify(boundary_triple[1] - boundary_triple[0]) > 0
    controls = []
    for exponents, sign in (
            ((sympy.Rational(7, 2), sympy.Integer(5), sympy.Integer(5)), -1),
            ((sympy.Rational(15, 4), sympy.Rational(11, 2), sympy.Rational(11, 2)), 1),
            ((sympy.Rational(15, 4), sympy.Integer(6), sympy.Integer(7)), 1)):
        value = sympy.factor(endpoint.subs(dict(zip((minimum, middle, maximum), exponents))))
        control_matrix = sympy.Matrix(complement_quotient(exponents))
        assert sympy.expand((2 * sympy.eye(6) - control_matrix).det()) == 2 * value
        assert sympy.sign(value) == sign
        assert exponents[2] >= exponents[1] >= 2 * exponents[0] - 2 >= exponents[0]
        controls.append({"exponents": list(map(str, exponents)), "endpoint_two": str(value), "sign": sign})
    source = (ROOT / "paper/sections/endpoint-two-completion.tex").read_text()
    assert r"$\alpha=(7+\sqrt{13})/3$" in source
    assert r"For ordered real exponents $\alpha\leq a\leq b\leq c$" in source
    assert r"$b\leq2a-2$" in source
    assert r"$a=\alpha$, $b=c=2\alpha-2$" in source
    print(json.dumps({
        "statement": "On real alpha<=a<=b<=c,h_C(2)=0: b<=2a-2; equality exactly a=alpha,b=c=2alpha-2. For a>alpha the bound is strict.",
        "sharp_cutoff": str(threshold),
        "generic_middle_tail_identity": "passed against direct quotient determinant",
        "A0_constant_factorization": "6(a-alpha)(a-(7-sqrt13)/3), passed",
        "A0_derivative": "4u+7(a-2)>0 for a>=alpha,u>=0",
        "positive_shift_three_coefficients": coefficient_reports,
        "exact_ordered_endpoint_boundary": "passed over Q(sqrt13)",
        "fixed_rational_controls": controls,
        "current_manuscript_statement": "passed",
        "integer_middle_bound_minimum": 4,
        "maximum_bound_minimum": 8,
        "sympy": sympy.__version__,
        "scope": "Written real-domain strengthening and sharp boundary by the existing cubic-in-tail identity. Generic direct determinant, positive shift-three coefficients, exact algebraic boundary and three fixed rational controls. Shared set-disjointness model and SymPy; no original characteristic helper. No parameter scan,new finite base,historical finite-base rerun,floats or Lean. The integer proof and maximum bound retain their scopes.",
        "status": "passed",
    }, indent=2))


if __name__ == "__main__":
    main()
