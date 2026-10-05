import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    parameters = (first, middle, last)
    total = sum(parameters)
    product = sympy.prod(parameters)
    matrix = support_quotient(parameters, complement=True)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    endpoint = quintic.eval(1)
    residual = sympy.Poly(sympy.cancel((quintic.as_expr() - variable * endpoint) / (variable - 1)), variable)
    comparison = last + first - middle ** 2 - 2 * middle
    assert sympy.expand(quintic.eval(middle) - product ** 2 * comparison) == 0
    assert sympy.expand((middle - 1) * residual.eval(middle)
                        - product ** 2 * comparison + middle * endpoint) == 0
    principal = matrix.extract((2, 3, 4, 5), (2, 3, 4, 5))
    quadratic = variable ** 2 - (first * middle + first + middle + last) * variable + last * (first + middle)
    assert sympy.expand(principal.charpoly(variable).as_expr()
                        - (variable - first) * (variable - middle) * quadratic) == 0
    assert sympy.expand(quadratic.subs(variable, middle)
                        - first * (last - middle ** 2 - middle)) == 0
    assert sympy.expand(quadratic.subs(variable, first + middle)
                        + first * middle * (first + middle)) == 0
    assert sympy.expand(last - middle ** 2 - middle - comparison - (middle - first)) == 0
    pair_principal = matrix.extract((3, 4, 5), (3, 4, 5))
    assert pair_principal == sympy.diag(last, middle, first)
    weights = sympy.diag(first, middle, last, first * middle, first * last, middle * last)
    assert weights * matrix == (weights * matrix).T
    controls = []
    for pair, bracket in (((9, 12), (177, 178)), ((9, 30), (247, 248))):
        exponent_polynomial = sympy.Poly(endpoint.subs({first: pair[0], middle: pair[1]}), last)
        threshold = pair[1] ** 2 + 2 * pair[1] - pair[0]
        lower, upper = bracket
        lower_value = int(exponent_polynomial.eval(lower))
        upper_value = int(exponent_polynomial.eval(upper))
        assert lower_value < 0 < upper_value
        assert exponent_polynomial.count_roots(pair[1], sympy.oo) == 1
        assert exponent_polynomial.count_roots(lower, upper) == 1
        above = lower >= threshold
        below = upper <= threshold
        assert above != below
        controls.append({'fixed_exponents_a_b': pair,
                         'endpoint_one_exponent_cubic': str(exponent_polynomial.as_expr()),
                         'unique_real_c_bracket': bracket,
                         'h_C_at_one_at_bracket': [lower_value, upper_value],
                         'exact_Sturm_roots_on_c_greater_than_b': 1,
                         'exact_Sturm_roots_in_bracket': 1,
                         'comparison_threshold_for_c': threshold,
                         'middle_root_branch': 'mu_1>b' if above else 'a<mu_1<b<mu_2',
                         'new_smallest_root_window': [pair[1], sum(pair)] if above else [pair[0], pair[1]],
                         'previous_smallest_root_window': [pair[0], sum(pair)],
                         'integer_endpoint_one_triple_claimed': False})
    return {'written_middle_root_location': 'For real4<=a<=b<=c on h_C(1)=0, if c+a>b(b+2), then mu_1>b. If c+a<b(b+2), exactly one residual root is belowb and a<mu_1<b<mu_2. If equality holds, F(b)=0; no smallest-root identification or integer feasibility is claimed for this equality regime.',
            'written_refined_divisor_windows': 'Integer spectra require d|N with b<d<min(c,a+b) in the positive comparison regime, or a<d<b in the negative regime. Apply prior coefficient/anchor congruences within these windows. Equality gives b as a residual integer root, not integer splitting of the other factor.',
            'generic_middle_determinant_identity': str(product ** 2 * comparison),
            'generic_principal_quadratic': str(quadratic),
            'quadratic_at_b': str(first * (last - middle ** 2 - middle)),
            'generic_symbolic_identities': 'passed',
            'fully_distinct_real_endpoint_controls': controls,
            'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                              for source in (Path(__file__), Path(__file__).with_name('check_six_support_quotient.py'))},
            'scope': 'Written unbounded real endpoint-one smallest-root location relative to middle exponent, using existing determinant identity and principal interlacing. No finite base required. Exactly two selected fixed-pair cubic/Sturm controls represent real algebraic endpoint points, not integer triples or finite proof of the theorem. Equality only asserts b is a residual root. No new nonintegrality family, integer-feasibility decision, globalQ3closure, exponent/modulus scan, higher2adicshift, floating spectra or Lean. Prior manuscript/proofs/finite dependencies and oldn7/four native axioms retained.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
