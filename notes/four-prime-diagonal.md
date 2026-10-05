# Every four-prime diagonal exponent vector is nonintegral

**Theorem.** For four distinct primes and every integer a>=5, the ideal
intersection graph with exponent vector (a,a,a,a) has a noninteger
Laplacian eigenvalue in (V-3,V-2), where V=(a+1)^4-2. More precisely,
the smallest eigenvalue of the repeated-pair operator satisfies
3<kappa_min<4.

Together with the existing [unit-exponent theorem](unit-exponent-any-prime-count.md)
and [pair-two](four-prime-pair-two.md), [pair-three](four-prime-pair-three.md),
and [pair-four](four-prime-pair-four.md) theorems, this settles every
positive four-prime diagonal vector (a,a,a,a). The new a>=5 proof is
unbounded and uses no finite exponent base.

These vectors are outside the [uniform product-tail criterion](repeated-pair-product-tail.md).
The argument instead uses the second coordinate-swap symmetry to reduce
the invariant four-dimensional operator to a scalar and a cubic block.
It retains the established graph convention: nonzero proper ideals of
Z_n are vertices, with adjacency exactly when their intersection is nonzero.

## A second symmetry inside the invariant block

The general repeated-pair construction gives the genuine complement
restriction K_a-I, where K_a=(a+1)E_a tensor E_a+aF_a tensor F_a.
In the order T=empty,{4},{3},{3,4}, its matrix is

```text
K_a = [[(a+1)^3+a, a^2,         a^2,         a^3],
       [a,         (a+1)^2,    a^2,         0  ],
       [a,         a^2,        (a+1)^2,    0  ],
       [a,         0,          0,          a+1]].
```

The two middle coordinates can be exchanged. The antisymmetric vector
(0,1,-1,0) is an eigenvector at 2a+1. The symmetric vectors (x,y,y,z)
form an invariant three-dimensional space with operator

```text
Q_a = [[(a+1)^3+a, 2a^2,         a^3],
       [a,         2a^2+2a+1,    0  ],
       [a,         0,            a+1]].
```

The matrix diag(1,2a,a^2) symmetrizes Q_a, so it is similar to a real
symmetric matrix. This is an invariant restriction inside an already
invariant support space; no graph eigenvalue is inferred merely from a
principal submatrix. Its characteristic polynomial is

```text
p_a(x) = x^3 - (a+1)^2(a+3)x^2
         + (a+1)(2a^4+6a^3+13a^2+11a+3)x
         - (2a+1)^3(a^2+a+1).
```

Thus det(xI-K_a)=(x-(2a+1))*p_a(x).

## Strict lower endpoint three

The three leading principal minors of Q_a-3I are

```text
M_1 = a^3+3a^2+4a-2,
M_2 = 2(a^5+4a^4+5a^3-a^2-6a+2),
M_3 = 2(a^5-2a^4-11a^3-4a^2+14a-4).
```

Diagonal similarity preserves these principal minors, so they are also
the leading minors of the symmetric similar matrix minus 3I. Put a=5+u.
Their complete expansions are

```text
M_1 = u^3+18u^2+109u+218,
M_2 = 2u^5+58u^4+670u^3+3848u^2+10968u+12394,
M_3 = 2u^5+46u^4+398u^3+1562u^2+2548u+932.
```

Every coefficient is positive. For all real a>=5, Sylvester's criterion
therefore makes the symmetric matrix Q_a-3I positive definite.
Every Q_a eigenvalue exceeds three; the remaining K_a eigenvalue
2a+1 exceeds three too. Hence kappa_min(K_a)>3.

## Strict upper endpoint four

Direct evaluation gives

```text
p_a(4) = 12a^4+34a^3-3a^2-63a+27
       = 12u^4+274u^3+2307u^2+8457u+11387 > 0,
```

where again a=5+u, u>=0. Since det(Q_a-4I)=-p_a(4)<0, the real
symmetric similar matrix Q_a-4I has a negative eigenvalue. Consequently
its smallest eigenvalue is below four. Combined with the lower bound,
this proves 3<kappa_min(K_a)<4. Equivalently, p_a(3)=-M_3<0 and
p_a(4)>0 give a root in (3,4).

The paired-support graph vector has weighted sum zero. The complement
reflection and universal-vertex extension established in the tensor
construction send a K_a eigenvalue kappa to V+1-kappa in the original
graph. Thus the smallest restricted eigenvalue supplies the claimed
noninteger graph eigenvalue in (V-3,V-2).

## Coverage relative to the earlier sufficient conditions

At b=c=a, the principal-minor failure margin for the product-tail
criterion is

```text
2a^3+a^2-5a+1 = 2u^3+31u^2+155u+251 > 0.
```

Thus none of the new diagonal family satisfies that criterion. In the
earlier small-exponent Rayleigh criterion, every distinguished exponent
is a, the product of the other exponents is a^3, and their proper-support
weight is 3a^2+3a. Its failure margin is

```text
(a^2-1)(3a^2+3a)-(a-1)-a^3
  = 3a^4+2a^3-3a^2-4a+1
  = 3u^4+62u^3+477u^2+1616u+2031 > 0.
```

For a>=5 there is also no exponent one, two, three or four. This proves
additional coverage relative to the recorded unit, fixed repeated-pair,
small-exponent and product-tail results. It is not a literature-priority
claim or a full four-prime classification.

## Exact verification and next scope

The [checker](../scripts/check_four_prime_diagonal.py) verifies both
invariant embeddings, the complete characteristic factorization, the
weighted symmetry, all three leading-minor identities and four-endpoint
identity, and both failure margins. It checks all 30 coefficients in
the six complete shifted positive expansions. Three specified controls,
a=5,6,11, independently reconstruct all four support embedding columns,
their weighted zero sums, symmetry and complement/universal lifts.
For each control the cubic coefficients are also reconstructed by four
direct 3x3 Bareiss determinant evaluations and polynomial interpolation;
exact Sturm counts check the root in (3,4).

The [certificate](../results/four-prime-diagonal.json) reproduces
byte-for-byte with SymPy 1.14.0 using
`python3 scripts/check_four_prime_diagonal.py`. The checker records the
hash of its reused support-embedding dependency. These are fixed exact
implementation controls; the full infinite family has the written proof
above. No expanded vertex graph, floating eigensolver, exponent-range
scan, historical finite-base rerun or Lean run is used.

The completed three-prime manuscript remains unchanged. The next bounded
spectral question is the unequal double-pair vector (a,a,b,b), a,b>=5,
outside the product-tail criterion, using the same second-swap decomposition.
General repeated-pair and fully unequal four-prime vectors, higher-prime
nonsquarefree Q3 and old orthogonality n=7 remain open.
