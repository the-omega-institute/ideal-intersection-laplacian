# Even tail gaps: a unit interval and completion of gap four

**Theorem.** For positive integer exponents (a,a,b,b+r) on four
distinct primes, suppose r>=2 is even and

```text
8ab >= (2a+1)r^2.
```

Then the ideal intersection graph is Laplacian nonintegral. The genuine
repeated-pair restriction has an eigenvalue in
(a+b+r/2,a+b+r/2+1). Its graph lift lies in
(V-a-b-r/2,V+1-a-b-r/2), where V=(a+1)^2(b+1)(b+r+1)-2.
Both are open intervals between consecutive integers. No ordering
between a and b is required; equality in the condition is included.

For even r>=4 the sufficient lower bound
b>=(1/4+1/(8a))r^2 halves the preceding
[weighted midpoint bound](four-prime-weighted-midpoint.md).
The coefficient is at most 11/40 when a>=5. This is a sufficient
condition, rather than an optimal bound or a full classification.

**Corollary.** Every positive vector (a,a,b,b+4) is nonintegral.
Together with the earlier results, all positive tail gaps one through
four are settled. The corollary uses different intervals for small tails.

## The parity-aware endpoint proof

We use the existing graph convention: nonzero proper ideals of Z_n
are adjacent precisely when their intersection is nonzero. The
[general support construction](four-prime-pair-three.md) gives, with
c=b+r and tail-support order empty,{4},{3},{3,4}, the restriction K-I
of the complement Laplacian, where

```text
K = [(a+1)(b+1)(c+1)+a, ac,          ab,          abc]
    [a,                   (a+1)(b+1), ab,          0  ]
    [a,                   ac,          (a+1)(c+1), 0  ]
    [a,                   0,           0,          a+1].
```

The positive diagonal diag(1,c,b,bc) symmetrizes K. The support
embedding has weighted sum zero; complement reflection and restoring
the universal vertices transfer a restricted eigenvalue kappa to
V+1-kappa. Unequal tails do not admit the second-swap cubic.

Put p(x)=det(xI-K), m=a+b+1+r/2. The established generic identity
16p(m)=r^2(2a+1)B(a,b,r)>0 uses the 18 positive terms of B displayed
in the [first midpoint note](four-prime-single-pair-midpoint.md).
For even r, m is an integer, so the longer interval (m-1,m)
still excludes all integers. Its lower endpoint permits a smaller
tail threshold. Put

```text
z=8ab-(2a+1)r^2>=0,
v=r-2>=0,
b=((2a+1)r^2+z)/(8a).
```

The complete exact lower-endpoint identity is

```text
-8192a^3 p(m-1) = sum_(j,i) z^j a^i C_(j,i)(v).
```

Each row below lists the coefficients of C_(j,i) in increasing powers
of v. Every unlisted (j,i) is zero.

| j | i | Coefficients of C_(j,i)(v) |
|---|---|---|
| 0 | 0 | 1024,3072,3840,2560,960,192,16 |
| 0 | 1 | 15360,44032,52992,34560,13120,2880,336,16 |
| 0 | 2 | 86016,239616,282624,183040,70400,16128,2048,112 |
| 0 | 3 | 223232,626688,728064,469504,181120,41728,5312,288 |
| 0 | 4 | 266240,776192,903168,577536,220416,49792,6144,320 |
| 0 | 5 | 122880,360448,434176,278528,102912,22016,2560,128 |
| 0 | 6 | 16384,24576,24576,16384,5120,512 |
| 1 | 0 | 1024,2304,2112,1024,288,48,4 |
| 1 | 1 | 11776,25344,22464,10624,2880,432,28 |
| 1 | 2 | 47104,98816,85632,39296,10048,1344,72 |
| 1 | 3 | 77312,163840,137728,60416,14368,1728,80 |
| 1 | 4 | 47104,101376,81920,32768,7040,768,32 |
| 1 | 5 | 10240,16384,9216,2048,128 |
| 2 | 0 | 384,576,336,96,12 |
| 2 | 1 | 3072,4416,2448,624,60 |
| 2 | 2 | 7424,10368,5376,1200,96 |
| 2 | 3 | 5504,7424,3392,672,48 |
| 2 | 4 | 1280,896,128 |
| 3 | 0 | 64,48,12 |
| 3 | 1 | 288,208,36 |
| 3 | 2 | 256,160,24 |
| 3 | 3 | 32 |
| 4 | 0 | 4 |
| 4 | 1 | 4 |

All 128 nonzero coefficients are positive, including constant term
1024. Thus p(m-1)<0<p(m) for a>=1,v,z>=0. Continuity supplies
a genuine restricted eigenvalue in (m-1,m), and the graph transfer
proves the theorem. The argument includes z=0 and r=2.

The polynomial sign identity holds for real r>=2, but the integrality
conclusion from this particular unit interval uses even r. For odd r
the interval has half-integer endpoints and contains an integer;
the preceding half-unit theorem retains its separate scope.

## Completion of gap four

For a,b>=5 write a=5+u,b=5+w. At r=4 the new condition follows from

```text
8ab-16(2a+1)=8uw+8u+40w+24>0.
```

For a>=5 and b<=4, the generic endpoint factorization in the
[small-gap note](four-prime-single-pair-small-gap.md) gives
p(a+b+1)<0. The intermediate endpoint at gap four is:

| b | p(a+b+2) |
|---|---|
| 1 | 42a^3+91a^2+108a+54 |
| 2 | 48a^3+84a^2+189a+153 |
| 3 | 22a^3-121a^2+168a+324 |
| 4 | -48a^3-704a^2-105a+585 |

The first two rows are positive for every a>0. For b=3, setting
a=5+u gives 22u^3+209u^2+608u+889>0. These three tails give a
root in (a+b+1,a+b+2). For b=4, setting a=1+u gives

```text
-p(a+6)=48u^3+848u^2+1657u+272>0.
```

The positive generic midpoint p(a+7)>0 instead gives a root in
(a+6,a+7). The four rows are polynomial identities for unbounded a,
with no finite exponent base.

Finally a=1 or b=1 falls under the
[unit-exponent theorem](unit-exponent-any-prime-count.md), while
a=2,3,4 and b>=2 are covered by the earlier
[pair-two](four-prime-pair-two.md), [pair-three](four-prime-pair-three.md)
and [pair-four](four-prime-pair-four.md) results. This exhausts all
positive a,b at gap four. The single interval in the main theorem
is not asserted for all small cases.

## An equality family outside the previous weighted region

For any integer s>=3 choose

```text
a=2s, b=4s^2+s, r=4s, c=4s^2+5s.
```

These are repeated minima with a>=6, and satisfy

```text
8ab-(2a+1)r^2=0,
4ab-(2a+1)r^2=-8s^2(4s+1)<0.
```

Thus the new theorem includes the equality boundary and supplies
an unbounded family beyond the previous weighted condition. Examples
are (6,6,39,51), (8,8,68,84) and (10,10,105,125).
The balanced condition fails because c>2a-6. The failure margin for
the product-tail condition is exactly

```text
(a^2-1)(b+c)+(a-1)(2a-1)-bc
  =(s-1)(16s^3+16s^2+11s-1)>0.
```

The earlier general comparison excludes the small-exponent criterion
at every coordinate of these repeated minima. Every coordinate is
at least six, the tails are unequal and r>=12, so the unit/small-pair,
double-pair and gaps-one-through-four results do not already cover
this family. This is a comparison with our established sufficient
criteria, rather than a literature-priority claim.

## Exact verification and remaining scope

The [checker](../scripts/check_four_prime_even_midpoint.py) derives
the generic characteristic polynomial, symmetry, positive midpoint,
all 128 lower-endpoint coefficients, four small-tail cubics and
coverage identities. The [certificate](../results/four-prime-even-midpoint.json)
records all terms and eight specified controls. They reconstruct
448 support-column actions, weighted zero sums and graph lifts.
Forty-eight independent standard-library integer determinants
reconstruct and cross-check the quartics; sixteen additional direct
endpoint determinants check the intervals. Eight exact Sturm counts
give seven witnesses and one diagnostic. Two controls lie exactly
on the new weighted equality boundary.

The diagnostic (a,b,r)=(5,5,6) fails the new condition and has
p(13)=115624, p(14)=510741, with no root in (13,14). It refutes
an unconditional extension of this particular unit interval; it
does not establish graph integrality.

This is a written unbounded proof with exact controls. No exponent
scan, expanded graph, floating eigensolver, historical finite-base
rerun or Lean validation is used. The complete three-prime main
manuscript and its existing finite inputs are retained. General
single-pair, fully unequal four-prime and higher-prime Q3 remain
open. The next bounded question concerns odd gaps r>=5 below the
previous weighted condition, or even gaps r>=6 below this new one,
outside the other sufficient regions. Manuscript inclusion and a
natural stopping/submission decision remain joint author decisions.
