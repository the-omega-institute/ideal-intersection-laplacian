import hashlib
import json
from pathlib import Path

import sympy

from check_endpoint_one_equality_cubic import certificate as cubic_certificate


def certificate():
    prior = cubic_certificate()
    first, middle, product, variable, anchor_symbol = sympy.symbols('a b q x v')
    curve = sympy.sympify(prior['curve_G'])
    cubic = sympy.sympify(prior['cubic_P3'])
    discriminant = sympy.sympify(prior['discriminant_expanded_q_b'])
    anchor = -1 + 2 * middle + 3 * middle ** 2
    curve_quotient = -middle ** 4 - 8 * middle ** 3 + 8 * middle ** 2 + 20 * middle - 7
    discriminant_coefficients = [-4, -302, -324, 3263, 5840, -14202, -17770,
                                 5913, 10222, 376, -1774, -328, 56, 13]
    discriminant_quotient = sum(coefficient * middle ** degree
                                for degree, coefficient in enumerate(discriminant_coefficients))
    assert sympy.expand(curve.subs(product, anchor) - middle ** 3 * curve_quotient) == 0
    assert sympy.expand(discriminant.subs(product, anchor)
                        - 13 * middle ** 2 - middle ** 3 * discriminant_quotient) == 0
    difference_factor = ((3 * middle - 1) * (product + anchor_symbol)
                         + middle * (middle ** 2 + 4 * middle - 1))
    assert sympy.expand(curve - curve.subs(product, anchor_symbol)
                        - (product - anchor_symbol) * difference_factor) == 0
    assert difference_factor.subs({middle: 0, product: -1, anchor_symbol: -1}) == 2
    discriminant_difference = sympy.div(
        discriminant - discriminant.subs(product, anchor_symbol),
        product - anchor_symbol, product)
    assert discriminant_difference[1] == 0
    assert sympy.expand(curve.subs(middle, 0) - (1 - product ** 2)) == 0
    assert sympy.expand(cubic.subs({middle: 0, product: -1})
                        - variable * (variable + 1) ** 2) == 0
    assert sympy.expand(cubic.subs({middle: 0, product: 1})
                        - variable * (variable ** 2 + 1)) == 0
    assert sympy.expand((first * (middle * (middle + 2) - first)).subs(middle, 0)
                        + first ** 2) == 0
    prime_examples = []
    for prime in (5, 7, 11):
        squares = sorted({residue ** 2 % prime for residue in range(prime)})
        assert 13 % prime not in squares
        if prime in (7, 11):
            assert prime % 4 == 3 and prime - 1 not in squares
        prime_examples.append({'prime': prime, 'squares': squares,
                               'thirteen_is_nonsquare': True,
                               'minus_one_is_nonsquare': prime - 1 not in squares})
    prior_mod_five = json.loads((Path(__file__).resolve().parents[1]
                                / 'results/endpoint-one-equality-mod-five.json').read_text())
    split_pairs = prior_mod_five['equality_residue_tables']['5']['split_rows']
    excluded_pairs = [pair for pair in split_pairs if pair[1] == 0 and pair[0] ** 2 % 5 == 1]
    remaining_pairs = [pair for pair in split_pairs if pair not in excluded_pairs]
    assert excluded_pairs == [[1, 0], [4, 0]]
    assert remaining_pairs == [[0, 2], [2, 0], [3, 0], [3, 2]]
    root_reductions = {
        'b=0, q=-1': str(variable * (variable + 1) ** 2),
        'b=0, q=1': str(variable * (variable ** 2 + 1)),
    }
    repository = Path(__file__).resolve().parents[1]
    return {
        'anchor_v': str(anchor),
        'curve_anchor_quotient_by_b_cubed': str(curve_quotient),
        'discriminant_anchor_identity': 'Delta(v,b)=13*b^2+b^3*R(b)',
        'R_ascending_coefficients': discriminant_coefficients,
        'curve_difference_factor': str(difference_factor),
        'difference_factor_unit_mod_p_on_negative_branch': 2,
        'generic_discriminant_difference_divisible_by_q_minus_v': True,
        'generic_quotient_and_sylvester_reverified': True,
        'root_reductions_mod_prime_dividing_b': root_reductions,
        'valuation_theorem': 'For odd p|b and q=-1 mod p, e=v_p(b) gives q=v mod p^(3e), Delta=13*b^2 mod p^(3e). If 13 is nonsquare mod p, v_p(Delta)=2e and Delta is not a rational square.',
        'integer_spectrum_excluded': 'G=0, p odd dividing b, a^2=1 mod p, and 13 nonsquare mod p. In particular p=7 or11 dividing b suffices, because a^4=1 and -1 is nonsquare.',
        'remaining_equality_pairs_mod5': remaining_pairs,
        'newly_excluded_equality_pairs_mod5': excluded_pairs,
        'prime_examples': prime_examples,
        'prior_mod_five_certificate_sha256': hashlib.sha256(
            (repository / 'results/endpoint-one-equality-mod-five.json').read_bytes()).hexdigest(),
        'prior_cubic_certificate_sha256': hashlib.sha256(
            (repository / 'results/endpoint-one-equality-cubic.json').read_bytes()).hexdigest(),
        'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                          for source in (Path(__file__),
                                         Path(__file__).with_name('check_endpoint_one_equality_cubic.py'),
                                         Path(__file__).with_name('check_six_support_quotient.py'))},
        'sympy': sympy.__version__,
        'scope': 'Written uniform prime-adic discriminant obstruction on the equality curve. Generic integer polynomial identities checked exactly, including direct six-support quotient and independent Sylvester discriminant. Three specified prime examples only; no exponent scan, prime search, enumerated integer equality points, finite exponent base, new two-adic lift or Lean. Root equation plus square discriminant system has no solution in the excluded classes. Full endpoint-one classification and Q3 remain open.',
    }


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
