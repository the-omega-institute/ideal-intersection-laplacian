import json
from pathlib import Path

import sympy

from verify_minimum_three import complement_quotient


ROOT = Path(__file__).resolve().parents[1]


def root_count(polynomial, lower, upper):
    return int(sum(multiplicity * factor.count_roots(lower, upper)
                   for factor, multiplicity in polynomial.sqf_list()[1]))


def main():
    minimum, middle, variable = sympy.symbols("a b x")
    maximum = middle * (middle + 2) - minimum
    matrix = sympy.Matrix(complement_quotient((minimum, middle, maximum)))
    weights = sympy.diag(minimum, middle, maximum, minimum * middle,
                        minimum * maximum, middle * maximum)
    assert sympy.simplify(weights * matrix - matrix.T * weights) == sympy.zeros(6)
    assert matrix * sympy.ones(6, 1) == sympy.zeros(6, 1)
    indices = [0, 2, 3, 5]
    principal = matrix.extract(indices, indices)
    principal_determinant = sympy.expand((variable * sympy.eye(4) - principal).det(method="domain-ge"))
    cubic = (variable ** 3 - middle * (middle ** 2 + 4 * middle + 5) * variable ** 2
             + (minimum * maximum * (middle ** 2 + 1)
                + middle ** 2 * (middle + 2) * (middle ** 2 + 3 * middle + 3)) * variable
             - minimum * middle * maximum * (middle + 3))
    assert sympy.expand(principal_determinant - (variable - middle) * cubic) == 0
    positive_at_middle = middle * (middle + 1) * (
        minimum * (middle - minimum) * (middle - 2)
        + minimum * middle * (middle - 2) * (middle + 1)
        + middle ** 2 * (middle + 1) * (middle + 2))
    assert sympy.expand(cubic.subs(variable, middle) - positive_at_middle) == 0
    assert matrix.extract([3, 5], [3, 5]) == sympy.diag(maximum, minimum)
    kept = [0, 2, 3, 4, 5]
    assert matrix[4, 4] == middle
    assert all(matrix[4, index] == matrix[index, 4] == 0 for index in kept if index != 4)
    assert sympy.cancel(weights[4, 4] * matrix[4, 1] ** 2 / weights[1, 1]
                        - minimum * middle * maximum) == 0
    assert sympy.expand(maximum - middle - (middle ** 2 + middle - minimum)) == 0
    determinant = sympy.expand((variable * sympy.eye(6) - matrix).det(method="domain-ge"))
    assert sympy.expand(determinant.subs(variable, middle)) == 0
    minimum_shift, gap = sympy.symbols("m t")
    shifted_positive = sympy.Poly(sympy.expand(positive_at_middle.subs(
        {minimum: 2 + minimum_shift, middle: 2 + minimum_shift + gap}, simultaneous=True)),
                                 minimum_shift, gap)
    assert all(coefficient > 0 for coefficient in shifted_positive.coeffs())
    controls = []
    for minimum_value, middle_value in ((2, 2), (2, 3), (3, 3)):
        maximum_value = middle_value * (middle_value + 2) - minimum_value
        exponent_sum = minimum_value + middle_value + maximum_value
        specialized = sympy.Poly(determinant.subs(
            {minimum: minimum_value, middle: middle_value}), variable)
        remaining, remainder = specialized.div(sympy.Poly(variable * (variable - middle_value), variable))
        assert remainder.is_zero and remaining.degree() == 4
        assert remaining.eval(0) != 0 and remaining.eval(middle_value) != 0
        assert remaining.eval(exponent_sum) != 0
        counts = [root_count(remaining, lower, upper)
                  for lower, upper in ((0, middle_value), (middle_value, exponent_sum),
                                       (exponent_sum, sympy.oo))]
        assert counts == [1, 0, 3]
        controls.append({"exponents": [minimum_value, middle_value, maximum_value],
                         "characteristic_factorization": str(sympy.factor(specialized.as_expr())),
                         "root_b_multiplicity": 1,
                         "remaining_root_counts_0_b__b_s__s_infinity": counts})
    source = (ROOT / "paper/sections/endpoint-one-spectrum.tex").read_text()
    proposition = source.split(r"\label{prop:endpoint-one-equality-spectrum}", 1)[1]
    assert r"For real $2\leq a\leq b$" in proposition
    print(json.dumps({
        "real_domain": "2<=a<=b, c=b(b+2)-a",
        "weighted_symmetry_and_zero_vector": "passed",
        "four_support_principal_factorization": "passed against direct determinant",
        "cubic_value_at_middle_identity": "passed",
        "positive_shifted_cubic_value_terms": len(shifted_positive.terms()),
        "middle_root_generic_identity": "passed against direct six-support determinant",
        "pair_principal_block": "diag(c,a) passed",
        "isolated_b_in_five_support_principal_block": "passed",
        "nonzero_symmetric_coupling_squared": "abc identity passed",
        "ordering_identity": "c-b=b^2+(b-a) passed",
        "fixed_exact_controls": controls,
        "manuscript_domain": "real minimum two passed",
        "sympy": sympy.__version__,
        "scope": "Generic determinant, weighted-symmetry, principal-block and coupling identities; three specified exact root-count controls, with squarefree-factor multiplicities. Shares set-disjointness model and SymPy backend, no original characteristic helper. Root index/simplicity and conditional endpoint-one cubic separation have written proofs. No parameter scan, integer-point enumeration, historical finite-base rerun, expanded graph, floats or Lean.",
        "status": "passed",
    }, indent=2))


if __name__ == "__main__":
    main()
