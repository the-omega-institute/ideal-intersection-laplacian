import ast
import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def integer_horner(coefficients, point):
    value = 0
    for coefficient in coefficients:
        value = value * point + coefficient
    return value


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    minimum_shift, middle_shift, last_shift, interval_shift = sympy.symbols('m t u v')
    parameters = (first, middle, last)
    matrix = support_quotient(parameters, complement=True)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    residual = sympy.Poly(sympy.cancel((quintic.as_expr() - variable * quintic.eval(1)) / (variable - 1)), variable)
    assert residual.degree() == 4 and residual.LC() == 1
    assert sympy.expand(quintic.as_expr() - variable * quintic.eval(1) - (variable - 1) * residual.as_expr()) == 0
    total = first + middle + last
    pairs = first * middle + first * last + middle * last
    product = first * middle * last
    symmetric = (variable ** 4 + (1 - pairs - 3 * total) * variable ** 3
                 + (total * product + 2 * total * pairs + 3 * total ** 2 - 3 * total + 1) * variable ** 2
                 - (product ** 2 + (total ** 2 - total + 1) * product + total ** 2 * pairs
                    + pairs ** 2 + total ** 3 - 3 * total ** 2 + 3 * total - 1) * variable
                 + product * total * (pairs + total))
    assert sympy.expand(residual.as_expr() - symmetric) == 0
    assert sympy.expand(residual.eval(1) - quintic.diff().eval(1) + quintic.eval(1)) == 0
    substitution = 4 * interval_shift / (1 + interval_shift)
    assert sympy.cancel(substitution.subs(interval_shift, variable / (4 - variable)) - variable) == 0
    transformed = sympy.cancel((1 + interval_shift) ** 4 * residual.as_expr().subs(variable, substitution))
    shifts = {first: 8 + minimum_shift, middle: 8 + minimum_shift + middle_shift,
              last: 8 + minimum_shift + middle_shift + last_shift}
    positive = sympy.Poly(transformed.subs(shifts, simultaneous=True).expand(),
                          minimum_shift, middle_shift, last_shift, interval_shift)
    assert len(positive.terms()) == 350
    assert all(coefficient > 0 for monomial, coefficient in positive.terms())
    assert positive.nth(0, 0, 0, 0) == 2654208
    assert positive.nth(0, 0, 0, 4) == 188596
    boundary_four = sympy.Poly(positive.as_expr(), interval_shift).nth(4)
    assert sympy.expand(boundary_four - residual.eval(4).subs(shifts, simultaneous=True)) == 0
    vectors = {}
    for monomial, coefficient in positive.terms():
        powers, interval_degree = monomial[:3], monomial[3]
        vectors.setdefault(powers, [0] * 5)[interval_degree] = int(coefficient)
    assert len(vectors) == 70
    assert all(all(coefficient > 0 for coefficient in vector) for vector in vectors.values())
    reconstructed = sum(coefficient * minimum_shift ** powers[0] * middle_shift ** powers[1]
                        * last_shift ** powers[2] * interval_shift ** degree
                        for powers, vector in vectors.items() for degree, coefficient in enumerate(vector))
    assert sympy.expand(reconstructed - positive.as_expr()) == 0
    note = Path(__file__).parents[1] / 'notes/endpoint-one-spectral-gap.md'
    if note.exists():
        recorded = {}
        for line in note.read_text().splitlines():
            cells = [cell.strip() for cell in line.split('|')]
            if len(cells) == 6 and all(cell.isdigit() for cell in cells[1:4]):
                recorded[tuple(map(int, cells[1:4]))] = ast.literal_eval(cells[4])
        assert recorded == vectors
    fixtures = []
    for exponents in [(8, 9, 10), (8, 118, 122), (9, 12, 100), (20, 22, 815), (40, 200, 5866),
                      (8, 8, 105), (9, 9, 136), (20, 20, 741)]:
        direct = support_quotient(exponents, complement=True)
        direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        assert direct_quintic == sympy.Poly(quintic.as_expr().subs(dict(zip(parameters, exponents))), variable)
        endpoint = int(direct_quintic.eval(1))
        direct_residual = sympy.Poly(sympy.cancel((direct_quintic.as_expr() - variable * endpoint) / (variable - 1)), variable)
        coefficients = list(map(int, direct_residual.all_coeffs()))
        values = [integer_horner(coefficients, point) for point in (0, 1, 4)]
        assert values == [int(direct_residual.eval(point)) for point in (0, 1, 4)]
        assert all(value > 0 for value in values)
        assert direct_residual.count_roots(0, 4) == 0
        record = {'exponents': exponents, 'h_C_at_one': endpoint, 'residual_quartic_coefficients': coefficients,
                  'integer_Horner_at_0_1_4': values, 'residual_roots_in_0_through_4': 0}
        if endpoint == 0:
            assert direct_quintic.diff().eval(1) == values[1] > 0
            assert direct_quintic.count_roots(0, 4) == 1
            assert direct_residual.count_roots(4, sympy.oo) == 4
            record.update({'spectral_root_one_simple': True, 'other_quotient_roots_strictly_above_four': 4,
                           'actual_spectral_derivative_at_one': values[1]})
        fixtures.append(record)
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
    return {'written_residual_positivity': 'For all reala,b,c>=8, F(x)=(h_C(x)-x*h_C(1))/(x-1), continued polynomially at1, is strictly positive throughout closedinterval[0,4].',
            'written_endpoint_one_spectral_gap': 'For realexponentsa,b,c>=8with h_C(1)=0, spectralroot1 is simple and the smallestpositive quotientroot; allfour remainingquotientroots are strictlygreaterthan4. Weightedselfadjointpositive-semidefinitequotient gives realnonnegative roots. This is spectral simplicity, distinct from prior exponent-cubic simplicity.',
            'scope_of_consequence': 'Underintegerexponents/integral-spectrumassumption onendpointone, the otherfourquotientroots must be integers>=5. Positivity/location alone does not prove a nonintegerroot or exclude integerendpointonepoints. FullQ3 remainsopen.',
            'symmetric_quartic_formula': 'x^4+(1-p-3s)x^3+(sr+2sp+3s^2-3s+1)x^2-[r^2+(s^2-s+1)r+s^2p+p^2+s^3-3s^2+3s-1]x+rs(p+s); s=a+b+c,p=ab+ac+bc,r=abc.',
            'positive_identity': {'substitution': 'a=8+m,b=8+m+t,c=8+m+t+u,x=4v/(1+v),m,t,u,v>=0',
                                  'clearing_factor': '(1+v)^4', 'nonzero_positive_terms': 350,
                                  'constant': 2654208, 'v_four_constant': 188596,
                                  'ascending_v_vectors': [{'powers_m_t_u': list(powers), 'coefficients': vector}
                                                          for powers, vector in sorted(vectors.items())]},
            'note_vectors_checked': 70, 'direct_quotient_fixtures': fixtures,
            'sympy': sympy.__version__, 'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
            'scope': 'Written universal residual positivity on closed[0,4]and endpoint-one spectral simplicity/gap, complete350termpositiveidentity and all70notevectors. Eight directquotient/integer-Horner/exactSturmfixtures, including3genuineendpoint-onecontrols, supplement proofs. Nofinitebase/parameterormodulusscan/floats/Lean. Residual is a spectralfactor onlyonh_C(1)=0; otherrootlocation doesnotcloseQ3. Oldresults/certificates/manuscriptunchanged; oldn7/fournativeaxiomsunaffected.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
