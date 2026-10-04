# Every three-prime graph with a unit exponent is nonintegral

**Theorem.** For distinct primes p,q,r and every b,c≥1, the ideal
intersection graph of `Z_(p q^b r^c)` is not Laplacian integral.
The prime factors may be permuted. This includes all fully distinct
triples `(1,b,c)` with `2 <= b < c`, without any bound on b or c.

The proof uses the complement of the six-support quotient and does not
assume equal exponents. Fully distinct triples whose exponents are all
at least2, and nonsquarefree vectors with more than three prime factors,
remain open. No Lean verification is claimed.

## General six-support quotient

For arbitrary a,b,c≥1, remove the u=abc−1 full-support universal vertices.
The remaining graph H has six support classes, ordered as
1,2,3,12,13,23, with weights w=(a,b,c,ab,ac,bc) and

$$N=a+b+c+ab+ac+bc.$$

The complement of H connects precisely the disjoint support classes.
Its cell-constant Laplacian quotient is

$$C=\begin{pmatrix}
b+c+bc&-b&-c&0&0&-bc\\
-a&a+c+ac&-c&0&-ac&0\\
-a&-b&a+b+ab&-ab&0&0\\
0&0&-c&c&0&0\\
0&-b&0&0&b&0\\
-a&0&0&0&0&a
\end{pmatrix}.$$

For example, a vertex in support1 has b,c,bc complement neighbors in
supports2,3,23. A support12 vertex has c complement neighbors, all in3.
Multiplication by diag(w) makes C symmetric; hence C has real eigenvalues.
It has zero row sums and weighted column sums w^T C=0.

Writing B for the quotient of H, the graph-complement identity is

$$B+C=NI-\mathbf1w^T.$$

If Cv=μv with μ≠0, then w^T v=0, so Bv=(N−μ)v. Provided N−μ≠0,
the [universal-vertex lift](../paper/sections/graph.tex) gives a graph
eigenvalue N+u−μ. Thus a complement root μ strictly between0 and1
produces a graph eigenvalue strictly between V−1 and V, where
V=N+u is the integer vertex count.

## Two determinant values prove the infinite family

Let det(xI−C)=x h_(a,b,c)(x), where h is monic of degree5.
Direct determinant expansion gives the polynomial identities

$$h_{a,b,c}(0)=-abc(a+b+c)N<0,$$

$$h_{a,b,c}(a)=-a^2b^2c^2(a^2+2a-b-c).$$

In particular, at a=1,

$$h_{1,b,c}(1)=b^2c^2(b+c-3).$$

When b+c>3, the signs at0 and1 are opposite, so the intermediate
value theorem gives μ∈(0,1). The lifting argument gives a noninteger
Laplacian eigenvalue in (V−1,V). When b+c≤3, the only positive pairs
are (1,1),(1,2),(2,1); the resulting vectors are permutations of
(1,1,k), k=1,2, already settled by the quadratic obstruction.
This proves the theorem for all b,c≥1.

## Requested diagnostic and its exact scope

Reza requested a run of `scripts/check_fully_distinct.py` in his public
PR3 comment5978978582. At the remote check, that file was absent from
all three branches. We keep its name available for his source and provide
an independent [six-support checker](../scripts/check_six_support_quotient.py).
Its range is explicitly `1 <= a < b < c <= 6`, exactly20triples; it is
not represented as output from the unavailable script.

All20 degree-five factors have an irreducible nonlinear factor over Q.
Most are irreducible quintics, but (2,3,5) has factor degrees1,4 and
(2,4,6) has factor degrees2,3. Therefore irreducibility of the whole
quintic cannot be a uniform obstruction, even on this small range.
The displayed prime field is the first witness among the explicitly
tested primes for a nonlinear rational factor; an absent prime witness
does not overturn the exact rational factorization.

The checker verifies the general quotient/complement identities, both
determinant values, the a=1 endpoint and the reflected quintic identity.
Direct coordinatewise-maximum ideal adjacency independently reproduces
the quotient at (1,2,3) and(2,3,4), using22 and58vertices and312
representative-to-vertex pairs in total. These are finite checks; the
all-b,c conclusion follows from the written endpoint proof.

Read the [saved exact certificate](../results/six-support-quotient.json)
and [full console output](../results/six-support-quotient.txt).

## Source

The motivating Q3 is in R. Nikandish,
*Laplacian Spectrum of the Ideal Intersection Graph of Z_n:
Generalized Joins and a Schur-Weyl Reduction*, Zenodo (2026),
[DOI10.5281/zenodo.23134979](https://doi.org/10.5281/zenodo.23134979).
The public record and PDF match the previously supplied source; the source
already treats the equal-exponent family and develops the general
generalized-join reduction. The complement interval above extends our
nonintegrality argument to triples with a unit exponent and unequal others.
