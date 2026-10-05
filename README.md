# Laplacian integrality of ideal intersection graphs

Public workspace for the follow-on collaboration between **Haobo Ma,
Reza Nikandish and Wenlin Zhang**, studying ideal intersection graphs of
`Z_n` and their Laplacian spectra.

Our first question is the **Laplacian integrality characterization**:
which graphs in this family have only integer Laplacian eigenvalues?
This is a new research track; no complete characterization is claimed here.

Theorem14.2 now includes the global real gap
lambda_3<a+b<a+b+c<=lambda_4, with equality only at(2,2,2).
Corollary14.3 combines the smallest-root divisor window with the strict
coefficient interval N/D<mu_1<N/(D-NR), and puts the three larger
endpoint-one roots above s=a+b+c. The equality
index/simplicity proof is retained, with its redundant gap proof removed;
the E-sign test now refines only the smallest-root window. Exact supporting
sources are pinned to PR9 `4a451ac51055c6d04926967749196f12ac8e49c8`.
Residue additions are paused; residual quartic/globalQ3 remain open.

Proposition13.9 now requires b=104mod169 for an integral equality spectrum
on the negative q=-1mod13 branch with13 dividing b. Its refined anchor
gives Delta=13b²-18b³mod13^(4v_13(b)); every other such class has an odd
discriminant valuation. The positive branch remains locally split.
The full written proof is integrated, with exact identities pinned to
PR9 `eb6b7d37`; the b=104mod169 class and global equality problem remain open.

Proposition13.8 now classifies local equality-cubic splitting at odd p|b,
except the negative branch at p=13. The positive branch q=1modp always
splits by simple-root Hensel lifting; the negative branch q=-1modp splits
exactly when13is a quadratic residue. In particular, the surviving
b=0mod5rows(2,0)/(3,0)pass every five-power splitting test. This is a
written local theorem, not global integer splitting or an integer-point
construction. Each fixed b in5Z_5 also has two unique compatible local
curve points with split cubics; finite five-power curve-and-splitting
tests cannot exclude these rows. Supporting identities are pinned to
PR9 `8b87f9df`.

Proposition13.6 now excludes every permutation of `(1,1,2)` or `(1,4,4)`
modulo five by a full quadratic/cubic splitting obstruction, without size
or endpoint hypotheses. On the equality curve, integer spectra require
one of six initial (a,b) residue pairs, in particular b!=1mod5.
An irreducible cubic with square discriminant modulo five demonstrates
the additional force of the root equation. The complete proof is in the
manuscript; exact supporting sources are pinned to PR9 `7d917aff`.

Proposition13.7 gives a uniform local discriminant obstruction on G=0:
for an odd prime p|b, a²=1modp and 13 a nonresidue imply nonintegrality.
In particular neither7nor11may divide b in an integral equality spectrum.
The identity Delta=13b²modp^(3v_p(b)) excludes the two earlier rows
(1,0),(4,0)mod5, leaving {(2,0),(3,0),(0,2),(3,2)}. Its written proof
needs no finite exponent base. Exact identities and the three specified
prime examples are pinned to PR9 `4878e512`.

The manuscript now completes the endpoint-two nonintegrality alternative.
Theorem14.8 gives a written further-root interval(4,5) at minimum>=40;
the necessary complete8,658-triple base handles fully distinct minima8through39,
with the earlier repeated and minimum<=7 dependencies retained. Corollary14.9
settles every all-even triple and all permutations(1,3,2)/(3,3,0)mod4.
The full middle/maximum-bound proof and all positive coefficient vectors
appear in the manuscript. The closing section presents endpoint one as
the single remaining three-prime spectral problem, with four explicit
reductions. Its equality problem includes G(a,b)=0 as well as an integer
cubic root above a+b and square discriminant; no exhaustive point list
or full Q3 characterization is claimed.

The manuscript now includes the short endpoint-one spectral proof: for
real 4<=a<=b<=c on h_C(1)=0, root one is simple and smallest positive,
all four residual roots exceed a, and their smallest lies below
min(c,a+b). The twelve-term identity is in the main text; the generic
350termresidual positivity is retained as a verification remark.
The quartic constant rs(p+s) is positive, and its smallest integer root
must be a divisor in that window. The other three roots need not be
below c. Proposition 14.6 now integrates the equality spectrum: when
c=b(b+2)-a, b is simple and third smallest, and the other three positive
roots exceed a+b. On endpoint one, the remaining spectral factor is cubic
with all roots above a+b. Other standalone PR9 results await integration.

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
