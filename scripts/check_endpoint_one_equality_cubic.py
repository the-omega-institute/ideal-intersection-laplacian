import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


def certificate():
    first, middle, product, variable = sympy.symbols('a b q x')
    total = middle * (middle + 2)
    last = total - first
    product_value = first * last
    curve = ((3 * middle - 1) * product ** 2
             + middle * (middle ** 2 + 4 * middle - 1) * product
             - (middle ** 2 + 2 * middle - 1) * (middle ** 2 + 3 * middle - 1)
             * (middle ** 3 + 3 * middle ** 2 + 3 * middle - 1))
    root_sum = product + middle ** 3 + 5 * middle ** 2 + 8 * middle - 1
    root_pairs = (product * middle * (middle ** 2 + 5 * middle + 5)
                  + 2 * middle ** 5 + 12 * middle ** 4 + 25 * middle ** 3
                  + 16 * middle ** 2 - 8 * middle + 1)
    root_product = product * middle * (middle + 3) * (product + middle * (middle ** 2 + 3 * middle + 3))
    cubic = variable ** 3 - root_sum * variable ** 2 + root_pairs * variable - root_product
    matrix = support_quotient((first, middle, last), complement=True)
    quintic = sympy.cancel(matrix.charpoly(variable).as_expr() / variable)
    expected = (variable - 1) * (variable - middle) * cubic + variable * (variable - middle) * curve
    assert sympy.expand(quintic - expected.subs(product, product_value)) == 0
    assert sympy.expand(quintic.subs(variable, 1) - (1 - middle) * curve.subs(product, product_value)) == 0
    discriminant = sympy.expand(root_sum ** 2 * root_pairs ** 2 - 4 * root_pairs ** 3
                               - 4 * root_sum ** 3 * root_product - 27 * root_product ** 2
                               + 18 * root_sum * root_pairs * root_product)
    assert sympy.expand(discriminant - sympy.discriminant(cubic, variable)) == 0
    derivative = sympy.diff(cubic, variable)
    cubic_coefficients = sympy.Poly(cubic, variable).all_coeffs()
    derivative_coefficients = sympy.Poly(derivative, variable).all_coeffs()
    sylvester = sympy.zeros(5)
    for offset in range(2):
        for column, value in enumerate(cubic_coefficients):
            sylvester[offset, column + offset] = value
    for offset in range(3):
        for column, value in enumerate(derivative_coefficients):
            sylvester[offset + 2, column + offset] = value
    assert sympy.expand(sylvester.det(method='bareiss') + discriminant) == 0
    candidate = sympy.Symbol('d')
    quadratic = variable ** 2 + (candidate - root_sum) * variable + root_product / candidate
    remainder = cubic.subs(variable, candidate)
    assert sympy.cancel(cubic - (variable - candidate) * quadratic - variable * remainder / candidate) == 0
    abstract = variable ** 3 - 3 * variable + 1
    assert sympy.discriminant(abstract, variable) == 81
    assert all(abstract.subs(variable, value) != 0 for value in (-1, 1))
    prior = Path(__file__).resolve().parents[1] / 'results/endpoint-one-equality-second-root.json'
    return {'parameters': 'c=b(b+2)-a, q=ac, G=(3b-1)q^2+b(b^2+4b-1)q-(b^2+2b-1)(b^2+3b-1)(b^3+3b^2+3b-1)',
            'cubic_P3': str(cubic), 'root_sum_A': str(root_sum),
            'root_pair_sum_B': str(root_pairs), 'root_product_N': str(root_product),
            'curve_G': str(curve), 'generic_quintic_identity': 'h_C(x)=(x-1)(x-b)P3(x)+x(x-b)G',
            'discriminant_formula': 'A^2 B^2-4B^3-4A^3 N-27N^2+18ABN',
            'discriminant_expanded_q_b': str(discriminant),
            'discriminant_degree_q': sympy.degree(discriminant, product).__int__(),
            'discriminant_degree_b': sympy.degree(discriminant, middle).__int__(),
            'discriminant_term_count_q_b': len(sympy.Poly(discriminant, product, middle).terms()),
            'generic_determinant_identity_checked': True, 'generic_discriminant_and_sylvester_checked': True,
            'generic_divisor_and_quadratic_identity_checked': True,
            'square_discriminant_counterexample': 'x^3-3x+1 has discriminant81 and no rational root; it is an abstract cubic, not an endpoint triple.',
            'prior_pair_sum_certificate_sha256': hashlib.sha256(prior.read_bytes()).hexdigest(),
            'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                              for source in (Path(__file__), Path(__file__).with_name('check_six_support_quotient.py'))},
            'sympy': sympy.__version__,
            'scope': 'Exact generic identities for explicit equality endpoint cubic and discriminant, independently checked by direct quotient characteristic polynomial and 5x5 Sylvester determinant. No parameter scan, integer endpoint solution, finite base, point enumeration, rank calculation, new nonintegrality exclusion or Lean. Square discriminant is necessary, not sufficient for cubic integral splitting.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
