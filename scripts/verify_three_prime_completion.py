import argparse
import csv
import hashlib
from itertools import permutations
import json
from pathlib import Path


class IntegerPolynomial:
    def __init__(self, coefficients):
        self.coefficients = {powers: value for powers, value in coefficients.items() if value}

    @staticmethod
    def constant(value):
        return IntegerPolynomial({(0, 0, 0): value})

    def __add__(self, other):
        if isinstance(other, int):
            other = self.constant(other)
        coefficients = self.coefficients.copy()
        for powers, value in other.coefficients.items():
            coefficients[powers] = coefficients.get(powers, 0) + value
        return IntegerPolynomial(coefficients)

    __radd__ = __add__

    def __neg__(self):
        return IntegerPolynomial({powers: -value for powers, value in self.coefficients.items()})

    def __sub__(self, other):
        if isinstance(other, int):
            other = self.constant(other)
        return self + -other

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if isinstance(other, int):
            other = self.constant(other)
        coefficients = {}
        for first_powers, first_value in self.coefficients.items():
            for second_powers, second_value in other.coefficients.items():
                powers = tuple(first + second for first, second in zip(first_powers, second_powers))
                coefficients[powers] = coefficients.get(powers, 0) + first_value * second_value
        return IntegerPolynomial(coefficients)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        result = self.constant(1)
        for index in range(exponent):
            result = result * self
        return result

    def __eq__(self, other):
        return isinstance(other, IntegerPolynomial) and self.coefficients == other.coefficients


def determinant_from_supports(exponents, argument):
    supports = (1, 2, 4, 3, 5, 6)
    weights = []
    for support in supports:
        weight = IntegerPolynomial.constant(1)
        for index, exponent in enumerate(exponents):
            if support & (1 << index):
                weight = weight * exponent
        weights.append(weight)
    entries = []
    for row, support in enumerate(supports):
        diagonal = argument
        for column, neighbor in enumerate(supports):
            if row != column and not support & neighbor:
                diagonal = diagonal - weights[column]
        entries.append([diagonal if row == column else
                        weights[column] if not support & neighbor else IntegerPolynomial.constant(0)
                        for column, neighbor in enumerate(supports)])
    determinant = IntegerPolynomial.constant(0)
    nonzero_products = 0
    for permutation in permutations(range(6)):
        product = IntegerPolynomial.constant(1)
        for row, column in enumerate(permutation):
            if not entries[row][column].coefficients:
                break
            product = product * entries[row][column]
        else:
            inversions = sum(permutation[first] > permutation[second]
                             for first in range(6) for second in range(first + 1, 6))
            determinant = determinant + (-product if inversions % 2 else product)
            nonzero_products += 1
    return determinant, nonzero_products


def read_table(table):
    coefficients = {}
    for row in table['rows']:
        for minimum_power, value in enumerate(row['ascending_minimum_coefficients']):
            powers = (minimum_power, row['middle_power'], row['maximum_power'])
            assert powers not in coefficients
            assert isinstance(value, int) and value > 0
            coefficients[powers] = value
    polynomial = IntegerPolynomial(coefficients)
    assert len(polynomial.coefficients) == table['nonzero_terms']
    assert polynomial.coefficients[(0, 0, 0)] == table['constant']
    return polynomial


def univariate(vector):
    return IntegerPolynomial({(degree, 0, 0): value for degree, value in enumerate(vector)})


def exact_polynomial_quotient(dividend, divisor):
    remainder = dividend
    quotient = IntegerPolynomial.constant(0)
    divisor_powers = max(divisor.coefficients)
    divisor_coefficient = divisor.coefficients[divisor_powers]
    while remainder.coefficients:
        leading_powers = max(remainder.coefficients)
        powers = tuple(first - second for first, second in zip(leading_powers, divisor_powers))
        coefficient = remainder.coefficients[leading_powers]
        assert all(power >= 0 for power in powers)
        assert coefficient % divisor_coefficient == 0
        term = IntegerPolynomial({powers: coefficient // divisor_coefficient})
        quotient = quotient + term
        remainder = remainder - term * divisor
    return quotient


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def finite_certificate_coverage(root):
    small_path = root / 'results/open-region-discriminants.csv'
    endpoint_path = root / 'results/endpoint-two-completion-base.csv'
    small_manifest = json.loads((root / 'results/open-region-certificate-check.json').read_text())
    endpoint_manifest = json.loads((root / 'results/endpoint-two-completion.json').read_text())
    assert digest(small_path) == small_manifest['certificate_sha256']
    assert digest(endpoint_path) == endpoint_manifest['finite_base_csv_sha256']
    small_domain = {(minimum, middle, maximum)
                    for minimum in range(4, 8)
                    for middle in range(minimum + 1, 4 * minimum ** 2 - 2 * minimum - 1)
                    for maximum in range(middle + 1, 4 * minimum ** 2 - 2 * minimum)}
    endpoint_domain = {(minimum, middle, maximum)
                       for minimum in range(8, 40)
                       for middle in range(minimum + 1, 2 * minimum - 2)
                       for maximum in range(middle + 1, (9 * minimum - 33) // 4 + 1)}
    assert len(small_domain) == 27562
    assert len(endpoint_domain) == 8658
    report = {}
    for label, path, domain in (('minimum_through_seven', small_path, small_domain),
                                ('endpoint_two', endpoint_path, endpoint_domain)):
        seen = set()
        counts = {}
        with path.open(newline='') as stream:
            for row in csv.DictReader(stream):
                triple = tuple(int(row[field]) for field in ('a', 'b', 'c'))
                assert triple in domain and triple not in seen
                seen.add(triple)
                counts[triple[0]] = counts.get(triple[0], 0) + 1
                if label == 'minimum_through_seven':
                    discriminant = int(row['discriminant'])
                    square_floor = int(row['floor_sqrt'])
                    assert square_floor >= 0 and square_floor ** 2 < discriminant < (square_floor + 1) ** 2
                else:
                    value = int(row['h_C_at_two_integer_Horner'])
                    determinant = int(row['det_two_I_minus_C_integer_Bareiss'])
                    assert value != 0 and determinant == 2 * value
        assert seen == domain
        report[label] = {'complete_rows': len(seen), 'duplicate_or_missing_rows': 0,
                         'counts_by_minimum': counts, 'sha256': digest(path)}
    report['scope'] = ('Saved CSV coverage, uniqueness, strict square brackets and stored determinant/Horner agreement only. '
                       'Discriminants and historical determinant calculations are not recomputed; their prior verifiers remain dependencies.')
    return report


def check_manuscript_tables(path, certificate):
    source = path.read_text()
    checked = 0
    for table in certificate['complete_positive_tables'].values():
        for row in table['rows']:
            vector = r',\allowbreak '.join(map(str, row['ascending_minimum_coefficients']))
            assert '{} & {} & $[{}]$'.format(row['middle_power'], row['maximum_power'], vector) in source
            checked += 1
    for gap, data in certificate['preserved_small_gap_written_signs'].items():
        for field, expression in (('ascending_diagonal_negative_vector', r'$-Q(b)$'),
                                  ('ascending_lower_negative_vector', r'$-Q(L_d)$'),
                                  ('ascending_upper_positive_vector', r'$Q(L_d+1)$')):
            vector = r',\allowbreak '.join(map(str, data[field]))
            assert '{} & {} & $[{}]$'.format(gap, expression, vector) in source
            checked += 1
    return {'matched_rows': checked, 'sha256': digest(path)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manuscript-table', type=Path)
    arguments = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    certificate_path = root / 'results/largest-root-unit-interval.json'
    certificate = json.loads(certificate_path.read_text())
    minimum_shift = IntegerPolynomial({(1, 0, 0): 1})
    middle_shift = IntegerPolynomial({(0, 1, 0): 1})
    maximum_shift = IntegerPolynomial({(0, 0, 1): 1})
    minimum = 3 + minimum_shift
    middle = minimum + 3 + middle_shift
    maximum = minimum ** 2 - minimum + maximum_shift
    anchor = middle * maximum + minimum + middle + maximum
    lower = read_table(certificate['complete_positive_tables']['lower'])
    upper = read_table(certificate['complete_positive_tables']['upper'])
    determinant_checks = []
    independently_computed_extracts = {}
    for offset, expected in ((0, -anchor * minimum ** 2 * middle * maximum * lower),
                              (1, (anchor + 1) * upper)):
        actual, products = determinant_from_supports((minimum, middle, maximum), anchor + offset)
        assert actual == expected
        divisor = -anchor * minimum ** 2 * middle * maximum if offset == 0 else anchor + 1
        reconstructed = exact_polynomial_quotient(actual, divisor)
        assert reconstructed == (lower if offset == 0 else upper)
        sample_powers = ((0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (0, 0, 1))
        independently_computed_extracts['lower' if offset == 0 else 'upper'] = [
            {'powers_m_u_v': powers, 'coefficient': reconstructed.coefficients[powers]}
            for powers in sample_powers]
        determinant_checks.append({'offset': offset, 'leibniz_permutations': 720,
                                   'nonzero_products': products, 'full_polynomial_terms': len(actual.coefficients),
                                   'coefficientwise_identity': 'passed'})
    minimum = 8 + minimum_shift
    small_gap_checks = []
    for gap, data in certificate['preserved_small_gap_written_signs'].items():
        middle = minimum + int(gap)
        anchor = 2 * minimum ** 2 - minimum - 2 if gap == '1' else 2 * minimum ** 2 + minimum - 6
        for label, maximum, sign, field in (
            ('diagonal', middle, -1, 'ascending_diagonal_negative_vector'),
            ('lower', anchor, -1, 'ascending_lower_negative_vector'),
            ('upper', anchor + 1, 1, 'ascending_upper_positive_vector')):
            actual, products = determinant_from_supports((minimum, middle, maximum), IntegerPolynomial.constant(1))
            vector = data[field]
            assert all(isinstance(value, int) and value > 0 for value in vector)
            assert actual * sign == univariate(vector)
            small_gap_checks.append({'gap': int(gap), 'boundary': label,
                                     'leibniz_permutations': 720, 'nonzero_products': products,
                                     'positive_terms': len(vector), 'coefficientwise_identity': 'passed'})
    report = {'method': 'Python standard library only; sparse integer polynomial ring and direct six-by-six Leibniz determinant from disjoint supports. No SymPy, floating arithmetic or original checker imports.',
              'largest_root_determinant_checks': determinant_checks,
              'complete_positive_terms': {'lower': len(lower.coefficients), 'upper': len(upper.coefficients)},
              'independently_computed_five_term_extracts': independently_computed_extracts,
              'small_gap_determinant_checks': small_gap_checks,
              'generic_polynomial_determinants': 8,
              'finite_certificate_coverage': finite_certificate_coverage(root),
              'source_certificate_sha256': digest(certificate_path), 'script_sha256': digest(Path(__file__)),
              'scope': 'Independent exact polynomial identities for the written unbounded largest-root and small-gap steps, plus saved finite-certificate integrity/coverage. No new nonintegrality theorem, no exponent-range expansion or historical determinant rerun. Full higher-prime nonsquarefree Q3 and original orthogonality n=7 stay open; no Lean.'}
    if arguments.manuscript_table:
        report['manuscript_table_agreement'] = check_manuscript_tables(arguments.manuscript_table, certificate)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
