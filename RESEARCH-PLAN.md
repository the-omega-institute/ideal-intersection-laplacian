# First task: Laplacian integrality

The [local splitting classification](notes/endpoint-one-equality-local-splitting.md)
now settles every odd prime divisor of b except the negative branch at13.
The positive q=1branch splits overZ_p; the negative q=-1branch splits
iff13is a residue. Thus the surviving (a,b)=(2,0)/(3,0)mod5rows pass
every5-power splitting test.
The curve also has two unique compatible local points for every fixed
b in5Z_5, so simultaneous curve/splitting lifts do not exclude either row.
Further work should use the actual integer
root equation/global discriminant, primes not dividing b, the two b=2mod5
rows, or a specific reduction for the exceptional negative branch at13.
Do not enlarge5-power tables on the positive branch. Local compatibility
does not construct an integer equality point or prove integral spectra.

The [uniform local discriminant obstruction](notes/endpoint-one-equality-local-discriminant.md)
now excludes equality spectra when p|b, a²=1modp and13 is a nonresidue
at an odd prime. In particular7and11cannot divide b. It resolves the
double-root degeneracy by Delta=13b²modp^(3v_p(b)), refining the necessary
mod5pairs to{(2,0),(3,0),(0,2),(3,2)}. These remain necessary conditions.
Next seek an obstruction on the positive branch q=1modp, or combine the
actual integer cubic root equation with G=0. No integer equality-point
list or global splitting classification follows from the local conditions.

The [modulo-five obstruction](notes/endpoint-one-equality-mod-five.md)
excludes two complete global residue classes and restricts the equality
splitting problem to six (a,b) residue pairs. Modulo three gives no further
splitting exclusions on the equality curve. Subsequent bounded research
should combine this necessary residue information with the actual integer
curve/root equations; compatible finite-field rows do not establish solutions.
The endpoint-two completion is already integrated in the working PR3.

The equality cubic now has explicit coefficient and discriminant formulas
in [the arithmetic note](notes/endpoint-one-equality-cubic.md). A known
integer equality point can be tested by its positive divisors above a+b
and the residual quadratic discriminant. The global missing step is an
exhaustive integer-point computation, or a uniform splitting obstruction.
Square discriminant alone does not prove splitting; Siegel finiteness and
Riemann-Roch spaces do not supply an effective candidate bound.

The current [standalone endpoint-two completion](notes/endpoint-two-completion.md)
settles every all-even triple and every permutation(1,3,2)/(3,3,0)mod4 triple.
For ordered real minimum>=40, an endpoint-two zero forces another quotient
root in(4,5), by two full positive identities. The complete8,658triple
necessary base at fully distinct minima8through39 has no endpoint-two zeros,
with independent integer-Horner/6x6Bareiss agreement in every case. The global
result also uses earlier repeated/minimum<=7theorems and their finite scopes.
Unbounded integer-point emptiness of the endpoint-two surface is not needed
or proved. Focus subsequent research on the remaining endpoint-one classes;
full Q3 and higher-prime nonsquarefree vectors stay open. Standalone integration
into the manuscript awaits review; historical reductions below are preserved.

The [endpoint-one geometry](notes/endpoint-one-geometry.md) now gives exact
real feasibility/uniqueness at fixed a>=8,b>=a: R1_a(b)>0 iff one c>b
solution exists, with thresholdgamma(a)in(2a^2-a-2,2a^2-a-1). Integer middle
exponents require b<=2a^2-a-2; the unique real c must also satisfy
b+c<4a^2-2a. The sum tail proves nonintegrality for every parity pattern.
Further bounded work should target integer feasibility of this unique root
or its other quotient roots, retaining full Q3 as open. These standalone
written results need no finite base or new congruence shifts.

The [endpoint-one growing-gap proof](notes/endpoint-one-growing-gap.md)
excludes integer endpoint one for all d=b-a>=1,a>=2d^2+20; gaps1and2
are excluded for every a>=8. Its unique real exponent is bracketed by
L=2a^2+(2d-3)a-d^2-ceil(3d/2)+1 and L+1. Written endpoint-one/two
exclusions finish all parity patterns when d>=5,a>=2d^2+20 without a
finite base. Broader spectral consequences use prior finite certificates.
Focus subsequent bounded work inside d>=3,a<2d^2+20,b<=2a^2-a-2,
b<c,b+c<4a^2-2a, on integer feasibility or other quotient roots.
This is a necessary surviving region; full Q3 remains open. Earlier
results and manuscript files remain unchanged pending coauthor review.

The [minimum-eight certificate](notes/minimum-eight.md) completes every
triple with minimum exactlyeight using written reductions and a complete
108pair endpoint-one unit-bracket base, covering all c>b. Each boundary
has independent integer-Horner/6x6Bareiss agreement; full-interval and
unit-interval Sturm counts are1for each pair. The new result requires
finite computation; its endpoint-two reduction is written and does not
use the global8658triple base. Cumulative minimum<=8retains the earlier
27562triple finite certificate. Remaining candidates have minimum>=9.
Next target a specified structural obstruction or another quotient root;
do not expand the minimum range without a stated mathematical question.

The [endpoint-one spectral theorem](notes/endpoint-one-spectral-gap.md)
now identifies one as a simple smallest positive quotient root and puts
allfourremainingroots strictly above four, at real exponents>=8onh_C(1)=0.
The exact residual quartic is positive throughout closed[0,4], by a
complete350termpositive identity and all70note vectors, with no finite
base. Further structural work should target quartic integer splitting or
a noninteger root above four, or integer exponent feasibility in the
surviving region. The gap alone does not prove nonintegrality or closeQ3;
prior finite dependencies and manuscript scope remain unchanged.

The [constant and divisor window](notes/endpoint-one-divisor-window.md)
now gives F(0)=rs(p+s)>0 and the written strict interlacing bound
lambda_3<c for all positive ordered real triples. On endpoint one at
minimum>=8 this means 4<mu_1<c. For each fixed integer triple, test every
positive divisor of rs(p+s) in [5,c-1] with exact F evaluation. Three
established controls pass this nonintegrality diagnostic; no new family
is claimed. Next seek a uniform obstruction to these candidate roots
in the surviving region, rather than treating per-triple finiteness as
a global decision of the unbounded endpoint-one surface. Full Q3 open.

The [minimum-dependent root theorem](notes/endpoint-one-minimum-root.md)
now puts all four residual roots above a on endpoint one for every real
4<=a<=b<=c, with one simple and smallest positive. It proves the sum
lower bound b+c>=2a²-2a+1 and its unique repeated-boundary equality case,
then uses determinant sign and interlacing to count exactly two roots
below a. No finite base or earlier350termgap certificate is needed.
The smallest quartic root lies in (a,c), so refine the uniform splitting
question to divisors a<d<c of rs(p+s) with h_C(1)=F(d)=0. Three established
controls suffice for the diagnostic; no parameter scan or new family.
Full Q3 and prior finite dependencies remain as recorded.

The [pair-sum window](notes/endpoint-one-pair-sum-window.md) strengthens
the universal upper bound to lambda_3<a+b for all ordered positive real
exponents. A four-support principal block has exactly three roots below
a+b, as its quadratic factor has Q(a+b)=-ab(a+b)<0. On endpoint one
at real minimum>=4, refine the splitting target to positive divisors
a<d<min(c,a+b) of rs(p+s) with h_C(1)=F(d)=0. The three established
controls leave23exact nonzero candidates; no parameter scan is needed.
Written bounds require no finite base; full Q3 stays open.

The [constant-divisibility proof](notes/endpoint-one-constant-divisibility.md)
shows universal divisibility by 12 and exact gcd 12 over the whole integer
endpoint-one surface at minimum>=4, including settled repeated triples.
The family a=6k,b=a,c=(a-1)(2a-1) has divisors d=3a/2 in the window
for infinitely many a, yet exact F(d)<0. A uniform splitting obstruction
must use F(d)=0; divisor presence/size alone cannot close the full surface.
The gcd on the narrower fully distinct surviving region is not determined.
No higher two-adic lifts or exponent scan were used; full Q3 remains open.

The [root-congruence note](notes/endpoint-one-root-congruences.md) records
F(21)>0 at the existing (20,20,741) control, so negativity is not uniform
over the full divisor window. For a root d, N/d=D modulo d and d-e divides
F(e)=-r^2(e^2+3e-s)/(e-1) for e=a,b,c,d!=e; if d=e, require F(e)=0.
These uniform necessary tests reduce the existing 23 candidates to one,
which is still a nonroot. Seek a uniform obstruction in the fully distinct
surviving region; passing these tests is not sufficient for being a root.
No new family, range scan, endpoint lifting or full Q3 closure is claimed.

The [middle-root location proof](notes/endpoint-one-middle-root.md)
now refines the candidate window on real endpoint one at minimum>=4:
c+a>b(b+2) gives b<mu_1<min(c,a+b); c+a<b(b+2) gives a<mu_1<b<mu_2.
At equality the [equality theorem](notes/endpoint-one-equality-root.md)
identifies b as the simple smallest residual root, even proving
lambda_3=b on the full real equality subfamily without endpoint one.
The [equality pair-sum gap](notes/endpoint-one-equality-second-root.md) proves
lambda_4>a+b without endpoint one; all three remaining cubic roots lie above
a+b on endpoint one. Integer equality feasibility and splitting of that
cubic stay open. The [equality curve](notes/endpoint-one-equality-curve.md) has geometric
genus ten, so integer points are finite but not enumerated. Effective integer
classification requires additional work.
The [quotient descent check](notes/endpoint-one-equality-quotient.md) rules out
further rational degree-two descent to genus one or two on the known
genus-three quotient. Other maps and both Jacobian ranks remain open.
Use coefficient/anchor congruences in the refined windows
when studying integer feasibility or splitting. Two selected real algebraic
endpoint controls show both strict regimes; the written proof needs no
finite base. No new nonintegrality family or full Q3 closure is claimed.

The [root-hierarchy note](notes/endpoint-one-root-hierarchy.md) adds necessary
quadratic/cubic coefficient congruences and rejects the sole prior control
survivor15 at the quadratic stage. It uniformly rejects the earlier boundary
candidate d=3a/2, while preserving the distinction from all-divisor exclusion.
Both strict E regimes and equality occur for every real minimum>=9 in
specified real families. Integer regime dominance is unresolved. Equality
reduces to G(a,b)=0,c=b(b+2)-a, with necessary a<b<2a and sum bounds at
minimum>=8. Further work should address this exact integer equation or
uniform root exclusion in the refined windows; no sufficiency/global closure.

The manuscript now combines the mixed-parity restrictions in Theorem 13.5
and the endpoint reductions in Theorem 14.1. Complete case proofs remain in
Appendices B/C; Appendix A summarizes verification, with the full checker
catalogue retained in an optional detailed build. No result or certificate
is removed, and this reorganization introduces no new mathematical claim.

The standalone [middle-diagonal proof](notes/endpoint-two-middle-inertia.md)
now narrows the structural endpoint-two problem. In size order `4<=a<b<c`,
a possible integer spectrum in the all-even or `(1,3,2)/(3,3,0)` modulo-four
classes requires both `(a-2)(a+b+c-2)<2bc` and
`(b-2)(a+b+c-2)>2ac`, with two the smallest positive quotient root and simple;
the middle-dependent upper tail is additional to the old minimum-only bound.
No endpoint-zero enumeration or new two-adic shift is needed. The current
manuscript files in this PR remain unchanged pending review of the standalone
deductions; the editorial revision is maintained separately on PR3.

The [full determinant positivity proof](notes/endpoint-two-middle-tail.md)
settles the previously surviving `b>=2a+2` branch, and more: every ordered
triple with minimum at least four and `b>=2a-2` has `h_C(2)>0` and a positive
root in `(0,2)`. Endpoint-two candidates require `b<2a-2` as well as the
existing maximum bound. The next structural target is the secular equation
inside this smaller region; the other mixed-parity endpoint-one cases remain
open. Reza has deferred manuscript closure while structural work is informative.

The [positive interval transformation](notes/endpoint-two-maximum-tail.md)
now strengthens the maximum bound to `c<3a-4` on the endpoint-two surface.
It uses the bounded middle interval `a<=b<2a-2` and a single exact
positive-coefficient identity, without enlarging any parameter search.
The next structural target is `h_C(2)=0` and the remaining quotient roots
inside both new bounds, retaining the independent endpoint-one cases.

The [root-geometry theorem](notes/endpoint-two-surface-geometry.md) now
characterizes fixed-pair real feasibility: R_a(b)>0 iff there is a c>b
endpoint-two solution, unique and simple as a polynomial root in c.
For a>=8, b must lie below the unique threshold beta(a) in(a,2a-2).
Focus further arithmetic work on integer feasibility of this unique
real root, or on the other quotient roots there; the general surface
and other endpoint-one cases remain open.

The [gap-two proof and complete finite base](notes/endpoint-two-gap-two.md)
now exclude integer endpoint-two solutions for all a>=8,b=a+2,c>b.
The written tail a>=20 brackets the unique real exponent between2a-8and2a-7;
the remaining twelve fixed pairs are certified by complete constant-divisor
checks, independently cross-checked by rational-factor extraction.
Further work should address a different specified structural subfamily or
the other quotient roots, retaining the general integer-feasibility and
endpoint-one problems as open rather than enlarging an arbitrary scan.

The [growing-gap proof](notes/endpoint-two-growing-gap.md) now brackets the
unique real endpoint-two root for `d=b-a>=5,a>=2d^2+20` between consecutive
integers `2a+d-11` and `2a+d-10`. Integer endpoint-two solutions are excluded
throughout this unbounded family by a written proof with no finite base.
The general integer-feasibility problem outside the stated hypotheses and
other endpoint-one cases remain open. Further work should address a specified
remaining structural case or the other quotient roots; manuscript integration
of the standalone results awaits review.

The [small-middle-gap exclusion](notes/endpoint-two-small-middle-gaps.md)
now covers all integer a>=8,1<=b-a<=4,c>b. New gaps1,3,4 use written tails
and a complete76pair finite base; gap2 uses the earlier preserved result.
Combining this with the growing-gap theorem, every fully distinct integer
endpoint-two zero at minimum>=8 requires d=b-a>=5 and a<2d^2+20, in addition
to b<beta(a),c<3a-4. Focus any next structural work inside this remaining
region or on the other quotient roots; other endpoint-one cases remain open.

The [nine-fourths maximum proof](notes/endpoint-two-sharp-maximum.md)
now gives c<9a/4-8 for every endpoint-two zero at ordered minimum>=8.
Its complete transformed identity has two nonnegative square expressions
and an84term positive residual; the full unbounded theorem needs no finite
base or parameter scan. The surviving fully distinct integer region requires
d>=5,a<2d^2+20,b<beta(a),b<c<9a/4-8. Further work should target a specified
case inside these restrictions or the other quotient roots; general endpoint-two
feasibility and other endpoint-one cases remain open.

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
The [clustered-root proof](notes/clustered-odd-roots.md) now requires
`a+c=b(b+2)mod128` and `b=11or15mod16`, followed by the stated third-shift
parity condition. It uses the exact value factorization at b and a
derivative identity; a further binary cubic excludes cases passing both.
The compatible classes, combined with endpoint-zero/interval restrictions,
remain a focused next problem. No exponent or modulus range is scanned.
The [mixed endpoint-root proof](notes/mixed-endpoint-roots.md) now settles
every positive permutation of (3,0,0)mod4 using the uniform low root.
It also forces the surviving patterns (1,3,2) and (3,3,0)mod4 below
the linear endpoint-two bound. The next focused step is to combine
their necessary endpoint-two zero with its divisor constraint inside
this linear region, or examine the remaining one-odd-exponent patterns.
Reza's scope and closure questions motivate a stopping point for new
two-adic shifts: no finite closure has been established. Consolidate the
existing conditions and pursue the structural endpoint-two problem first.
Detailed checker scopes now form the manuscript's verification appendix.
The [consolidation](notes/manuscript-consolidation.md) now places the
strongest (1,3,2) arithmetic conditions, endpoint-two zero and linear
maximum bound in one main theorem. Complete lifting proofs form Appendix B.
The next research question remains the endpoint-two surface inside this
linear region, using its exact cubic/divisor constraints and other roots.
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
