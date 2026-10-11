# Every repeated-exponent triple is nonintegral

**Theorem.** For distinct primes p,q,r and every a,b≥1, the ideal
intersection graph of `Z_(p^a q^a r^b)` is not Laplacian integral.
Permuting the three prime factors gives the same conclusion whenever at
least two exponents agree.

This closes the repeated-exponent part of Q3. Three pairwise distinct
exponents and nonsquarefree integers with more than three prime factors
remain open. The result is a written infinite-family proof, supported by
exact identities and finite modular certificates; no Lean is claimed.

## The two blocks and the already settled factor levels

Use the [graph, blocks and lifting definitions](../paper/sections/graph.tex).
The antisymmetric block has discriminant

$$D=(a+1)^2b^2+2a(3a+1)b+a^2.$$

If D is nonsquare, its irrational eigenvalues persist after the integer
universal-vertex shift a²b−1. For a=1 the quadratic bound in the
[divisor proof](aa-b-diagnostic.md) would force b≤0 if D were square,
so every positive b is settled.

For a≥2 and square D, put h=a+1, M=a³(2a+1), C=(a−1)(2a−1).
The same proof gives d≤e, de=M, d≡e≡1 mod h and
d+e=h²b+a(3a+1). Write d=1+hj. Index j=0 is
[Reza's boundary family](repeated-exponent-family.md); j=1 is settled
by the complete [divisor-of-24 argument](second-linear-cutoff.md), and
j=2 by the complete [divisor-of-108 argument](factor-index-reduction.md).
We settle j=3 next and then handle every j≥4 at once.

## Complete third-index certificate

The proved fixed-index criterion says d divides K_j=(j+1)³(j+2).
For j=3, K_3=320. The divisors with d=3a+4 and a≥2 are exactly
10,16,40,64,160. Setting e=M/d and v=(e−1)/(a+1) gives:

| d | a | e | v | b=C−3v | Outcome |
| --- | --- | --- | --- | --- | --- |
| 10 | 2 | 4 | 1 | 0 | d>e; not the smaller factor |
| 16 | 4 | 36 | 7 | 0 | b is not positive |
| 40 | 12 | 1080 | 83 | 4 | Cubic root-free modulo 5 |
| 64 | 20 | 5125 | 244 | 9 | Cubic root-free modulo 7 |
| 160 | 52 | 92274 | 1741 | 30 | Cubic root-free modulo 7 |

The three cubics and their values at every residue of the indicated prime are:

| (a,b) | f(x) | Prime | Residue values |
| --- | --- | --- | --- |
| (12,4) | x³−568x²+100032x−5248512 | 5 | 3,3,3,4,2 |
| (20,9) | x³−1769x²+992820x−174744000 | 7 | 3,2,4,1,6,4,1 |
| (52,30) | x³−13394x²+57771168x−80229951360 | 7 | 1,6,4,1,3,2,4 |

A monic cubic with no root modulo a prime is irreducible over Q.
These cubics have real nonzero roots, and their noninteger roots lift
to graph eigenvalues. Thus all j=3 cases are settled. This finite set is
complete by the divisor criterion, without any upper bound on a.

## Uniform sign obstruction for the remaining indices

For every a,b the symmetric cubic satisfies the exact identities

$$f_{a,b}(2ab)=2a^2b^2,$$

$$f_{a,b}(2ab-1)=-(a+b+1)
\bigl(a^3+2a^2+2a+1-a(2a+1)b\bigr).$$

Consequently if

$$b<L(a)=\frac{a^3+2a^2+2a+1}{a(2a+1)},$$

then f has opposite signs at the consecutive integers 2ab−1 and 2ab.
The intermediate value theorem gives a real root strictly between them,
which is noninteger and nonzero. Strict inequality is essential.

Now any remaining square-discriminant pair has j≥4, so
d≥Q=4a+5. Since e≥d≥Q,

$$\frac MQ+Q-(d+e)=(d-Q)\left(\frac eQ-1\right)\geq0.$$

It follows that

$$b\leq B_4(a)=\frac{M/Q+Q-a(3a+1)}{(a+1)^2}
=\frac{(a-5)(2a-5)}{4a+5}.$$

For every a≥2 this bound is strictly below the sign threshold:

$$L(a)-B_4(a)=
\frac{41a^3-17a^2-11a+5}{a(2a+1)(4a+5)}>0.$$

Indeed, writing z=a−2≥0, the numerator is
41z³+229z²+413z+243. Therefore every remaining pair satisfies
b≤B_4(a)<L(a) and has the trapped noninteger cubic root.
Together with a=1, nonsquare D and indices j=0,1,2,3, this exhausts
all positive a,b and proves the theorem.

## Exact validation

[The checker](../scripts/check_repeated_exponent_completion.py) reconstructs
the general cubic directly from the 4×4 quotient, verifies both endpoint
identities and the cutoff/gap identities symbolically, and exhausts all
divisors of320. It checks the three modular lists by both polynomial
evaluation and integer Horner arithmetic. It also reproduces the earlier
j=1 and j=2 finite certificates, so all exceptional factor levels used in
the completion proof are covered together. The j=0 boundary is the existing
written proof and its separate checker.

[Saved results](../results/repeated-exponent-completion.json) record source
hashes and the exact scope. There is no arbitrary parameter scan,
floating-point eigenvalue evidence or Lean run.
