import hashlib
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path


def integer_determinant(entries):
    size = len(entries)
    result = 0
    for permutation in permutations(range(size)):
        product = 1
        for row, column in enumerate(permutation):
            product *= entries[row][column]
            if not product:
                break
        if product:
            inversions = sum(permutation[first] > permutation[second]
                             for first in range(size) for second in range(first + 1, size))
            result += -product if inversions % 2 else product
    return result


def complement_matrix(exponents):
    supports = (1, 2, 4, 3, 5, 6)
    weights = []
    for support in supports:
        weight = 1
        for index, exponent in enumerate(exponents):
            if support & (1 << index):
                weight *= exponent
        weights.append(weight)
    entries = []
    for row, support in enumerate(supports):
        diagonal = sum(weights[column] for column, neighbor in enumerate(supports)
                       if row != column and not support & neighbor)
        entries.append([diagonal if row == column else
                        -weights[column] if not support & neighbor else 0
                        for column, neighbor in enumerate(supports)])
    return entries


def quotient_value(entries, argument):
    argument = Fraction(argument)
    size = len(entries)
    if not argument:
        negative = [[-value for value in row] for row in entries]
        return Fraction(sum(integer_determinant([
            [value for column_index, value in enumerate(row) if column_index != removed]
            for row_index, row in enumerate(negative) if row_index != removed])
            for removed in range(size)))
    denominator = argument.denominator
    shifted = [[(argument.numerator if row == column else 0) - denominator * value
                for column, value in enumerate(values)] for row, values in enumerate(entries)]
    return Fraction(integer_determinant(shifted), denominator ** size) / argument


def repeated_matrix(repeated, third):
    return [[repeated ** 2 + repeated * third, 0, -repeated ** 2, -repeated * third],
            [0, 2 * repeated * third, 0, -2 * repeated * third],
            [-2 * repeated, 0, 2 * repeated + 2 * repeated * third, -2 * repeated * third],
            [-repeated, -third, -repeated ** 2, repeated ** 2 + repeated + third]]


def cubic_coefficients(entries):
    residuals = [quotient_value(entries, point) - point ** 3 for point in (1, 2, 3)]
    quadratic = (residuals[2] - 2 * residuals[1] + residuals[0]) / 2
    linear = residuals[1] - residuals[0] - 3 * quadratic
    constant = residuals[0] - quadratic - linear
    coefficients = [Fraction(1), quadratic, linear, constant]
    assert all(value.denominator == 1 for value in coefficients)
    return [int(value) for value in coefficients]


def horner(coefficients, argument):
    result = 0
    for coefficient in coefficients:
        result = result * argument + coefficient
    return result


def main():
    root = Path(__file__).resolve().parents[1]
    sources = {name: root / 'results' / filename for name, filename in (
        ('minimum_three', 'distinct-tail.json'),
        ('repeated_exponents', 'repeated-exponent-completion.json'),
        ('minimum_two', 'minimum-two.json'))}
    certificates = {name: json.loads(path.read_text()) for name, path in sources.items()}
    domain = {(3, middle, maximum) for middle in range(4, 30) for maximum in range(middle + 1, 30)}
    seen = set()
    signs = {'positive': 0, 'negative': 0}
    for case in certificates['minimum_three']['cases']:
        exponents = tuple(case['exponents'])
        assert exponents in domain and exponents not in seen
        seen.add(exponents)
        entries = complement_matrix(exponents)
        at_one = quotient_value(entries, 1)
        assert at_one == case['h1'] != 0
        assert quotient_value(entries, 2) == case['h2']
        interval = list(map(Fraction, case['complement_interval']))
        values = [quotient_value(entries, point) for point in interval]
        assert values == list(map(Fraction, case['endpoint_values']))
        assert values[0] * values[1] < 0
        assert (interval == [0, 1] or interval == [1, 2]
                or (exponents == (3, 4, 5) and interval == [1, Fraction(3, 2)]))
        vertex_count = 1
        for exponent in exponents:
            vertex_count *= exponent + 1
        vertex_count -= 2
        assert vertex_count == case['graph_vertex_count']
        assert [vertex_count - interval[1], vertex_count - interval[0]] == list(map(Fraction, case['graph_eigenvalue_interval']))
        signs['positive' if at_one > 0 else 'negative'] += 1
    assert seen == domain and len(seen) == 325
    assert signs == {'positive': 257, 'negative': 68}
    modular_pairs = []
    assert [entry['index'] for entry in certificates['repeated_exponents']['complete_fixed_index_certificates']] == [1, 2, 3]
    for index_data in certificates['repeated_exponents']['complete_fixed_index_certificates']:
        factor_index = index_data['index']
        assert factor_index in (1, 2, 3)
        bound = (factor_index + 1) ** 3 * (factor_index + 2)
        assert bound == index_data['index_constant']
        divisors = [value for value in range(1, bound + 1) if bound % value == 0]
        assert [record['divisor'] for record in index_data['all_divisors']] == divisors
        admissible_pairs = []
        for record in index_data['all_divisors']:
            divisor = record['divisor']
            admissible = False
            if (divisor - 1) % factor_index == 0:
                repeated = (divisor - 1) // factor_index - 1
                if repeated >= 2:
                    product = repeated ** 3 * (2 * repeated + 1)
                    assert product % divisor == 0
                    other = product // divisor
                    assert (other - 1) % (repeated + 1) == 0
                    second_index = (other - 1) // (repeated + 1)
                    third = (repeated - 1) * (2 * repeated - 1) - factor_index * second_index
                    admissible = divisor <= other and third > 0
            assert admissible == record['admissible']
            if admissible:
                pair = [repeated, third]
                assert pair == [record['repeated_exponent'], record['third_exponent']]
                admissible_pairs.append(pair)
                coefficients = cubic_coefficients(repeated_matrix(*pair))
                prime = record['prime']
                assert prime >= 2 and all(prime % candidate for candidate in range(2, prime))
                residues = [horner(coefficients, residue) % prime for residue in range(prime)]
                assert residues == record['values_modulo_prime'] and all(residues)
                modular_pairs.append({'exponents': pair, 'prime': prime, 'cubic_coefficients': coefficients})
        assert admissible_pairs == index_data['complete_positive_pairs']
    assert len(modular_pairs) == 8
    exception = certificates['minimum_two']['exception']
    assert exception['exponents'] == [2, 3, 4]
    entries = complement_matrix(exception['exponents'])
    values = []
    for endpoint in exception['endpoints']:
        value = quotient_value(entries, Fraction(endpoint['argument']))
        assert value == Fraction(endpoint['value'])
        values.append(value)
    assert values == [Fraction(-48), Fraction(13437, 32)]
    report = {'method': 'Python standard library only; disjoint-support matrix and direct integer Leibniz determinants, exact rational endpoint arithmetic; cubic coefficients recovered from independent 4x4 determinants at 1,2,3. No original checker imports or SymPy.',
              'minimum_three': {'complete_pairs': 325, 'h1_sign_counts': signs,
                                'h1_h2_and_all_interval_endpoint_values': 'passed',
                                'graph_lift_intervals': 'passed'},
              'repeated_exponents': {'complete_factor_indices': [1, 2, 3], 'divisor_constants': [24, 108, 320],
                                     'root_free_cubic_certificates': modular_pairs},
              'minimum_two': {'exception': [2, 3, 4], 'rational_endpoint_values': [str(value) for value in values]},
              'historical_certificate_sha256': {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in sources.items()},
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Independent checks of the selected smaller finite inputs in the established three-prime proof. Written infinite reductions, repeated boundary family, unit-exponent theorem and other symbolic identities remain dependencies; not a fresh verification of every theorem. No new range, theorem or Lean; higher-prime nonsquarefree Q3 and orthogonality n=7 remain open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
