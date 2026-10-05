import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient, support_weights
from check_endpoint_one_divisor_window import integer_horner


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    pair_sum, pair_product, repeated_last = sympy.symbols('q z t')
    minimum_shift, gap_shift = sympy.symbols('m u')
    parameters = (first, middle, last)
    matrix = support_quotient(parameters, complement=True)
    weighted = sympy.diag(*support_weights(parameters)) * matrix
    assert weighted == weighted.T
    assert matrix.extract((3, 4, 5), (3, 4, 5)) == sympy.diag(last, middle, first)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    cutoff = 4 * first ** 2 - 2 * first + 1
    boundary = 2 * first ** 2 - 2 * first + 1
    remainder = ((first ** 2 - 1) * pair_sum ** 3
                 + (first ** 3 - first ** 2 - 3 * first + 3) * pair_sum ** 2
                 + (-3 * first ** 2 + 6 * first - 3) * pair_sum
                 - first ** 3 + 3 * first ** 2 - 3 * first + 1)
    endpoint = ((pair_sum - cutoff) * pair_product ** 2
                - first * (first - 1) * (pair_sum + 2 * first - 1) * pair_product + remainder)
    assert sympy.expand(endpoint.subs({pair_sum: middle + last, pair_product: middle * last})
                        - quintic.eval(1)) == 0
    product_lower = first * (pair_sum - first)
    assert sympy.expand(middle * last - product_lower.subs(pair_sum, middle + last)
                        - (middle - first) * (last - first)) == 0
    difference = ((pair_product - product_lower)
                  * ((pair_sum - cutoff) * (pair_product + product_lower)
                     - first * (first - 1) * (pair_sum + 2 * first - 1)))
    assert sympy.expand(endpoint - endpoint.subs(pair_product, product_lower) - difference) == 0
    repeated_factor = (first ** 3 - 2 * first ** 2 * repeated_last ** 2
                       + first ** 2 * repeated_last + first ** 2 + 3 * first * repeated_last
                       - 3 * first + repeated_last ** 2 - 2 * repeated_last + 1)
    assert sympy.expand(endpoint.subs({pair_product: first * repeated_last,
                                      pair_sum: first + repeated_last}, simultaneous=True)
                        - ((first - 1) * (2 * first - 1) - repeated_last) * repeated_factor) == 0
    positive = sympy.Poly((-repeated_factor).subs({first: 4 + minimum_shift,
                                                  repeated_last: 4 + minimum_shift + gap_shift},
                                                 simultaneous=True).expand(), minimum_shift, gap_shift)
    expected = (2 * minimum_shift ** 4 + 4 * minimum_shift ** 3 * gap_shift + 30 * minimum_shift ** 3
                + 2 * minimum_shift ** 2 * gap_shift ** 2 + 47 * minimum_shift ** 2 * gap_shift
                + 163 * minimum_shift ** 2 + 16 * minimum_shift * gap_shift ** 2
                + 179 * minimum_shift * gap_shift + 381 * minimum_shift
                + 31 * gap_shift ** 2 + 222 * gap_shift + 323)
    assert sympy.expand(positive.as_expr() - expected) == 0
    assert len(positive.terms()) == 12 and all(coefficient > 0 for powers, coefficient in positive.terms())
    assert sympy.expand(boundary - cutoff + 2 * first ** 2) == 0
    assert sympy.expand(boundary - first ** 2 - 2 * first
                        - ((first - 4) ** 2 + 4 * (first - 4) + 1)) == 0
    assert sympy.expand(quintic.eval(first) + first ** 2 * middle ** 2 * last ** 2
                        * (first ** 2 + 2 * first - middle - last)) == 0
    assert sympy.expand(quintic.eval(last) + first ** 2 * middle ** 2 * last ** 2
                        * (last ** 2 + 2 * last - first - middle)) == 0
    assert sympy.expand(quintic.eval(1).subs({middle: first, last: (first - 1) * (2 * first - 1)})) == 0
    controls = []
    for exponents, expected_count in [((8, 8, 105), 34), ((9, 9, 136), 35), ((20, 20, 741), 183)]:
        direct = support_quotient(exponents, complement=True)
        direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        assert direct_quintic == sympy.Poly(quintic.as_expr().subs(dict(zip(parameters, exponents))), variable)
        assert direct_quintic.eval(1) == 0
        assert exponents[1] + exponents[2] == 2 * exponents[0] ** 2 - 2 * exponents[0] + 1
        assert direct_quintic.eval(exponents[0]) > 0
        quartic = sympy.Poly(sympy.cancel(direct_quintic.as_expr() / (variable - 1)), variable)
        coefficients = list(map(int, quartic.all_coeffs()))
        candidates = [int(divisor) for divisor in sympy.divisors(quartic.eval(0))
                      if exponents[0] < divisor < exponents[2]]
        assert len(candidates) == expected_count
        values = [integer_horner(coefficients, divisor) for divisor in candidates]
        assert values == [int(quartic.eval(divisor)) for divisor in candidates]
        assert all(value != 0 for value in values)
        integer_roots = []
        for factor, multiplicity in sympy.factor_list(quartic)[1]:
            if factor.degree() == 1:
                root = -factor.nth(0) / factor.nth(1)
                if root.is_Integer:
                    integer_roots.extend([int(root)] * multiplicity)
        assert not any(exponents[0] < root < exponents[2] for root in integer_roots)
        assert quartic.count_roots(0, exponents[0]) == 0
        assert quartic.count_roots(exponents[0], exponents[2]) == 1
        assert direct_quintic.count_roots(0, exponents[0]) == 1
        assert direct_quintic.diff().eval(1) > 0
        controls.append({'exponents': exponents, 'sum_bound_equality': True,
                         'quartic_coefficients': coefficients, 'quartic_constant': int(quartic.eval(0)),
                         'h_C_at_a': int(direct_quintic.eval(exponents[0])),
                         'candidate_count': len(candidates), 'candidate_divisors': candidates,
                         'integer_Horner_values': values, 'candidate_roots': [],
                         'rational_factorization': str(sympy.factor(quartic.as_expr())),
                         'integer_roots_from_rational_factorization': integer_roots,
                         'exact_Sturm_quartic_roots_in_0_through_a': 0,
                         'exact_Sturm_quartic_roots_between_a_and_c': 1,
                         'exact_Sturm_quintic_roots_in_0_through_a': 1,
                         'spectral_derivative_at_one': int(direct_quintic.diff().eval(1))})
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py'),
               Path(__file__).with_name('check_endpoint_one_divisor_window.py')]
    return {'written_sum_bound': 'For real 4<=a<=b<=c with h_C(1)=0, b+c>=2a^2-2a+1, with equality exactly b=a,c=(a-1)(2a-1).',
            'written_spectral_theorem': 'For real 4<=a<=b<=c on endpoint one, root1 is simple and smallest positive, and allfour other quotient roots>a. Weighted principal interlacing gives lambda_4>=a; h_C(a)>0 gives an even number below a, at least2and at most3, hence exactly2(the roots0and1). Together with prior strict upper bound, a<mu_1<c.',
            'integer_spectrum_necessary_condition': 'Smallest quartic root must be a positive divisor of rs(p+s) in [a+1,c-1]. Finite per fixed triple, not global endpoint-one surface decision.',
            'symmetric_endpoint_formula': str(endpoint), 'generic_symbolic_identities': 'passed',
            'positive_identity': {'substitution': 'a=4+m,t=4+m+u,m,u>=0',
                                  'polynomial': str(positive.as_expr()), 'constant': 323,
                                  'terms': [{'powers_m_u': list(powers), 'coefficient': int(coefficient)}
                                            for powers, coefficient in positive.terms()]},
            'endpoint_one_controls': controls, 'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
            'scope': 'Written unbounded sum bound with exact equality case and spectral location above minimum for real endpoint-one triples at minimum>=4, no finite base or dependence on previous350termminimum-eight gap certificate. That earlier off-surface residual positivity remains unchanged. Three established controls/252exact candidate evaluations, independent rational factorization and Sturm counts supplement proofs; controls already nonintegral by repeated theorem. No new nonintegrality family/globalQ3closure, parameter/modulus scan/floats/Lean. Previous certificates/manuscript and oldn7/four native axioms unaffected.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
