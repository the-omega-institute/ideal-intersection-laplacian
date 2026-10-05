import hashlib
from itertools import product
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def certificate():
    first, middle, last, variable = sympy.symbols('a b c x')
    shift, family_parameter = sympy.symbols('m k')
    parameters = (first, middle, last)
    matrix = support_quotient(parameters, complement=True)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    endpoint = quintic.eval(1)
    constant = first * middle * last * (first + middle + last) * (
        first * middle + first * last + middle * last + first + middle + last)
    assert sympy.expand(quintic.eval(0) + constant) == 0
    for permutation in ((middle, first, last), (last, middle, first)):
        assert sympy.expand(endpoint.subs(dict(zip(parameters, permutation)), simultaneous=True) - endpoint) == 0
    parity = []
    for residues in product(range(2), repeat=3):
        value = int(endpoint.subs(dict(zip(parameters, residues)))) % 2
        assert value == int(len(set(residues)) == 1)
        parity.append({'residues': residues, 'h_C_at_one_mod2': value})
    modulo_three = []
    for residues in product(range(3), repeat=3):
        replacement = dict(zip(parameters, residues))
        endpoint_residue = int(endpoint.subs(replacement)) % 3
        constant_residue = int(constant.subs(replacement)) % 3
        assert endpoint_residue != 0 or constant_residue == 0
        modulo_three.append({'residues': residues, 'h_C_at_one_mod3': endpoint_residue,
                             'constant_mod3': constant_residue})
    boundary = (first - 1) * (2 * first - 1)
    repeated = {middle: first, last: boundary}
    assert sympy.expand(endpoint.subs(repeated)) == 0
    factors = [first ** 2, first - 1, 2 * first - 1,
               2 * first ** 2 - first + 1, 4 * first ** 3 - 3 * first ** 2 + first + 1]
    boundary_constant = sympy.prod(factors)
    assert sympy.expand(constant.subs(repeated) - boundary_constant) == 0
    assert sympy.Poly(boundary_constant, first).degree() == 9
    assert sympy.Poly(boundary_constant, first).LC() == 16
    assert int(boundary_constant.subs(first, 4)) % 5 == 2
    assert int(boundary_constant.subs(first, 5)) % 7 == 1
    valuation_family = 36 * family_parameter + 26
    for factor in factors[1:]:
        assert sympy.Poly(factor.subs(first, valuation_family), family_parameter, modulus=2).is_one
    assert sympy.Poly(valuation_family / 2, family_parameter, modulus=2).is_one
    for index in (0, 1, 3, 4):
        reduced = sympy.Poly(factors[index].subs(first, valuation_family), family_parameter, modulus=3)
        assert reduced.degree() == 0 and reduced.nth(0) % 3 != 0
    assert sympy.expand((2 * valuation_family - 1) / 3 - (24 * family_parameter + 17)) == 0
    assert sympy.Poly((2 * valuation_family - 1) / 3, family_parameter, modulus=3).nth(0) % 3 != 0
    divisor_family = 6 * family_parameter
    assert sympy.cancel(divisor_family ** 2 / (3 * divisor_family / 2)) == 4 * family_parameter
    assert sympy.expand((boundary - 2 * first).subs(first, 6 + shift)
                        - (2 * shift ** 2 + 19 * shift + 43)) == 0
    repeated_quintic = sympy.Poly(quintic.as_expr().subs(repeated), variable)
    residual = sympy.Poly(sympy.cancel(repeated_quintic.as_expr() / (variable - 1)), variable)
    sign_factor = 8 * first ** 5 + 48 * first ** 4 - 132 * first ** 3 + 95 * first ** 2 - 32 * first + 4
    expected_value = -first ** 2 * (4 * first ** 2 - 2 * first - 1) * sign_factor / 16
    assert sympy.expand(residual.eval(3 * first / 2) - expected_value) == 0
    positive = sympy.Poly(sign_factor.subs(first, 4 + shift).expand(), shift)
    assert positive.all_coeffs() == [8, 208, 1916, 8239, 16920, 13428]
    assert sympy.expand((4 * first ** 2 - 2 * first - 1).subs(first, 4 + shift)
                        - (4 * shift ** 2 + 30 * shift + 55)) == 0
    controls = []
    for exponents in ((8, 8, 105), (9, 9, 136), (20, 20, 741)):
        direct = support_quotient(exponents, complement=True)
        direct_quintic = sympy.Poly(sympy.cancel(direct.charpoly(variable).as_expr() / variable), variable)
        assert direct_quintic.eval(1) == 0
        direct_constant = -int(direct_quintic.eval(0))
        assert direct_constant == int(constant.subs(dict(zip(parameters, exponents))))
        assert direct_constant % 12 == 0
        controls.append({'exponents': exponents, 'h_C_at_one': 0, 'quartic_constant': direct_constant,
                         'constant_divided_by12': direct_constant // 12})
    sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
    return {'written_uniform_divisibility': 'For every positive integer endpoint-one triple,12divides F(0)=rs(p+s): mixed parity gives4and the complete modulo3nonzero-residue argument gives3.',
            'written_full_surface_gcd': 'For all ordered integer4<=a<=b<=c on h_C(1)=0, gcd of the quartic constants is exactly12. Boundary family a=36k+26 gives v2=2,v3=1; residuesa=4mod5/a=5mod7exclude5/7; boundary polynomial degree9with leading16 excludes a universal prime ell>=11 by finite-field root count. This includes settled repeated triples, not a conclusion about the remaining fully distinct region.',
            'written_infinite_divisor_candidates': 'For a=6k,k>=1,c=(a-1)(2a-1), h_C(1)=0, c>2a, d=3a/2 lies in(a,2a)and dividesa^2henceF(0), but F(d)<0. Divisibility/size alone cannot eliminate all window candidates; F(d)=0is essential.',
            'boundary_constant_factorization': str(boundary_constant),
            'boundary_candidate_evaluation': str(expected_value),
            'positive_sign_factor_at_a4plusm': str(positive.as_expr()),
            'parity_table': parity, 'modulo_three_table': modulo_three,
            'generic_symbolic_identities': 'passed', 'endpoint_one_controls': controls,
            'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest() for source in sources},
            'scope': 'Written universal constant divisibility12, exact full-surface gcd12and unbounded repeated-family false-positive divisor candidates with exact negative evaluation. Eight basic parity and27mod3residue rows, three established controls supplement proofs. No higher2adicshift or arbitrary parameter/modulus scan/floats/Lean. No fullydistinct survivor gcd classification, new nonintegrality family or fullQ3closure. Earlier proofs/certificates/manuscript unchanged; oldn7/four native axioms unaffected.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
