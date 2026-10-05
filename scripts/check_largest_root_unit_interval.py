import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def coefficient_rows(expression, minimum_shift, middle_shift, maximum_shift):
    polynomial = sympy.Poly(expression, middle_shift, maximum_shift)
    rows = []
    for powers, coefficient in reversed(polynomial.terms()):
        minimum_polynomial = sympy.Poly(coefficient, minimum_shift)
        vector = [int(minimum_polynomial.nth(index))
                  for index in range(minimum_polynomial.degree() + 1)]
        assert all(value > 0 for value in vector)
        rows.append({'middle_power': powers[0], 'maximum_power': powers[1],
                     'ascending_minimum_coefficients': vector})
    assert sympy.expand(expression - sum(
        middle_shift ** row['middle_power'] * maximum_shift ** row['maximum_power']
        * sum(value * minimum_shift ** index for index, value in
              enumerate(row['ascending_minimum_coefficients'])) for row in rows)) == 0
    return rows


def open_root_count(polynomial, lower, upper):
    return sum(multiplicity * (factor.count_roots(lower, upper)
               - int(factor.eval(lower) == 0) - int(factor.eval(upper) == 0))
               for factor, multiplicity in polynomial.sqf_list()[1])


def main():
    first, second, third, variable = sympy.symbols('a b c x')
    minimum_shift, middle_shift, maximum_shift = sympy.symbols('m u v')
    exponent_sum = first + second + third
    exponent_product = first * second * third
    matrix = support_quotient((first, second, third), complement=True)
    characteristic = sympy.Poly(matrix.charpoly(variable).as_expr(), variable)
    quintic = sympy.Poly(sympy.cancel(characteristic.as_expr() / variable), variable)
    diagonal_numerators = [(variable - exponent_sum) * (variable - exponent)
                           - variable * sympy.cancel(exponent_product / exponent)
                           for exponent in (first, second, third)]
    schur_determinant = sympy.prod(diagonal_numerators) + sum(
        exponent * (variable - exponent)
        * sympy.prod(diagonal_numerators[other] for other in range(3) if other != index)
        for index, exponent in enumerate((first, second, third)))
    assert sympy.expand(characteristic.as_expr() - schur_determinant) == 0
    anchor = second * third + exponent_sum
    lower_positive = ((2 * second ** 2 - first * second + second - first) * third ** 2
                      - ((first - 1) * second ** 2 + first ** 2) * third
                      - first * second * (first + second))
    assert sympy.expand(quintic.eval(anchor)
                        + first ** 2 * second * third * lower_positive) == 0
    upper_positive = sympy.expand(quintic.eval(anchor + 1))
    substitutions = {second: first + 3 + middle_shift,
                     third: first ** 2 - first + maximum_shift}
    tables = {}
    for label, expression in (('lower', lower_positive), ('upper', upper_positive)):
        shifted = sympy.expand(expression.subs(substitutions).subs(first, 3 + minimum_shift))
        rows = coefficient_rows(shifted, minimum_shift, middle_shift, maximum_shift)
        tables[label] = {'rows': rows, 'nonzero_terms': len(sympy.Poly(
            shifted, minimum_shift, middle_shift, maximum_shift).terms()),
            'constant': int(shifted.subs({minimum_shift: 0, middle_shift: 0, maximum_shift: 0}))}
    assert tables['lower']['nonzero_terms'] == 36
    assert tables['upper']['nonzero_terms'] == 170
    fixtures = []
    for triple in ((3, 6, 6), (4, 7, 12), (8, 11, 56),
                   (9, 12, 72), (9, 12, 159), (9, 30, 951), (9, 150, 160)):
        evaluated = support_quotient(triple, complement=True)
        direct = sympy.Poly(evaluated.charpoly(variable).as_expr(), variable)
        midpoint = triple[1] * triple[2] + sum(triple)
        endpoint_values = []
        for endpoint in (midpoint, midpoint + 1):
            value = int((endpoint * sympy.eye(6) - evaluated).det(method='bareiss'))
            assert value == direct.eval(endpoint)
            endpoint_values.append(value)
        assert endpoint_values[0] < 0 < endpoint_values[1]
        assert open_root_count(direct, midpoint, midpoint + 1) == 1
        assert open_root_count(direct, midpoint + 1, sympy.oo) == 0
        fixtures.append({'exponents': list(triple), 'interval': [midpoint, midpoint + 1],
                         'independent_bareiss_values': endpoint_values,
                         'roots_in_open_interval_with_multiplicity': 1,
                         'roots_above_upper': 0})
    small_gap = {}
    endpoint_cubic = sympy.Poly(quintic.eval(1), third)
    for gap, anchor_expression in ((1, 2 * first ** 2 - first - 2),
                                  (2, 2 * first ** 2 + first - 6)):
        specialized = endpoint_cubic.as_expr().subs(second, first + gap)
        signs = []
        for offset, sign in ((0, -1), (1, 1)):
            expression = sympy.expand(sign * specialized.subs(third, anchor_expression + offset)
                                     .subs(first, 8 + minimum_shift))
            polynomial = sympy.Poly(expression, minimum_shift)
            vector = [int(polynomial.nth(index)) for index in range(polynomial.degree() + 1)]
            assert all(value > 0 for value in vector)
            signs.append(vector)
        diagonal_positive = sympy.Poly(sympy.expand(-specialized.subs(third, first + gap)
                                                   .subs(first, 8 + minimum_shift)), minimum_shift)
        diagonal_vector = [int(diagonal_positive.nth(index))
                           for index in range(diagonal_positive.degree() + 1)]
        assert all(value > 0 for value in diagonal_vector)
        small_gap[str(gap)] = {'lower_anchor': str(anchor_expression),
                              'ascending_diagonal_negative_vector': diagonal_vector,
                              'ascending_lower_negative_vector': signs[0],
                              'ascending_upper_positive_vector': signs[1]}
    root = Path(__file__).resolve().parents[1]
    dependencies = [
        'scripts/check_six_support_quotient.py',
        'notes/endpoint-one-minimum-root.md', 'notes/endpoint-one-geometry.md',
        'notes/endpoint-one-growing-gap.md', 'results/endpoint-one-growing-gap.json',
        'notes/endpoint-two-completion.md', 'results/endpoint-two-completion.json',
        'notes/open-region-diagnostic.md', 'notes/repeated-exponent-completion.md',
    ]
    result = {
        'theorem': 'Real 3<=a<=b<=c, b-a>=3, c>=a^2-a: bc+a+b+c<lambda_max<bc+a+b+c+1.',
        'generic_charpoly_and_independent_schur_identity': 'passed',
        'lower_identity': str(lower_positive),
        'upper_identity': str(upper_positive),
        'substitution': 'a=3+m, b=a+3+u, c=a^2-a+v; m,u,v>=0',
        'complete_positive_tables': tables,
        'fixed_spectral_controls': fixtures,
        'direct_six_by_six_bareiss_determinants': 14,
        'preserved_small_gap_written_signs': small_gap,
        'classification_dependency_audit': {
            'repeated': 'Established all-repeated-exponent theorem.',
            'minimum_at_most_seven': 'Established computer-assisted theorem, including 27562-triple base.',
            'endpoint_two_at_minimum_at_least_eight': 'Established completion, including 8658-triple base.',
            'endpoint_one_gaps_one_two': 'Written unit brackets at a>=8, unique c>b by established real geometry.',
            'endpoint_one_gap_at_least_three': 'Written sum bound gives c> a^2-a, then new maximum-root unit interval.',
            'minimum_eight_108_pair_base_required_by_this_route': False,
            'historical_bases_rerun': False,
        },
        'source_sha256': {path: digest(root / path) for path in dependencies},
        'script_sha256': digest(Path(__file__)), 'sympy': sympy.__version__,
        'scope': 'Written unbounded real unit interval and endpoint-one completion. Combining established written/computer-assisted results proves nonintegrality for every three-prime exponent vector. Seven fixed spectral controls supplement proof, not an exponent scan. Historical finite bases retained, not rerun. Full Q3 for higher-prime nonsquarefree vectors and original orthogonality n=7 remain open. No Lean or floating spectra.',
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
