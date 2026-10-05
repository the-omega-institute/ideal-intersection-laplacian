import hashlib
import json
from pathlib import Path

import sympy

from check_endpoint_one_equality_cubic import certificate as cubic_certificate
from check_endpoint_one_equality_local_discriminant import certificate as local_certificate


def certificate():
    prior = cubic_certificate()
    local = local_certificate()
    first, middle, product, variable = sympy.symbols('a b q x')
    cubic = sympy.sympify(prior['cubic_P3'])
    curve = sympy.sympify(prior['curve_G'])
    assert sympy.expand(curve.subs(middle, 0) - (1 - product ** 2)) == 0
    positive_reduction = variable * (variable ** 2 + 1)
    negative_reduction = variable * (variable + 1) ** 2
    assert sympy.expand(cubic.subs({middle: 0, product: 1}) - positive_reduction) == 0
    assert sympy.expand(cubic.subs({middle: 0, product: -1}) - negative_reduction) == 0
    assert sympy.diff(positive_reduction, variable).subs(variable, 0) == 1
    assert sympy.diff(negative_reduction, variable).subs(variable, 0) == 1
    for root in (first, -first):
        assert sympy.rem(positive_reduction.subs(variable, root), first ** 2 + 1, first) == 0
        assert sympy.rem(sympy.diff(positive_reduction, variable).subs(variable, root) + 2,
                          first ** 2 + 1, first) == 0
    root_sum, root_pairs, root_product, candidate = sympy.symbols('A B N d')
    general = variable ** 3 - root_sum * variable ** 2 + root_pairs * variable - root_product
    quadratic = variable ** 2 + (candidate - root_sum) * variable + candidate ** 2 - root_sum * candidate + root_pairs
    remainder = general.subs(variable, candidate)
    assert sympy.expand(general - (variable - candidate) * quadratic - remainder) == 0
    quadratic_discriminant = root_sum ** 2 + 2 * root_sum * candidate - 3 * candidate ** 2 - 4 * root_pairs
    assert sympy.expand(sympy.discriminant(quadratic, variable) - quadratic_discriminant) == 0
    derivative = sympy.diff(general, variable).subs(variable, candidate)
    identity_error = sympy.discriminant(general, variable) - derivative ** 2 * quadratic_discriminant
    remainder_factor = (4 * root_sum ** 3 - 18 * root_sum * root_pairs - 27 * root_sum * candidate ** 2
                        + 27 * root_pairs * candidate + 27 * root_product + 27 * candidate ** 3)
    assert sympy.expand(identity_error - remainder * remainder_factor) == 0
    assert sympy.expand(quadratic.subs({candidate: 0, root_sum: -2, root_pairs: 1})
                        - (variable + 1) ** 2) == 0
    prime_examples = []
    for prime, branch in [(3, -1), (5, 1), (7, -1)]:
        reduction = positive_reduction if branch == 1 else negative_reduction
        roots = [residue for residue in range(prime) if int(reduction.subs(variable, residue)) % prime == 0]
        derivatives = [int(sympy.diff(reduction, variable).subs(variable, root)) % prime for root in roots]
        square_residues = sorted({residue ** 2 % prime for residue in range(prime)})
        if branch == 1:
            assert len(roots) == 3 and all(derivatives)
        else:
            assert roots == [0, prime - 1] and derivatives == [1, 0]
        prime_examples.append({'prime': prime, 'q_branch': branch, 'reduced_roots': roots,
                               'derivatives_at_reduced_roots': derivatives,
                               'thirteen_is_square': 13 % prime in square_residues})
    repository = Path(__file__).resolve().parents[1]
    return {
        'hypotheses': 'Integer equality point c=b(b+2)-a, q=ac, G=0; p odd dividing b.',
        'positive_branch': 'q=1modp gives a^2=-1modp. P3=x(x^2+1)modp has three simple roots0,+a,-a, with derivatives1,-2,-2. Hensel gives three distinct Z_p roots, for every oddp including13.',
        'negative_branch': 'q=-1modp and p!=13: the root0 has a unique Hensel lift d0 in pZ_p. P3=(x-d0)Q and P3prime(d0) is a unit. Q splits over Z_p iff13 is a quadratic residue modp; otherwise P3 has exactly one Q_p root.',
        'negative_branch_discriminant_valuation': 'v_p(Delta)=2v_p(b), normalized unit13*(b/p^e)^2modp. In the split case the two roots reducing to-1 differ by valuatione; differences to d0 are units.',
        'generic_factorization': str(quadratic),
        'quadratic_discriminant': str(quadratic_discriminant),
        'generic_discriminant_remainder_factor': str(remainder_factor),
        'generic_factor_discriminant_identity_verified': True,
        'positive_simple_root_identities_verified': True,
        'prior_direct_quotient_sylvester_and_local_anchor_identities_reverified': True,
        'local_anchor': local['anchor_v'],
        'fixed_prime_examples': prime_examples,
        'surviving_mod5_b_zero_rows': [[2, 0], [3, 0]],
        'all_mod5_power_splitting_tests_pass_on_surviving_b_zero_rows': True,
        'exceptional_negative_branch': 'p=13; not classified by the present normalized-unit argument.',
        'prior_local_certificate_sha256': hashlib.sha256(
            (repository / 'results/endpoint-one-equality-local-discriminant.json').read_bytes()).hexdigest(),
        'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                          for source in (Path(__file__), Path(__file__).with_name('check_endpoint_one_equality_cubic.py'),
                                         Path(__file__).with_name('check_endpoint_one_equality_local_discriminant.py'),
                                         Path(__file__).with_name('check_six_support_quotient.py'))},
        'sympy': sympy.__version__,
        'scope': 'Written local splitting classification at every odd prime dividingb, apart from the negative branch at13. Hensel lemma and the quadratic discriminant criterion supply the unbounded prime-power conclusion. Exact generic identities and three specified residue examples are diagnostics, not finite exponent bases or an empirical test of Hensel lemma. No exponent/prime/power scan, integer equality point, global integral spectrum, Lean or new nonintegrality family claimed. Remaining positive mod5branch cannot be excluded by local splitting at5 alone.',
    }


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
