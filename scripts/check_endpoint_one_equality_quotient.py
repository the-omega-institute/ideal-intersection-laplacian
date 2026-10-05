import hashlib
import json
from itertools import product
from math import comb
from pathlib import Path

import sympy


def transformed_form(coefficients, entries, prime):
    upper_left, upper_right, lower_left, lower_right = entries
    transformed = [0] * len(coefficients)
    total_degree = len(coefficients) - 1
    for degree, coefficient in enumerate(coefficients):
        for first_degree in range(degree + 1):
            first = (comb(degree, first_degree) * upper_left ** first_degree
                     * upper_right ** (degree - first_degree))
            for second_degree in range(total_degree - degree + 1):
                second = (comb(total_degree - degree, second_degree) * lower_left ** second_degree
                          * lower_right ** (total_degree - degree - second_degree))
                target = first_degree + second_degree
                transformed[target] = (transformed[target] + coefficient * first * second) % prime
    return transformed


def certificate():
    variable = sympy.Symbol('b')
    coefficients = [4, -44, 161, -172, -154, 172, 233, 92, 12]
    discriminant = sum(coefficient * variable ** degree for degree, coefficient in enumerate(coefficients))
    prime = 5
    reduced = sympy.Poly(discriminant, variable, modulus=prime)
    assert reduced.degree() == 8
    assert sympy.gcd(reduced, reduced.diff()) == sympy.Poly(1, variable, modulus=prime)
    reference = [coefficient % prime for coefficient in coefficients]
    matches = []
    count = 0
    for entries in product(range(prime), repeat=4):
        if not any(entries) or next(entry for entry in entries if entry) != 1:
            continue
        upper_left, upper_right, lower_left, lower_right = entries
        if (upper_left * lower_right - upper_right * lower_left) % prime == 0:
            continue
        count += 1
        transformed = transformed_form(reference, entries, prime)
        scale = transformed[0] * pow(reference[0], -1, prime) % prime
        if scale and all(actual == scale * expected % prime for actual, expected in zip(transformed, reference)):
            matches.append(entries)
    assert count == prime * (prime ** 2 - 1) == 120
    assert matches == [(1, 0, 0, 1)]
    first, middle, last = sympy.symbols('a b c')
    equality_last = middle * (middle + 2) - first
    swapped_middle_condition = (middle + last - first * (first + 2)).subs(last, equality_last)
    assert sympy.expand(swapped_middle_condition - (middle - first) * (middle + first + 3)) == 0
    curve_certificate = Path(__file__).resolve().parents[1] / 'results/endpoint-one-equality-curve.json'
    prior = json.loads(curve_certificate.read_text())
    assert sympy.expand(discriminant - sympy.sympify(prior['quotient_discriminant_D'])) == 0
    return {'quotient': 'H: y^2=D(b), geometric genus3', 'prime': prime,
            'D_coefficients_ascending': coefficients, 'D_mod5_coefficients_ascending': reference,
            'squarefree_mod5': True, 'good_reduction_at5': True,
            'PGL2_F5_elements_exhausted': count, 'branch_stabilizer_F5': matches,
            'written_no_extra_Q_involution_on_H': True,
            'written_no_degree_two_Q_quotient_of_H_of_genus_one_or_two': True,
            'all_low_genus_maps_from_genus10_curve_excluded': False,
            'jacobian_rank_computed': False, 'integer_points_computed': False,
            'sympy': sympy.__version__,
            'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
            'input_curve_certificate_sha256': hashlib.sha256(curve_certificate.read_bytes()).hexdigest(),
            'scope': 'One complete120element PGL2(F5) branch-stabilizer computation at verified good reduction, supporting written tame-specialization exclusion of extra rational involutions on known genus3quotient. This is not an exponent/modulus scan, a rank computation, or exclusion of all low-genus maps of original genus10curve. Classical Chabauty requires rank<genus; quotient rank<=2 would suffice on H, no rank bound established. Prior proof/finite dependencies/oldn7/four native axioms retained; no Lean/sharedCI/merge/publication/email.'}


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
