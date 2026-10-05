import hashlib
import json
from pathlib import Path

import sympy

from check_endpoint_one_equality_cubic import certificate as cubic_certificate


def certificate():
    prior = cubic_certificate()
    middle, product, anchor_symbol = sympy.symbols('b q w')
    curve = sympy.sympify(prior['curve_G'])
    discriminant = sympy.sympify(prior['discriminant_expanded_q_b'])
    anchor = -1 + 2 * middle + 3 * middle ** 2 + sympy.Rational(7, 2) * middle ** 3
    curve_remainder = (sympy.Rational(143, 4) * middle ** 3
                       + sympy.Rational(185, 4) * middle ** 2
                       + 43 * middle - sympy.Rational(37, 2))
    assert sympy.expand(curve.subs(product, anchor) - middle ** 4 * curve_remainder) == 0
    discriminant_remainder, remainder = sympy.div(
        sympy.expand(discriminant.subs(product, anchor)
                     - 13 * middle ** 2 + 18 * middle ** 3), middle ** 4, middle)
    assert remainder == 0
    assert discriminant_remainder.subs(middle, 0) == -169
    assert all(coefficient.q & (coefficient.q - 1) == 0
               for coefficient in sympy.Poly(discriminant_remainder, middle).all_coeffs())
    difference_factor = ((3 * middle - 1) * (product + anchor_symbol)
                         + middle * (middle ** 2 + 4 * middle - 1))
    assert sympy.expand(curve - curve.subs(product, anchor_symbol)
                        - (product - anchor_symbol) * difference_factor) == 0
    assert difference_factor.subs({middle: 0, product: -1, anchor_symbol: -1}) == 2
    discriminant_difference, remainder = sympy.div(
        discriminant - discriminant.subs(product, anchor_symbol),
        product - anchor_symbol, product)
    assert remainder == 0
    assert sympy.diff(discriminant, product).subs({middle: 0, product: -1}) == -4
    unit = sympy.symbols('u')
    leading = (13 * middle ** 2 - 18 * middle ** 3).subs(middle, 13 * unit)
    assert sympy.expand(leading - 13 ** 3 * unit ** 2 * (1 - 18 * unit)) == 0
    assert sympy.invert(18, 13) == 8
    assert (1 - 18 * 8) % 13 == 0
    assert 13 * 8 == 104
    repository = Path(__file__).resolve().parents[1]
    return {
        'anchor_w': str(anchor),
        'curve_anchor_identity': 'G(w,b)=b^4*S(b)',
        'S': str(curve_remainder),
        'discriminant_anchor_identity': 'Delta(w,b)=13*b^2-18*b^3+b^4*T(b)',
        'T_ascending_coefficients': [str(coefficient) for coefficient in reversed(
            sympy.Poly(discriminant_remainder, middle).all_coeffs())],
        'coefficient_ring': 'Z[1/2], contained in Z_13',
        'curve_difference_factor': str(difference_factor),
        'negative_branch_difference_unit_mod13': 2,
        'discriminant_difference_quotient': str(discriminant_difference),
        'generic_quotient_and_sylvester_reverified': True,
        'valuation_congruence': 'On G=0, q=-1 mod13, e=v_13(b)>=1: q=w mod13^(4e), Delta=13*b^2-18*b^3 mod13^(4e).',
        'e_at_least_two': 'v_13(Delta)=2e+1, odd; hence nonsquare and cubic does not split over Q_13.',
        'e_equals_one': 'b=13*u with u a unit; Delta=13^3*u^2*(1-18*u) mod13^4. If u!=8 mod13, valuation is3 and the discriminant is nonsquare.',
        'necessary_negative_branch_integer_splitting_condition': 'b=104 mod169',
        'exceptional_residue': {'u_mod13': 8, 'b_mod169': 104,
                                'discriminant_valuation_at_least': 4,
                                'splitting_decided': False},
        'positive_branch_at13': 'Unchanged: a^2=-1 mod13 gives q=1 and three simple Z_13 roots.',
        'prior_cubic_certificate_sha256': hashlib.sha256(
            (repository / 'results/endpoint-one-equality-cubic.json').read_bytes()).hexdigest(),
        'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                          for source in (Path(__file__),
                                         Path(__file__).with_name('check_endpoint_one_equality_cubic.py'),
                                         Path(__file__).with_name('check_six_support_quotient.py'))},
        'sympy': sympy.__version__,
        'scope': 'Written unbounded valuation obstruction at the specified prime13 on the negative equality branch. Exact rational polynomial identities, direct six-support characteristic identity and independent Sylvester discriminant reverified. No prime/power/exponent scan, finite exponent base, constructed integer equality point or Lean. The b=104 mod169 negative branch, global equality classification and full Q3 remain open.',
    }


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
