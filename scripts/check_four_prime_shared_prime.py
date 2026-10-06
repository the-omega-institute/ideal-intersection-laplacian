import hashlib
import json
from math import gcd
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding
from check_four_prime_single_pair_midpoint import integer_determinant


def valuation(value, prime):
    assert value != 0
    power = 0
    value = abs(int(value))
    while value % prime == 0:
        power += 1
        value //= prime
    return power


def symbolic_checks():
    root, middle, maximum, difference, variable, progression = sympy.symbols('s b c h x n')
    matrix = operator(root - 1 + difference, middle, maximum)
    expression = sympy.expand(sympy.Matrix(matrix).charpoly(variable).as_expr().subs(variable, root))
    direct = integer_determinant([[(root if row == column else 0) - matrix[row][column]
                                  for column in range(4)] for row in range(4)])
    assert sympy.expand(expression - direct) == 0
    cubic = -difference * (root - 1) * ((root - 1) * middle - root * maximum - difference) * (
        root * middle - (root - 1) * maximum + difference)
    anchor = -(root - 1) ** 2 * (2 * root - 1) * middle ** 2 * maximum ** 2
    remainder = sympy.Poly(sympy.expand(expression - cubic - anchor), difference, middle, maximum)
    assert remainder.domain == sympy.ZZ.poly_ring(root)
    assert all(powers[0] >= 1 and sum(powers) >= 4 and powers[1] <= 2 and powers[2] <= 2
               for powers, coefficient in remainder.terms())
    assert sympy.expand(expression.subs(difference, 0) - anchor) == 0
    assert sympy.expand(expression.subs({middle: 0, maximum: 0})
                        - difference ** 3 * (root - 1 + 2 * difference)) == 0
    assert sympy.Poly(expression, difference, middle, maximum).total_degree() == 6
    written_progression = 156 + 2450 * progression
    assert sympy.expand(written_progression - 1 - 5 * (31 + 490 * progression)) == 0
    assert sympy.expand(written_progression - 2 - 7 * (22 + 350 * progression)) == 0
    assert 31 % 5 and 490 % 5 == 0 and 22 % 7 and 350 % 7 == 0
    return {'independent_symbolic_permutation_determinant': 'passed',
            'cubic': str(cubic), 'constant_in_h_anchor': str(anchor),
            'complete_remainder_terms_h_power_b_power_c_power_coefficient':
            [list(powers) + [str(coefficient)] for powers, coefficient in remainder.terms()],
            'remainder_monomial_conditions': 'h power>=1,total degree>=4,b power<=2,c power<=2',
            'remainder_terms': len(remainder.terms()),
            'zero_tail_specialization': 'p(s)|b=c=0=h^3(s-1+2h)',
            'first_valuation_corollary': 'v_ell(h)=1 forces v_ell(gcd(b,c))=1 at every good prime',
            'progression': 'a=156+2450n,n>=0;v_5(a-1)=v_7(a-2)=1'}


def valuation_control(exponent, middle, maximum, endpoint, prime, power, determinant):
    difference = exponent + 1 - endpoint
    middle_power = valuation(middle, prime)
    maximum_power = valuation(maximum, prime)
    smaller, larger = sorted((middle_power, maximum_power))
    actual = valuation(determinant, prime)
    allowed = ((smaller < larger and power in (smaller, 2 * larger))
               or (smaller == larger and smaller >= 1 and smaller <= power <= 2 * smaller))
    record = {'prime': prime, 'h_valuation': power, 'tail_valuations': [middle_power, maximum_power],
              'necessary_valuation_branch_passes': allowed, 'determinant_valuation': actual}
    if not allowed:
        if smaller == larger == 0:
            predicted = 0
            reason = 'neither tail divisible;anchor unit'
        elif power < smaller:
            predicted = 3 * power
            reason = 'h cubic has uniquely lowest valuation'
        elif smaller < larger and power > smaller:
            predicted = min(power + 2 * smaller, 2 * smaller + 2 * larger)
            reason = 'unequal tail valuations;unmatched cubic/anchor valuations'
        else:
            assert smaller == larger and power > 2 * smaller
            predicted = 4 * smaller
            reason = 'equal tail valuations;anchor has uniquely lowest valuation'
        assert actual == predicted
        record.update({'predicted_nonzero_determinant_valuation': predicted, 'exclusion_reason': reason})
    if power == smaller and power >= 1:
        scaled_h = difference // prime ** power
        scaled_b = middle // prime ** power
        scaled_c = maximum // prime ** power
        predicted_residue = (-scaled_h * (endpoint - 1)
                             * ((endpoint - 1) * scaled_b - endpoint * scaled_c - scaled_h)
                             * (endpoint * scaled_b - (endpoint - 1) * scaled_c + scaled_h)) % prime
        assert determinant % (prime ** (3 * power)) == 0
        assert determinant // prime ** (3 * power) % prime == predicted_residue
        record['cubic_resonance_residue'] = predicted_residue
        record['necessary_cubic_resonance_passes'] = predicted_residue == 0
    return record


def fixed_control(exponent, middle, maximum):
    assert exponent >= 5 and middle >= exponent and maximum >= exponent
    matrix = operator(exponent, middle, maximum)
    variable = sympy.Symbol('x')
    polynomial = sympy.Poly(sympy.Matrix(matrix).charpoly(variable).as_expr(), variable)
    determinants = [integer_determinant([[argument * (row == column) - matrix[row][column]
                                         for column in range(4)] for row in range(4)])
                    for argument in range(5)]
    assert sympy.Poly(sympy.interpolate(list(enumerate(determinants)), variable), variable) == polynomial
    assert int(polynomial.count_roots(1, 4)) == 1
    controls = []
    for endpoint in (2, 3):
        good = [valuation_control(exponent, middle, maximum, endpoint, int(prime), int(power), determinants[endpoint])
                for prime, power in sympy.factorint(exponent + 1 - endpoint).items()
                if endpoint * (endpoint - 1) * (2 * endpoint - 1) % prime != 0]
        controls.append({'endpoint': endpoint, 'good_prime_controls': good,
                         'excluded_by_valuation_ranges': any(not item['necessary_valuation_branch_passes'] for item in good)})
    common = gcd(middle, maximum)
    in_progression = exponent >= 156 and (exponent - 156) % 2450 == 0
    progression_criterion = in_progression and valuation(common, 5) != 1 and valuation(common, 7) != 1
    embedding = support_embedding(exponent, middle, maximum)
    embedding.update({'tail_gcd': common, 'quartic_coefficients_descending': [int(value) for value in polynomial.all_coeffs()],
                      'five_direct_integer_determinants_at_zero_through_four': determinants,
                      'exact_low_window_sturm_count': 1, 'endpoint_controls': controls,
                      'both_endpoints_excluded_by_valuation_ranges': all(item['excluded_by_valuation_ranges'] for item in controls),
                      'in_new_progression_region': progression_criterion})
    return embedding


def comparison_example(control):
    assert control['exponents'] == (156, 156, 73005, 48048)
    assert control['tail_gcd'] == 3
    assert 73005 == 3 * 155 * 157 and 48048 == 3 * 154 * 104
    assert (3 * 73005 ** 2 * 48048 ** 2) % 155 == 0
    assert (20 * 73005 ** 2 * 48048 ** 2) % 154 == 0
    assert sympy.isprime(157)
    variable = sympy.Symbol('x')
    for tail, roots in ((73005, (0, 1)), (48048, (3, -2))):
        assert sympy.Poly(variable ** 2 - variable - tail, variable, modulus=157) == sympy.Poly(
            (variable - roots[0]) * (variable - roots[1]), variable, modulus=157)
    assert control['five_direct_integer_determinants_at_zero_through_four'][2:4] == [
        -618942518275209847040, -606895825753733049902060]
    return {'exponents': control['exponents'], 'tail_gcd': 3,
            'both_old_coarse_endpoint_divisibilities_pass': True,
            'modular_factor_roots_at_only_prime_157': [[0, 1], [3, -2]],
            'previous_coprime_tail_lemma_hypothesis_passes': False,
            'new_obstruction': 'v_5(h_2)=v_7(h_3)=1 but min tail valuations at5,7are0'}


def main():
    symbolic = symbolic_checks()
    fixtures = ((156, 73005, 48048), (156, 192325, 193550), (2606, 7821, 7824),
                (156, 71610, 298375), (26, 27, 30), (126, 130, 135))
    controls = [fixed_control(*fixture) for fixture in fixtures]
    assert [control['in_new_progression_region'] for control in controls] == [True, True, True, False, False, False]
    assert [control['both_endpoints_excluded_by_valuation_ranges'] for control in controls] == [True, True, True, False, False, True]
    assert all(control['tail_gcd'] > 1 for control in controls)
    dependencies = ('check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py')
    report = {'written_theorem': 'For positive a,b,c and an integer restricted root s>=2,put h=a+1-s. For good ell|h not dividing s(s-1)(2s-1),e=v_ell(h),r=min(v_ell(b),v_ell(c)),t=max(...). If r<t then e=r or e=2t. If r=t then r>=1 and r<=e<=2r. No tail coprimality hypothesis.',
              'written_first_valuation_corollary': 'e=1 implies v_ell(gcd(b,c))=1;both tails divisible by ell and at least one not divisible by ell^2.',
              'written_nonintegrality_region': 'a=156+2450n,n>=0,b,c>=a and both v_5(gcd(b,c)),v_7(gcd(b,c)) differ from1 imply nonintegrality;tails need not be coprime.',
              'symbolic': symbolic, 'fixed_controls': controls, 'extra_coverage_example': comparison_example(controls[0]),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in dependencies},
              'sympy_version': sympy.__version__, 'requires_finite_base': False,
              'validation_counts': {'support_column_actions': 336, 'direct_integer_determinants': 30,
                                    'exact_low_window_sturm_counts': 6},
              'scope': 'Written unbounded valuation ranges,cubic resonance and progression. Six noncoprime-tail controls check symbolic/support/determinant/Sturm implementation,including permitted valuation branches and failed sufficient hypotheses. No parameter scan,expanded graph,historical finite-base rerun,floating eigenvalues or Lean. Passing local conditions does not prove an integer root or graph integrality;bad primes and general classification remain open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
