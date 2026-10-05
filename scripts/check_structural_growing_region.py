import hashlib
import json
from pathlib import Path

import sympy

from check_endpoint_one_growing_gap import certificate as growing_certificate
from check_endpoint_one_equality_quotient import certificate as quotient_certificate
from check_six_support_quotient import support_quotient


def certificate():
    growing = growing_certificate()
    quotient = quotient_certificate()
    first, middle, last, variable = sympy.symbols('a b c x')
    minimum_shift, middle_shift, last_shift = sympy.symbols('m t u')
    matrix = support_quotient((first, middle, last), complement=True)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    endpoint_two = quintic.eval(2)
    small_gap_records = []
    for gap, threshold, offset in [(1, 20, -9), (2, 20, -8), (3, 16, -7)]:
        lower = 2 * first + offset
        endpoint = endpoint_two.subs(middle, first + gap)
        boundaries = []
        for shift, sign in [(0, -1), (1, 1)]:
            polynomial = sympy.Poly(sympy.expand(sign * endpoint.subs(last, lower + shift)
                                                .subs(first, threshold + minimum_shift)), minimum_shift)
            assert all(coefficient > 0 for coefficient in polynomial.all_coeffs())
            boundaries.append(list(map(int, polynomial.all_coeffs())))
        assert 2 * threshold + offset > threshold + gap
        small_gap_records.append({'gap': gap, 'written_tail_minimum': threshold,
                                  'endpoint_two_lower': str(lower),
                                  'positive_boundary_vectors_descending': boundaries})
    five_difference = sympy.expand(4 * endpoint_two - quintic.eval(5))
    positive_five = sympy.Poly(five_difference.subs({first: 8 + minimum_shift,
                                                   middle: 8 + middle_shift,
                                                   last: 8 + last_shift}).expand(),
                               minimum_shift, middle_shift, last_shift)
    assert len(positive_five.terms()) == 44
    assert all(coefficient > 0 for coefficient in positive_five.coeffs())
    four_difference = sympy.expand(quintic.eval(4) - 3 * endpoint_two)
    middle_substitution = first * (1 + 2 * middle_shift) / (1 + middle_shift)
    last_substitution = first * (4 + 9 * last_shift) / (4 * (1 + last_shift))
    transformed = sympy.cancel(64 * (1 + middle_shift) ** 3 * (1 + last_shift) ** 3
                              * four_difference.subs({middle: middle_substitution, last: last_substitution}))
    positive_four = sympy.Poly(transformed.subs(first, 40 + minimum_shift).expand(),
                               minimum_shift, middle_shift, last_shift)
    assert len(positive_four.terms()) == 112
    assert all(coefficient > 0 for coefficient in positive_four.coeffs())
    repository = Path(__file__).resolve().parents[1]
    prior = json.loads((repository / 'results/endpoint-two-completion.json').read_text())
    for polynomial, key in [(positive_four, 'positive_four_difference'),
                            (positive_five, 'positive_five_difference')]:
        vectors = prior[key]['vectors_ascending_in_m_by_t_power_and_u_power']
        reconstructed = sum(coefficient * minimum_shift ** degree
                            * middle_shift ** middle_power * last_shift ** last_power
                            for middle_power, row in enumerate(vectors)
                            for last_power, vector in enumerate(row)
                            for degree, coefficient in enumerate(vector))
        assert sympy.expand(reconstructed - polynomial.as_expr()) == 0
    assert 2 * 4 ** 2 + 20 >= 40
    threshold_comparison = [{'gap': gap, 'region_minimum': 2 * gap ** 2 + 20,
                             'endpoint_two_tail_minimum': threshold,
                             'tail_covers_whole_region': 2 * gap ** 2 + 20 >= threshold}
                            for gap, threshold in [(1, 20), (2, 20), (3, 16)]]
    assert all(row['tail_covers_whole_region'] for row in threshold_comparison)
    dependencies = ['endpoint-one-growing-gap', 'endpoint-two-completion',
                    'endpoint-two-middle-tail', 'endpoint-two-sharp-maximum',
                    'endpoint-one-equality-quotient', 'endpoint-one-equality-curve']
    sources = [Path(__file__), Path(__file__).with_name('check_endpoint_one_growing_gap.py'),
               Path(__file__).with_name('check_endpoint_one_equality_quotient.py'),
               Path(__file__).with_name('check_six_support_quotient.py')]
    return {
        'written_structural_theorem': 'For every integer d>=1, a>=2*d^2+20, c>a+d, the ideal intersection graph is Laplacian nonintegral for every parity and residue pattern. No finite exponent base is required for this whole region.',
        'proof': 'Endpoint one has its unique exponent root in a unit interval. At a>=40 an endpoint-two zero forces a quotient root in(4,5). Below40 the threshold allows only d=1,2,3, whose written endpoint-two tails cover minima22,28,38. The uniform positive root in(0,3) then rules out an integer spectrum.',
        'endpoint_one_boundary_positive_terms': {key: value['positive_terms']
                                                for key, value in growing['boundary_positive_identities'].items()},
        'endpoint_one_all31_note_vectors_reverified': True,
        'endpoint_one_fixed_fixtures_reverified': 8,
        'endpoint_two_small_gap_written_boundaries': small_gap_records,
        'threshold_comparison': threshold_comparison,
        'endpoint_two_real_tail_positive_terms': {'four_difference': 112, 'five_difference': 44},
        'endpoint_two_saved_tail_vectors_agree': True,
        'finite_base_8658_rerun': False,
        'finite_base_27562_rerun': False,
        'finite_exponent_base_required_for_structural_region': False,
        'broader_minimum8_gap1or2_consequence_retains_finite_dependencies': True,
        'descent_review': {'known_quotient_genus': 3,
                           'branch_stabilizer_elements_reverified': quotient['PGL2_F5_elements_exhausted'],
                           'extra_rational_involution_on_known_quotient': False,
                           'known_quotient_has_Q_map_to_genus2': False,
                           'maps_from_original_genus10_curve_classified': False,
                           'Jacobian_rank_computed': False},
        'covering_review': 'CRT limitations apply to finite congruence tests; they do not disprove a finite covering that also uses spectral inequalities and exact root/divisor conditions. No complete covering is established.',
        'scope': 'Written structural proof and exact polynomial identity review, not a new residue slice. The spectral region was already recorded as a broader consequence; its finite-dependency requirement is removed here by using written tails only. Full Q3 and the remaining endpoint-one region stay open. No exponent/prime/power scan, new finite base, integer-point/rank computation or Lean. Manuscript unchanged.',
        'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
        'prior_certificate_sha256': {name: hashlib.sha256((repository / 'results' / (name + '.json')).read_bytes()).hexdigest()
                                     for name in dependencies},
        'sympy': sympy.__version__,
    }


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
