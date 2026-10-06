# A weighted midpoint bound and completion of tail gap three

**Theorem.** For positive integer exponents (a,a,b,b+r) on four
distinct primes, suppose r>=3 and

```text
4ab >= (2a+1)r^2.
```

Then the ideal intersection graph is Laplacian nonintegral. The
genuine repeated-pair restriction has an eigenvalue in
(a+b+(r+1)/2,a+b+(r+2)/2). Its graph lift lies in
(V-a-b-r/2,V-a-b-(r-1)/2), where
V=(a+1)^2(b+1)(b+r+1)-2. These open half-unit intervals contain
no integers. No ordering between a and b is assumed, and equality
in the condition is included.

The condition is b>=(1/2+1/(4a))r^2, improving the previous
[midpoint region](four-prime-single-pair-midpoint.md) b>=r^2.
For a>=5 its coefficient is at most 11/20. This bound is sufficient;
we do not claim it is optimal or completes the general single-pair
classification.

**Corollary.** Every positive integer vector (a,a,b,b+3) on four
distinct primes is nonintegral. Together with the prior
[gap-one/two theorem](four-prime-single-pair-small-gap.md), all
positive tail gaps one, two and three are now settled.

## The weighted lower endpoint

We retain the existing graph convention: nonzero proper ideals of Z_n
are adjacent exactly when their intersection is nonzero. Use the
[general antisymmetric support construction](four-prime-pair-three.md)
with c=b+r. In the tail-support order empty,{4},{3},{3,4}, its
complement restriction is K-I, where

```text
K = [(a+1)(b+1)(c+1)+a, ac,          ab,          abc]
    [a,                   (a+1)(b+1), ab,          0  ]
    [a,                   ac,          (a+1)(c+1), 0  ]
    [a,                   0,           0,          a+1].
```

The positive diagonal diag(1,c,b,bc) symmetrizes K. Its support
embedding has weighted sum zero; complement reflection and restoring
the a^2bc-1 universal vertices give the graph eigenvalue V+1-kappa.
No second-swap cubic is used for unequal tails.

Put p(x)=det(xI-K) and m=a+b+1+r/2. The established generic midpoint
identity is 16p(m)=r^2(2a+1)B(a,b,r)>0, with all 18 terms of B
displayed in the previous midpoint note. Here we strengthen the
negative lower-endpoint argument by using the actual weighted slack

```text
z=4ab-(2a+1)r^2>=0,
v=r-3>=0,
b=((2a+1)r^2+z)/(4a).
```

After this substitution the exact polynomial identity is

```text
-256a^3 p(m-1/2) = sum_(j,i) z^j a^i C_(j,i)(v).
```

The following complete table specifies every coefficient. Each entry
lists the coefficients of C_(j,i) in increasing powers of v; for
example `3,2` denotes 3+2v. Every unlisted (j,i) is zero.

| j | i | Coefficients of C_(j,i)(v) |
|---|---|---|
| 0 | 0 | 729,1458,1215,540,135,18,1 |
| 0 | 1 | 11097,23058,20439,10014,2927,510,49,2 |
| 0 | 2 | 62748,131544,118332,59222,17812,3220,324,14 |
| 0 | 3 | 165476,345264,309364,154300,46260,8336,836,36 |
| 0 | 4 | 202840,419608,371872,183032,54040,9576,944,40 |
| 0 | 5 | 91296,189600,166816,80688,23232,4000,384,16 |
| 0 | 6 | 288,3360,4160,1984,416,32 |
| 1 | 0 | 972,1782,1377,576,138,18,1 |
| 1 | 1 | 9756,17250,12775,5076,1142,138,7 |
| 1 | 2 | 35052,59684,42346,16012,3400,384,18 |
| 1 | 3 | 53228,87096,59116,21288,4284,456,20 |
| 1 | 4 | 29664,46176,29592,10032,1904,192,8 |
| 1 | 5 | 2736,3264,1408,256,16 |
| 2 | 0 | 270,342,165,36,3 |
| 2 | 1 | 1838,2190,985,198,15 |
| 2 | 2 | 3876,4344,1828,342,24 |
| 2 | 3 | 2508,2616,1024,180,12 |
| 2 | 4 | 216,120,16 |
| 3 | 0 | 28,18,3 |
| 3 | 1 | 108,62,9 |
| 3 | 2 | 84,44,6 |
| 3 | 3 | 4 |
| 4 | 0 | 1 |
| 4 | 1 | 1 |

All 128 nonzero coefficients are positive, including constant term
729. Hence -256a^3p(m-1/2)>0 for a>=1,v,z>=0. Since a>0,
p(m-1/2)<0<p(m), and continuity gives an actual restricted root
in (m-1/2,m). For even r one endpoint is an integer; for odd r the
other is an integer. The endpoints are consecutive points of (1/2)Z,
so the open interval contains no integer. The graph transfer proves
the theorem. This proof also covers z=0 and v=0.

## Completion of tail gap three

When a,b>=5, write a=5+u,b=5+w. The new condition at r=3 holds
throughout this whole quadrant because

```text
4ab-9(2a+1)=4uw+2u+20w+1>0.
```

For a>=5 and b<=4, use p(a+b+1)<0 from the prior generic endpoint
factorization and the following complete cubic values for c=b+3:

| b | p(a+b+2) |
|---|---|
| 1 | 26a^3+62a^2+68a+28 |
| 2 | 37a^3+98a^2+150a+84 |
| 3 | 36a^3+72a^2+224a+184 |
| 4 | 17a^3-94a^2+230a+340 |

The first three are positive for every positive a. For b=4,
writing a=5+u gives 17u^3+161u^2+565u+1265>0. Thus these four
tails supply a restricted noninteger root in (a+b+1,a+b+2).
The four rows are written polynomial identities covering all a>=5,
not a finite exponent base.

Finally, a=1 is covered by the [unit-exponent theorem](unit-exponent-any-prime-count.md).
For a=2,3,4 and b>=2, the established [pair-two](four-prime-pair-two.md),
[pair-three](four-prime-pair-three.md) and [pair-four](four-prime-pair-four.md)
theorems apply; b=1 again has a unit exponent. These earlier written results
exhaust a<=4. This completes every positive a,b at tail gap three.
Only the first case uses the new half-unit localization; the corollary
does not assert that this particular interval holds in every case.

## An unbounded family below the old square boundary

For any integer r>=4, put a=r(r-1)/2, b=2a=r(r-1), c=r^2.
Then

```text
4ab-(2a+1)r^2=r^2(r^2-3r+1)>0,
b=r^2-r<r^2.
```

Thus the new theorem covers this entire family, while the old
midpoint size condition fails. These are repeated minima with a>=6.
They also lie outside the balanced region, since c=2a+r>2a-6.
The product-tail failure margin at b=2a is

```text
C=4a^3+(r-2)a^2-(2r+7)a+1-r
 =[4a^3-2a^2-8a+1]+(r-2)a^2+(a-r)(2a+1)>0.
```

Indeed a>=r for r>=4, and the bracket is
2a(2a^2-a-4)+1>0. The previous general small-exponent comparison
excludes that criterion at every coordinate of these repeated minima.
All entries are at least six, and the tails are unequal with r>=4,
so the earlier fixed small pairs, double pairs and gaps one through
three do not cover them. Examples are (6,6,12,16), (10,10,20,25)
and (45,45,90,100). This establishes additional recorded coverage,
not literature priority.

## Verification and remaining scope

The [checker](../scripts/check_four_prime_weighted_midpoint.py)
verifies the generic symmetrizer/midpoint identity, all 128 lower
coefficients, the four small-tail cubics, the gap-three quadrant
margin and the new-family identities. The complete 24-row written
coefficient table is separately compared with the exact output.

Eight specified controls (a,b,r)=(5,5,3),(5,9,4),(10,20,5),
(5,55,10),(30,5,3),(100,600,30),(5,4,3),(1,1,3) cover the
near-boundary region, both parities, exact weighted equality,
unordered a>b, an added family, growing gaps, the small-b gap-three
case and a condition-outside diagnostic. They reconstruct 448
support-column actions, weighted zero sums, symmetry and
complement/universal lifts. Forty-eight independent integer
determinants interpolate and cross-check the quartics; sixteen
doubled-matrix determinants check their exact interval endpoints.
Eight exact Sturm counts give seven witnesses and one diagnostic.

For that diagnostic (a,b,r)=(1,1,3), the half-unit interval (4,9/2)
has p(4)=184,p(9/2)=5427/16 and no root. The graph is nonintegral
by the unit-exponent theorem. Thus the weighted size hypothesis cannot
simply be discarded from this localization; no sharpness or integral
counterexample is claimed.

The [certificate](../results/four-prime-weighted-midpoint.json)
reproduces byte-for-byte with SymPy 1.14.0 using
`python3 scripts/check_four_prime_weighted_midpoint.py`. It records
the checker and both reused helper hashes. The unbounded theorem
uses the written identities; controls validate implementation.
No exponent scan, finite exponent base, expanded graph, floating
eigensolver, historical finite-base rerun or Lean was used.

Keep the completed three-prime main focused. The next bounded
spectral question is a repeated minimum a>=5 with tail gap r>=4,
4ab<(2a+1)r^2, outside the balanced/product-tail criteria. The
general positive midpoint and wider higher-root window remain
available, but their signs alone do not decide that region. General
single-pair, fully unequal four-prime and higher-prime nonsquarefree
Q3 remain open, as does old orthogonality n=7.
