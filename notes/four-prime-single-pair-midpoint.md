# A half-unit spectral interval for arbitrary tail gaps

**Theorem.** Let a,b,r be positive integers with r>=2 and b>=r^2.
For four distinct primes, the ideal intersection graph with exponent
vector (a,a,b,b+r) is Laplacian nonintegral. Its repeated-pair
restriction has an eigenvalue kappa in

```text
(a+b+(r+1)/2, a+b+(r+2)/2).
```

The graph consequently has an eigenvalue in

```text
(V-a-b-r/2, V-a-b-(r-1)/2),
V=(a+1)^2(b+1)(b+r+1)-2.
```

Both intervals have length one half and consecutive endpoints in
(1/2)Z, so neither contains an integer. The repeated exponent a is
arbitrary: it need not be the smallest or comparable to either tail.
Unlike the prior gap-one/two theorem, this condition permits arbitrarily
large gaps r. It is a sufficient region, not a full single-pair
classification or a claim that b>=r^2 is optimal.

## Invariant restriction and midpoint

We retain the established graph convention: nonzero proper ideals of
Z_n are adjacent exactly when their intersection is nonzero. The
[general repeated-pair proof](four-prime-pair-three.md) gives the
genuine four-dimensional complement restriction K-I, with c=b+r:

```text
K = [(a+1)(b+1)(c+1)+a, ac,          ab,          abc]
    [a,                   (a+1)(b+1), ab,          0  ]
    [a,                   ac,          (a+1)(c+1), 0  ]
    [a,                   0,           0,          a+1].
```

The positive diagonal D=diag(1,c,b,bc) satisfies DK=K^T D. The
paired support functions have weighted sum zero; complement reflection
and restoration of a^2bc-1 universal vertices lift any K eigenvalue
kappa to V+1-kappa. No second-swap cubic is invoked for unequal tails.

Put p(x)=det(xI-K) and m=a+b+1+r/2. Direct expansion gives the
generic midpoint identity

```text
16p(m)=r^2(2a+1)B(a,b,r),
B=4a^2b^2+4a^2br+8a^2b+4a^2r
  +4ab^3+6ab^2r+8ab^2+2abr^2+8abr+4ab
  +2ar^2+2ar
  +4b^3+6b^2r+4b^2+2br^2+4br+r^2.
```

All 18 terms of B have positive coefficients. In particular p(m)>0
for every positive a,b,r, without the theorem's gap or size restriction.
We now establish p(m-1/2)<0 under the stated condition.

## The lower endpoint

Set

```text
a=1+u, r=2+v, b=r^2+w,
u,v,w>=0.
```

The following complete coefficient table gives the exact identity

```text
-16p(m-1/2) = sum_(i,j) u^i v^j C_(i,j)(w).
```

Each entry lists the coefficients of C_(i,j) in increasing powers of
w; for example `3,2` denotes 3+2w. Every unlisted (i,j) is zero.
The table thus specifies a complete polynomial identity, not finite
values of the parameters.

| i | j | Coefficients of C_(i,j)(w) |
|---|---|---|
| 3 | 6 | 8 |
| 3 | 5 | 112 |
| 3 | 4 | 632,32 |
| 3 | 3 | 1848,296 |
| 3 | 2 | 2968,1000,40 |
| 3 | 1 | 2496,1472,184 |
| 3 | 0 | 864,800,208,16 |
| 2 | 8 | 8 |
| 2 | 7 | 148 |
| 2 | 6 | 1224,40 |
| 2 | 5 | 5912,552 |
| 2 | 4 | 18132,3292,72 |
| 2 | 3 | 35836,10836,660 |
| 2 | 2 | 44196,20532,2428,56 |
| 2 | 1 | 30912,20948,4204,256 |
| 2 | 0 | 9360,8888,2812,360,16 |
| 1 | 8 | 20 |
| 1 | 7 | 374 |
| 1 | 6 | 3084,108 |
| 1 | 5 | 14660,1500 |
| 1 | 4 | 43860,8818,204 |
| 1 | 3 | 84280,28094,1878 |
| 1 | 2 | 101202,50986,6690,164 |
| 1 | 1 | 69222,49710,10914,752 |
| 1 | 0 | 20610,20224,6810,956,48 |
| 0 | 8 | 8 |
| 0 | 7 | 156 |
| 0 | 6 | 1336,56 |
| 0 | 5 | 6568,792 |
| 0 | 4 | 20243,4724,120 |
| 0 | 3 | 39950,15212,1116 |
| 0 | 2 | 49180,27824,3988,104 |
| 0 | 1 | 34470,27308,6484,480 |
| 0 | 0 | 10521,11188,4020,600,32 |

All 91 nonzero coefficients are positive, and the constant term is
10521. Therefore p(m-1/2)<0 throughout u,v,w>=0, including all
boundary faces. Combined with p(m)>0, continuity gives a root in
(m-1/2,m). This root is an actual restricted eigenvalue and lifts
to the asserted graph interval.

For even r, m is an integer and this root lies between m-1/2 and m.
For odd r, m-1/2 is an integer and the root lies between m-1/2 and
m. In either case the open interval contains no integer, completing
the proof. Its existence is sufficient; no general uniqueness claim
or classification of the other roots is needed.

## Added coverage with unbounded gaps

For every integer r>=3 and a>=r^2, choose b=2a. The vectors
(a,a,2a,2a+r) satisfy b>=r^2 and have arbitrarily large tail gaps.
They have a repeated minimum, and c=2a+r>2a-6 excludes the earlier
balanced region. The only repeated value is a, and the product-tail
failure margin equals

```text
C=(a^2-1)(b+c)+(a-1)(2a-1)-bc
 =4a^3+(r-2)a^2-(2r+7)a+1-r.
```

Since r>=3 and a>=r^2 imply 2<=r<=a,

```text
C = [4a^3-2a^2-8a+1] + (r-2)a^2 + (a-r)(2a+1)
  >= 2a(2a^2-a-4)+1 > 0.
```

Thus the product-tail sufficient condition fails. The
[general small-exponent comparison](four-prime-single-pair-balanced.md)
also excludes that criterion at every coordinate of these repeated
minima. All entries are at least nine, the two tails are unequal,
and r>=3, so the fixed pair-two/three/four, double-pair and tail-gap-one/two
results do not cover these vectors either. Examples include
(9,9,18,21), (25,25,50,55) and (100,100,200,210).
This compares coverage of recorded results, not literature priority.

## A limitation and exact verification

The half-unit localization does not hold for all positive parameters
if the size hypothesis is simply removed. At (a,b,r)=(1,1,2), m=4,

```text
p(7/2)=471/16, p(4)=99,
```

and the quartic has no root in (7/2,4), as an exact Sturm count
confirms. That graph is still nonintegral by the earlier unit/gap-two
results. This diagnoses the proposed stronger root interval, not an
integral graph counterexample or a sharp threshold for b.

The [checker](../scripts/check_four_prime_single_pair_midpoint.py)
verifies generic symmetry, the complete midpoint identity, all 91
lower-endpoint coefficients and the coverage identities. The written
coefficient table is compared separately with the exact checker output.
Seven specified controls (a,b,r)=(1,4,2),(5,10,3),(30,9,3),
(5,16,4),(25,50,5),(100,200,10),(1,1,2) cover the domain corner,
both parities, equality b=r^2, unordered a>b, growing gaps and the
outside-hypothesis diagnostic. They reconstruct 392 support-column
actions, weighted zero sums, symmetry and complement/universal lifts.
Forty-two direct standard-library integer determinants interpolate
and cross-check the quartics. Fourteen additional integer determinants
of doubled matrices independently check the half-integer endpoints,
using det(2xI-2K)=16p(x). Seven exact Sturm counts give one root in
each theorem control and zero in the diagnostic interval.

The [certificate](../results/four-prime-single-pair-midpoint.json)
reproduces byte-for-byte with SymPy 1.14.0 using
`python3 scripts/check_four_prime_single_pair_midpoint.py`; checker
and reused support-helper hashes are recorded. This is a written
unbounded three-parameter result. No exponent scan, finite exponent
base, expanded vertex graph, floating eigensolver, historical finite-base
rerun or Lean was used.

Keep the completed three-prime main manuscript focused. The next
bounded question is an unequal tail gap r>=3 with b<r^2, outside
the balanced/product-tail criteria. The generic midpoint identity is
available, but positivity there alone does not isolate a noninteger
root when the lower half-unit endpoint changes sign. General single-pair,
fully unequal four-prime and higher-prime nonsquarefree Q3 remain open,
as does old orthogonality n=7.
