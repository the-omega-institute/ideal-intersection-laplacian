import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient, support_weights
from check_endpoint_one_divisor_window import integer_horner


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    parameters = (first, middle, last)
    matrix = support_quotient(parameters, complement=True)
    weighted = sympy.diag(*support_weights(parameters)) * matrix
    assert weighted == weighted.T
    principal = matrix.extract((2, 3, 4, 5), (2, 3, 4, 5))
    expected = sympy.Matrix([[first * middle + first + middle, -first * middle, 0, 0],
                            [-last, last, 0, 0], [0, 0, middle, 0], [0, 0, 0, first]])
    assert principal == expected
    quadratic = sympy.Poly(variable ** 2 - (first * middle + first + middle + last) * variable
                            + last * (first + middle), variable)
    assert sympy.expand(principal.charpoly(variable).as_expr()
                        - (variable - first) * (variable - middle) * quadratic.as_expr()) == 0
    assert sympy.expand(quadratic.eval(first + middle) + first * middle * (first + middle)) == 0
    discriminant = (first * middle + first + middle - last) ** 2 + 4 * first * middle * last
    assert sympy.expand(sympy.discriminant(quadratic.as_expr(), variable) - discriminant) == 0
    assert sympy.expand(principal.extract((0, 1), (0, 1)).det() - last * (first + middle)) == 0
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    controls = []
    fixtures = [((8, 8, 105), [10, 11, 12, 14, 15]),
                ((9, 9, 136), [11, 12, 14, 16, 17]),
                ((20, 20, 741), [21, 22, 24, 25, 26, 28, 30, 33, 34, 35, 37, 38, 39])]
    for exponents, expected_divisors in fixtures:
        direct = support_quotient(exponents, complement=True)
        direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        assert direct_quintic == sympy.Poly(quintic.as_expr().subs(dict(zip(parameters, exponents))), variable)
        assert direct_quintic.eval(1) == 0
        quartic = sympy.Poly(sympy.cancel(direct_quintic.as_expr() / (variable - 1)), variable)
        coefficients = list(map(int, quartic.all_coeffs()))
        upper = min(exponents[2], exponents[0] + exponents[1])
        candidates = [int(divisor) for divisor in sympy.divisors(quartic.eval(0))
                      if exponents[0] < divisor < upper]
        assert candidates == expected_divisors
        values = [integer_horner(coefficients, divisor) for divisor in candidates]
        assert values == [int(quartic.eval(divisor)) for divisor in candidates]
        assert all(value != 0 for value in values)
        integer_roots = []
        for factor, multiplicity in sympy.factor_list(quartic)[1]:
            if factor.degree() == 1:
                root = -factor.nth(0) / factor.nth(1)
                if root.is_Integer:
                    integer_roots.extend([int(root)] * multiplicity)
        assert not any(exponents[0] < root < upper for root in integer_roots)
        assert quartic.count_roots(0, exponents[0]) == 0
        assert quartic.count_roots(exponents[0], upper) == 1
        direct_principal = direct.extract((2, 3, 4, 5), (2, 3, 4, 5))
        principal_polynomial = sympy.Poly(direct_principal.charpoly(variable).as_expr(), variable)
        assert principal_polynomial.count_roots(0, upper) == 2
        assert sympy.Poly(quadratic.as_expr().subs(dict(zip(parameters, exponents))), variable).count_roots(0, upper) == 1
        controls.append({'exponents': exponents, 'quartic_coefficients': coefficients,
                         'quartic_constant': int(quartic.eval(0)), 'upper_endpoint': upper,
                         'candidate_count': len(candidates), 'candidate_divisors': candidates,
                         'integer_Horner_values': values, 'candidate_roots': [],
                         'rational_factorization': str(sympy.factor(quartic.as_expr())),
                         'integer_roots_from_rational_factorization': integer_roots,
                         'exact_Sturm_quartic_roots_in_0_through_a': 0,
                         'exact_Sturm_quartic_roots_between_a_and_upper': 1,
                         'exact_Sturm_quadratic_roots_between_0_and_upper': 1,
                         'principal_characteristic_polynomial': str(principal_polynomial.as_expr())})
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py'),
               Path(__file__).with_name('check_endpoint_one_divisor_window.py')]
    return {'written_universal_upper_bound': 'For ordered positive real a<=b<=c, second smallest nonzero quotient root lambda_3<a+b. Four-support principal block on3,12,13,23 has eigenvalues a,b,rho_-,rho_+; Q(a+b)=-ab(a+b)<0 places exactly3principal eigenvalues below a+b; interlacing lambda_3<=beta_3<a+b.',
            'written_refined_principal_bound': 'lambda_3<=max(b,rho_-), rho_-=(ab+a+b+c-sqrt((ab+a+b-c)^2+4abc))/2. This inequality may be non-strict; lambda_3<a+b is strict.',
            'written_endpoint_one_window': 'For real4<=a<=b<=c on h_C(1)=0, prior minimum-root theorem and strictc bound give a<mu_1<min(c,a+b).',
            'integer_spectrum_necessary_condition': 'Smallest residual root must be a positive divisor of rs(p+s) with a+1<=d<=min(c,a+b)-1. Per-triple finite test does not decide whole unbounded surface.',
            'nonsymmetric_principal_block': str(principal), 'principal_quadratic': str(quadratic.as_expr()),
            'quadratic_discriminant': str(discriminant), 'generic_symbolic_identities': 'passed',
            'endpoint_one_controls': controls, 'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
            'scope': 'Written universal positive-real pair-sum upper bound, refined principal bound and endpoint-one window by prior written minimum-root/c bounds. Three established controls/23exact candidate values, independent factorization/Sturm diagnostics supplement proofs; already nonintegral by repeated theorem. No finite base needed for written bounds, new nonintegrality family, globalQ3closure, parameter/modulus scan/floats/Lean. Prior certificates/manuscript and oldn7/four native axioms unaffected.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
