# Working manuscript

Read [the PDF](paper.pdf), or edit [paper.tex](paper.tex) and the section
files it includes. This is a growing mathematical draft, not a submission
package. Author metadata and any manuscript disclosure are for joint agreement.
The main text ends with explicit remaining questions and references.
Theorem 13.5 combines the mixed-parity classes and their necessary conditions;
Theorem 14.1 combines the endpoint reductions. The main text gives one worked
shifted-root example. Appendix A summarizes the actual verification scopes,
Appendix B retains all mixed-parity case proofs, and Appendix C retains the
endpoint polynomial, divisor and certificate arguments.
The complete per-checker catalogue is preserved in
[verification-details.tex](sections/verification-details.tex) and can be
included with the optional detailed build below.
Further two-adic shifts are paused while the endpoint-two argument inside
the linear region and consolidation of the existing results are pursued.

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
| [aa-small.tex](sections/aa-small.tex) | All-b theorem for a=2 through9, divisor/modular certificates and cubic-test scope |
| [verification.tex](sections/verification.tex) | Appendix A: grouped verification scopes, complete finite-domain counts and evidence boundaries |
| [verification-details.tex](sections/verification-details.tex) | Complete per-checker catalogue, included in the optional detailed build |
| [two-adic-lifting.tex](sections/two-adic-lifting.tex) | Appendix B: residue/modulus/condition table, complete case proofs, derivative thresholds and successive lifting |
| [endpoint-details.tex](sections/endpoint-details.tex) | Appendix C: complete endpoint polynomial, positivity, divisor, finite-certificate, modulo-three and CRT-scope proofs |
| [open.tex](sections/open.tex) | Ordered 8<=a<b<c<4a^2-2a outside the proved criteria; endpoint-zero necessary condition and nonsquarefree higher-prime vectors |

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
