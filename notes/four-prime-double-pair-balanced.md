# A balanced region for unequal repeated pairs

**Theorem.** For four distinct primes and positive integer exponents
(a,a,b,b) satisfying a<=b<=2a-6, the ideal intersection graph has a
noninteger Laplacian eigenvalue in (V-3,V-2), where
V=(a+1)^2(b+1)^2-2. Its smallest repeated-pair eigenvalue satisfies
3<kappa_min<4. The hypotheses imply a>=6.

This proves an unbounded two-parameter region, including arbitrarily large
gaps b-a, rather than a list of fixed exponents. The remaining a=b=5
case is covered by the [diagonal theorem](four-prime-diagonal.md).
Neither repeated-pair orientation satisfies the earlier
[product-tail criterion](repeated-pair-product-tail.md) in this region,
and every coordinate fails the [small-exponent criterion](small-exponent-rayleigh.md).
The subsequent [completion](four-prime-double-pair-completion.md) settles
all double pairs. The general four-prime classification remains open.

We use the existing graph convention: nonzero proper ideals of Z_n are
vertices, with adjacency exactly when their intersection is nonzero.

## The general second-swap decomposition

The established antisymmetric space for the first repeated pair gives
the complement operator K-I. Specializing the other two exponents to b
gives, in the order T=empty,{4},{3},{3,4},

```text
K = [[(a+1)(b+1)^2+a, ab,          ab,          ab^2],
     [a,               (a+1)(b+1), ab,          0   ],
     [a,               ab,          (a+1)(b+1), 0   ],
     [a,               0,           0,           a+1]].
```

The middle-coordinate swap splits K into the scalar a+b+1 on
(0,1,-1,0) and the following restriction on vectors (x,y,y,z):

```text
Q = [[(a+1)(b+1)^2+a, 2ab,            ab^2],
     [a,               (2a+1)b+a+1,   0   ],
     [a,               0,             a+1]].
```

The matrix D=diag(1,2b,b^2) symmetrizes Q, so Q is similar to a real
symmetric matrix. These are genuine invariant spaces. The support
embedding, weighted zero sum and complement/universal-vertex transfer
remain those of the [general tensor construction](four-prime-pair-three.md).
In particular a K eigenvalue kappa lifts to V+1-kappa in the graph.

Put p(x)=det(xI-Q). The generic factorization is
det(xI-K)=(x-(a+b+1))*p(x). We bound its smallest root through three
principal minors and one endpoint value.

## The lower endpoint three

The first two leading minors of Q-3I are

```text
M_1 = (a+1)(b+1)^2+a-3,
M_2 = M_1*((2a+1)b+a-2)-2a^2b.
```

They are positive for a>=6,b>=a. Indeed M_1>0 and

```text
M_2 >= (a+1)(b+1)^2(2a+1)b - 2a^2b > 0,
```

since (a+1)(2a+1)>2a^2. The third minor is M_3=det(Q-3I).
Write d=b-a and u=2a-b-6. The theorem's domain is exactly d,u>=0,
with a=d+u+6 and b=2d+u+6. Direct expansion gives the complete identity

```text
M_3 = 8d^4u+4d^4+24d^3u^2+180d^3u+138d^3
      +26d^2u^3+375d^2u^2+1534d^2u+1314d^2
      +12du^4+255du^3+1894du^2+5542du+4636d
      +2u^5+56u^4+602u^3+3052u^2+7060u+5488 > 0.
```

Diagonal similarity preserves the principal minors. All three leading
minors of the symmetric similar matrix Q-3I are positive, so Sylvester's
criterion gives every Q eigenvalue above three. The scalar a+b+1 also
exceeds three, proving kappa_min(K)>3.

## The upper endpoint four

Under the same exact transformation,

```text
p(4) = 16d^5+48d^4u+376d^4+52d^3u^2+852d^3u+3354d^3
       +24d^2u^3+644d^2u^2+5370d^2u+14193d^2
       +4du^4+180du^3+2533du^2+14385du+28728d
       +12u^4+322u^3+3201u^2+13941u+22437 > 0.
```

Thus det(Q-4I)=-p(4)<0. The symmetric similar matrix Q-4I has a
negative eigenvalue, so kappa_min(K)<4. Its graph lift is in
(V-3,V-2), proving the theorem. Both boundary lines d=0 and u=0 are
included: the constant terms in the displayed expansions are positive.

## Why the region adds coverage

For the repeated pair a, the product-tail criterion fails by the margin

```text
C_a = 2(a^2-1)b+(a-1)(2a-1)-b^2.
```

Because b<=2a-6, its first and last terms have sum at least
2(a^2-a+2)b>0. The remaining term is positive. For the repeated pair b,
the corresponding margin is

```text
C_b = 2(b^2-1)a+(b-1)(2b-1)-a^2 > 0,
```

since a<=b and 2(b^2-1)>b. Hence both possible pair orientations fail
that earlier sufficient condition throughout the theorem's domain.

For the small-exponent condition, there are only two distinguished values.
Their failure margins are

```text
F_a = (a^2-a-1)b^2+2(a^2-1)(a+1)b+a(a^2-1)-(a-1),
F_b = (b^2-1)((2a+1)b+2a)+a^2(b^2-b-1)-(b-1).
```

Both are positive for a,b>=2: the first two F_a terms are positive and
a(a^2-1)>a-1; b^2-b-1>=b-1 makes the final two F_b terms positive too. Thus every
coordinate choice fails this criterion on the new region. All entries
are at least six, also excluding the earlier unit/pair-two/three/four
families. This compares coverage of the recorded results; it makes no
literature-priority claim.

## A precise limitation at the neighboring boundary

The offset six cannot be uniformly replaced by five in the assertion
3<kappa_min<4. At (a,b)=(20,35), which has b=2a-5, the exact values are

```text
p(2)=-39374484, p(3)=222118, p(4)=39761312.
```

The three leading minors of Q-2I are positive, while det(Q-3I)<0,
so its smallest root is strictly between two and three. This is a fixed
exact diagnostic of the proposed interval extension, not an integral
graph counterexample; the same graph is nonintegral. It does not imply
that every b>2a-6 shares this interval or that the remaining classification
is settled.

## Verification and next scope

The [checker](../scripts/check_four_prime_double_pair_balanced.py) verifies
the generic second-swap embedding, scalar eigenvector, symmetrizer and
characteristic factorization. All 71 coefficients in the complete four
positive minor/endpoint expansions check, including the 40 coefficients
displayed above. It also verifies the four criterion-failure identities
and their positive transformed coefficients.

Five specified controls (a,b)=(6,6),(7,8),(10,14),(30,54),(20,35) cover
the lower corner, first unequal pair, two growing-gap boundary points
and the neighboring-boundary diagnostic. They independently reconstruct
all four support embedding columns, zero sums, weighted symmetry and
complement/universal lifts. Twenty-five direct 3x3 Bareiss determinants
reconstruct and cross-check the cubics; exact leading minors and Sturm
counts check the claimed intervals. No expanded vertex graphs are used.

The [certificate](../results/four-prime-double-pair-balanced.json)
reproduces byte-for-byte with SymPy 1.14.0 using
`python3 scripts/check_four_prime_double_pair_balanced.py`; its reused
support-checker dependency hash is recorded. The unbounded conclusion
uses the written proof, with no finite exponent base, exponent scan,
floating eigensolver, historical finite-base rerun or Lean claim.

Keep the completed three-prime manuscript focused. The subsequent
[completion](four-prime-double-pair-completion.md) settles the entire
double-pair transition using unique-positive-root endpoint brackets.
The next spectral question is a single repeated pair with unequal
remaining entries outside the product criterion. General repeated-pair
and higher-prime nonsquarefree Q3 remain open, as does old orthogonality n=7.
