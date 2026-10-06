import hashlib
import json
from math import gcd
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def valuation(value, prime):
    assert value != 0
    multiplicity = 0
    value = abs(value)
    while value % prime == 0:
        multiplicity += 1
        value //= prime
    return multiplicity


def symbolic_checks():
    exponent, middle, maximum, root, variable, progression = sympy.symbols('a b c s x r')
    polynomial = sympy.Matrix(operator(exponent, middle, maximum)).charpoly(variable).as_expr()
    multiplier = (root - 1) ** 2 * (2 * root - 1)
    numerator = sympy.expand(polynomial.subs(variable, root) + multiplier * middle ** 2 * maximum ** 2)
    quotient, remainder = sympy.div(numerator, exponent + 1 - root, exponent)
    assert remainder == 0
    quotient = sympy.Poly(quotient, exponent, middle, maximum, root, domain=sympy.ZZ).as_expr()
    assert sympy.expand(polynomial.subs(variable, root)
                        + multiplier * middle ** 2 * maximum ** 2
                        - (exponent + 1 - root) * quotient) == 0
    for missing, other in ((middle, maximum), (maximum, middle)):
        specialization = quotient.subs({exponent: root - 1, missing: 0})
        assert sympy.expand(specialization + root * (root - 1) ** 2 * other ** 2) == 0
    assert sympy.expand(polynomial.subs(variable, exponent + 1)
                        + exponent ** 2 * middle ** 2 * maximum ** 2 * (2 * exponent + 1)) == 0
    for endpoint, good_lower_bound in ((2, 5), (3, 7)):
        bad_primes = sorted(sympy.factorint(endpoint * (endpoint - 1) * (2 * endpoint - 1)))
        assert bad_primes == ([2, 3] if endpoint == 2 else [2, 3, 5])
        assert int(sympy.nextprime(bad_primes[-1])) == good_lower_bound
    arithmetic_progression = 156 + 2450 * progression
    assert sympy.expand(arithmetic_progression - 1 - 5 * (31 + 490 * progression)) == 0
    assert sympy.expand(arithmetic_progression - 2 - 7 * (22 + 350 * progression)) == 0
    assert 31 % 5 != 0 and 490 % 5 == 0 and 22 % 7 != 0 and 350 % 7 == 0
    assert sympy.expand((exponent + 1 - root).subs(root, exponent + 1 + progression) + progression) == 0
    return {'integer_polynomial_quotient': str(quotient),
            'generic_identity': 'p(s)=-(s-1)^2(2s-1)b^2c^2+(a+1-s)Q_s(a,b,c)',
            'unit_specializations': ['Q_s(s-1,0,c)=-s(s-1)^2c^2',
                                     'Q_s(s-1,b,0)=-s(s-1)^2b^2'],
            'nonzero_anchor': 'p(a+1)=-a^2b^2c^2(2a+1)',
            'bad_primes_at_two': [2, 3], 'bad_primes_at_three': [2, 3, 5],
            'unbounded_progression': 'a=156+2450r,r>=0;v_5(a-1)=v_7(a-2)=1',
            'second_root_offset_identity': 's=a+1+t implies h=-t'}


def fixed_control(exponent, middle, maximum):
    assert exponent >= 5 and middle >= exponent and maximum >= exponent
    assert gcd(middle, maximum) == 1
    embedding = support_embedding(exponent, middle, maximum)
    matrix = operator(exponent, middle, maximum)
    variable = sympy.Symbol('x')
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    determinants = [integer_determinant([[argument * (row == column) - matrix[row][column]
                                         for column in range(4)] for row in range(4)])
                    for argument in range(5)]
    assert sympy.Poly(sympy.interpolate(list(enumerate(determinants)), variable), variable) == polynomial
    assert int(polynomial.count_roots(1, 4)) == 1
    rows = []
    for endpoint in (2, 3):
        difference = exponent + 1 - endpoint
        bad_product = endpoint * (endpoint - 1) * (2 * endpoint - 1)
        witnesses = []
        for prime, multiplicity in sympy.factorint(difference).items():
            prime, multiplicity = int(prime), int(multiplicity)
            if bad_product % prime != 0 and multiplicity % 2 == 1:
                tail_multiplicity = valuation(middle * maximum, prime)
                expected = min(multiplicity, 2 * tail_multiplicity)
                actual = valuation(determinants[endpoint], prime)
                assert actual == expected
                witnesses.append({'prime': prime, 'v_prime_h': multiplicity,
                                  'v_prime_bc': tail_multiplicity,
                                  'v_prime_p_endpoint': actual,
                                  'unequal_summand_valuations': [multiplicity, 2 * tail_multiplicity]})
        rows.append({'endpoint': endpoint, 'odd_good_prime_witnesses': witnesses,
                     'old_coarse_divisibility_passes':
                     ((endpoint - 1) ** 2 * (2 * endpoint - 1) * middle ** 2 * maximum ** 2) % difference == 0})
    in_region = all(row['odd_good_prime_witnesses'] for row in rows)
    assert in_region == (exponent != 26)
    embedding.update({'tail_gcd': 1, 'quartic_coefficients_descending': [int(value) for value in polynomial.all_coeffs()],
                      'five_direct_integer_determinants_at_zero_through_four': determinants,
                      'exact_low_window_sturm_count': 1, 'endpoint_controls': rows,
                      'in_new_sufficient_region': in_region})
    return embedding


def comparison_example(control):
    assert control['exponents'] == (156, 156, 24335, 16016)
    assert all(row['old_coarse_divisibility_passes'] for row in control['endpoint_controls'])
    assert 24335 == 155 * 157 and 16016 == 154 * 104
    assert sympy.isprime(157) and 24335 % 157 == 0 and 16016 % 157 == 2
    variable = sympy.Symbol('x')
    for tail, roots in ((24335, (0, 1)), (16016, (2, -1))):
        assert sympy.Poly(variable ** 2 - variable - tail, variable, modulus=157) == sympy.Poly(
            (variable - roots[0]) * (variable - roots[1]), variable, modulus=157)
    assert control['five_direct_integer_determinants_at_zero_through_four'][2:4] == [
        72785938852601822540, -7452438203099991664332]
    return {'exponents': control['exponents'], 'tail_gcd': 1,
            'both_old_endpoint_divisibilities_pass': True,
            'all_prime_divisors_of_a_plus_one': [157],
            'modular_factor_roots': [[0, 1], [2, -1]],
            'new_obstruction': 'v_5(a-1)=1 and v_7(a-2)=1 exclude both low integer roots'}


def main():
    fixtures = ((156, 24335, 16016), (156, 157, 158), (2606, 2607, 2608),
                (5056, 5057, 5058), (156, 1550, 16017), (26, 27, 28))
    controls = [fixed_control(*fixture) for fixture in fixtures]
    dependencies = ('check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py')
    report = {'written_theorem': 'If a,b,c are positive,gcd(b,c)=1,and integer s>=2 is a root of the genuine restriction,then h=a+1-s is nonzero and v_ell(h)=2v_ell(bc) for every prime ell|h with ell not dividing s(s-1)(2s-1).',
              'written_nonintegrality_corollary': 'For a>=5,b,c>=a,gcd(b,c)=1,a prime ell>=5 of odd multiplicity in a-1 and a prime q>=7 of odd multiplicity in a-2 exclude roots2,3 and graph integrality. In particular a=156+2450r,r>=0 works for every coprime pair of tails.',
              'symbolic': symbolic_checks(), 'fixed_controls': controls,
              'extra_coverage_example': comparison_example(controls[0]),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                    for name in dependencies},
              'sympy_version': sympy.__version__, 'requires_finite_base': False,
              'validation_counts': {'support_column_actions': 336, 'direct_integer_determinants': 30,
                                    'exact_low_window_sturm_counts': 6},
              'scope': 'Written unbounded root-valuation lemma and nonintegrality progression; six fixed algebra/support/Sturm controls,including one limitation outside the sufficient region. No parameter scan,expanded graph,historical finite-base rerun,floating eigenvalues or Lean. General shared-prime tails,single-pair,fully unequal four-prime and higher-prime classification remain open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
