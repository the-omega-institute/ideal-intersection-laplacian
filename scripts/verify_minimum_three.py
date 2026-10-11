import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def complement_quotient(exponents):
    supports = [frozenset(support) for size in (1, 2) for support in combinations(range(3), size)]
    weights = [prod(exponents[index] for index in support) for support in supports]
    matrix = [[0] * len(supports) for support in supports]
    for row, source in enumerate(supports):
        for column, target in enumerate(supports):
            if source.isdisjoint(target):
                matrix[row][column] = -weights[column]
                matrix[row][row] += weights[column]
    return matrix


def determinant(matrix):
    entries = [row[:] for row in matrix]
    previous = 1
    sign = 1
    for pivot_index in range(len(entries) - 1):
        if entries[pivot_index][pivot_index] == 0:
            replacement = next((row for row in range(pivot_index + 1, len(entries))
                                if entries[row][pivot_index] != 0), None)
            if replacement is None:
                return 0
            entries[pivot_index], entries[replacement] = entries[replacement], entries[pivot_index]
            sign = -sign
        pivot = entries[pivot_index][pivot_index]
        for row in range(pivot_index + 1, len(entries)):
            for column in range(pivot_index + 1, len(entries)):
                numerator = entries[row][column] * pivot - entries[row][pivot_index] * entries[pivot_index][column]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError("Nonexact Bareiss division")
                entries[row][column] = quotient
            entries[row][pivot_index] = 0
        previous = pivot
    return sign * entries[-1][-1]


def quintic_value(matrix, argument):
    argument = Fraction(argument)
    numerator, denominator = argument.numerator, argument.denominator
    if numerator == 0:
        raise ValueError("Use interpolation to recover the value at zero")
    scaled = [[(numerator if row == column else 0) - denominator * entry
               for column, entry in enumerate(values)] for row, values in enumerate(matrix)]
    return Fraction(determinant(scaled), numerator * denominator ** 5)


def interpolate(values):
    coefficients = [Fraction(0)] * len(values)
    for index, value in enumerate(values):
        node = index + 1
        basis = [Fraction(1)]
        divisor = 1
        for other_node in range(1, len(values) + 1):
            if other_node == node:
                continue
            expanded = [Fraction(0)] * (len(basis) + 1)
            for degree, coefficient in enumerate(basis):
                expanded[degree] -= other_node * coefficient
                expanded[degree + 1] += coefficient
            basis = expanded
            divisor *= node - other_node
        for degree, coefficient in enumerate(basis):
            coefficients[degree] += value * coefficient / divisor
    if any(coefficient.denominator != 1 for coefficient in coefficients):
        raise ArithmeticError("Noninteger characteristic coefficients")
    return [int(coefficient) for coefficient in reversed(coefficients)]


def main():
    archived = json.loads((ROOT / "results/distinct-tail.json").read_text())
    expected = {(3, lower, upper) for lower in range(4, 30) for upper in range(lower + 1, 30)}
    saved = {tuple(case["exponents"]): case for case in archived["cases"]}
    if len(archived["cases"]) != len(saved) or set(saved) != expected:
        raise ValueError("Archived rows do not cover the exact finite domain once")
    counts = Counter()
    negative_ranges = {}
    endpoint_checks = 0
    for exponents in sorted(expected):
        case = saved[exponents]
        matrix = complement_quotient(exponents)
        values = [quintic_value(matrix, argument) for argument in range(1, 7)]
        coefficients = interpolate(values)
        if coefficients != case["quintic_coefficients"] or coefficients[0] != 1 or coefficients[-1] >= 0:
            raise ValueError(f"Characteristic polynomial mismatch at {exponents}")
        lower, upper = exponents[1:]
        endpoint_one = ((lower ** 2 + 8) * upper ** 3
                        + (lower - 1) * (lower ** 2 - 30 * lower - 12) * upper ** 2
                        + 6 * (lower - 1) * (3 * lower + 2) * upper
                        + 4 * (lower - 1) * (lower + 2) * (2 * lower + 1))
        if values[0] != endpoint_one or values[0] != case["h1"] or values[1] != case["h2"]:
            raise ValueError(f"Endpoint mismatch at {exponents}")
        if endpoint_one > 0:
            counts["h1_positive"] += 1
            interval = [Fraction(0), Fraction(1)]
            endpoints = [Fraction(coefficients[-1]), values[0]]
        elif endpoint_one < 0:
            counts["h1_negative"] += 1
            negative_ranges.setdefault(lower, []).append(upper)
            right = Fraction(3, 2) if exponents == (3, 4, 5) else Fraction(2)
            interval = [Fraction(1), right]
            endpoints = [values[0], quintic_value(matrix, right)]
            endpoint_checks += 1
        else:
            raise ValueError(f"Zero endpoint at {exponents}")
        vertices = prod(exponent + 1 for exponent in exponents) - 2
        if endpoints[0] * endpoints[1] >= 0:
            raise ValueError(f"No strict sign change at {exponents}")
        actual = ([str(value) for value in interval], [str(value) for value in endpoints],
                  vertices, [str(vertices - interval[1]), str(vertices - interval[0])])
        stored = (case["complement_interval"], case["endpoint_values"],
                  case["graph_vertex_count"], case["graph_eigenvalue_interval"])
        if actual != stored:
            raise ValueError(f"Root interval or graph lift mismatch at {exponents}")
    ranges = []
    for lower, upper_values in sorted(negative_ranges.items()):
        if upper_values != list(range(min(upper_values), max(upper_values) + 1)):
            raise ValueError("Negative range is not contiguous")
        ranges.append({"b": lower, "c_min": min(upper_values), "c_max": max(upper_values)})
    if ranges != archived["negative_h1_ranges"] or dict(counts) != {"h1_positive": 257, "h1_negative": 68}:
        raise ValueError("Published sign counts or ranges mismatch")
    print(json.dumps({"domain": "a=3, 4<=b<c<30", "cases": len(expected),
                      "counts": dict(counts) | {"h1_zero": 0}, "negative_h1_ranges": ranges,
                      "characteristic_polynomials_matched": len(expected),
                      "bareiss_determinants": 6 * len(expected) + endpoint_checks,
                      "strict_root_intervals_matched": len(expected),
                      "lifted_graph_intervals_matched": len(expected),
                      "exception": {"exponents": [3, 4, 5], "interval": ["1", "3/2"],
                                    "values": ["-3792", "48825/32"]},
                      "method": "Set disjointness quotient, integer Bareiss determinants, rational interpolation; standard library only",
                      "shared_input": "Six support-class model and archived finite certificate; no original checker/helper imports",
                      "scope": "Finite input to Theorem4.4, including strict sign intervals and graph reflection. Written infinite cutoff and earlier theorems remain required; no new theorem or Lean.",
                      "status": "passed"}, indent=2))


if __name__ == "__main__":
    main()
