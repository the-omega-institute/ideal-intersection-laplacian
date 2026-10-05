import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def certificate():
    first, middle, last, product, variable = sympy.symbols('a b c q x')
    matrix = support_quotient((first, middle, last), complement=True)
    quintic = sympy.Poly(sympy.cancel(matrix.charpoly(variable).as_expr() / variable), variable)
    total = middle * (middle + 2)
    equality = sympy.cancel(-quintic.eval(1).subs(last, total - first) / (middle - 1))
    leading = 3 * middle - 1
    linear = middle * (middle ** 2 + 4 * middle - 1)
    constant = -(middle ** 2 + 2 * middle - 1) * (middle ** 2 + 3 * middle - 1) * (middle ** 3 + 3 * middle ** 2 + 3 * middle - 1)
    reduced = leading * product ** 2 + linear * product + constant
    assert sympy.expand(equality - reduced.subs(product, first * (total - first))) == 0
    assert sympy.expand(equality - equality.subs(first, total - first)) == 0
    assert sympy.Poly(equality, first, middle).total_degree() == 7
    assert sympy.degree(equality, first) == 4 and sympy.degree(equality, middle) == 7
    discriminant = sympy.discriminant(reduced, product)
    assert sympy.degree(discriminant, middle) == 8
    assert sympy.gcd(discriminant, sympy.diff(discriminant, middle)) == 1
    numerator = ((middle ** 3 + 5 * middle ** 2 + 6 * middle - 2)
                 * (3 * middle ** 6 + 8 * middle ** 5 - 6 * middle ** 4 - 36 * middle ** 3 - 28 * middle ** 2 + 40 * middle - 8))
    assert sympy.expand(16 * reduced.subs(product, total ** 2 / 4) - numerator) == 0
    assert sympy.degree(numerator, middle) == 9
    assert sympy.gcd(numerator, sympy.diff(numerator, middle)) == 1
    assert sympy.gcd(numerator, discriminant) == 1
    pole = sympy.Rational(1, 3)
    assert numerator.subs(middle, pole) == sympy.Rational(368, 729)
    assert discriminant.subs(middle, pole) == sympy.Rational(16, 729)
    assert sympy.degree(linear, middle) == 3 and sympy.degree(constant, middle) == 7
    assert sympy.expand((middle - 1) * quintic.eval(middle)
                        - (first * middle * last) ** 2 * (last + first - middle * (middle + 2)) * (middle - 1)) == 0
    return {'plane_total_degree': 7, 'degree_in_a': 4, 'degree_in_b': 7,
            'quotient_R': str(reduced), 'quotient_discriminant_D': str(discriminant),
            'norm_numerator_N': str(numerator), 'norm_denominator': str(leading),
            'gcd_D_Dprime': 1, 'gcd_N_Nprime': 1, 'gcd_N_D': 1,
            'N_at_one_third': '368/729', 'D_at_one_third': '16/729',
            'written_quotient_genus': 3, 'written_double_cover_branch_count': 10,
            'written_geometric_genus': 10, 'geometrically_irreducible': True,
            'integer_point_list_computed': False, 'literature_identification_established': False,
            'sympy': sympy.__version__,
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                              for source in (Path(__file__), Path(__file__).with_name('check_six_support_quotient.py'))},
            'scope': 'Exact curve identities and written normalization/ramification/Riemann-Hurwitz genus10 proof; Siegel gives integer-point finiteness, not a list or admissible-triple emptiness. Existing regime-specific windows and division-free necessary middle-anchor condition only; no new spectral family/globalQ3closure, integer/modulus scan, higher2adicshift or Lean. Prior manuscript/proofs/finite dependencies and oldn7/four native axioms retained.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
