import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient, support_weights


def open_root_count(polynomial, lower, upper):
    count = 0
    for factor, multiplicity in polynomial.sqf_list()[1]:
        factor_count = factor.count_roots(lower, upper)
        for endpoint in (lower, upper):
            if endpoint not in (-sympy.oo, sympy.oo) and factor.eval(endpoint) == 0:
                factor_count -= 1
        count += multiplicity * factor_count
    return int(count)


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    parameters = (first, middle, last)
    total = first + middle + last
    pairs = first * middle + first * last + middle * last
    product = first * middle * last
    matrix = support_quotient(parameters, complement=True)
    weighted = sympy.diag(*support_weights(parameters)) * matrix
    assert weighted == weighted.T
    characteristic = sympy.Poly(matrix.charpoly(variable).as_expr(), variable)
    quintic = characteristic.exquo(sympy.Poly(variable, variable))
    shifted = (matrix.extract((0, 1), (0, 1)) - total * sympy.eye(2)).applyfunc(sympy.expand)
    assert shifted == sympy.Matrix([[middle * last - first, -middle], [-first, first * last - middle]])
    ordered_positive = (first * middle * (last - middle)
                        + (first - 1) * (middle - first) * (middle + first) + (first - 2) * first ** 2)
    assert sympy.expand(shifted.det() - last * ordered_positive) == 0
    symmetric_positive = (first ** 2 * (middle * last - middle - last)
                          + middle ** 2 * (first * last - first - last)
                          + last ** 2 * (first * middle - first - middle))
    assert sympy.expand(symmetric_positive - (product * (total + 3) - total * pairs)) == 0
    assert sympy.expand(quintic.eval(total) + product * total * symmetric_positive) == 0
    virtual_quartic = sympy.Poly(sympy.cancel((quintic.as_expr() - variable * quintic.eval(1)) / (variable - 1)), variable)
    trace = pairs + 3 * total - 1
    constant = product * total * (pairs + total)
    linear = (product ** 2 + (total ** 2 - total + 1) * product
              + total ** 2 * pairs + pairs ** 2 + (total - 1) ** 3)
    assert sympy.expand(virtual_quartic.nth(3) + trace) == 0
    assert sympy.expand(virtual_quartic.nth(1) + linear) == 0
    assert sympy.expand(virtual_quartic.nth(0) - constant) == 0
    denominator_positive = (product * (product - 4 * total) + product * (total ** 2 - 3 * pairs + 1)
                            + total ** 2 * pairs + pairs ** 2 + (total - 1) ** 3)
    assert sympy.expand(linear - 3 * constant / total - denominator_positive) == 0
    assert sympy.expand(total ** 2 - 3 * pairs
                        - ((first - middle) ** 2 + (first - last) ** 2 + (middle - last) ** 2) / 2) == 0
    spectral_controls = []
    for exponents in ((2, 2, 2), (2, 2, 3), (4, 4, 4), (9, 9, 136), (9, 12, 159), (9, 30, 951)):
        direct = support_quotient(exponents, complement=True)
        polynomial = sympy.Poly(direct.charpoly(variable).as_expr(), variable)
        endpoint = sum(exponents)
        determinant = (endpoint * sympy.eye(6) - direct).det(method='bareiss')
        assert determinant == polynomial.eval(endpoint)
        assert polynomial == sympy.Poly(characteristic.as_expr().subs(dict(zip(parameters, exponents))), variable)
        below = open_root_count(polynomial, -sympy.oo, endpoint)
        above = open_root_count(polynomial, endpoint, sympy.oo)
        assert below == 3
        if exponents == (2, 2, 2):
            expected = variable * (variable - 6) * (variable ** 2 - 12 * variable + 12) ** 2
            assert sympy.expand(polynomial.as_expr() - expected) == 0
            assert determinant == 0 and above == 2
        else:
            assert determinant < 0 and above == 3
        spectral_controls.append({'exponents': exponents, 'total_sum': endpoint,
                                  'characteristic_factorization': str(sympy.factor(polynomial.as_expr())),
                                  'Bareiss_determinant_at_total': int(determinant),
                                  'roots_strictly_below_with_multiplicity': below,
                                  'roots_strictly_above_with_multiplicity': above,
                                  'roots_at_endpoint_with_multiplicity': 6 - below - above})
    coefficient_controls = []
    fixtures = [((8, 8, 105), [10, 11, 12, 14, 15], [10]),
                ((9, 9, 136), [11, 12, 14, 16, 17], [11]),
                ((20, 20, 741), [21, 22, 24, 25, 26, 28, 30, 33, 34, 35, 37, 38, 39], [25, 26])]
    for exponents, previous_candidates, expected_candidates in fixtures:
        direct = support_quotient(exponents, complement=True)
        polynomial = sympy.Poly(direct.charpoly(variable).as_expr(), variable)
        quartic = polynomial.exquo(sympy.Poly(variable * (variable - 1), variable))
        substitution = dict(zip(parameters, exponents))
        assert quartic == sympy.Poly(virtual_quartic.as_expr().subs(substitution), variable)
        endpoint = sum(exponents)
        old_upper = min(exponents[2], exponents[0] + exponents[1])
        direct_trace = -quartic.nth(3)
        direct_linear = -quartic.nth(1)
        direct_constant = quartic.nth(0)
        reciprocal_bound = sympy.Rational(2, endpoint) + 1 / (direct_trace - old_upper - 2 * endpoint)
        lower = direct_constant / direct_linear
        upper = direct_constant / (direct_linear - direct_constant * reciprocal_bound)
        assert direct_linear - direct_constant * reciprocal_bound > 0
        assert exponents[0] < lower < upper < old_upper
        original_divisors = [int(divisor) for divisor in sympy.divisors(direct_constant)
                             if exponents[0] < divisor < old_upper]
        assert original_divisors == previous_candidates
        candidates = [candidate for candidate in previous_candidates if lower < candidate < upper]
        assert candidates == expected_candidates
        values = []
        for candidate in candidates:
            value = 0
            for coefficient in quartic.all_coeffs():
                value = value * candidate + int(coefficient)
            assert value == quartic.eval(candidate) != 0
            values.append(value)
        assert open_root_count(quartic, lower, upper) == 1
        assert open_root_count(quartic, endpoint, sympy.oo) == 3
        coefficient_controls.append({'exponents': exponents, 'quartic_coefficients': list(map(int, quartic.all_coeffs())),
                                     'lower': str(lower), 'upper': str(upper), 'reciprocal_bound': str(reciprocal_bound),
                                     'old_candidates': previous_candidates, 'filtered_candidates': candidates,
                                     'integer_Horner_values': values, 'exact_roots_in_coefficient_window': 1,
                                     'exact_roots_above_total_with_multiplicity': 3})
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py'),
               Path(__file__).with_name('check_fully_distinct.py')]
    prior = Path(__file__).parent.parent / 'results/endpoint-one-pair-sum-window.json'
    return {'written_global_theorem': 'For real2<=a<=b<=c except(2,2,2), lambda_3<a+b<a+b+c<lambda_4. Boundary lambda_4=6.',
            'written_coefficient_window': 'On real endpoint1/minimum>=4, N/D<mu_1<N/(D-NR), R=2/s+1/(A-U-2s), U=min(c,a+b), D-NR>0.',
            'generic_symbolic_identities': 'passed', 'ordered_high_pair_positive': str(ordered_positive),
            'symmetric_total_sign_factor': str(symmetric_positive), 'denominator_positive_identity': str(denominator_positive),
            'spectral_controls': spectral_controls, 'coefficient_controls': coefficient_controls,
            'candidate_counts': {'before': 23, 'after': 4}, 'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
            'prior_certificate_sha256': hashlib.sha256(prior.read_bytes()).hexdigest(),
            'scope': 'Written global total-sum gap including sharp boundary and real coefficient window; six fixed spectral controls/six Bareiss checks and three existing endpoint-one controls/23old candidates filtered to4nonzero Horner values. No new nonintegrality region, scan, floats or Lean. Residual integer splitting/three-prime/fullQ3/higher-prime nonsquarefree remain open; oldn7/four native axioms retained.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
