import json
import re
from pathlib import Path

import sympy

from verify_minimum_three import complement_quotient


ROOT = Path(__file__).resolve().parents[1]


def coefficient_table(content, minimum_shift, middle_shift, maximum_shift):
    rows = re.findall(r"^([0-9]+) & ([0-9]+) & \$\[([^\]]+)\]\$", content, re.MULTILINE)
    polynomial = 0
    indices = set()
    coefficient_count = 0
    for middle_power, maximum_power, vector in rows:
        powers = (int(middle_power), int(maximum_power))
        assert powers not in indices
        indices.add(powers)
        coefficients = [int(value.strip()) for value in vector.replace(r"\allowbreak", "").split(",")]
        assert all(coefficient > 0 for coefficient in coefficients)
        coefficient_count += len(coefficients)
        polynomial += middle_shift ** powers[0] * maximum_shift ** powers[1] * sum(
            coefficient * minimum_shift ** degree for degree, coefficient in enumerate(coefficients))
    assert rows
    return sympy.expand(polynomial), len(rows), coefficient_count


def main():
    minimum, middle, maximum, variable = sympy.symbols("a b c x")
    minimum_shift, middle_shift, maximum_shift = sympy.symbols("m u v")
    matrix = sympy.Matrix(complement_quotient((minimum, middle, maximum)))
    determinant = sympy.expand((variable * sympy.eye(6) - matrix).det(method="domain-ge"))
    quintic, remainder = sympy.div(determinant, variable, variable)
    assert remainder == 0
    exponent_sum = minimum + middle + maximum
    diagonal_numerators = [(variable - exponent_sum) * (variable - exponent)
                           - variable * sympy.prod(other for other in (minimum, middle, maximum)
                                                   if other != exponent)
                           for exponent in (minimum, middle, maximum)]
    schur_determinant = sympy.prod(diagonal_numerators) + sum(
        exponent * (variable - exponent)
        * sympy.prod(diagonal_numerators[other] for other in range(3) if other != index)
        for index, exponent in enumerate((minimum, middle, maximum)))
    assert sympy.expand(determinant - schur_determinant) == 0
    anchor = middle * maximum + exponent_sum
    lower_positive = ((2 * middle ** 2 - minimum * middle + middle - minimum) * maximum ** 2
                      - ((minimum - 1) * middle ** 2 + minimum ** 2) * maximum
                      - minimum * middle * (minimum + middle))
    assert sympy.expand(quintic.subs(variable, anchor)
                        + minimum ** 2 * middle * maximum * lower_positive) == 0
    upper_positive = sympy.expand(quintic.subs(variable, anchor + 1))
    substitutions = {minimum: 3 + minimum_shift,
                     middle: 6 + minimum_shift + middle_shift,
                     maximum: (3 + minimum_shift) ** 2 - (3 + minimum_shift) + maximum_shift}
    source = (ROOT / "paper/sections/largest-root-identities.tex").read_text()
    sections = source.split(r"\subsection")
    reports = {}
    for index, label, expression, expected_count, expected_constant in (
            (1, "lower", lower_positive, 36, 1404),
            (2, "upper", upper_positive, 170, 513220)):
        displayed, row_count, coefficient_count = coefficient_table(
            sections[index], minimum_shift, middle_shift, maximum_shift)
        reconstructed = sympy.expand(expression.subs(substitutions, simultaneous=True))
        assert sympy.expand(displayed - reconstructed) == 0
        assert len(sympy.Poly(reconstructed, minimum_shift, middle_shift, maximum_shift).terms()) == expected_count
        assert coefficient_count == expected_count
        assert displayed.subs({minimum_shift: 0, middle_shift: 0, maximum_shift: 0}) == expected_constant
        reports[label] = {"rows": row_count, "positive_coefficients": coefficient_count,
                          "constant": expected_constant, "displayed_table_identity": "passed"}
    lower_diagonal_bounds = [maximum * (middle - minimum) + 1 - minimum,
                             middle * (maximum - minimum) + 1 - minimum]
    for expression in lower_diagonal_bounds:
        assert all(coefficient > 0 for coefficient in sympy.Poly(
            sympy.expand(expression.subs(substitutions, simultaneous=True)),
            minimum_shift, middle_shift, maximum_shift).coeffs())
    assert sympy.expand(minimum ** 2 - minimum - (minimum + 3)
                        - (minimum - 3) * (minimum + 1)) == 0
    endpoint = quintic.subs(variable, 1)
    for gap in (1, 2):
        cubic = sympy.Poly(endpoint.subs(middle, minimum + gap), maximum)
        assert cubic.degree() == 3
        for expression in (cubic.LC(), cubic.eval(0)):
            assert all(coefficient > 0 for coefficient in sympy.Poly(
                sympy.expand(expression.subs(minimum, 8 + minimum_shift)), minimum_shift).coeffs())
    small_gap_rows = re.findall(r"^([12]) & (.*?) & \$\[([^\]]+)\]\$", sections[3], re.MULTILINE)
    vectors = []
    labels = set()
    for gap_text, label, vector in small_gap_rows:
        gap = int(gap_text)
        label = label.strip("$")
        assert (gap, label) not in labels
        labels.add((gap, label))
        boundary = 2 * minimum ** 2 + (2 * gap - 3) * minimum - (2 if gap == 1 else 6)
        candidate = {r"-Q(b)": minimum + gap, r"-Q(L_d)": boundary,
                     r"Q(L_d+1)": boundary + 1}[label]
        sign = 1 if label == r"Q(L_d+1)" else -1
        expression = sympy.expand(sign * endpoint.subs(middle, minimum + gap)
                                  .subs(maximum, candidate).subs(minimum, 8 + minimum_shift))
        coefficients = [int(value.strip()) for value in vector.replace(r"\allowbreak", "").split(",")]
        assert all(coefficient > 0 for coefficient in coefficients)
        assert sympy.expand(expression - sum(coefficient * minimum_shift ** degree
                                            for degree, coefficient in enumerate(coefficients))) == 0
        assert all(coefficient > 0 for coefficient in sympy.Poly(
            sympy.expand((boundary - minimum - gap).subs(minimum, 8 + minimum_shift)),
            minimum_shift).coeffs())
        vectors.append({"gap": gap, "expression": label, "coefficients": coefficients})
    assert len(vectors) == 6
    total_coefficients = sum(report["positive_coefficients"] for report in reports.values()) + sum(
        len(vector["coefficients"]) for vector in vectors)
    assert total_coefficients == 247
    for document in ("classification-core.tex", "paper.tex"):
        assert r"\input{sections/largest-root-identities}" in (ROOT / "paper" / document).read_text()
    print(json.dumps({
        "generic_direct_determinant_and_schur_identity": "passed",
        "lower_endpoint_identity": "passed",
        "manuscript_coefficient_tables": reports,
        "upper_schur_diagonal_lower_bounds": "positive coefficient expansions passed",
        "small_gap_displayed_vectors": vectors,
        "small_gap_boundary_above_middle": "passed at real a>=8",
        "small_gap_cubic_degree_and_positive_leading_constant": "passed for gaps1and2",
        "total_displayed_coefficients": total_coefficients,
        "main_and_supporting_table_inclusions": "passed",
        "sympy": sympy.__version__,
        "scope": "Independent direct determinant reconstruction and literal manuscript-table check; shared set-disjointness quotient constructor and SymPy backend. Written root-location and degree-exhaustion arguments reviewed separately. No historical finite-base rerun, exponent scan, graph enumeration, floats or Lean.",
        "status": "passed",
    }, indent=2))


if __name__ == "__main__":
    main()
