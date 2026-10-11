import json
import re
from pathlib import Path

import sympy

from verify_largest_root_coefficients import coefficient_table
from verify_minimum_three import complement_quotient


ROOT = Path(__file__).resolve().parents[1]


def positive_shift(expression, minimum, minimum_shift, middle_shift):
    polynomial = sympy.Poly(sympy.expand(expression.subs(minimum, 4 + minimum_shift)),
                            minimum_shift, middle_shift)
    assert all(coefficient > 0 for coefficient in polynomial.coeffs())
    return len(polynomial.terms())


def main():
    minimum, middle, maximum, variable = sympy.symbols("a b c x")
    minimum_shift, middle_shift, maximum_shift = sympy.symbols("m t u")
    tail_shift = sympy.Symbol("v")
    matrix = sympy.Matrix(complement_quotient((minimum, middle, maximum)))
    determinant = sympy.expand((variable * sympy.eye(6) - matrix).det(method="domain-ge"))
    quintic, remainder = sympy.div(determinant, variable, variable)
    assert remainder == 0
    endpoint = quintic.subs(variable, 2)
    first_factor = (2 * middle_shift ** 2 + 7 * (minimum - 2) * middle_shift
                    + 2 * (3 * minimum ** 2 - 14 * minimum + 12))
    second_factor = ((minimum + 2) * middle_shift ** 3
                     + (4 * minimum ** 2 + 10 * minimum - 12) * middle_shift ** 2
                     + (4 * minimum ** 3 + 25 * minimum ** 2 - 48 * minimum + 12) * middle_shift
                     + 2 * (13 * minimum ** 3 - 28 * minimum ** 2 + 8 * minimum + 8))
    quadratic_coefficient = (2 * (minimum - 2) * (9 * minimum ** 3 + 24 * minimum ** 2 - 56 * minimum + 16)
                             + (33 * minimum ** 3 + 20 * minimum ** 2 - 208 * minimum + 136) * middle_shift
                             + (20 * minimum ** 2 + 23 * minimum - 62) * middle_shift ** 2
                             + 4 * (minimum + 2) * middle_shift ** 3)
    cubic_coefficient = (2 * (3 * minimum ** 3 - minimum ** 2 - 8 * minimum + 4)
                         + (5 * minimum ** 2 + 3 * minimum - 10) * middle_shift
                         + (minimum + 2) * middle_shift ** 2)
    middle_boundary = 2 * minimum - 2 + middle_shift
    direct_middle = endpoint.subs({middle: middle_boundary, maximum: middle_boundary + tail_shift},
                                  simultaneous=True)
    product = first_factor * second_factor
    middle_identity = (product + sympy.diff(product, middle_shift) * tail_shift / 2
                       + quadratic_coefficient * tail_shift ** 2 + cubic_coefficient * tail_shift ** 3)
    assert sympy.expand(direct_middle - middle_identity) == 0
    factor_counts = [positive_shift(expression, minimum, minimum_shift, middle_shift)
                     for expression in (first_factor, second_factor, quadratic_coefficient, cubic_coefficient)]
    middle_parameter = (minimum + (2 * minimum - 2) * middle_shift) / (1 + middle_shift)
    maximum_boundary = sympy.Rational(9, 4) * minimum - 8
    scaled_maximum = sympy.cancel(64 * (1 + middle_shift) ** 3 * endpoint.subs(
        {middle: middle_parameter, maximum: maximum_boundary + tail_shift}, simultaneous=True))
    squares = (9 * minimum_shift ** 6 * (1 + 2 * middle_shift)
               * (14 * (1 - middle_shift) ** 2 + 5 * middle_shift + middle_shift ** 2)
               + 308 * minimum_shift ** 5 * middle_shift * (middle_shift - 1) ** 2)
    residual = sympy.expand(scaled_maximum.subs(minimum, 8 + minimum_shift) - squares)
    difference_five = sympy.expand(4 * endpoint - quintic.subs(variable, 5))
    shifted_five = sympy.expand(difference_five.subs(
        {minimum: 8 + minimum_shift, middle: 8 + middle_shift, maximum: 8 + maximum_shift},
        simultaneous=True))
    difference_four = sympy.expand(quintic.subs(variable, 4) - 3 * endpoint)
    upper_middle = minimum * (1 + 2 * middle_shift) / (1 + middle_shift)
    upper_maximum = minimum * (4 + 9 * maximum_shift) / (4 * (1 + maximum_shift))
    scaled_four = sympy.cancel(64 * (1 + middle_shift) ** 3 * (1 + maximum_shift) ** 3
                               * difference_four.subs({middle: upper_middle, maximum: upper_maximum},
                                                       simultaneous=True))
    shifted_four = sympy.expand(scaled_four.subs(minimum, 40 + minimum_shift))
    inverse_middle = (middle - minimum) / (2 * minimum - 2 - middle)
    inverse_upper_middle = (middle - minimum) / (2 * minimum - middle)
    inverse_upper_maximum = 4 * (maximum - minimum) / (9 * minimum - 4 * maximum)
    for parameter, inverse, argument, target in (
            (middle_parameter, inverse_middle, middle_shift, middle),
            (upper_middle, inverse_upper_middle, middle_shift, middle),
            (upper_maximum, inverse_upper_maximum, maximum_shift, maximum)):
        assert sympy.cancel(parameter.subs(argument, inverse) - target) == 0
    source = (ROOT / "paper/sections/endpoint-two-identities.tex").read_text()
    sections = source.split(r"\subsection")
    reports = {}
    for index, label, expression, last_shift, expected_count, expected_constant in (
            (1, "maximum_bound_residual", residual, tail_shift, 84, 3014656),
            (2, "difference_at_five", shifted_five, maximum_shift, 44, 4629843),
            (3, "difference_at_four", shifted_four, maximum_shift, 112, 611305472)):
        displayed, row_count, coefficient_count = coefficient_table(
            sections[index], minimum_shift, middle_shift, last_shift, allow_zero_rows=index == 2)
        assert sympy.expand(displayed - expression) == 0
        assert len(sympy.Poly(expression, minimum_shift, middle_shift, last_shift).terms()) == expected_count
        assert coefficient_count == expected_count
        assert displayed.subs({minimum_shift: 0, middle_shift: 0, last_shift: 0}) == expected_constant
        reports[label] = {"rows": row_count, "positive_coefficients": coefficient_count,
                          "constant": expected_constant, "displayed_table_identity": "passed"}
    assert re.search(r"^3 & 3 & \$\[0\]\$", sections[2], re.MULTILINE)
    displayed_counts = {}
    count_rows = re.findall(r"^([0-9]+) & ([0-9]+) & ([0-9]+) & ([0-9]+) ", sections[4], re.MULTILINE)
    for row in count_rows:
        for minimum_text, count_text in (row[:2], row[2:]):
            minimum_value = int(minimum_text)
            assert minimum_value not in displayed_counts
            displayed_counts[minimum_value] = int(count_text)
    assert set(displayed_counts) == set(range(8, 40))
    for minimum_value, displayed_count in displayed_counts.items():
        maximum_integer = (9 * minimum_value - 33) // 4
        middle_upper = min(2 * minimum_value - 3, maximum_integer - 1)
        middle_count = max(0, middle_upper - minimum_value)
        computed_count = (middle_count * maximum_integer
                          - middle_count * (minimum_value + 1 + middle_upper) // 2)
        assert displayed_count == computed_count
        assert sympy.Rational(9 * minimum_value - 32, 4) > maximum_integer
        assert sympy.Rational(9 * minimum_value - 32, 4) <= maximum_integer + 1
    assert displayed_counts[8] == 0
    assert sum(displayed_counts.values()) == 8658
    for document in ("classification-core.tex", "paper.tex"):
        assert r"\input{sections/endpoint-two-identities}" in (ROOT / "paper" / document).read_text()
    print(json.dumps({
        "middle_bound_generic_identity": "passed against direct quotient determinant",
        "middle_bound_four_positive_factor_term_counts": factor_counts,
        "rational_parameter_inverses": "all three passed",
        "manuscript_coefficient_tables": reports,
        "total_displayed_positive_coefficients": sum(report["positive_coefficients"] for report in reports.values()),
        "difference_at_five_absent_component": "the displayed t^3*u^3 row is exactly [0]",
        "finite_domain_count_formula": "n*c_max-n*(a+1+b_max)/2, c_max=(9a-33)//4, b_max=min(2a-3,c_max-1), n=max(0,b_max-a)",
        "all_32_displayed_per_minimum_counts": dict(sorted(displayed_counts.items())),
        "finite_domain_total": 8658,
        "minimum_eight_count": 0,
        "strict_integer_maximum_boundary": "passed for minima8through39",
        "main_and_supporting_table_inclusions": "passed",
        "sympy": sympy.__version__,
        "scope": "Direct determinant reconstruction and literal manuscript-table/count verification; shared set-disjointness model, table parser and SymPy backend, no original characteristic helper. Two square expressions are nonnegative by their displayed form. Written root-location/domain-cover arguments reviewed separately. No endpoint evaluation on the8658triple base, historical finite-base rerun, parameter scan, graph enumeration, floats or Lean.",
        "status": "passed",
    }, indent=2))


if __name__ == "__main__":
    main()
