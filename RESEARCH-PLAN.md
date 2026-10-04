# First task: Laplacian integrality

**Status:** graph convention reviewed; the [working manuscript](paper/paper.tex)
consolidates the squarefree classification, `(1,1,k)`, Reza's boundary family,
the successive linear cutoffs, all `(a,a,b)` with `a,b>=1`, and all
`(1,b,c)`, `(2,b,c)` and `(3,b,c)` with `b,c>=1`, plus the uniform
cutoff `c >= 4a^2 - 2a` for ordered `2 <= a <= b <= c`.
The general Schur-complement inertia criterion also proves the four families
with gaps `(1,2),(1,3),(2,3),(3,4)`, for every positive minimum exponent.
Thus all triples with maximum minus minimum at most3 are settled.
The coauthor-requested complete finite region at minima4through7 has
27,562nonsquare discriminants, all independently reconstructed by integer
Sylvester determinants. With the cutoff, every minimum-entry<=7 triple
has a complete certificate. This extension depends on the finite computation.
The corrected repeated-exponent diagnostic and exact certificates remain
available. A uniform comparison now places a positive complement root
in `(0,3)` for every minimum exponent at least4. The sufficient inequality
`(a-2)(a+b+c-2)>2bc` places a root in `(2,3)` and proves nonintegrality;
in particular, every minimum `a>=3(c-a)+8` is covered. Read
[the mixed-sign comparison and balanced-region proof](notes/mixed-inertia.md).
The [arithmetic obstructions](notes/arithmetic-obstructions.md) additionally
settle every gcd>=3 triple, every all-odd triple and general common-residue
classes with a quadratic nonresidue criterion. This includes residues1,3,4
modulo5 and1,2,4,5 modulo7, with arbitrarily large unequal exponents.
Full Q3 remains open.
The [endpoint residue proof](notes/endpoint-residues.md) also settles
every residue triple (2,2,2) and permutation of (1,2,2) modulo three.
Complete modulo-two/three root sets are recorded; no pair is root-free
on either surface, so retaining only root-free pairs misses these classes.
A fixed finite set of endpoint congruences alone cannot establish global
emptiness for fully distinct triples; combine them with further restrictions.
The [mixed-parity proof](notes/mixed-parity-congruence.md) adds six exponent
classes modulo eight. Three hypothetical odd quotient roots force either
32|h_C(1) or32|h_C(3), contradicted by explicit polynomial congruences.
This tests the whole quotient spectrum and requires no exponent-size bound.
The [root-distribution proof](notes/odd-root-distribution.md) now also
settles every permutation of (3,3,2) modulo four. The shifted quintic
forces all three odd roots to be one modulo four; endpoint and derivative
divisibilities give contradictory parity requirements on the shifts.
Reza's [higher-modulus diagnostic](notes/higher-2adic-moduli-review.md)
has also been checked at his fixed moduli8,16,32. Both endpoint values
modulo32 already have coordinate period8 for mixed-parity exponents,
so increasing the exponent modulus alone adds no exclusions.
The [higher-derivative review](notes/higher-derivatives-review.md) gives
the conditional first-three-derivative thresholds and proves a stronger
value obstruction: exponent residues(1,3,2)mod4 require a+c=15mod16
for an integer spectrum. The second/third thresholds alone add no
exclusions with the present root information; representative valuations
must not be treated as uniform class data.
The [second shifted-root proof](notes/odd-root-lift.md) strengthens the
sum condition to `a+c+4b=27mod32`, with a,b,c labelled by residues
(1,3,2)mod4. A binary cubic containing the irreducible quadratic
z^2+z+1 excludes half the previously remaining sum classes, with no
size or ratio bound. Compatible hypothetical odd roots would all be
bmod8. The remaining weighted-sum class and one-odd-exponent patterns
are focused next cases; congruence compatibility does not imply integrality.
The [requested endpoint diagnostic](notes/endpoint-surfaces-diagnostic.md)
exhausts all66pairs `4<=a<b<=15` and all integer `c>b` by exact divisor
reduction, finding neither endpoint zero. With the low-root theorem and
earlier cases, every triple whose second-smallest exponent is at most15
is now nonintegral. The remaining region has `b>=16`; there is no new
arbitrary bound on c or extension of the requested pair range.
The [scaled parity obstruction](notes/even-exponent-congruence.md) settles
every triple all congruent to two modulo four, with no minimum or ratio
bound. Together with the earlier all-odd and gcd arguments, every common
2-adic valuation is settled. Remaining even triples have both a multiple
of four and an exponent congruent to two modulo four.
The [endpoint-two reduction](notes/endpoint-reduction.md) proves
`h_C(2)=0 => c<7a-16+40/(a+2)` for ordered minimum>=4, and settles
every all-even triple beyond that linear bound. At minimum>=8,
`c>=7a-12` suffices. The remaining all-even region has gcd2 and this
linear upper bound; the mixed-parity endpoint-one surface stays open.

Read [the exact diagnostic and finite-reduction proof](notes/aa-b-diagnostic.md).
With SymPy 1.14.0, reproduce the requested output using:

```sh
python3 scripts/check_aa_b.py
python3 scripts/check_aa_b.py --json
python3 scripts/check_fixed_repeated_exponents.py
python3 scripts/check_second_cutoff.py
python3 scripts/check_factor_index_reduction.py
python3 scripts/check_repeated_exponent_completion.py
python3 scripts/check_six_support_quotient.py
python3 scripts/check_fully_distinct.py
python3 scripts/check_minimum_two.py
python3 scripts/check_distinct_tail.py
python3 scripts/check_low_spectrum.py
python3 scripts/check_mixed_inertia.py
python3 scripts/check_arithmetic_obstructions.py
python3 scripts/check_endpoint_reduction.py
python3 scripts/check_even_exponent_congruence.py
python3 scripts/check_endpoint_surfaces.py
python3 scripts/verify_endpoint_surfaces.py
python3 scripts/check_endpoint_residues.py
python3 scripts/check_mixed_parity_congruence.py
python3 scripts/check_open_region2.py
python3 scripts/check_open_region_certificate.py
```

The [completion proof](notes/repeated-exponent-completion.md) settles the
remaining factor indices using a uniform cubic sign interval. The next
focused question is the six-support quotient for the remaining ordered region
`8 <= a < b < c < 4a^2 - 2a`. The [complement interval proof](notes/one-unit-exponent.md)
and [positive expansions](notes/minimum-two.md) now settle every triple
with minimum exponent at most2. The [uniform cutoff](notes/distinct-tail.md)
reduces each fixed minimum exponent to finitely many pairs; the complete
325-case integer endpoint certificate at minimum3 closes that entire family.
The [inertia criterion](notes/low-spectrum.md) handles two roots in one
interval, which endpoint signs can miss. Four bounded-gap families are now
settled using38root-free modular residues, without an exponent scan.
The [mixed-sign comparison](notes/mixed-inertia.md) now gives the uniform
low-eigenvalue bound and an exact inertia formula for nonsingular diagonals.
After the new balanced-region obstruction, focus on the necessary condition
`h_C(1)h_C(2)=0`: either exclude integer triples on these endpoint-zero
surfaces or find a different noninteger quotient root there. Do not infer
integrality from this necessary condition. The arithmetic restrictions
leave gcd1or2, at least one even exponent, and residue classes outside
the proved modular obstruction. Focus any endpoint-zero analysis there.
Use the new linear bound on the second surface and the exact constant-term
divisor constraints for both surfaces. The next question is whether an
endpoint-zero triple in the remaining region necessarily has a different
noninteger root; divisor membership alone does not answer it.
Apply the new unequal-valuation restriction as well. For the all-even
region, the scaled quotient modulo two has two parity classes left:
exactly one or exactly two odd half-exponents. The first divisibility
conditions in those classes are compatible and do not settle them.
The [requested open-region diagnostic](notes/open-region-diagnostic.md)
records its exact bounds and keeps H/complement endpoint patterns separate.
It exhausts the remaining pairs for minimum4,5,6,7 under the written cutoff,
but does not bound the minimum exponent in general.
The coordinate-swap decomposition is specific to repeated exponents.
Do not replace the open classification by an arbitrary finite scan.

Reza proposes the Laplacian integrality question, Q3 in his
[public source preprint](https://doi.org/10.5281/zenodo.23134979),
as the first follow-on task.

## First deliverable

The first note fixes the graph definition and Laplacian convention, gives
the squarefree classification and an unequal-exponent infinite family, and
includes a public reference for the originating graph. Reza's source
preprint is now linked via its verified Zenodo DOI.

Read [Reza's integrated extension](notes/repeated-exponent-family.md).
Next, address exponent triples outside the two proved families and nonsquarefree
vectors with more prime factors. The `(2,2,3)` example has an integral
antisymmetric block but a nonintegral remaining block, so a general proof
must handle this distinction. Use small, exact checks to diagnose stated
conjectures; numerical approximations do not establish integrality.

## Reproduce the checks

The infinite-family block checker uses Python 3.10 or later and its standard
library:

```sh
python3 scripts/check_integrality_obstructions.py
```

For the exact `(2,2,3)` characteristic-polynomial diagnostic, install the
pinned SymPy dependency in your own environment:

```sh
python3 -m pip install -r requirements-verification.txt
python3 scripts/check_remaining_case.py
python3 scripts/check_repeated_exponent_family.py
```

Compare outputs with `results/integrality-obstructions.json` and
`results/remaining-case-2-2-3.json` and `results/repeated-exponent-family.json`.
The new checker also verifies exact polynomial identities; its direct graph
checks cover 34, 174 and 548 vertices. These are finite independent checks;
the infinite-family claims use the written proofs. No Lean run is reported.

## Contribution checklist

1. State the graph convention, hypotheses and result.
2. Provide the readable proof, or clearly label the finite scope of a computation.
3. Record exact input identities, commands and verification range.
4. Give the source and attribution for existing results.
5. Identify the unresolved step and next mathematical question.

If Lean is used, record its toolchain, dependency revision and theorem axioms.
Select the execution machine and check available resources before a run.
Independent finite checks and formal verification retain separate scopes.

## Later directions

Vertex connectivity may accompany Q3 if the arguments connect naturally.
Other spectral invariants and the unequal-exponent matrix problem remain
separate follow-ups.

The source manuscript is linked rather than copied into this repository.
Attribute its earlier spectral results and keep its reported computations
separate from our independently checked claims.

[Return to the project entrance](README.md).
