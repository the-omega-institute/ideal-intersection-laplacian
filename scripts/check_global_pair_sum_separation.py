import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient, support_weights


def roots_with_multiplicity(polynomial, lower, upper):
    return sum(multiplicity * factor.count_roots(lower, upper)
               for factor, multiplicity in polynomial.sqf_list()[1])


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    parameters = (first, middle, last)
    matrix = support_quotient(parameters, complement=True)
    weighted = sympy.diag(*support_weights(parameters)) * matrix
    assert weighted == weighted.T
    assert matrix * sympy.ones(6, 1) == sympy.zeros(6, 1)
    characteristic = sympy.Poly(matrix.charpoly(variable).as_expr(), variable)
    quintic = characteristic.exquo(sympy.Poly(variable, variable))
    low_block = matrix.extract((2, 3, 4, 5), (2, 3, 4, 5))
    quadratic = variable ** 2 - (first * middle + first + middle + last) * variable + last * (first + middle)
    assert sympy.expand(low_block.charpoly(variable).as_expr()
                        - (variable - first) * (variable - middle) * quadratic) == 0
    assert sympy.expand(quadratic.subs(variable, first + middle) + first * middle * (first + middle)) == 0
    five_block = matrix.extract((0, 1, 3, 4, 5), (0, 1, 3, 4, 5))
    high_block = matrix.extract((0, 1, 4, 5), (0, 1, 4, 5))
    assert five_block[2, 2] == last
    assert all(five_block[2, index] == five_block[index, 2] == 0 for index in (0, 1, 3, 4))
    assert sympy.expand(five_block.charpoly(variable).as_expr()
                        - (variable - last) * high_block.charpoly(variable).as_expr()) == 0
    high_pair = matrix.extract((0, 1), (0, 1))
    shifted = (high_pair - (middle + last) * sympy.eye(2)).applyfunc(sympy.expand)
    assert shifted == sympy.Matrix([[middle * last, -middle], [-first, first * last + first - middle]])
    shifted_determinant = middle * (first * (last ** 2 + last - 1) - middle * last)
    assert sympy.expand(shifted.det() - shifted_determinant) == 0
    positive_remainder = ((first - 2) * (last ** 2 + last - 1)
                          + last * (last - middle) + last ** 2 + 2 * last - 2)
    assert sympy.expand(shifted_determinant / middle - positive_remainder) == 0
    pair_identities = []
    for selected_first, selected_second, remaining in ((first, middle, last), (middle, last, first)):
        positive_factor = (selected_first * selected_second * (selected_first + selected_second) * (remaining - 1)
                           + remaining * (selected_first * selected_second - selected_first - selected_second + remaining))
        expected = -first * middle * last * (selected_first + selected_second + 1) * positive_factor
        assert sympy.expand(quintic.eval(selected_first + selected_second) - expected) == 0
        pair_identities.append(str(expected))
    controls = []
    for exponents in ((2, 2, 3), (4, 4, 4), (9, 9, 136), (9, 12, 159), (9, 30, 951)):
        direct = support_quotient(exponents, complement=True)
        polynomial = sympy.Poly(direct.charpoly(variable).as_expr(), variable)
        assert polynomial == sympy.Poly(characteristic.as_expr().subs(dict(zip(parameters, exponents))), variable)
        endpoints = (exponents[0] + exponents[1], exponents[1] + exponents[2])
        evaluations = []
        for endpoint in endpoints:
            determinant = (endpoint * sympy.eye(6) - direct).det(method='bareiss')
            assert determinant == polynomial.eval(endpoint) < 0
            below = roots_with_multiplicity(polynomial, -sympy.oo, endpoint)
            above = roots_with_multiplicity(polynomial, endpoint, sympy.oo)
            assert (below, above) == (3, 3)
            evaluations.append({'endpoint': endpoint, 'Bareiss_determinant': int(determinant),
                                'roots_below_with_multiplicity': int(below), 'roots_above_with_multiplicity': int(above)})
        case = {'exponents': exponents, 'characteristic_polynomial': str(sympy.factor(polynomial.as_expr())),
                'pair_sum_checks': evaluations}
        if exponents == (4, 4, 4):
            expected = variable * (variable - 20) * (variable ** 2 - 32 * variable + 48) ** 2
            assert sympy.expand(polynomial.as_expr() - expected) == 0
            assert polynomial.count_roots(-sympy.oo, 8) == 2
            case['distinct_roots_below_8'] = 2
            case['roots_below_8_with_multiplicity'] = 3
        if exponents == (9, 9, 136):
            assert polynomial.eval(1) == 0
            quartic = polynomial.exquo(sympy.Poly(variable * (variable - 1), variable))
            assert roots_with_multiplicity(quartic, 9, 18) == 1
            assert roots_with_multiplicity(quartic, -sympy.oo, 145) == 1
            assert roots_with_multiplicity(quartic, 145, sympy.oo) == 3
            case['endpoint_one_quartic_coefficients'] = list(map(int, quartic.all_coeffs()))
            case['quartic_roots_in_9_18'] = 1
            case['quartic_roots_below_145'] = 1
            case['quartic_roots_above_145_with_multiplicity'] = 3
        controls.append(case)
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py'),
               Path(__file__).with_name('check_fully_distinct.py')]
    return {'written_theorem': 'For real 2<=a<=b<=c, lambda_3<a+b<=b+c<lambda_4, counting multiplicity.',
            'written_proof': 'Four-support low block and interlacing give lambda_3<a+b. Positive definite shifted singleton pair gives lambda_5,lambda_6>b+c. Negative determinant at b+c and parity then give exactly three eigenvalues below it.',
            'endpoint_one_consequence': 'At real minimum>=4 on h_C(1)=0: a<mu_1<min(c,a+b), and b+c<mu_2<=mu_3<=mu_4.',
            'symbolic_identities': 'passed', 'pair_sum_quintic_identities': pair_identities,
            'shifted_high_pair_determinant': str(shifted_determinant),
            'positive_determinant_remainder': str(positive_remainder), 'specified_controls': controls,
            'root_count_method': 'Exact Sturm counts on squarefree factors, weighted by multiplicity; interval endpoints are checked nonroots.',
            'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
            'scope': 'Written global real theorem; five fixed supplementary controls and ten direct Bareiss determinants. No scan, floats or Lean. No full integer-splitting, three-prime classification or full Q3 closure. Manuscript unchanged; old n7 open and four native axioms retained.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
