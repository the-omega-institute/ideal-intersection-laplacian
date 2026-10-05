import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    parameters = (first, middle, last)
    equality_last = middle ** 2 + 2 * middle - first
    matrix = support_quotient(parameters, complement=True)
    equal_matrix = matrix.subs(last, equality_last)
    weights = sympy.diag(first, middle, equality_last, first * middle, first * equality_last, middle * equality_last)
    assert (weights * equal_matrix - (weights * equal_matrix).T).applyfunc(sympy.expand) == sympy.zeros(6)
    block_four = equal_matrix.extract((0, 2, 3, 5), (0, 2, 3, 5))
    block_five = equal_matrix.extract((0, 2, 3, 4, 5), (0, 2, 3, 4, 5))
    block_pair = equal_matrix.extract((3, 5), (3, 5))
    assert block_pair == sympy.diag(equality_last, first)
    coefficient_sum = middle * (middle ** 2 + 4 * middle + 5)
    coefficient_pairs = (first * equality_last * (middle ** 2 + 1)
                         + middle ** 2 * (middle + 2) * (middle ** 2 + 3 * middle + 3))
    cubic = sympy.Poly(variable ** 3 - coefficient_sum * variable ** 2 + coefficient_pairs * variable
                       - first * middle * equality_last * (middle + 3), variable)
    assert sympy.expand(block_four.charpoly(variable).as_expr() - (variable - middle) * cubic.as_expr()) == 0
    assert sympy.expand(block_five.charpoly(variable).as_expr() - (variable - middle) ** 2 * cubic.as_expr()) == 0
    positive = (first * (middle - first) * (middle - 2)
                + first * middle * (middle - 2) * (middle + 1)
                + middle ** 2 * (middle + 1) * (middle + 2))
    assert sympy.expand(cubic.eval(middle) - middle * (middle + 1) * positive) == 0
    assert sympy.expand(cubic.eval(first) - first * middle ** 2 * (first + middle + 2) * equality_last) == 0
    assert block_five[:, 3] == sympy.Matrix([0, 0, 0, middle, 0])
    assert sympy.expand(equal_matrix[1, 4] + first * equality_last) == 0
    assert equal_matrix[4, 1] == -middle
    assert sympy.expand(equal_matrix[1, 4] * equal_matrix[4, 1] - first * middle * equality_last) == 0
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    equal_quintic = sympy.Poly(quintic.as_expr().subs(last, equality_last), variable)
    assert equal_quintic.eval(middle) == 0
    remaining_four = sympy.Poly(sympy.cancel(equal_quintic.as_expr() / (variable - middle)), variable)
    assert sympy.expand(equal_quintic.as_expr() - (variable - middle) * remaining_four.as_expr()) == 0
    endpoint = quintic.eval(1)
    residual = sympy.Poly(sympy.cancel((quintic.as_expr() - variable * endpoint) / (variable - 1)), variable)
    equal_residual = sympy.Poly(residual.as_expr().subs(last, equality_last), variable)
    quotient, remainder = equal_residual.div(sympy.Poly(variable - middle, variable))
    assert sympy.expand((middle - 1) * remainder.as_expr() + middle * endpoint.subs(last, equality_last)) == 0
    assert quotient.degree() == 3 and quotient.LC() == 1
    controls = []
    for exponents in ((4, 4, 20), (9, 12, 159), (9, 30, 951)):
        lower, middle_value, upper = exponents
        assert upper == middle_value ** 2 + 2 * middle_value - lower
        direct = support_quotient(exponents, complement=True)
        direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        assert direct_quintic.eval(middle_value) == 0
        assert direct_quintic.diff().eval(middle_value) != 0
        direct_remaining = sympy.Poly(sympy.cancel(direct_quintic.as_expr() / (variable - middle_value)), variable)
        assert direct_remaining.eval(middle_value) != 0
        assert direct_remaining.count_roots(0, middle_value) == 1
        assert direct_remaining.count_roots(middle_value, sympy.oo) == 3
        direct_four = direct.extract((0, 2, 3, 5), (0, 2, 3, 5))
        direct_cubic = sympy.Poly(sympy.cancel(direct_four.charpoly(variable).as_expr() / (variable - middle_value)), variable)
        assert direct_cubic.count_roots(0, middle_value) == 1
        assert direct_cubic.count_roots(middle_value, sympy.oo) == 2
        assert (direct - middle_value * sympy.eye(6)).rank() == 5
        assert (direct.extract((0, 2, 3, 4, 5), (0, 2, 3, 4, 5)) - middle_value * sympy.eye(5)).rank() == 3
        endpoint_value = int(direct_quintic.eval(1))
        assert endpoint_value != 0
        controls.append({'exponents': exponents, 'E': 0, 'h_C_at_one': endpoint_value,
                         'endpoint_one_point': False, 'h_C_at_b': 0,
                         'h_C_derivative_at_b': int(direct_quintic.diff().eval(middle_value)),
                         'full_eigenspace_dimension_at_b': 1, 'principal_five_eigenspace_dimension_at_b': 2,
                         'exact_Sturm_other_nonzero_roots_below_b': 1,
                         'exact_Sturm_other_nonzero_roots_above_b': 3,
                         'exact_Sturm_K_roots_below_b': 1,
                         'exact_Sturm_K_roots_above_b': 2,
                         'remaining_nonzero_quartic': str(direct_remaining.as_expr())})
    return {'written_unconditional_equality_index': 'For real4<=a<=b and c=b(b+2)-a, the complement quotient has b as its simple second-smallest nonzero eigenvalue lambda_3. No endpoint-one condition is needed. Five-support principal block deleting singleton2 has characteristic(x-b)^2K, with K(b)>0 and exactly one Kroot belowb, two above. Its beta_2=beta_3=b sandwich lambda_3=b. Nonzero coupling from scalar pair13 to deleted singleton2 makes full b-eigenspace one-dimensional.',
            'written_endpoint_one_equality_index': 'If also h_C(1)=0, the prior minimum-root theorem gives lambda_2=1; hence mu_1=b is simple and all three other residual roots exceedb. F=(x-b)P_3 with monic cubic P_3; integer feasibility of G(a,b)=0 and integral splitting of P_3 remain open.',
            'written_complete_regime_partition': 'At real4<=a<=b<=c on endpoint one, E>0 has mu_1>b, E<0 has mu_1<b, and E=0 has simplemu_1=b. In every regime mu_2>b. The earlier strict windows are retained; equality fixes the smallest residual root.',
            'principal_cubic_K': str(cubic.as_expr()),
            'K_at_b_positive_decomposition': str(middle * (middle + 1) * positive),
            'generic_endpoint_residual_cubic_quotient': str(quotient.as_expr()),
            'generic_symbolic_identities': 'passed', 'equality_controls_off_endpoint_one': controls,
            'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                              for source in (Path(__file__), Path(__file__).with_name('check_six_support_quotient.py'))},
            'scope': 'Written unbounded equality eigenvalue index and simplicity, unconditional on endpoint one; completes prior endpoint-one Epartition at minimum>=4. No finite base. Three selected exact integer Ezero fixtures are off endpoint one and only diagnose unconditional theorem; no integer endpoint solution or new nonintegrality family/globalQ3closure. Equality Diophantine classification and remaining cubic integer splitting open. No parameter/modulus scan,higher2adicshift,floats/Lean; prior manuscript/proofs/finite dependencies and oldn7/four native axioms retained.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
