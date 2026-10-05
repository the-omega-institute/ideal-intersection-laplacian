# Laplacian integrality of ideal intersection graphs

Public workspace for the follow-on collaboration between **Haobo Ma,
Reza Nikandish and Wenlin Zhang**, studying ideal intersection graphs of
`Z_n` and their Laplacian spectra.

Our first question is the **Laplacian integrality characterization**:
which graphs in this family have only integer Laplacian eigenvalues?
This is a new research track; no complete characterization is claimed here.

The [endpoint-two completion](notes/endpoint-two-completion.md) now settles
**every all-even exponent triple**, and every permutation of `(1,3,2)` or
`(3,3,0)` modulo four, with no size/gap/ratio bound. On an endpoint-two zero
at minimum>=40, a written proof puts another quotient root in `(4,5)`.
A complete8,658triple necessary base excludes fully distinct endpoint-two
zeros at minima8through39, independently checked by integer Horner and6x6
Bareiss determinants. Earlier repeated/minimum<=7results handle the other
cases. The global completion uses finite computation; remaining endpoint-one
classes and full Q3 stay open. Standalone manuscript integration awaits review.

The remaining [endpoint-one geometry](notes/endpoint-one-geometry.md) now
has an exact fixed-pair real existence test and a unique simple exponent
root c>b. Its middle threshold lies in(2a^2-a-2,2a^2-a-1) at a>=8.
Every ordered endpoint-one zero also requires **b+c<4a^2-2a**; beyond
this sum cutoff a root in(0,1)proves nonintegrality without a parity
hypothesis. These are written unbounded results, with no finite base.
General integer endpoint-one feasibility and full Q3 remain open.

The [endpoint-one growing-gap theorem](notes/endpoint-one-growing-gap.md)
now excludes every integer endpoint-one solution for d=b-a>=1,
**a>=2d^2+20**, by an exact unit-width bracket for its unique real
exponent c>b. Gaps1and2 are excluded already at every a>=8. Combining
the written endpoint-one/two brackets proves nonintegrality for every
parity pattern at **d>=5,a>=2d^2+20**, with no finite base. Broader
consequences retain the earlier endpoint-two finite dependencies.
Any fully distinct integer spectrum at minimum>=8 would now require
**d>=3,a<2d^2+20**, in addition to the existing endpoint-one bounds.
Full Q3 and the remaining endpoint-one region stay open.

The [minimum-eight completion](notes/minimum-eight.md) now certifies
nonintegrality for **every triple with minimum exactly eight**. Written
reductions leave precisely108middle exponents11through118on endpoint one.
The complete fixed-pair certificate brackets each unique real exponent
between consecutive integers, with216independent6x6Bareiss boundary
checks and216exact Sturm counts, covering every integer c>b. Endpoint
two is excluded here by the written maximum cutoff, without its global
finite base. The theorem requires the108pair finite certificate; the
cumulative minimum<=8result also retains the earlier27562triple base.
Full Q3 remains open, with remaining minimum at least nine.

The [endpoint-one spectral gap](notes/endpoint-one-spectral-gap.md) now
proves that, for real exponents at least eight on h_C(1)=0, **one is a
simple smallest positive quotient root and all four other roots exceed
four**. A complete350termpositive identity proves residual-quartic
positivity on the closed interval[0,4], without a finite base. This is
actual spectral simplicity, distinct from exponent-root uniqueness.
The gap does not itself exclude integer spectra; the remaining quartic
must be studied above four. Full Q3 stays open.

The [endpoint-one divisor window](notes/endpoint-one-divisor-window.md)
answers the constant-term and upper-bound questions: F(0)=rs(p+s)>0,
and weighted principal interlacing gives the second smallest nonzero
quotient root strictly below c for every ordered positive real triple.
On endpoint one at minimum>=8, the smallest quartic root lies in (4,c).
An integer spectrum therefore requires a divisor of rs(p+s) in [5,c-1]
to vanish in F. Exact checks on the three established controls find none.
This is a finite test per fixed triple, not a global surface decision.

The [minimum-dependent endpoint-one theorem](notes/endpoint-one-minimum-root.md)
strengthens the window to **a<mu_1<c**, and proves root one simple with
all four other roots above a, for every real 4<=a<=b<=c on endpoint one.
A written comparison proves b+c>=2a²-2a+1, with equality exactly at the
repeated boundary; determinant sign and interlacing then count exactly
two quotient eigenvalues below a, zero and one. This uses no finite base
or minimum-eight positivity certificate. Integer candidates now lie in
[a+1,c-1]; three established controls leave252nonzero evaluations.
The unbounded surface and full Q3 remain open.

The [pair-sum upper bound](notes/endpoint-one-pair-sum-window.md) now gives
lambda_3<a+b for every ordered positive real triple, by interlacing with
a four-support principal block. On endpoint one at real minimum>=4,
the smallest quartic root therefore lies in **(a,min(c,a+b))**.
Hypothetical integer spectra require a divisor of rs(p+s) in that window.
The three established controls leave only23candidates, all nonzero under
exact evaluation. No finite base or new nonintegrality family is claimed;
the unbounded surface and full Q3 remain open.

The [constant-divisibility analysis](notes/endpoint-one-constant-divisibility.md)
proves **12 divides F(0)** on every integer endpoint-one triple, and the
greatest common divisor of the constants over the full surface at
minimum>=4 is exactly 12. The known repeated boundary also gives infinitely
many divisors inside the smallest-root window that are not spectral roots.
Thus the splitting problem must use F(d)=0 alongside divisibility and size.
These are written unbounded results; the fully distinct region remains open.

The [root-congruence analysis](notes/endpoint-one-root-congruences.md)
shows that window candidates can give either sign: F(21)>0 at (20,20,741).
Integer roots must additionally satisfy N/d=D modulo d and three congruences
from exact evaluations at a,b,c. Together these necessary conditions leave
one of the existing 23 candidates, which still fails exact F evaluation.
The fully distinct sign question and global splitting problem remain open.

The [middle-exponent location theorem](notes/endpoint-one-middle-root.md)
refines the smallest-root window on real endpoint one at minimum>=4.
If c+a>b(b+2), the smallest residual root exceeds b; if c+a<b(b+2),
exactly one residual root lies below b. Integer candidates therefore lie
in (b,min(c,a+b)) or (a,b), respectively. At equality the
[equality theorem](notes/endpoint-one-equality-root.md) identifies b as
the simple smallest residual root; integer feasibility and splitting
of the remaining cubic stay open. The [equality curve analysis](notes/endpoint-one-equality-curve.md)
gives geometric genus ten and integer-point finiteness, without a point list.
The [quotient descent check](notes/endpoint-one-equality-quotient.md) rules out
extra rational involutions on its known genus-three quotient; other low-genus
maps and Jacobian ranks remain unclassified.
The proof
uses determinant sign and principal interlacing, with no finite base.

The [higher-coefficient analysis](notes/endpoint-one-root-hierarchy.md)
adds necessary tests modulo d^3 and d^4; the quadratic and exponent tests
reject all23existing candidates. The earlier infinite boundary candidate
d=3a/2 fails the linear test uniformly. Both E sign regimes and E=0 points
occur at arbitrarily large real minima, with no integer-feasibility claim.
The equality subfamily has an explicit Diophantine equation G(a,b)=0.
These results do not establish sufficiency or close full Q3.

A standalone [middle-diagonal inertia restriction](notes/endpoint-two-middle-inertia.md)
narrows the endpoint-two problem without further congruence lifting. For
`4<=a<b<c`, `(b-2)(a+b+c-2)<=2ac` supplies a positive quotient root in `(0,2)`.
This proves nonintegrality for all-even triples and the mixed patterns
`(1,3,2)/(3,3,0)` modulo four. The consolidated manuscript is unchanged.

The [full endpoint-two determinant](notes/endpoint-two-middle-tail.md) now
excludes every `b>=2a-2` for ordered `4<=a<=b<=c`: its endpoint polynomial
is strictly positive and gives a root in `(0,2)`. Every endpoint-two zero
therefore requires `b<2a-2`. Nonintegrality follows in the same three parity
classes; the other endpoint-one cases remain open.

The [sharper maximum tail](notes/endpoint-two-maximum-tail.md) now proves
`c>=3a-4 => h_C(2)>0` for ordered minimum at least four. Every endpoint-two
zero therefore requires both `b<2a-2` and `c<3a-4`, replacing the earlier
maximum bound `c<7a-16+40/(a+2)`. Full Q3 remains open.

The [endpoint-two root geometry](notes/endpoint-two-surface-geometry.md)
now gives an exact existence test and a unique real c>b solution for
each fixed a>=8,b>=a that passes it. The middle threshold is a unique
cubic root beta(a)<2a-2. Minimum eight has no fully distinct endpoint-two
solutions; at (a,b)=(20,22) the sole real c lies between32and33, excluding
every integer endpoint-two solution for that pair.

The [gap-two integer-feasibility result](notes/endpoint-two-gap-two.md)
extends this to every ordered `(a,a+2,c)` with integer a>=8,c>a+2:
endpoint two never occurs. A uniform unit-width real-root bracket proves
the infinite tail a>=20; a complete twelve-pair exact computation covers
8<=a<=19. Nonintegrality follows in the all-even and stated mixed classes;
other endpoint-one cases and arbitrary middle gaps remain open.

The [growing-gap integer exclusion](notes/endpoint-two-growing-gap.md) now
allows an unbounded middle difference d: for real `d>=5,a>=2d^2+20,b=a+d`,
the unique endpoint-two solution c>b lies in `(2a+d-11,2a+d-10)`.
For integer exponents this excludes endpoint two throughout the stated
family. The complete domain has a written coefficient-positivity proof,
with no finite base required. Nonintegrality follows in the all-even and
stated mixed classes; general endpoint-two feasibility remains open.

The [small-middle-gap theorem](notes/endpoint-two-small-middle-gaps.md) now
excludes endpoint two for every integer `(a,a+d,c)` with a>=8,1<=d<=4,c>a+d.
Gaps1,3,4 use written infinite tails and a complete76pair finite base;
gap2 uses its preserved theorem. With the growing-gap result, every fully
distinct integer endpoint-two zero at minimum>=8 must have **d=b-a>=5 and
a<2d^2+20**. General feasibility in this remaining region stays open.

The [nine-fourths maximum bound](notes/endpoint-two-sharp-maximum.md)
now improves the whole endpoint-two region at minimum>=8 to **c<9a/4-8**,
strictly below the preceding3a-4bound. Two nonnegative square expressions
and a complete84term positive residual prove h_C(2)>0 beyond this cutoff
throughout the unbounded real domain, with no finite base or exponent scan.
The remaining fully distinct integer region requires d>=5,a<2d^2+20,
b<beta(a),b<c<9a/4-8. General integer feasibility stays open.

## First results

We prove nonintegrality for every squarefree integer with at least three
distinct prime factors and for every exponent vector that is a permutation
of `(1,1,k)`, `k >= 1`. This completes the squarefree composite classification:
the integral case is exactly two prime factors, including the edgeless graph.
Read [the proofs and exact verification scope](notes/integrality-obstructions.md).
Reza's [further infinite family](notes/repeated-exponent-family.md) covers
`(a,a,(a-1)(2a-1))`, `a >= 2`, including `(2,2,3)`. Its antisymmetric block
has integer eigenvalues; a symmetric cubic proves nonintegrality.
We now prove nonintegrality for **every `(a,a,b)`, a,b >= 1**:
read [the complete repeated-exponent proof](notes/repeated-exponent-completion.md).
We also prove nonintegrality for **every `(1,b,c)`, b,c >= 1** using the
general six-support complement quotient:
[read the proof and exact diagnostic](notes/one-unit-exponent.md).
The same quotient now settles **every `(2,b,c)`, b,c >= 1**:
[read the minimum-two proof](notes/minimum-two.md). Thus every triple
with minimum exponent at most2 is nonintegral.
We now also settle **every `(3,b,c)`, b,c >= 1**, and prove the uniform
cutoff **`c >= 4a^2 - 2a`** for ordered `2 <= a <= b <= c`:
[read the cutoff and minimum-three proof](notes/distinct-tail.md).
Thus every triple with minimum exponent at most3 is nonintegral.
The subsequently [requested finite-region run](notes/open-region-diagnostic.md)
exhausts all27,562remaining triples at minimum4,5,6,7. Every discriminant
is independently verified nonsquare by integer Sylvester determinants.
Together with the written cutoff, **every triple with minimum exponent
at most7 is now certified nonintegral**; this extension uses the complete
finite computation.
An inertia argument now also settles **every triple whose maximum minus
minimum is at most3**, and **every `(a,a+3,a+4)`, a>=1**:
[read the low-eigenvalue proof](notes/low-spectrum.md).
It counts two complement eigenvalues below3 and excludes the integers
1 and2 with positive polynomial factors and four complete modular certificates.
For **every `4<=a<=b<=c`**, a uniform comparison now places a positive
complement quotient eigenvalue in `(0,3)`. If
**`(a-2)(a+b+c-2)>2bc`**, a root lies in `(2,3)`, proving nonintegrality.
In particular, **minimum exponent `a>=3r+8`, with span `r=c-a`, suffices**:
[read the uniform comparison and balanced-region proof](notes/mixed-inertia.md).
This written argument allows unbounded spans and does not enlarge any scan.
Arithmetic arguments now also settle **every triple with gcd at least3**,
**every all-odd triple**, and explicit common-residue classes, including
**common residues1,3,4 modulo5**:
[read the divisibility and congruence proofs](notes/arithmetic-obstructions.md).
These results allow arbitrarily large exponent ratios and differences.
Scaling now also settles **every triple whose exponents are all congruent
to two modulo four**, and hence **every triple with equal 2-adic valuations**:
[read the parity and divisibility contradiction](notes/even-exponent-congruence.md).
This includes gcd-two triples inside the remaining even region.
Reza's requested endpoint diagnostic now has a complete independent
certificate for **all66pairs `4<=a<b<=15`, with every integer `c>b`**.
Neither endpoint vanishes. With the low-root theorem and earlier cases,
**every triple whose second-smallest exponent is at most15 is nonintegral**:
[read the corrected diagnostic and exact scope](notes/endpoint-surfaces-diagnostic.md).
An integer complement root at two now forces the linear bound
**`c<7a-16+40/(a+2)`** for ordered `4<=a<=b<=c`. Every all-even triple
beyond this bound is nonintegral; **`c>=7a-12` suffices at minimum>=8**:
[read the endpoint reduction and divisor constraints](notes/endpoint-reduction.md).
The remaining triples lie within `8 <= a < b < c < 4a^2 - 2a`, outside
these families and the general inertia criterion;
the complete endpoint certificate additionally requires `b>=16`.
The full characterization remains open.
The root distributions and low-root theorem now also settle **every
permutation of (3,0,0) modulo four**, an entire one-odd-exponent class.
For mixed residue patterns **(1,3,2)** and **(3,3,0) modulo four**, integer
spectra require the same linear maximum bound as the all-even region:
**`M<7m-16+40/(m+2)`**, where m and M are the minimum and maximum.
[Read the proof and independent exact checks](notes/mixed-endpoint-roots.md).
Endpoint congruences also settle **all residue triples (2,2,2) and
permutations of (1,2,2) modulo three**:
[read the proof, full parity table and covering limitation](notes/endpoint-residues.md).
A stronger divisibility argument also settles **six mixed-parity exponent
classes modulo eight**, without bounds on sizes or ratios:
[read the three-odd-root proof](notes/mixed-parity-congruence.md).
The shifted quintic and its derivative now settle **every permutation
of (3,3,2) modulo four**, including odd exponents equal modulo eight:
[read the uniform root-distribution proof](notes/odd-root-distribution.md).
For exponent residue roles **(1,3,2) modulo four**, one main theorem now
collects the necessary conditions: **`a+c=b(b+2)mod128`**,
**`b=11or15mod16`**, and the stated binary-cubic parity condition.
For minimum m>=4, it also requires **`h_C(2)=0`** and
**`M<7m-16+40/(m+2)`**, where M is the maximum exponent.
The earlier sum congruences follow from these arithmetic conditions.
[Read the consolidated statement and proof guide](notes/manuscript-consolidation.md).
Theorem 13.5 combines all the mixed-parity exclusions and restrictions,
with one worked example in the main text. Theorem 14.1 combines the endpoint
reductions. The complete case calculations are grouped in Appendix B,
and the endpoint proofs in Appendix C. Appendix A gives grouped verification
scopes; the full per-checker catalogue remains in the optional detailed build.
Earlier notes and exact certificates remain available in the navigation below.

## Start here

| What you want | Where to go |
| --- | --- |
| Understand the first task and current status | [Research plan](RESEARCH-PLAN.md) |
| Read the consolidated working manuscript | [PDF](paper/paper.pdf) · [LaTeX source](paper/paper.tex) · [Build and section guide](paper/README.md) |
| Read the complete repeated-exponent theorem | [All (a,a,b) proof](notes/repeated-exponent-completion.md) · [Exact certificate](results/repeated-exponent-completion.json) |
| Read the unit-exponent theorem and unequal-triple diagnostic | [All (1,b,c) proof](notes/one-unit-exponent.md) · [Requested 35-case output](results/fully-distinct-diagnostic.txt) |
| Read the minimum-two theorem | [All (2,b,c) proof](notes/minimum-two.md) · [Exact certificate](results/minimum-two.json) |
| Read the uniform cutoff and minimum-three theorem | [Proof](notes/distinct-tail.md) · [Complete 325-case certificate](results/distinct-tail.json) |
| Read the inertia criterion and bounded-gap families | [Proof](notes/low-spectrum.md) · [Exact modular certificate](results/low-spectrum.json) |
| Read the uniform low-root bound and growing balanced region | [Proof](notes/mixed-inertia.md) · [Exact checks](results/mixed-inertia.json) |
| Read the common-divisor, all-odd and congruence-class theorems | [Proof](notes/arithmetic-obstructions.md) · [Exact checks](results/arithmetic-obstructions.json) |
| Read the all-two-modulo-four and common-valuation theorems | [Proof](notes/even-exponent-congruence.md) · [Exact checks](results/even-exponent-congruence.json) |
| Read the six mixed-parity modulo-eight classes | [Proof](notes/mixed-parity-congruence.md) · [Exact checks](results/mixed-parity-congruence.json) |
| Read the uniform (3,3,2) modulo-four family | [Proof](notes/odd-root-distribution.md) · [Exact checks](results/odd-root-distribution.json) |
| Read the linear endpoint-two bound and all-even tail | [Proof](notes/endpoint-reduction.md) · [Exact checks](results/endpoint-reduction.json) |
| Read the modulo-three endpoint classes and complete parity table | [Proof and covering limitation](notes/endpoint-residues.md) · [Exact residue tables](results/endpoint-residues.json) |
| Understand finite endpoint tests inside the geometric restrictions | [Scope and explicit constructions](notes/endpoint-congruence-scope.md) · [Exact identities](results/endpoint-congruence-scope.json) |
| Read Reza's requested finite-region run and minimum-through-seven result | [Report and proof](notes/open-region-diagnostic.md) · [Complete CSV](results/open-region-discriminants.csv) · [Independent verification](results/open-region-certificate-check.json) |
| Read the source preprint and original Q3 | [Zenodo DOI10.5281/zenodo.23134979](https://doi.org/10.5281/zenodo.23134979) |
| Read the requested (a,a,b) diagnostic and fixed-a theorem | [Exact diagnostic and proof](notes/aa-b-diagnostic.md) |
| Read the sharper cutoff and complete a=5,6 families | [Second linear cutoff](notes/second-linear-cutoff.md) |
| Read the fixed-index divisor criterion and current cutoff | [Factor-index reduction](notes/factor-index-reduction.md) |
| Read the first checked contributions | [Nonintegrality proofs](notes/integrality-obstructions.md) |
| Read Reza's extension of the (2,2,3) case | [Repeated-exponent family](notes/repeated-exponent-family.md) |
| Read the requested endpoint diagnostic and exact scope | [Report](notes/endpoint-surfaces-diagnostic.md) · [Corrected output](results/endpoint-surfaces-corrected.txt) · [Complete certificate](results/endpoint-surfaces-verification.json) |
| Read the modular endpoint script review and corrected candidate logic | [Review](notes/modular-endpoints-review.md) · [Full root sets](results/modular-endpoints.json) · [Independent verification](results/modular-endpoints-verification.json) |
| Read the higher-modulus diagnostic and its period-eight limit | [Review](notes/higher-2adic-moduli-review.md) · [Original output](results/higher-2adic-moduli-original.txt) · [Independent verification](results/higher-2adic-moduli-verification.json) |
| Read the conditional derivative thresholds and new sum-congruence family | [Proof and review](notes/higher-derivatives-review.md) · [Requested output](results/higher-derivatives-original.txt) · [Independent verification](results/higher-derivatives-verification.json) |
| Read the stronger weighted-sum condition for the remaining sum class | [Proof](notes/odd-root-lift.md) · [Exact certificate](results/odd-root-lift.json) |
| Read the clustered-root value, derivative and third-shift conditions | [Proof](notes/clustered-odd-roots.md) · [Exact certificate](results/clustered-odd-roots.json) |
| Discuss a conjecture or share a checked argument | [Project issues](https://github.com/the-omega-institute/ideal-intersection-laplacian/issues) |
| Review proposed additions | [Pull requests](https://github.com/the-omega-institute/ideal-intersection-laplacian/pulls) |
| Read the previous joint paper | [Binary subspace orthogonality project](https://github.com/the-omega-institute/binary-subspace-orthogonality) |

## Current status

We have agreed to start with Q3, the integrality question proposed by Reza.
The graph convention has been reviewed. The working manuscript consolidates
the squarefree classification, the `(1,1,k)` family, Reza's boundary family,
the successive linear cutoffs, and the complete fixed-exponent families.
Reza's diagnostic request now has exact output for all 90 requested pairs.
The repeated-exponent family is now completely settled: every `(a,a,b)`
with positive exponents is nonintegral. For square antisymmetric
discriminant, the boundary and factor indices 1,2,3 have complete proofs
and finite modular certificates. Every later index forces
`b <= (a-5)(2a-5)/(4a+5)`, strictly below a uniform cubic sign threshold;
a root lies between the consecutive integers `2ab-1` and `2ab`.
The earlier cutoffs and fixed-a checks remain as intermediate results.
The complement quotient now also settles every triple with a unit exponent.
Reza has hand-checked the repeated-exponent completion identities and gap.
Two positive-coefficient expansions and a single rational interval now
settle every triple with an exponent of two, as well.
The uniform endpoint cutoff reduces the remaining pairs for any fixed minimum
exponent to a finite set. For minimum3, the derived 325 pairs have complete
integer sign certificates; positive endpoint expansions and one rational
exception close the whole family. No arbitrary parameter cutoff is used.
The Schur-complement inertia criterion now counts two low eigenvalues
without relying on a sign change. Four complete bounded-gap families use
38 root-free modular residues to exclude integer endpoints; no minimum-exponent
scan is needed. In particular every triple with exponent span at most3 is settled.
Reza's requested finite range at minima4through7 is now completely certified:
all27,562discriminants pass independent integer determinant reconstruction
and strict square brackets. The original and complement quotient signs
are kept separate. With the cutoff this certifies every minimum-entry<=7 triple.
The mixed-sign Schur complement now has a uniform positive root below3
for every minimum exponent at least4. The lower endpoint inequality
`(a-2)(a+b+c-2)>2bc` places a root in `(2,3)` and settles a growing
balanced region, including every minimum `a>=3(c-a)+8`.
In the remaining region `8 <= a < b < c < 4a^2 - 2a`, any integral graph
must satisfy `h_C(1)h_C(2)=0`. These two endpoint-zero surfaces are the
next mathematical question; the necessary condition does not classify them.
The new arithmetic theorems restrict the remaining triples to gcd1or2,
at least one even exponent, and residues outside the proved congruence classes.
The endpoint-two surface now has the strict linear bound
`c<7a-16+40/(a+2)`. Every remaining all-even triple has gcd2 and obeys
this bound. The two endpoint equations also give exact divisor candidates
for a fixed pair `(a,b)`; the candidate still has to satisfy the equation.
Every possible integral triple also has unequal 2-adic valuations. In
the remaining all-even region, at least one exponent is divisible by four
and at least one is congruent to two modulo four.
The requested endpoint certificate excludes every middle exponent through15;
remaining triples have `b>=16`. The absence of roots in the66pair domain
does not establish a global absence of integer points on either surface.
nonsquarefree vectors with more than three prime factors also remain open.

The source preprint is public on
[Zenodo](https://doi.org/10.5281/zenodo.23134979). Its general spectral
reduction and equal-exponent results motivate this follow-on work.
We link the source PDF; private correspondence remains outside this repository.

## How we work

We use short cycles of conjecture, proof or counterexample, and independent
verification. Each contribution states its assumptions and separates written
proofs, exact finite computations and Lean verification.

The initial work is to fix the graph convention and spectral reduction,
then develop the integrality argument. Vertex connectivity may become a
companion result if it fits naturally; other invariants and unequal-exponent
matrix questions remain later directions.

Use one focused pull request for each checked contribution, with a readable
explanation and reproducible evidence where relevant. Existing collaborator
edits are preserved. See [rights and provenance](RIGHTS.md).
