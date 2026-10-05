# A three-parameter balanced region for a single repeated pair

**Theorem.** For four distinct primes and positive integer exponents
(a,a,b,c) satisfying a<=b<=c<=2a-6, the ideal intersection graph has
a noninteger Laplacian eigenvalue in (V-3,V-2), where
V=(a+1)^2(b+1)(c+1)-2. Its smallest repeated-pair eigenvalue satisfies
3<kappa_min(K)<4. The hypotheses imply a>=6.

This includes unequal tails b<c, extending the recorded
[balanced double-pair region](four-prime-double-pair-balanced.md) to
three independent parameters. Every positive double pair is already
[settled](four-prime-double-pair-completion.md); the new coverage here
is the unequal-tail part of the region. It lies outside both the
product-tail and small-exponent sufficient criteria. We also prove the
independent bound kappa_min(K)<4 for every repeated-minimum vector
a>=5,b>=a,c>=a. That upper bound alone does not establish nonintegrality
throughout its larger domain.

We use the existing graph convention: nonzero proper ideals of Z_n
are adjacent exactly when their intersection is nonzero. Permuting
coordinates preserves the graph. General single-pair and fully unequal
four-prime classification remains open.

## The genuine four-dimensional restriction

For T subset of {3,4}, take functions h(T) on support {1} union T,
-h(T) on {2} union T, and zero on all other proper nonempty supports.
The two paired classes have equal weights; these functions have weighted
sum zero, and the disjoint-support complement preserves their space.
In the order T=empty,{4},{3},{3,4}, the complement acts by K-I, with

```text
K = [(a+1)(b+1)(c+1)+a, ac,          ab,          abc]
    [a,                   (a+1)(b+1), ab,          0  ]
    [a,                   ac,          (a+1)(c+1), 0  ]
    [a,                   0,           0,          a+1].
```

Equivalently K=(a+1) E_b tensor E_c+a F_b tensor F_c, where
E_k=diag(k+1,1) and F_k=[[1,k],[1,0]]. The diagonal
D=diag(1,c,b,bc) satisfies DK=K^T D. Thus
S=D^(1/2) K D^(-1/2) is real symmetric, and diagonal similarity
preserves each principal minor. We use all four dimensions here:
the second-swap cubic is invariant only when b=c.

The complement has N=(a+1)^2(b+1)(c+1)-a^2bc-1 vertices after
removing a^2bc-1 universal vertices from the original graph. On the
zero-sum subspace, complement reflection gives N-(kappa-1);
adding back those universals gives V+1-kappa. Consequently an open
unit interval for kappa provides an open unit interval for the graph.
The [general tensor proof](four-prime-pair-three.md) already gives
kappa_min(K)>1 for every positive a,b,c.

## The lower endpoint three

Put

```text
P=(a+1)(b+1)(c+1)+a-3,
Q=(a+1)(b+1)-3, R=(a+1)(c+1)-3,
H=QR-a^2bc.
```

The four leading principal minors of K-3I are exactly

```text
M1=P,
M2=PQ-a^2c,
M3=PH-a^2(cR+bQ-2abc),
M4=(a-2)M3-a^2bcH.
```

Make the invertible change of nonnegative variables

```text
d=b-a, e=c-b, u=2a-c-6,
a=d+e+u+6, b=2d+e+u+6, c=2d+2e+u+6.
```

The following complete table specifies the polynomial identities
Mi=sum_(r,s) d^r e^s C_i(r,s;u). Each table entry is the list of
coefficients of C_i in increasing powers of u: for example `8,4`
means 8+4u. A dash means the zero polynomial. Every unlisted (r,s)
has all four coefficients zero. Thus the table is a complete algebraic
identity, including zero coefficients, rather than sampled values.

| r | s | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|
| 6 | 0 | — | — | 48 | — |
| 5 | 1 | — | — | 244 | 12 |
| 5 | 0 | — | 8 | 1300,200 | 12,24 |
| 4 | 2 | — | — | 510 | 54 |
| 4 | 1 | — | 32 | 5458,840 | 344,148 |
| 4 | 0 | — | 196,28 | 14276,4416,340 | 454,628,88 |
| 3 | 3 | — | — | 560 | 96 |
| 3 | 2 | — | 50 | 9034,1391 | 1129,335 |
| 3 | 1 | — | 616,88 | 47554,14713,1133 | 4247,2981,365 |
| 3 | 0 | 4 | 1850,532,38 | 81450,38004,5881,302 | 5322,6678,1725,126 |
| 2 | 4 | — | — | 340 | 84 |
| 2 | 3 | — | 38 | 7354,1133 | 1443,357 |
| 2 | 2 | — | 707,101 | 58473,18097,1394 | 9076,4918,550 |
| 2 | 1 | 10 | 4281,1232,88 | 202017,94259,14586,749 | 25280,22517,5250,365 |
| 2 | 0 | 56,8 | 8404,3651,525,25 | 255234,159684,37253,3843,148 | 27048,34594,12500,1775,88 |
| 1 | 5 | — | — | 108 | 36 |
| 1 | 4 | — | 14 | 2938,453 | 815,181 |
| 1 | 3 | — | 350,50 | 31388,9719,749 | 7227,3405,357 |
| 1 | 2 | 8 | 3208,924,66 | 164191,76620,11858,609 | 31716,23799,5163,345 |
| 1 | 1 | 91,13 | 12745,5545,798,38 | 419426,262348,61190,6311,243 | 69984,73774,24716,3371,163 |
| 1 | 0 | 246,70,5 | 18438,10762,2337,224,8 | 417600,328384,102664,15958,1234,38 | 62824,85872,39180,8144,798,30 |
| 0 | 6 | — | — | 14 | 6 |
| 0 | 5 | — | 2 | 460,71 | 169,35 |
| 0 | 4 | — | 63,9 | 6193,1919,148 | 1944,840,84 |
| 0 | 3 | 2 | 777,224,16 | 43624,20365,3153,162 | 11758,7960,1638,106 |
| 0 | 2 | 35,5 | 4684,2041,294,14 | 169134,105792,24675,2545,98 | 39808,37410,11852,1564,74 |
| 0 | 1 | 197,56,4 | 13762,8050,1751,168,6 | 341320,268284,83840,13027,1007,31 | 72200,87576,37776,7600,729,27 |
| 0 | 0 | 346,148,21,1 | 15700,11544,3366,487,35,1 | 279400,265040,104092,21672,2524,156,4 | 54880,81576,44640,12124,1764,132,4 |

There are respectively 20,56,84,83 nonzero coefficients, all positive.
The constant terms at d=e=u=0 are respectively
346,15700,279400,54880. Hence every Mi is strictly positive for
d,e,u>=0, including all boundaries. Sylvester's criterion applied to
S-3I proves positive definiteness, so kappa_min(K)>3.

## An upper endpoint for every repeated minimum

The empty/full-support principal minor of S-4I, equivalently the
{0,3} minor of K-4I, is

```text
J4=-(2a+3)bc+(a^2-2a-3)(b+c)+2a^2-9a+9.
```

For this identity only, write b=a+v,c=a+w with independent v,w>=0.
Then

```text
J4=-(2a+3)vw-(a^2+5a+3)(v+w)-5a^2-15a+9 < 0
```

for a>=5. A symmetric two-dimensional principal block with negative
determinant has a negative eigenvalue. Extending its eigenvector by
zeros supplies a negative Rayleigh quotient for S-4I, proving
kappa_min(K)<4. This does not need b<=c or the balanced upper bound.
Combining it with the lower-endpoint proof gives the theorem and its
graph interval (V-3,V-2).

## Comparison with earlier sufficient criteria

For the repeated pair a, the product-tail condition is equivalent to
the nonpositivity of

```text
C=-bc+(a^2-1)(b+c)+(a-1)(2a-1).
```

In the balanced region, bc<=(2a-6)b, so
C>=(a^2-2a+5)b+(a^2-1)c+(a-1)(2a-1)>0.
Thus that sufficient condition fails. For b<c the pair a is the
only repeated value, unless b=a, in which case choosing another two
of the three equal entries gives the same condition. The earlier
double-pair theorem already handles b=c.

In fact the small-exponent criterion fails for every coordinate of
every repeated-minimum vector a>=2,b,c>=a, not just the balanced
region. For a distinguished a its failure margin is

```text
F_a=(a^2-a-1)bc+(a^2-1)(a+1)(b+c)+a(a^2-1)-(a-1)>0.
```

For a distinguished tail m (either b or c), with the other tail z,
the failure margin is

```text
F_m=[(m^2-1)(2a+1)-a^2]z+(m^2-1)(a^2+2a)-(m-1)>0.
```

Indeed the first bracket is at least 2a^3-2a-1>0, and the last
two terms have positive sum since m^2-1>=m-1 and a^2+2a>1.
All coordinates in the balanced theorem are at least six, excluding
the earlier unit and fixed pair-two/three/four families as well.
This establishes additional coverage among our recorded results;
it does not assert literature priority.

## Boundary limitation and verification

The offset six cannot uniformly become five for the asserted (3,4)
interval. The previously diagnosed (a,b,c)=(20,35,35), with
c=2a-5, has kappa_min(K) in (2,3). Its graph is still nonintegral,
by the double-pair completion. This rules out that interval extension,
not every possible extension of nonintegrality.

The [checker](../scripts/check_four_prime_single_pair_balanced.py)
verifies the generic tensor/symmetrizer identities and all 56 support
actions symbolically, along with the four displayed minor formulas,
every coefficient in the complete table, the two upper-minor identities
and the criterion-failure identities. Six specified controls
(a,b,c)=(6,6,6),(7,7,8),(8,9,10),(10,11,14),(30,40,54),(20,35,35)
check another 336 support-column actions, weighted zero sums, symmetry
and complement/universal lifts. Direct standard-library integer
determinants at six points per control reconstruct each quartic,
independently checking its characteristic polynomial. Twenty-four
direct leading minors, six empty/full minors and six exact Sturm
counts check the claimed intervals. These controls validate the
implementation; the unbounded theorem follows from the written
polynomial identities and symmetric-matrix arguments.

The [certificate](../results/four-prime-single-pair-balanced.json)
reproduces byte-for-byte with SymPy 1.14.0 using
`python3 scripts/check_four_prime_single_pair_balanced.py`; it records
the checker and reused support-helper hashes. No finite exponent base,
exponent-range scan, expanded vertex graph, floating eigenvalue solver,
historical finite-base rerun or Lean was used.

Keep the completed three-prime main manuscript focused. The next
bounded spectral question is a repeated minimum a>=5 with unequal
tails beyond c<=2a-6 and outside the product-tail condition. The new
upper-four bound restricts the smallest root to (1,4), leaving integer
endpoints two and three to analyze; it does not exclude them. General
single-pair and fully unequal four-prime classification, higher-prime
nonsquarefree Q3 and old orthogonality n=7 remain open.
