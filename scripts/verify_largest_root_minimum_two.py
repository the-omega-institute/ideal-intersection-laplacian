import json
import re
from pathlib import Path

import sympy

from verify_minimum_three import complement_quotient


ROOT = Path(__file__).resolve().parents[1]


def root_count(polynomial, lower, upper):
    return sum(multiplicity * factor.count_roots(lower, upper)
               for factor, multiplicity in polynomial.sqf_list()[1])


def main():
    minimum, middle, maximum, variable = sympy.symbols("a b c x")
    minimum_shift, middle_shift, maximum_shift = sympy.symbols("m u v")
    matrix = sympy.Matrix(complement_quotient((minimum, middle, maximum)))
    determinant = sympy.expand((variable * sympy.eye(6) - matrix).det(method="domain-ge"))
    quintic, remainder = sympy.div(determinant, variable, variable)
    assert remainder == 0
    anchor = middle * maximum + minimum + middle + maximum
    lower = ((2 * middle ** 2 - minimum * middle + middle - minimum) * maximum ** 2
             - ((minimum - 1) * middle ** 2 + minimum ** 2) * maximum
             - minimum * middle * (minimum + middle))
    assert sympy.expand(quintic.subs(variable, anchor)
                        + minimum ** 2 * middle * maximum * lower) == 0
    lower_boundary = 2 * middle * ((middle - minimum + 1) * middle ** 2
                                 - minimum * middle - minimum ** 2)
    lower_derivative = middle ** 2 * (4 * middle - 3 * minimum + 3) - 2 * minimum * middle - minimum ** 2
    assert sympy.expand(lower.subs(maximum, middle) - lower_boundary) == 0
    assert sympy.expand(sympy.diff(lower, maximum).subs(maximum, middle) - lower_derivative) == 0
    substitutions = {minimum: 2 + minimum_shift,
                     middle: 5 + minimum_shift + middle_shift,
                     maximum: 5 + minimum_shift + middle_shift + maximum_shift}
    for expression in (sympy.Poly(lower, maximum).LC(), lower_boundary, lower_derivative,
                       lower_boundary - 2 * middle ** 3 * (middle - minimum - 1),
                       lower_derivative - middle ** 3):
        coefficients = sympy.Poly(sympy.expand(expression.subs(substitutions, simultaneous=True)),
                                  minimum_shift, middle_shift, maximum_shift).coeffs()
        assert all(coefficient >= 0 for coefficient in coefficients)
    upper = sympy.Poly(sympy.expand(quintic.subs(variable, anchor + 1)
                                   .subs(substitutions, simultaneous=True)),
                       minimum_shift, middle_shift, maximum_shift)
    lower_bound = 0
    difference = 0
    negatives = []
    for (minimum_power, middle_power, maximum_power), coefficient in upper.terms():
        monomial = middle_shift ** middle_power * maximum_shift ** maximum_power
        if minimum_power == 0:
            assert coefficient > 0
            lower_bound += coefficient * monomial
        elif coefficient < 0:
            lower_bound += coefficient * monomial
            difference -= coefficient * (1 - minimum_shift ** minimum_power) * monomial
            negatives.append({"powers": [minimum_power, middle_power, maximum_power],
                              "coefficient": int(coefficient)})
        else:
            assert coefficient > 0
            difference += coefficient * minimum_shift ** minimum_power * monomial
    assert sympy.expand(upper.as_expr() - lower_bound - difference) == 0
    assert len(upper.terms()) == 143 and len(negatives) == 39
    assert min(term["powers"][0] for term in negatives) == 3
    section = (ROOT / "paper/sections/largest-root-identities.tex").read_text().split(
        r"\subsection{The upper sign for minima between two and three}")[1]
    rows = re.findall(r"^([0-9]+) & \$\[([^\]]+)\]\$", section, re.MULTILINE)
    displayed = 0
    vectors = []
    for maximum_power, vector in rows:
        coefficients = [int(value.strip()) for value in vector.replace(r"\allowbreak", "").split(",")]
        assert all(coefficient > 0 for coefficient in coefficients)
        displayed += maximum_shift ** int(maximum_power) * sum(
            coefficient * middle_shift ** degree for degree, coefficient in enumerate(coefficients))
        vectors.append({"maximum_power": int(maximum_power), "coefficients": coefficients})
    assert [row["maximum_power"] for row in vectors] == list(range(5))
    assert sum(len(row["coefficients"]) for row in vectors) == 35
    assert sympy.expand(displayed - lower_bound) == 0
    assert displayed.subs({middle_shift: 0, maximum_shift: 0}) == 259876
    assert sympy.expand(minimum + 3 - (minimum ** 2 - minimum)
                        - (3 - minimum) * (minimum + 1)) == 0
    for expression in (maximum * (middle - minimum) + 1 - minimum,
                       middle * (maximum - minimum) + 1 - minimum):
        assert all(coefficient > 0 for coefficient in sympy.Poly(
            sympy.expand(expression.subs(substitutions, simultaneous=True)),
            minimum_shift, middle_shift, maximum_shift).coeffs())
    controls = []
    for exponents in ((2, 5, 5), (sympy.Rational(5, 2), sympy.Rational(11, 2), 6)):
        values = dict(zip((minimum, middle, maximum), exponents))
        control_matrix = sympy.Matrix(complement_quotient(exponents))
        control_determinant = sympy.expand((variable * sympy.eye(6) - control_matrix).det(method="domain-ge"))
        assert sympy.expand(control_determinant - determinant.subs(values)) == 0
        control_quintic = sympy.Poly(quintic.subs(values), variable)
        control_anchor = anchor.subs(values)
        endpoints = [control_quintic.eval(control_anchor), control_quintic.eval(control_anchor + 1)]
        assert endpoints[0] < 0 < endpoints[1]
        counts = [root_count(control_quintic, control_anchor, control_anchor + 1),
                  root_count(control_quintic, control_anchor + 1, sympy.oo)]
        assert counts == [1, 0]
        controls.append({"exponents": list(map(str, exponents)), "anchor": str(control_anchor),
                         "endpoint_values": list(map(str, endpoints)),
                         "roots_in_open_unit_interval": int(counts[0]),
                         "roots_above_upper_endpoint": int(counts[1])})
    print(json.dumps({
        "real_domain": "2<=a<=b<=c, b-a>=3, c>=a^2-a",
        "lower_identity_and_quadratic_bounds": "passed generically",
        "upper_slab_domain": "a=2+m,b=5+m+u,c=b+v,0<=m<=1,u>=0,v>=0",
        "upper_slab_terms": len(upper.terms()),
        "upper_slab_negative_terms": negatives,
        "exact_nonnegative_difference_identity": "passed",
        "literal_lower_bound_vectors": vectors,
        "lower_bound_positive_coefficients": 35,
        "lower_bound_constant": 259876,
        "slab_quadratic_hypothesis_and_schur_diagonal_bounds": "passed",
        "fixed_rational_controls": controls,
        "sympy": sympy.__version__,
        "scope": "Direct set-disjointness quotient determinant, exact coefficient lower bound and two fixed rational Sturm controls. Shared quotient constructor and SymPy backend; original characteristic-polynomial helper not imported. Written root-location proof covers the stated real domain. The existing a>=3 coefficient tables retain their separate literal checker. No parameter scan, new finite base, historical finite-base rerun, graph enumeration, floats or Lean.",
        "status": "passed",
    }, indent=2))


if __name__ == "__main__":
    main()
