import ast
import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def integer_horner(coefficients, point):
    value = 0
    for coefficient in coefficients:
        value = value * point + coefficient
    return value


def certificate():
    first, gap, last, variable = sympy.symbols('a d c x')
    minimum_shift, gap_shift = sympy.symbols('m t')
    matrix = support_quotient((first, first + gap, last), complement=True)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    endpoint = quintic.eval(1)
    middle = first + gap
    leading = first ** 2 + middle ** 2 - 1
    quadratic = (first ** 3 - 4 * first ** 2 * middle ** 2 + 2 * first ** 2 * middle - first ** 2
                 + 2 * first * middle ** 2 + first * middle - 3 * first + middle ** 3 - middle ** 2
                 - 3 * middle + 3)
    linear = (first - 1) * (middle - 1) * (2 * first * middle + 3 * first + 3 * middle - 3)
    constant = (first - 1) * (middle - 1) * (first + middle - 1) * (first * middle + first + middle - 1)
    assert sympy.expand(endpoint - leading * last ** 3 - quadratic * last ** 2 - linear * last - constant) == 0
    anchor = 2 * first ** 2 + (2 * gap - 3) * first - gap ** 2 - sympy.Rational(3, 2) * gap + 1
    boundary_records = {}
    vectors = {}
    cases = [('even_lower', 0, -1, 2), ('even_upper', 1, 1, 2),
             ('odd_lower', -sympy.Rational(1, 2), -1, 1),
             ('odd_upper', sympy.Rational(1, 2), 1, 1)]
    for label, offset, sign, gap_base in cases:
        boundary = sympy.expand(8 * sign * endpoint.subs(last, anchor + offset))
        shifted = sympy.Poly(boundary.subs(first, 2 * gap ** 2 + 20 + minimum_shift)
                            .subs(gap, gap_base + gap_shift).expand(), minimum_shift, gap_shift)
        assert all(coefficient > 0 for monomial, coefficient in shifted.terms())
        assert shifted.nth(0, 0) > 0
        rows = {}
        for degree in range(shifted.degree(minimum_shift) + 1):
            coefficient = sympy.Poly(shifted.as_expr(), minimum_shift).nth(degree)
            rows[str(degree)] = list(reversed(list(map(int, sympy.Poly(coefficient, gap_shift).all_coeffs()))))
            vectors[(label, degree)] = rows[str(degree)]
        boundary_records[label] = {'gap_base': gap_base, 'offset': str(offset), 'sign': sign,
                                   'clearing_factor': 8, 'unshifted_polynomial': str(boundary),
                                   'positive_terms': len(shifted.terms()),
                                   'constant': int(shifted.nth(0, 0)), 'ascending_gap_shift_vectors': rows}
    small_gap_records = {}
    small_gap_formulas = {
        (1, 0): 4 * first * (first + 1) * (first ** 4 - 4 * first ** 2 - 2 * first + 6),
        (1, 1): 4 * first * (first - 1) * (first + 1) * (first ** 3 - first ** 2 + 1),
        (2, 0): 16 * first ** 5 + 72 * first ** 4 - 76 * first ** 3 - 433 * first ** 2 + 69 * first + 595,
        (2, 1): 4 * (first + 2) * (2 * first ** 5 - 2 * first ** 4 - 17 * first ** 3 + 25 * first ** 2 + 28 * first - 42),
    }
    for difference, lower in [(1, 2 * first ** 2 - first - 2), (2, 2 * first ** 2 + first - 6)]:
        records = {}
        for offset, sign in [(0, -1), (1, 1)]:
            label = 'gap_' + str(difference) + ('_lower' if offset == 0 else '_upper')
            boundary = sympy.factor(sign * endpoint.subs({gap: difference, last: lower + offset}))
            assert sympy.expand(boundary - small_gap_formulas[(difference, offset)]) == 0
            shifted = sympy.Poly(boundary.subs(first, 8 + minimum_shift).expand(), minimum_shift)
            assert all(coefficient > 0 for coefficient in shifted.all_coeffs())
            coefficients = list(map(int, shifted.all_coeffs()))
            vectors[(label, 0)] = coefficients
            records[label] = {'boundary_polynomial': str(boundary), 'descending_minimum_shift_vector': coefficients}
        small_gap_records[str(difference)] = {'lower': str(lower), 'minimum': 8, 'boundaries': records}
    note = Path(__file__).parents[1] / 'notes/endpoint-one-growing-gap.md'
    if note.exists():
        recorded = {}
        for line in note.read_text().splitlines():
            cells = [cell.strip() for cell in line.split('|')]
            if len(cells) == 5 and cells[1] in {key[0] for key in vectors} and cells[2].isdigit():
                recorded[(cells[1], int(cells[2]))] = ast.literal_eval(cells[3])
        assert recorded == vectors
    fixtures = []
    for minimum, difference in [(8, 1), (8, 2), (38, 3), (52, 4), (70, 5), (92, 6), (262, 11), (820, 20)]:
        second = minimum + difference
        lower = 2 * minimum ** 2 + (2 * difference - 3) * minimum - difference ** 2 - (3 * difference + 1) // 2 + 1
        cubic = sympy.Poly(endpoint.subs({first: minimum, gap: difference}), last)
        coefficients = list(map(int, cubic.all_coeffs()))
        values = [integer_horner(coefficients, point) for point in (lower, lower + 1)]
        assert lower > second and values[0] < 0 < values[1]
        assert cubic.count_roots(lower, lower + 1) == cubic.count_roots(second, sympy.oo) == 1
        assert sympy.gcd(cubic, cubic.diff()).degree() == 0
        determinants = []
        for point, value in zip((lower, lower + 1), values):
            direct = support_quotient((minimum, second, point), complement=True)
            determinant = int((sympy.eye(6) - direct).det(method='bareiss'))
            assert determinant == value
            determinants.append(determinant)
        record = {'pair': [minimum, second], 'middle_gap': difference, 'exponent_cubic_coefficients': coefficients,
                  'unique_exponent_root_bracket': [lower, lower + 1], 'integer_Horner_boundary_values': values,
                  'independent_six_by_six_Bareiss_boundary_values': determinants,
                  'roots_strictly_above_middle': 1}
        if difference >= 5:
            second_cubic = sympy.Poly(quintic.eval(2).subs({first: minimum, gap: difference}), last)
            lower_two = 2 * minimum + difference - 11
            assert second_cubic.eval(lower_two) < 0 < second_cubic.eval(lower_two + 1)
            assert second_cubic.count_roots(second, sympy.oo) == second_cubic.count_roots(lower_two, lower_two + 1) == 1
            record['preserved_endpoint_two_bracket'] = [lower_two, lower_two + 1]
        fixtures.append(record)
    control = int(sympy.Poly(support_quotient((9, 9, 136), complement=True).charpoly(variable).as_expr()
                            / variable, variable).eval(1))
    assert control == 0
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
    return {'written_endpoint_one_theorem': 'For integer d>=1,a>=2d^2+20,b=a+d, the unique real c>b endpoint-one solution lies strictly between L and L+1, L=2a^2+(2d-3)a-d^2-ceil(3d/2)+1. No integer c>b has h_C(1)=0.',
            'written_small_gap_theorem': 'For integer a>=8,d=1or2,c>a+d, h_C(1) is nonzero; the unique real exponent roots have the same unit-width brackets.',
            'written_nonintegrality_family': 'Every integer d>=5,a>=2d^2+20,c>a+d is nonintegral for all parity patterns: written endpoint-one and preserved written endpoint-two growing-gap exclusions plus uniform low-root theorem. No finite base for this family.',
            'broader_consequence': 'For every d>=1,a>=2d^2+20,c>a+d and every d=1or2,a>=8,c>a+d, nonintegrality follows using previous global endpoint-two theorem/small-gap certificates. This broader consequence retains prior finite dependencies. A fully distinct integer spectrum at minimum>=8 would require d>=3,a<2d^2+20 and endpoint one; fullQ3 stays open.',
            'boundary_positive_identities': boundary_records, 'small_gap_positive_identities': small_gap_records,
            'exact_selected_fixtures': fixtures, 'preserved_repeated_control': {'exponents': [9, 9, 136], 'h_C_at_one': control},
            'sympy': sympy.__version__, 'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
            'scope': 'Written unbounded growing-gap endpoint-one integer exclusion, plus all-minimum>=8gaps1/2, with complete positive identities and exact unit-width brackets. All31note vectors checked. Eight selected cubic Sturm/Horner/independent6x6Bareiss fixtures and repeated control supplement proofs; no parameter scan or new finite base, floats or Lean. The d>=5spectral family uses written endpoint exclusions only; broader spectral consequences retain prior finite certificates. No endpoint-surface emptiness outside hypotheses, no spectral-multiplicity claim, old results/manuscript unchanged. FullQ3/higher-prime nonsquarefree vectors open.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
