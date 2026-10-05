import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    total = first + middle
    equality_last = middle * (middle + 2) - first
    matrix = support_quotient((first, middle, last), complement=True)
    equal_matrix = matrix.subs(last, equality_last)
    block = equal_matrix.extract((0, 2, 3, 5), (0, 2, 3, 5))
    cubic = sympy.Poly(sympy.cancel(block.charpoly(variable).as_expr() / (variable - middle)), variable)
    quintic = sympy.Poly(sympy.cancel(equal_matrix.charpoly(variable).as_expr() / variable), variable)
    principal_positive = (first ** 2 * middle * (middle ** 2 - first - 2) + 2 * first ** 2
                          + first * middle * (middle * (2 * middle ** 2 - 3) + 4 * middle ** 2 - 5)
                          + middle ** 2 * (middle + 1) ** 2 * (middle + 2))
    full_positive = (first ** 2 * middle * (middle ** 2 - first - 2) + first ** 2 * middle ** 2 + 2 * first ** 2
                     + first * middle * (middle * (middle ** 2 - 2) + 3 * middle ** 2 - 5)
                     + middle ** 2 * (middle + 1) * (middle + 2))
    assert sympy.expand(cubic.eval(total) - middle * principal_positive) == 0
    assert sympy.expand(quintic.eval(total) + first * middle * equality_last * (total + 1) * full_positive) == 0
    assert sympy.expand(equality_last - total - (middle * (middle + 1) - 2 * first)) == 0
    assert sympy.expand(middle ** 2 - first - 2 - ((middle - first) + (middle - 2) * (middle + 1))) == 0
    controls = []
    for exponents in ((4, 4, 20), (9, 12, 159), (9, 30, 951)):
        lower, middle_value, upper = exponents
        boundary = lower + middle_value
        assert upper == middle_value * (middle_value + 2) - lower and upper > boundary
        direct = support_quotient(exponents, complement=True)
        direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        remaining = sympy.Poly(sympy.cancel(direct_quintic.as_expr() / (variable - middle_value)), variable)
        direct_block = direct.extract((0, 2, 3, 5), (0, 2, 3, 5))
        direct_cubic = sympy.Poly(sympy.cancel(direct_block.charpoly(variable).as_expr() / (variable - middle_value)), variable)
        assert remaining.count_roots(0, boundary) == 1 and remaining.count_roots(boundary, sympy.oo) == 3
        assert direct_cubic.count_roots(0, boundary) == 1 and direct_cubic.count_roots(boundary, sympy.oo) == 2
        assert direct_quintic.eval(boundary) < 0 and direct_cubic.eval(boundary) > 0
        assert direct_quintic.eval(1) != 0
        controls.append({'exponents': exponents, 'pair_sum': boundary,
                         'endpoint_one_point': False, 'h_C_at_pair_sum': int(direct_quintic.eval(boundary)),
                         'K_at_pair_sum': int(direct_cubic.eval(boundary)),
                         'exact_Sturm_other_nonzero_roots_below_pair_sum': 1,
                         'exact_Sturm_other_nonzero_roots_above_pair_sum': 3,
                         'exact_Sturm_K_roots_below_pair_sum': 1,
                         'exact_Sturm_K_roots_above_pair_sum': 2})
    previous_certificate = Path(__file__).resolve().parents[1] / 'results/endpoint-one-equality-root.json'
    return {'written_unconditional_pair_sum_gap': 'For real4<=a<=b,c=b(b+2)-a, lambda3=b simple and lambda4>a+b. K(a+b)>0/c>a+b put beta4>a+b in the five-support principal block, hence lambda5>a+b; full determinant h_C(a+b)<0 and prior lambda3=b force lambda4>a+b.',
            'written_endpoint_one_cubic_window': 'If h_C(1)=0, mu1=b simple and all three roots of monic P3 in F=(x-b)P3 strictly exceed a+b. Integer equality feasibility and integral cubic splitting remain open.',
            'K_at_pair_sum_positive_U': str(principal_positive),
            'negative_h_C_at_pair_sum_positive_V': str(full_positive),
            'controls_off_endpoint_one': controls, 'requires_finite_base': False,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                              for source in (Path(__file__), Path(__file__).with_name('check_six_support_quotient.py'))},
            'previous_equality_root_certificate_sha256': hashlib.sha256(previous_certificate.read_bytes()).hexdigest(),
            'sympy': sympy.__version__,
            'scope': 'Written unconditional equality lambda4>a+b and endpointone remaining cubic roots>a+b, using two positive identities/interlacing/earlier simpleb-index theorem. Same3offendpointEzero fixtures only, exact Sturm diagnostics; no finite base, new integer triple exclusion, globalQ3closure, exponent/modulus scan,higher2adicshift,floats or Lean. Genus/finiteautomorphismcertificate not used; earlier manuscript/proofs/finite dependencies/oldn7/four native axioms retained.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
