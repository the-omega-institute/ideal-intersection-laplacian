import hashlib
import json
from math import gcd
from pathlib import Path

import sympy

from check_four_prime_a6_elliptic import ALPHA, WEIERSTRASS_LINEAR, WEIERSTRASS_CONSTANT


def reduction_certificate(linear, constant, prime):
    assert sympy.isprime(prime)
    discriminant = -16 * (4 * linear ** 3 + 27 * constant ** 2)
    assert discriminant % prime != 0
    residues = [(horizontal ** 3 + linear * horizontal + constant) % prime
                for horizontal in range(prime)]
    counts = [sum(vertical * vertical % prime == residue for vertical in range(prime))
              for residue in residues]
    characters = [0 if residue == 0 else 1 if pow(int(residue), (prime - 1) // 2, prime) == 1 else -1
                  for residue in residues]
    assert counts == [1 + character for character in characters]
    order = 1 + sum(counts)
    assert order == prime + 1 + sum(characters)
    return {'prime': prime, 'reduced_A_B': [int(linear % prime), int(constant % prime)],
            'discriminant_mod_prime': int(discriminant % prime),
            'cubic_residues_by_x': [int(value) for value in residues],
            'vertical_solution_counts_by_x': counts,
            'Legendre_symbols_by_x': characters, 'group_order_including_infinity': order}


def checks():
    linear, constant = int(WEIERSTRASS_LINEAR), int(WEIERSTRASS_CONSTANT)
    twist_linear = int(ALPHA ** 2 * WEIERSTRASS_LINEAR)
    twist_constant = int(ALPHA ** 3 * WEIERSTRASS_CONSTANT)
    rational = [reduction_certificate(linear, constant, prime) for prime in (11, 17)]
    twist = [reduction_certificate(twist_linear, twist_constant, prime) for prime in (11, 17)]
    assert [row['group_order_including_infinity'] for row in rational] == [10, 16]
    assert [row['group_order_including_infinity'] for row in twist] == [14, 20]
    assert gcd(10, 16) == gcd(14, 20) == 2
    prime = 23
    residues = [(horizontal ** 3 + linear * horizontal + constant) % prime for horizontal in range(prime)]
    assert sympy.isprime(prime) and all(residues)
    assert (linear % prime, constant % prime) == (22, 15)
    variable = sympy.Symbol('x')
    polynomial = variable ** 3 + linear * variable + constant
    assert sympy.Poly(polynomial, variable, modulus=prime).is_irreducible
    assert (ALPHA ** 3 * polynomial.subs(variable, variable / ALPHA)
            - (variable ** 3 + twist_linear * variable + twist_constant)).expand() == 0
    return {
        'rational_curve_reductions': rational, 'quadratic_twist_reductions': twist,
        'rational_and_twist_torsion_order_divisibility_bound': 2,
        'irreducibility_prime': prime, 'original_cubic_residues_mod_23': residues,
        'original_cubic_has_no_root_mod_23': True,
        'original_cubic_irreducible_over_Q': True,
        'twist_cubic_scaling_identity': 'g_twist(x)=d^3*g(x/d)',
        'rational_two_torsion': False, 'twist_rational_two_torsion': False,
        'proved_torsion_groups': {'E_Q': 'trivial', 'quadratic_twist_Q': 'trivial', 'E_K': 'trivial'},
        'field_torsion_proof': 'A K-torsion point has zero rational trace, so is anti-invariant and maps to rational twist torsion, hence is O',
        'Tzanakis_torsion_offset_s_over_t': '0/1',
        'Tzanakis_case_two_linear_form': 'rho0+m0+sum_i(mi*rho_i)',
    }


def main():
    dependencies = ('check_four_prime_a6_elliptic.py',)
    report = {
        'written_result': 'The rational, quadratic-twist rational and quadratic-field torsion groups are all trivial; the inhomogeneous quartic method has no torsion offset.',
        'exact_checks': checks(),
        'proof_inputs': ['Prime-to-p torsion injects under good reduction',
                         'Rational 2-torsion corresponds to rational roots of the short cubic',
                         'Galois trace and quadratic-twist isomorphism'],
        'exact_rank_or_full_basis_computed': False,
        'regulator_or_remaining_height_constants_computed': False,
        'initial_coefficient_bound_or_LLL_run': False,
        'complete_integral_points_enumerated': False, 'new_nonintegrality_classification': False,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in dependencies},
        'sympy_version': sympy.__version__,
        'scope': 'Written torsion proof and four finite-field point counts at the two specified good primes11/17, plus a root/irreducibility certificate at23. These targeted counts resolve the torsion input, with no parameter scan, graph/historical finite-base rerun, exact rank/full basis, remaining height/log bounds, LLL, full point list, floats or Lean.',
    }
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
