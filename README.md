# Laplacian integrality of ideal intersection graphs

Public workspace for the follow-on collaboration between **Haobo Ma,
Reza Nikandish and Wenlin Zhang**, studying ideal intersection graphs of
`Z_n` and their Laplacian spectra.

Our first question is the **Laplacian integrality characterization**:
which graphs in this family have only integer Laplacian eigenvalues?
This is a new research track; no complete characterization is claimed here.

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
An integer complement root at two now forces the linear bound
**`c<7a-16+40/(a+2)`** for ordered `4<=a<=b<=c`. Every all-even triple
beyond this bound is nonintegral; **`c>=7a-12` suffices at minimum>=8**:
[read the endpoint reduction and divisor constraints](notes/endpoint-reduction.md).
The remaining triples lie within `8 <= a < b < c < 4a^2 - 2a`, outside
these families and the general inertia criterion;
the full characterization remains open.

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
| Read the linear endpoint-two bound and all-even tail | [Proof](notes/endpoint-reduction.md) · [Exact checks](results/endpoint-reduction.json) |
| Read Reza's requested finite-region run and minimum-through-seven result | [Report and proof](notes/open-region-diagnostic.md) · [Complete CSV](results/open-region-discriminants.csv) · [Independent verification](results/open-region-certificate-check.json) |
| Read the source preprint and original Q3 | [Zenodo DOI10.5281/zenodo.23134979](https://doi.org/10.5281/zenodo.23134979) |
| Read the requested (a,a,b) diagnostic and fixed-a theorem | [Exact diagnostic and proof](notes/aa-b-diagnostic.md) |
| Read the sharper cutoff and complete a=5,6 families | [Second linear cutoff](notes/second-linear-cutoff.md) |
| Read the fixed-index divisor criterion and current cutoff | [Factor-index reduction](notes/factor-index-reduction.md) |
| Read the first checked contributions | [Nonintegrality proofs](notes/integrality-obstructions.md) |
| Read Reza's extension of the (2,2,3) case | [Repeated-exponent family](notes/repeated-exponent-family.md) |
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
