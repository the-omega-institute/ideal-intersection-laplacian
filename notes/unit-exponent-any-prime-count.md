# A unit exponent with any number of prime factors

**Theorem.** Let n be a product of t>=3 distinct prime powers with
positive integer exponents. If at least one exponent is one, the ideal
intersection graph of Z_n has a Laplacian eigenvalue in (V-1,V), where
V is its number of vertices. In particular it is Laplacian nonintegral.
There is no restriction on the other exponents or on t.

This extends the established three-prime unit-exponent result to all
higher-prime vectors with a unit exponent. The proof below uses an exact
Rayleigh quotient on the complement graph and needs no finite base.

## Support classes and the complement

Use the graph definition in [the manuscript](../paper/sections/graph.tex).
Permute the prime factors so that the final exponent is one, and write
the others as k_1,...,k_r with r=t-1>=2. Put

```text
A = product_i k_i,
B = product_i (k_i+1) - 1 - A.
```

Thus B is the sum of the weights of all nonempty proper subsets of the
first r coordinates; B>0 because r>=2. Remove the A-1 full-support
universal vertices from the ideal intersection graph and call the
remaining graph H. Its complement F has an independent support class
of weight product_{i in S} k_i for each nonempty proper support S.
Distinct classes are completely adjacent precisely when their supports
are disjoint. Here

```text
N = |H| = A+2B+1,
V = |G_n| = N+(A-1) = 2A+2B.
```

The support consisting only of the final coordinate has weight one;
let its unique vertex be z. The full support on the first r coordinates
has A vertices. Each of them is adjacent in F only to z, so these A
vertices are leaves. The other 2B vertices consist of two collections,
each of total weight B: nonempty proper old supports S, and supports
S union {t} for those same S. The vertex z is adjacent to every vertex
of the first collection and to none of the second.

The graph F is connected. Its singleton support classes form a connected
complete multipartite subgraph, and every nonempty proper support has a
singleton outside it to which it is completely adjacent.

## An exact Rayleigh quotient below one

Define a function f on the vertices of F by

```text
f = 2B on the A leaves,
f = 0 at z,
f = -A on the other 2B vertices.
```

Then sum f = A(2B)+(2B)(-A)=0 and f is nonzero. Every edge within the
last collection contributes zero to the Laplacian energy. The A edges
from z to its leaves contribute A(2B)^2, and its B other incident edges
contribute B A^2. Therefore

```text
f^T L(F) f = A B(4B+A),
f^T f     = 2 A B(2B+A),
R(f)      = (4B+A)/(4B+2A) < 1.
```

Since F is connected, its smallest positive Laplacian eigenvalue mu
is strictly positive. The variational characterization on the subspace
orthogonal to the constant vector gives

```text
0 < mu <= (4B+A)/(4B+2A) < 1.
```

The complement identity L(H)+L(F)=N I-J shows that the same eigenvector
has H-eigenvalue N-mu. This is nonzero because N>1 and mu<1. Extending
it by zero on the A-1 universal vertices gives a G_n-eigenvalue
N-mu+(A-1)=V-mu, strictly between the consecutive integers V-1 and V.
This proves the theorem, including squarefree vectors and the small
three-prime unit cases, without an exception.

The variational argument can also be applied on the support-constant
subspace: the trial function is support-constant and orthogonal to the
weighted constant vector, and the connected quotient has a simple zero.
Thus a nonzero quotient root below one is available as well.

## Boundary and verification

The hypothesis t>=3 is necessary. With two prime factors and a unit
exponent, B=0 and F is the star K_(1,A), whose spectrum is integral.
The original ideal graph is also integral: reflection and the universal
join give only integer eigenvalues. The trial vector above correctly
degenerates at B=0 and is not used in this case.

The [exact checker](../scripts/check_unit_exponent_any_prime_count.py)
constructs support weights and adjacency directly for a fixed set of
three-, four- and five-prime controls, verifies connectivity, the weighted
zero sum, both energy identities and the strict quotient bound, and
independently checks two small full graphs. Its controls validate the
implementation; the all-input theorem follows from the written counting
and variational proof. No exponent scan, floating eigenvalues or Lean
verification is used.

This settles the unit-exponent branch for arbitrary prime count.
Higher-prime nonsquarefree vectors with every exponent at least two
remain open; no full Q3 classification or submission decision follows.
