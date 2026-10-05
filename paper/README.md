# Working manuscript

Read [the PDF](paper.pdf), or edit [paper.tex](paper.tex) and the section
files it includes. This is a growing mathematical draft, not a submission
package. Author metadata and any manuscript disclosure are for joint agreement.
The main text ends with explicit remaining questions and references.
Theorem14.2 now proves the global gap lambda_3<a+b<=b+c<lambda_4
for real2<=a<=b<=c and retains the endpoint-one minimum-root theorem.
Corollary14.3 includes all four residual bounds; Proposition14.6 keeps
the equality index/simplicity argument and uses the stronger b+c gap.
The E-sign test refines only the smallest root, and equality cubic
divisor candidates must exceed b+c. Supporting proof/checker/certificate
are pinned to PR9 `fb1d7c0134ad385931e3b4e43e445695bc4bf566`; reproduce
`python3 scripts/check_global_pair_sum_separation.py` at that revision.
Proposition13.9 supplies the exceptional-prime valuation obstruction:
on q=-1mod13 with13 dividing b, integer splitting requires b=104mod169.
It retains the positive branch and leaves that remaining residue open.
Its exact anchor identities are pinned to PR9
`eb6b7d378205033154c328cd5c543332f27b6467`; run
`python3 scripts/check_endpoint_one_equality_thirteen.py` there.
Proposition13.8 gives the complete local cubic splitting test at odd
prime divisors of b, apart from the negative branch at13. The two
surviving b=0mod5rows pass all5-power splitting tests by Hensel's lemma.
Its exact polynomial identities are pinned to PR9
`8b87f9df6d402fafc60ed063ab8b12326707febf`; run
`python3 scripts/check_endpoint_one_equality_local_splitting.py` there.
Proposition13.6 excludes all permutations of (1,1,2)/(1,4,4)mod5 by a
full reduced-quintic splitting proof. Proposition13.7 adds a uniform local
discriminant obstruction on G=0 and refines the six initial compatibility
rows to {(2,0),(3,0),(0,2),(3,2)}mod5. Integral equality spectra require
7and11not to divide b. Its proof and exact identities are pinned to PR9
`4878e51211e2694e40a246759111d55dce070309`. The global mod5 evidence is pinned
to PR9 `7d917afffd7c2616bc052810718dcc720d916a8b`; run
`python3 scripts/check_endpoint_one_equality_mod_five.py` there and compare
with `results/endpoint-one-equality-mod-five.json`. This result has no finite
exponent base, and leaves effective equality classification open.
Remark 14.5 records the equality curve's genus ten and Siegel finiteness
consequence, with a short quotient/ramification argument and a linked detailed
verification note. It does not supply an effective integer-point list.
Proposition 14.6 gives the unconditional equality spectrum: b is simple
and third smallest, with all three larger roots above b+c. On endpoint
one this leaves a monic cubic whose three roots exceed b+c.
Lemma14.7 supplies the endpoint-two middle/maximum rectangle bounds;
Theorem14.8 completes that alternative using the written(4,5)tail and
the required8,658-triple base plus earlier finite dependencies.
Corollary14.9 settles all-even triples and both(1,3,2)/(3,3,0)mod4 classes.
Appendix D lists every positive coefficient vector and every base count.
The closing section presents one endpoint-one spectral problem with four
current reductions and a precise equality system including G(a,b)=0.
Theorem 13.5 combines the mixed-parity classes and their necessary conditions;
Theorem 14.1 combines the endpoint reductions. The main text gives one worked
shifted-root example. Appendix A summarizes the actual verification scopes,
Appendix B retains all mixed-parity case proofs, and Appendix C retains the
endpoint polynomial, divisor and certificate arguments.
The complete per-checker catalogue is preserved in
[verification-details.tex](sections/verification-details.tex) and can be
included with the optional detailed build below.
Further two-adic shifts are paused. Subsequent work targets endpoint-one
integer feasibility or splitting; the endpoint-two alternative is settled.

The section names follow Reza's proposed layout. At the time of integration,
his announced `paper/` files were not yet present on any of the three remote
branches. The introduction and open section have been developed with the proofs;
`aa-family.tex` is reconstructed from his already public PR #2 proof. His
own versions can be integrated when uploaded, preserving the five expanded
sections and their shared graph/lifting definitions.

| Section | Contents |
| --- | --- |
| [graph.tex](sections/graph.tex) | Ideal encoding, support classes, universal-vertex lift and both repeated-exponent blocks |
| [squarefree.tex](sections/squarefree.tex) | Complete squarefree composite classification, with odd and even tensor arguments |
| [pqrk.tex](sections/pqrk.tex) | Explicit irrational eigenvalues for `(1,1,k)` |
| [aa-family.tex](sections/aa-family.tex) | Reza's public boundary-family proof |
| [aa-bounds.tex](sections/aa-bounds.tex) | Exact fixed-a and fixed-index criteria, successive cutoffs and complete smaller-factor certificates |
| [aa-completion.tex](sections/aa-completion.tex) | All-positive-a,b theorem: third-index certificates and uniform cubic sign obstruction |
| [unit-exponent.tex](sections/unit-exponent.tex) | General six-support complement quotient and all (1,b,c) theorem |
| [minimum-two.tex](sections/minimum-two.tex) | All (2,b,c) theorem from two positive expansions and one rational interval |
| [distinct-tail.tex](sections/distinct-tail.tex) | Uniform c>=4a^2-2a cutoff and all (3,b,c) theorem with the complete derived 325-case endpoint certificate |
| [low-spectrum.tex](sections/low-spectrum.tex) | General inertia criterion, four complete bounded-gap families, every exponent span at most3, and complete finite minimum-through-seven certificate |
| [mixed-inertia.tex](sections/mixed-inertia.tex) | Uniform positive root below3 for every minimum at least4; root in(2,3) under the lower inequality; growing balanced region a>=3span+8 |
| [arithmetic-obstructions.tex](sections/arithmetic-obstructions.tex) | Every gcd>=3 triple, all-odd and prime-residue classes, all-two-modulo-four triples and every common 2-adic valuation |
| [mixed-parity-congruence.tex](sections/mixed-parity-congruence.tex) | Combined Theorem 13.5 for all mixed-parity exclusions/restrictions, with one worked example |
| [endpoint-reduction.tex](sections/endpoint-reduction.tex) | Combined Theorem 14.1 for the linear bound, tails, divisor candidates, second-smallest<=15 certificate and modulo-three classes |
| [endpoint-one-spectrum.tex](sections/endpoint-one-spectrum.tex) | Main-text twelve-term endpoint-one proof, simple root one, all residual roots>a, smallest root below min(c,a+b), nonzero constant and divisor window; generic350termpositivity retained as a verification remark |
| [endpoint-two-completion.tex](sections/endpoint-two-completion.tex) | Complete rectangle-bound, further-root and global integer/parity-class proofs, with explicit finite dependencies |
| [endpoint-two-identities.tex](sections/endpoint-two-identities.tex) | Appendix D: all84/44/112 positive coefficients and32per-minimum finite-base counts |
| [aa-small.tex](sections/aa-small.tex) | All-b theorem for a=2 through9, divisor/modular certificates and cubic-test scope |
| [verification.tex](sections/verification.tex) | Appendix A: grouped verification scopes, complete finite-domain counts and evidence boundaries |
| [verification-details.tex](sections/verification-details.tex) | Complete per-checker catalogue, included in the optional detailed build |
| [two-adic-lifting.tex](sections/two-adic-lifting.tex) | Appendix B: residue/modulus/condition table, complete case proofs, derivative thresholds and successive lifting |
| [endpoint-details.tex](sections/endpoint-details.tex) | Appendix C: complete endpoint polynomial, positivity, divisor, finite-certificate, modulo-three and CRT-scope proofs |
| [open.tex](sections/open.tex) | Single remaining endpoint-one spectral problem, four current reductions, explicit finite equality splitting system and nonsquarefree higher-prime vectors |

## Build

From this directory, with a standard TeX installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

To include the complete per-checker catalogue while preserving the default
PDF, use a separate job name and repeat the command for cross-references:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -jobname=paper-detailed '\def\DetailedVerification{1}\input{paper.tex}'
pdflatex -interaction=nonstopmode -halt-on-error -jobname=paper-detailed '\def\DetailedVerification{1}\input{paper.tex}'
```

## Evidence

The [consolidation guide](../notes/manuscript-consolidation.md) maps previous
theorem numbers to the current main statement and appendix propositions.
The prior checker sources and saved certificates retain their original
revisions, contents and verification scopes.

The initial notes and checkers are retained from PR #2 at
`f1284407b418979e8d3973805c85518489cab201`; the strengthened diagnostic,
factor certificates and cutoff are retained from PR #3 at
`fd8cffe184c0fff34647299fe6e08cdd1caac442`. The manuscript presents their
proofs in dependency order. No new parameter search or Lean validation is
needed to reproduce this consolidation.

The endpoint-two completion and equality-cubic supporting sources are pinned
to PR9 revision `4afe151e1dc7193e6776cc1b08d3606aa804238e`. The manuscript
includes the full proofs and positive coefficient vectors; that revision
retains the standalone checker scripts, JSON and complete base CSV. To rerun
them in an independent checkout of this same repository:

```sh
git fetch origin endpoint-two-middle-inertia-20261005
git worktree add --detach ../ideal-intersection-endpoint-checks 4afe151e1dc7193e6776cc1b08d3606aa804238e
cd ../ideal-intersection-endpoint-checks
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_middle_tail.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_sharp_maximum.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_completion.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_completion.py --csv
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_one_equality_cubic.py
```

Compare each output with its saved result at that revision. The global
endpoint-two theorem retains the earlier complete minimum-through-seven
finite dependency; the new base alone is not a proof for every minimum.

From the repository root, use Python 3.10+ and SymPy 1.14.0:

```sh
python3 scripts/check_integrality_obstructions.py
python3 scripts/check_remaining_case.py
python3 scripts/check_repeated_exponent_family.py
python3 scripts/check_aa_b.py --json
python3 scripts/check_fixed_repeated_exponents.py
python3 scripts/check_second_cutoff.py
python3 scripts/check_factor_index_reduction.py
python3 scripts/check_repeated_exponent_completion.py
python3 scripts/check_six_support_quotient.py --json
python3 scripts/check_fully_distinct.py
python3 scripts/check_minimum_two.py
python3 scripts/check_distinct_tail.py
python3 scripts/check_low_spectrum.py
python3 scripts/check_mixed_inertia.py
python3 scripts/check_arithmetic_obstructions.py
python3 scripts/check_endpoint_reduction.py
python3 scripts/check_endpoint_congruence_scope.py
python3 scripts/check_even_exponent_congruence.py
python3 scripts/check_endpoint_surfaces.py
python3 scripts/verify_endpoint_surfaces.py
python3 scripts/check_endpoint_residues.py
python3 scripts/check_mixed_parity_congruence.py
python3 scripts/check_odd_root_distribution.py
python3 scripts/check_2adic_higher_moduli.py
python3 scripts/verify_2adic_higher_moduli.py
python3 scripts/check_higher_derivatives.py
python3 scripts/verify_higher_derivatives.py
python3 scripts/check_odd_root_lift.py
python3 scripts/check_clustered_odd_roots.py
python3 scripts/check_mixed_endpoint_roots.py
python3 scripts/check_open_region2.py
python3 scripts/check_open_region2.py --json --certificate-csv results/open-region-discriminants.csv
python3 scripts/check_open_region_certificate.py
```

Compare with the corresponding JSON files under `results/`. The full text
output for the 90 diagnostics is also retained there. A separate direct
check for the cubic-scope example `(1,1,2)` is:

```sh
python3 - <<'PY'
from itertools import product
import sympy

bounds = (1, 1, 2)
vertices = [vertex for vertex in product(*(range(bound + 1) for bound in bounds))
            if vertex not in ((0, 0, 0), bounds)]
laplacian = sympy.zeros(len(vertices))
for first_index, first_vertex in enumerate(vertices):
    for second_index in range(first_index + 1, len(vertices)):
        second_vertex = vertices[second_index]
        if any(max(first, second) < bound
               for first, second, bound in zip(first_vertex, second_vertex, bounds)):
            laplacian[first_index, first_index] += 1
            laplacian[second_index, second_index] += 1
            laplacian[first_index, second_index] = -1
            laplacian[second_index, first_index] = -1
variable = sympy.Symbol('x')
expected = (variable * (variable - 10) * (variable - 9) ** 3
            * (variable - 7) ** 2 * (variable - 4)
            * (variable ** 2 - 13 * variable + 34))
assert sympy.expand(laplacian.charpoly(variable).as_expr() - expected) == 0
print(sympy.factor(expected))
PY
```

The bibliography places the original graph reference and Reza's source
preprint alongside verified ring-graph, Laplacian, partition and tensor
background. Citation checks and omitted ambiguous suggestions are recorded in
[the bibliography audit](../notes/bibliography-review.md). The source preprint is [Zenodo DOI10.5281/zenodo.23134979](https://doi.org/10.5281/zenodo.23134979).
Its public PDF has the same SHA256 as the previously supplied source.
The source PDF is linked rather than copied into this repository.

[Return to the project entrance](../README.md).
