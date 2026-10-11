import csv
import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def bareiss_determinant(matrix):
    size = len(matrix)
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if matrix[pivot_index][pivot_index] == 0:
            replacement = next((row for row in range(pivot_index + 1, size)
                                if matrix[row][pivot_index] != 0), None)
            if replacement is None:
                return 0
            matrix[pivot_index], matrix[replacement] = matrix[replacement], matrix[pivot_index]
            sign = -sign
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = pivot * matrix[row][column] - matrix[row][pivot_index] * matrix[pivot_index][column]
                assert numerator % previous == 0
                matrix[row][column] = numerator // previous
            matrix[row][pivot_index] = 0
        previous = pivot
    return sign * matrix[-1][-1]


def quintic_discriminant(coefficients):
    assert len(coefficients) == 6 and coefficients[0] == 1
    derivative = [coefficient * (5 - index) for index, coefficient in enumerate(coefficients[:-1])]
    sylvester = [[0] * 9 for row in range(9)]
    for row in range(4):
        sylvester[row][row:row + 6] = coefficients
    for row in range(5):
        sylvester[row + 4][row:row + 5] = derivative
    return bareiss_determinant(sylvester)


first, second, third, variable = sympy.symbols('a b c x')
generic_quotient = support_quotient((first, second, third))
quintic = sympy.Poly(sympy.cancel(generic_quotient.charpoly(variable).as_expr() / variable), variable)
specialize = sympy.lambdify((first, second, third), quintic.all_coeffs(), modules='math', cse=True)
certificate_path = Path('results/open-region-discriminants.csv')
checked = 0
counts = {}
with certificate_path.open(newline='') as stream:
    rows = csv.DictReader(stream)
    assert rows.fieldnames == ['a', 'b', 'c', 'discriminant', 'floor_sqrt']
    for minimum in range(4, 8):
        cutoff = 4 * minimum ** 2 - 2 * minimum
        counts[minimum] = 0
        for middle in range(minimum + 1, cutoff - 1):
            for maximum in range(middle + 1, cutoff):
                row = next(rows)
                assert [int(row[key]) for key in ('a', 'b', 'c')] == [minimum, middle, maximum]
                discriminant = int(row['discriminant'])
                root_floor = int(row['floor_sqrt'])
                assert root_floor >= 0 and root_floor ** 2 < discriminant < (root_floor + 1) ** 2
                coefficients = specialize(minimum, middle, maximum)
                assert all(isinstance(value, int) for value in coefficients)
                assert quintic_discriminant(coefficients) == discriminant
                checked += 1
                counts[minimum] += 1
    assert next(rows, None) is None
assert counts == {4: 1275, 5: 3486, 6: 7750, 7: 15051}
assert checked == 27562
print(json.dumps({'complete_requested_domain': '4<=a<=7, a<b<c<4a^2-2a',
                  'counts_by_minimum': counts, 'total_checked': checked,
                  'strict_integer_square_brackets': 'passed for all27562discriminants',
                  'independent_discriminant_reconstruction': 'Integer9x9Sylvester determinants with fraction-free Bareiss elimination; every exact division checked; all match the SymPy-generated CSV.',
                  'certificate_sha256': hashlib.sha256(certificate_path.read_bytes()).hexdigest(),
                  'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'scope': 'Complete finite certificate within the uniform cutoff for minimum4,5,6,7. Combined with the written tail and prior repeated/minimum-three theorems, this certifies every minimum-entry<=7 triple. Does not bound the minimum exponent in general; fullQ3open. No Lean.'}, indent=2))
