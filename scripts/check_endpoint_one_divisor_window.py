import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient, support_weights


def integer_horner(coefficients, point):
    value = 0
    for coefficient in coefficients:
        value = value * point + coefficient
    return value


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    parameters = (first, middle, last)
    matrix = support_quotient(parameters, complement=True)
    weighted = sympy.diag(*support_weights(parameters)) * matrix
    assert weighted == weighted.T
    pair_block = matrix.extract((3, 4, 5), (3, 4, 5))
    assert pair_block == sympy.diag(last, middle, first)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    residual = sympy.Poly(sympy.cancel((quintic.as_expr() - variable * quintic.eval(1))
                                     / (variable - 1)), variable)
    assert residual.degree() == 4 and residual.LC() == 1
    total = first + middle + last
    pairs = first * middle + first * last + middle * last
    product = first * middle * last
    assert sympy.expand(residual.eval(0) - product * total * (pairs + total)) == 0
    assert sympy.expand(quintic.eval(last) + product ** 2
                        * (last ** 2 + 2 * last - first - middle)) == 0
    controls = []
    for exponents, expected_count in [((8, 8, 105), 38), ((9, 9, 136), 39), ((20, 20, 741), 197)]:
        direct = support_quotient(exponents, complement=True)
        direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        assert direct_quintic == sympy.Poly(quintic.as_expr().subs(dict(zip(parameters, exponents))), variable)
        assert direct_quintic.eval(1) == 0
        quartic = sympy.Poly(sympy.cancel(direct_quintic.as_expr() / (variable - 1)), variable)
        assert quartic == sympy.Poly(residual.as_expr().subs(dict(zip(parameters, exponents))), variable)
        coefficients = list(map(int, quartic.all_coeffs()))
        constant = coefficients[-1]
        candidates = [int(divisor) for divisor in sympy.divisors(constant) if 5 <= divisor < exponents[2]]
        assert len(candidates) == expected_count
        values = [integer_horner(coefficients, divisor) for divisor in candidates]
        assert values == [int(quartic.eval(divisor)) for divisor in candidates]
        assert all(value != 0 for value in values)
        factors = sympy.factor_list(quartic)[1]
        integer_roots = []
        for factor, multiplicity in factors:
            if factor.degree() == 1:
                root = -factor.nth(0) / factor.nth(1)
                if root.is_Integer:
                    integer_roots.extend([int(root)] * multiplicity)
        assert not any(5 <= root < exponents[2] for root in integer_roots)
        assert quartic.count_roots(0, 4) == 0
        assert quartic.count_roots(4, exponents[2]) == 1
        assert quartic.eval(4) > 0 and quartic.eval(exponents[2]) < 0
        controls.append({'exponents': exponents, 'h_C_at_one': 0,
                         'quartic_coefficients': coefficients, 'quartic_constant': constant,
                         'candidate_count': len(candidates), 'candidate_divisors': candidates,
                         'integer_Horner_values': values, 'candidate_roots': [],
                         'rational_factorization': str(sympy.factor(quartic.as_expr())),
                         'integer_roots_from_rational_factorization': integer_roots,
                         'exact_Sturm_roots_in_0_through_4': 0,
                         'exact_Sturm_roots_between_4_and_c': 1,
                         'quartic_at_4_and_c': [int(quartic.eval(4)), int(quartic.eval(exponents[2]))]})
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
    return {'written_constant_identity': 'F(0)=rs(p+s)>0 for positive real a,b,c, including h_C(1)=0; s=a+b+c,p=ab+ac+bc,r=abc. F remains a monic quartic, not x times a cubic.',
            'written_upper_bound': 'For ordered positive real a<=b<=c, the second smallest nonzero complement quotient root lambda_3 is strictly below c. Weighted symmetric similarity has principal block diag(c,b,a); interlacing gives lambda_3<=c, and h_C(c)=-a^2*b^2*c^2*(c^2+2c-a-b)<0 excludes equality.',
            'written_endpoint_one_window': 'For 8<=a<=b<=c on h_C(1)=0, prior spectral gap identifies lambda_2=1 and lambda_3=the smallest residual-quartic root mu_1, so 4<mu_1<c. For integer exponents and a hypothetical integer spectrum, mu_1 is a positive divisor of rs(p+s) with 5<=mu_1<=c-1.',
            'pair_support_principal_block': str(pair_block), 'generic_symbolic_identities': 'passed',
            'endpoint_one_controls': controls, 'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
            'scope': 'Written unbounded constant identity and strict interlacing upper bound; lower bound uses prior written spectral-gap theorem. Exact divisor/Horner/rational-factorization/Sturm diagnostics on only three established endpoint-one controls, already nonintegral by prior repeated-exponent theorem. The candidate list is finite for each fixed triple; no global endpoint-one surface decision or new nonintegrality family. Full Q3 open. No parameter or modulus scan, floating spectra, Lean, manuscript, shared CI, merge or publication changes; old n7/four native axioms unaffected.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
