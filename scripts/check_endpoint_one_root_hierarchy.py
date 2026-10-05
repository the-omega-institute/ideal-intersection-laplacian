import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def certificate():
    first, middle, last, variable, shift = sympy.symbols('a b c x m')
    parameters = (first, middle, last)
    matrix = support_quotient(parameters, complement=True)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    endpoint = quintic.eval(1)
    residual = sympy.Poly(sympy.cancel((quintic.as_expr() - variable * endpoint) / (variable - 1)), variable)
    leading, negative_cubic, quadratic, negative_linear, constant = residual.all_coeffs()
    cubic = -negative_cubic
    linear = -negative_linear
    assert leading == 1
    candidate = sympy.symbols('d')
    assert sympy.expand(residual.eval(candidate) - constant + linear * candidate
                        - quadratic * candidate ** 2 + cubic * candidate ** 3 - candidate ** 4) == 0
    controls = []
    previous = json.loads(Path(__file__).parents[1].joinpath('results/endpoint-one-root-congruences.json').read_text())
    for prior in previous['endpoint_one_controls']:
        exponents = prior['exponents']
        direct = support_quotient(exponents, complement=True)
        direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        assert direct_quintic.eval(1) == 0
        direct_residual = sympy.Poly(sympy.cancel(direct_quintic.as_expr() / (variable - 1)), variable)
        coefficients = [int(value) for value in direct_residual.all_coeffs()]
        assert coefficients == prior['quartic_coefficients']
        direct_cubic, direct_quadratic, direct_linear, direct_constant = -coefficients[1], coefficients[2], -coefficients[3], coefficients[4]
        candidates = []
        for prior_entry in prior['candidates']:
            divisor = prior_entry['divisor']
            exact = int(direct_residual.eval(divisor))
            assert exact == prior_entry['exact_F_at_d']
            linear_remainder = (direct_constant - direct_linear * divisor) % divisor ** 2
            quadratic_remainder = (direct_constant - direct_linear * divisor
                                   + direct_quadratic * divisor ** 2) % divisor ** 3
            cubic_remainder = (direct_constant - direct_linear * divisor
                               + direct_quadratic * divisor ** 2 - direct_cubic * divisor ** 3) % divisor ** 4
            assert linear_remainder == exact % divisor ** 2
            assert quadratic_remainder == exact % divisor ** 3
            assert cubic_remainder == exact % divisor ** 4
            assert (linear_remainder == 0) == prior_entry['passes_linear']
            candidates.append({'divisor': divisor, 'exact_F_at_d': exact,
                               'linear_remainder_mod_d_squared': linear_remainder,
                               'quadratic_remainder_mod_d_cubed': quadratic_remainder,
                               'cubic_remainder_mod_d_fourth': cubic_remainder,
                               'passes_prior_anchor_tests': prior_entry['passes_anchors']})
        controls.append({'exponents': exponents, 'candidate_count': len(candidates),
                         'prior_combined_survivors': prior['combined_survivors'],
                         'quadratic_survivors': [entry['divisor'] for entry in candidates if entry['quadratic_remainder_mod_d_cubed'] == 0],
                         'anchors_and_quadratic_survivors': [entry['divisor'] for entry in candidates if entry['passes_prior_anchor_tests'] and entry['quadratic_remainder_mod_d_cubed'] == 0],
                         'candidates': candidates})
    survivor = next(entry for entry in controls[0]['candidates'] if entry['divisor'] == 15)
    assert survivor['quadratic_remainder_mod_d_cubed'] == 2925
    assert all(not control['anchors_and_quadratic_survivors'] for control in controls)
    abstract_quartic = sympy.prod(variable - multiple * candidate for multiple in (2, 3, 4, 5))
    assert sympy.expand(abstract_quartic.subs(variable, candidate) - 24 * candidate ** 4) == 0
    boundary = (first - 1) * (2 * first - 1)
    assert sympy.expand(endpoint.subs({middle: first, last: boundary})) == 0
    boundary_constant = sympy.factor(constant.subs({middle: first, last: boundary}))
    half_candidate = sympy.Rational(3, 2) * first
    sign_polynomial = 8 * first ** 5 + 48 * first ** 4 - 132 * first ** 3 + 95 * first ** 2 - 32 * first + 4
    numerator = (4 * first ** 2 - 2 * first - 1) * sign_polynomial
    boundary_value = residual.eval(half_candidate).subs({middle: first, last: boundary})
    assert sympy.expand(boundary_value + first ** 2 * numerator / 16) == 0
    assert sympy.cancel(boundary_value / half_candidate ** 2) == -sympy.expand(numerator) / 36
    assert sympy.Poly(numerator, first, modulus=3).nth(0) % 3 == 2
    family_parameter = sympy.symbols('k')
    assert sympy.Poly(numerator.subs(first, 6 * family_parameter), family_parameter, modulus=3).degree() == 0
    assert sympy.cancel((6 * family_parameter) ** 2 / (9 * family_parameter)) == 4 * family_parameter
    threshold = middle ** 2 + 2 * middle - first
    equality_polynomial = sympy.Poly(sympy.cancel(-endpoint.subs(last, threshold) / (middle - 1)), first)
    expected_coefficients = [3 * middle - 1,
                             -6 * middle ** 3 - 10 * middle ** 2 + 4 * middle,
                             3 * middle ** 5 + 11 * middle ** 4 + 7 * middle ** 3 - 8 * middle ** 2 + middle,
                             middle ** 5 + 6 * middle ** 4 + 7 * middle ** 3 - 2 * middle ** 2,
                             -middle ** 7 - 8 * middle ** 6 - 22 * middle ** 5 - 21 * middle ** 4
                             + 7 * middle ** 3 + 16 * middle ** 2 - 8 * middle + 1]
    assert equality_polynomial.all_coeffs() == expected_coefficients
    assert sympy.expand(endpoint.subs(last, threshold) + (middle - 1) * equality_polynomial.as_expr()) == 0
    assert sympy.expand((middle + threshold) - (middle ** 2 + 3 * middle - first)) == 0
    regimes = []
    for middle_family, expected_sign in ((first + 3, -1), (2 * first, 1)):
        value = sympy.factor(endpoint.subs(last, threshold).subs(middle, middle_family))
        positive = sympy.Poly((expected_sign * value).subs(first, 9 + shift).expand(), shift)
        assert all(coefficient > 0 for coefficient in positive.all_coeffs())
        feasibility_margin = sympy.expand(2 * first ** 2 - first - 2 - middle_family)
        assert all(coefficient > 0 for coefficient in sympy.Poly(feasibility_margin.subs(first, 9 + shift), shift).all_coeffs())
        regimes.append({'middle_family': str(middle_family), 'h_C_at_one_at_E_zero': str(value),
                        'sign': expected_sign, 'positive_coefficients_at_a9plusm': [int(value) for value in positive.all_coeffs()],
                        'real_endpoint_regime': 'E>0' if expected_sign < 0 else 'E<0',
                        'integer_c_feasibility_claimed': False})
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
    return {'written_coefficient_hierarchy': 'For integer root d>0, d|N, d^2|N-Dd, d^3|N-Dd+Bd^2 and d^4|N-Dd+Bd^2-Ad^3. Each is a necessary congruence; A/B/D are genuinely used. Even all congruences are only a modular condition, not F(d)=0.',
            'written_boundary_candidate_exclusion': 'For every a=6k,k>=1 on b=a,c=(a-1)(2a-1), d=3a/2 divides N and lies in the refined E>0 window, but fails the linear coefficient test: F(d)/d^2=-(4a^2-2a-1)T(a)/36 with numerator=2 mod3. Therefore d^2 does not divide F(d). Excludes this candidate uniformly, not the family by new means or every divisor.',
            'endpoint_one_controls': controls,
            'equality_G_coefficients_descending_a': [str(value) for value in expected_coefficients],
            'written_equality_reduction': 'For integer4<=a<=b and c=b(b+2)-a, h_C(1)=0 iff G(a,b)=0, with h_C(1)=-(b-1)G. Fully distinct endpoint-one points at minimum>=8 satisfy2a^2-a+1<b^2+3b<4a^2-a, hence a<b<2a. This is an exact Diophantine reduction, not a classification.',
            'written_unbounded_real_sign_regimes': 'For every reala>=9, b=a+3 has unique real endpoint c>b with E>0; b=2a has unique real endpoint c>b with E<0. Existing fixed-pair feasibility/uniqueness plus complete positive shifted coefficients at the E=0 threshold prove both. Thus neither sign eventually dominates the real endpoint surface. No assertion about dominance on integer endpoint triples.',
            'unbounded_real_regime_certificates': regimes,
            'written_real_equality_exists': 'For every reala>=9, feasibility holds throughout a+3<=b<=2a and the unique simple c>b root varies continuously. E has opposite signs at the endpoints, so some realb in(a+3,2a) has E=0. No integerb/c feasibility or equality root index classification is inferred.',
            'generic_symbolic_identities': 'passed', 'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
            'input_certificate_sha256': hashlib.sha256(Path(__file__).parents[1].joinpath('results/endpoint-one-root-congruences.json').read_bytes()).hexdigest(),
            'scope': 'Written coefficient congruences, uniform rejection of one infinite repeated-boundary candidate family, and two unbounded real sign regimes; exact equality Diophantine reduction with necessary sum bounds. Same3controls/23divisors only, quadratic stage removes sole prior survivor; no new nonintegrality family or fully distinct/globalQ3closure. Necessary congruences not sufficient. Integer sign dominance/equality feasibility remain open. No range/modulus scan, higher endpoint2adicshift, floats or Lean. Prior manuscript/proofs/finite dependencies and oldn7/four native axioms retained.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
