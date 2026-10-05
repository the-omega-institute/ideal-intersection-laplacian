import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def integer_horner(coefficients, candidate):
    result = 0
    for coefficient in coefficients:
        result = result * candidate + coefficient
    return result


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    parameters = (first, middle, last)
    total = sum(parameters)
    pairs = first * middle + first * last + middle * last
    product = first * middle * last
    constant = product * total * (pairs + total)
    cubic_coefficient = pairs + 3 * total - 1
    quadratic_coefficient = total * product + 2 * total * pairs + 3 * total ** 2 - 3 * total + 1
    linear_coefficient = (product ** 2 + (total ** 2 - total + 1) * product
                          + total ** 2 * pairs + pairs ** 2 + total ** 3
                          - 3 * total ** 2 + 3 * total - 1)
    matrix = support_quotient(parameters, complement=True)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    endpoint = quintic.eval(1)
    residual = sympy.Poly(sympy.cancel((quintic.as_expr() - variable * endpoint) / (variable - 1)), variable)
    expected = (variable ** 4 - cubic_coefficient * variable ** 3
                + quadratic_coefficient * variable ** 2 - linear_coefficient * variable + constant)
    assert sympy.expand(residual.as_expr() - expected) == 0
    for exponent in parameters:
        numerator = -product ** 2 * (exponent ** 2 + 3 * exponent - total)
        assert sympy.expand(quintic.eval(exponent) - numerator) == 0
        assert sympy.expand((exponent - 1) * residual.eval(exponent)
                            - numerator + exponent * endpoint) == 0
    candidate = sympy.symbols('d')
    assert sympy.expand(residual.eval(candidate) - constant + linear_coefficient * candidate
                        - candidate ** 2 * (candidate ** 2 - cubic_coefficient * candidate
                                          + quadratic_coefficient)) == 0
    controls = []
    for exponents in ((8, 8, 105), (9, 9, 136), (20, 20, 741)):
        replacement = dict(zip(parameters, exponents))
        direct = support_quotient(exponents, complement=True)
        direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        assert direct_quintic.eval(1) == 0
        direct_residual = sympy.Poly(sympy.cancel(direct_quintic.as_expr() / (variable - 1)), variable)
        assert sympy.expand(direct_residual.as_expr() - residual.as_expr().subs(replacement)) == 0
        coefficients = [int(coefficient) for coefficient in direct_residual.all_coeffs()]
        direct_constant = coefficients[-1]
        direct_linear = -coefficients[-2]
        lower, middle_value, upper = exponents
        ceiling = min(upper, lower + middle_value)
        anchors = []
        for exponent in exponents:
            numerator = -sympy.prod(exponents) ** 2 * (exponent ** 2 + 3 * exponent - sum(exponents))
            anchor, remainder = divmod(int(numerator), exponent - 1)
            assert remainder == 0 and anchor == integer_horner(coefficients, exponent)
            anchors.append((exponent, anchor))
        candidates = []
        for divisor in sympy.divisors(direct_constant):
            divisor = int(divisor)
            if not lower < divisor < ceiling:
                continue
            linear_remainder = (direct_constant // divisor - direct_linear) % divisor
            anchor_remainders = []
            for exponent, anchor in anchors:
                difference = divisor - exponent
                remainder = anchor if difference == 0 else anchor % abs(difference)
                anchor_remainders.append(remainder)
                if difference != 0:
                    assert integer_horner(coefficients, divisor) % abs(difference) == remainder
            evaluation = integer_horner(coefficients, divisor)
            assert evaluation == int(direct_residual.eval(divisor))
            assert evaluation % (divisor ** 2) == (divisor * linear_remainder) % (divisor ** 2)
            passed_linear = linear_remainder == 0
            passed_anchors = all(remainder == 0 for remainder in anchor_remainders)
            if evaluation == 0:
                assert passed_linear and passed_anchors
            candidates.append({'divisor': divisor, 'linear_remainder_mod_d': linear_remainder,
                               'anchor_remainders_at_a_b_c': anchor_remainders,
                               'passes_linear': passed_linear, 'passes_anchors': passed_anchors,
                               'passes_both': passed_linear and passed_anchors,
                               'exact_F_at_d': evaluation})
        controls.append({'exponents': exponents, 'quartic_coefficients': coefficients,
                         'quartic_constant': direct_constant, 'linear_D': direct_linear,
                         'anchor_values': anchors, 'candidate_count': len(candidates),
                         'linear_survivors': [entry['divisor'] for entry in candidates if entry['passes_linear']],
                         'anchor_survivors': [entry['divisor'] for entry in candidates if entry['passes_anchors']],
                         'combined_survivors': [entry['divisor'] for entry in candidates if entry['passes_both']],
                         'candidates': candidates})
    positive_control = controls[-1]
    assert positive_control['quartic_constant'] % 21 == 0
    positive_entry = next(entry for entry in positive_control['candidates'] if entry['divisor'] == 21)
    assert positive_entry['exact_F_at_d'] == 1207587225600 > 0
    boundary = (first - 1) * (2 * first - 1)
    assert sympy.expand(endpoint.subs({middle: first, last: boundary})) == 0
    boundary_at_a = sympy.factor(residual.eval(first).subs({middle: first, last: boundary}))
    assert sympy.expand(boundary_at_a - first ** 4 * (first - 1) * (2 * first - 1) ** 2
                        * (first ** 2 - 4 * first + 1)) == 0
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
    return {'written_linear_congruence': 'For integer endpoint-one exponents and an integer root d>0 of F, d|N and N/d=D mod d, with D=r^2+(s^2-s+1)r+s^2p+p^2+s^3-3s^2+3s-1. Equivalently d^2 divides N-Dd. Necessary, not sufficient.',
            'written_anchor_congruences': 'For exponents e in {a,b,c} all>=4 on endpoint one, K_e=-r^2(e^2+3e-s)/(e-1)=F(e) is integral. An integer root d requires d-e|K_e when d!=e and K_e=0 when d=e. Equivalently (d-e)(e-1)|r^2(e^2+3e-s) when d!=e. These avoid evaluating F at d and are necessary, not sufficient.',
            'sign_counterexample': {'exponents': [20, 20, 741], 'candidate': 21,
                                    'F_at_candidate': positive_entry['exact_F_at_d'],
                                    'scope': 'Existing repeated boundary, not a fully distinct surviving triple. F(d)<0 is not universal over the full endpoint-one divisor window. Its truth in the narrower fully distinct integer region is undetermined.'},
            'boundary_F_at_a': str(boundary_at_a),
            'generic_symbolic_identities': 'passed', 'endpoint_one_controls': controls,
            'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
            'scope': 'Written universal necessary coefficient/anchor root congruences and one exact positive-value counterexample on an established repeated control. Exactly the same three controls/23 divisor candidates as the prior window certificate; no exponent/modulus scan or higher endpoint two-adic lifting. No fully distinct sign decision, new nonintegrality family, sufficient root test, global Q3 closure or Lean. Prior manuscript/proofs/finite dependencies and old n7/four native axioms retained.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
