import json
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
    minimum_anchor = minimum ** 2 * middle ** 2 * maximum ** 2 * (
        middle + maximum - minimum ** 2 - 2 * minimum)
    maximum_anchor = -minimum ** 2 * middle ** 2 * maximum ** 2 * (
        maximum ** 2 + 2 * maximum - minimum - middle)
    assert sympy.expand(quintic.subs(variable, minimum) - minimum_anchor) == 0
    assert sympy.expand(quintic.subs(variable, maximum) - maximum_anchor) == 0
    threshold = 2 + sympy.sqrt(3)
    sum_bound = 2 * minimum ** 2 - 2 * minimum + 1
    threshold_polynomial = minimum ** 2 - 4 * minimum + 1
    assert sympy.expand(sum_bound - minimum ** 2 - 2 * minimum - threshold_polynomial) == 0
    assert sympy.expand(threshold_polynomial
                        - (minimum - threshold) * (minimum - 2 + sympy.sqrt(3))) == 0
    assert 3 < threshold < 4
    curve_maximum = (minimum - 1) * (2 * minimum - 1)
    curve_quintic = sympy.expand(quintic.subs({middle: minimum, maximum: curve_maximum}, simultaneous=True))
    assert curve_quintic.subs(variable, 1) == 0
    assert sympy.expand(minimum + curve_maximum - sum_bound) == 0
    assert sympy.expand(curve_maximum - minimum - (2 * (minimum - 1) ** 2 - 1)) == 0
    assert sympy.Poly(sympy.expand((curve_maximum - minimum).subs(minimum, 2 + minimum_shift)),
                      minimum_shift).all_coeffs() == [2, 4, 1]
    curve_anchor = minimum ** 4 * (minimum - 1) ** 2 * (2 * minimum - 1) ** 2 * threshold_polynomial
    assert sympy.expand(curve_quintic.subs(variable, minimum) - curve_anchor) == 0
    assert sympy.rem(curve_quintic.subs(variable, minimum), threshold_polynomial, minimum) == 0
    curve_quartic, remainder = sympy.div(curve_quintic, variable - 1, variable)
    assert remainder == 0
    assert sympy.simplify(curve_quartic.subs({minimum: threshold, variable: threshold})) == 0
    maximum_sign = sympy.expand((maximum ** 2 + 2 * maximum - minimum - middle).subs(
        {minimum: 2 + minimum_shift, middle: 2 + minimum_shift + middle_shift,
         maximum: 2 + minimum_shift + middle_shift + maximum_shift}, simultaneous=True))
    assert all(coefficient > 0 for coefficient in sympy.Poly(
        maximum_sign, minimum_shift, middle_shift, maximum_shift).coeffs())
    source = (ROOT / "paper/sections/endpoint-one-spectrum.tex").read_text()
    theorem_and_proof = source.split(r"\begin{corollary}")[0]
    assert r"If in addition $a>2+\sqrt3$" in theorem_and_proof
    assert r"Now assume also $a>2+\sqrt3$" in theorem_and_proof
    assert r"$b+c-(a^2+2a)\geq a^2-4a+1>0$" in theorem_and_proof
    assert r"For integer exponents $4\leq a\leq b\leq c$" in source
    controls = []
    for minimum_value in (sympy.Integer(2), sympy.Integer(3), sympy.Rational(15, 4)):
        exponents = (minimum_value, minimum_value, curve_maximum.subs(minimum, minimum_value))
        values = dict(zip((minimum, middle, maximum), exponents))
        control_matrix = sympy.Matrix(complement_quotient(exponents))
        direct_control = sympy.expand((variable * sympy.eye(6) - control_matrix).det(method="domain-ge"))
        assert sympy.expand(direct_control - determinant.subs(values)) == 0
        control_quintic = sympy.Poly(quintic.subs(values), variable)
        assert control_quintic.eval(1) == 0
        control_quartic, remainder = control_quintic.div(sympy.Poly(variable - 1, variable))
        assert remainder.is_zero
        assert control_quartic.eval(1) != 0
        exponent_sum = sum(exponents)
        upper_window = min(exponents[2], exponents[0] + exponents[1])
        counts = {
            "residual_roots_below_minimum": int(root_count(control_quartic, 0, minimum_value)),
            "residual_roots_in_minimum_upper_window": int(root_count(control_quartic, minimum_value, upper_window)),
            "residual_roots_above_total_sum": int(root_count(control_quartic, exponent_sum, sympy.oo)),
        }
        assert counts["residual_roots_above_total_sum"] == 3
        if minimum_value < threshold:
            assert control_quintic.eval(minimum_value) < 0
            assert counts["residual_roots_below_minimum"] == 1
        else:
            assert control_quintic.eval(minimum_value) > 0
            assert counts["residual_roots_below_minimum"] == 0
            assert counts["residual_roots_in_minimum_upper_window"] == 1
        controls.append({"exponents": list(map(str, exponents)),
                         "minimum_anchor_value": str(control_quintic.eval(minimum_value)),
                         "root_one_simple": True, **counts})
    print(json.dumps({
        "statement": "On real2<=a<=b<=c,h_C(1)=0,a>2+sqrt3: root1simple and smallest positive;residual roots satisfy a<mu1<min(c,a+b),s<mu2<=mu3<=mu4",
        "threshold": str(threshold),
        "generic_minimum_and_maximum_anchor_identities": "passed against direct quotient determinant",
        "sum_bound_threshold_factorization": "passed",
        "sharpness_family": "b=a,c=(a-1)(2a-1),a>=2",
        "sharpness_endpoint_ordering_sum_and_anchor_identities": "passed generically",
        "threshold_residual_root_equals_minimum": "passed exactly over Q(sqrt3)",
        "maximum_anchor_sign": "positive shifted coefficients passed for2<=a<=b<=c",
        "current_statement_and_integer_corollary_scope": "passed",
        "fixed_exact_controls": controls,
        "integer_divisor_corollary_minimum": 4,
        "sympy": sympy.__version__,
        "scope": "Written sharp real-cutoff proof by the established sum bound,principal interlacing and determinant parity. Direct set-disjointness quotient identities and three fixed exact controls:two below the cutoff and one in the newly admitted real range. Shared support constructor/SymPy,no original characteristic-polynomial helper. No parameter scan,new finite base,historical finite-base rerun,graph enumeration,floats or Lean. Existing integer classification/corollary retain their scopes.",
        "status": "passed",
    }, indent=2))


if __name__ == "__main__":
    main()
