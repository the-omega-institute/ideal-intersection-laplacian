# A finite quadratic tail reduction and the triple-five family

**Theorem.** For positive integer exponents (a,a,b,c) on four distinct
primes, put

```text
M=(a+1)(b+1), d=(a+1)b,
U=floor(d^2/4), Q(a,b)=U[U+a(d-1)+a^2b].
```

If the ideal intersection graph is Laplacian integral, there is an
integer t in [1,d-1] such that c is a positive integer zero of

```text
q_t(c)=det((a+1+t)I-K).
```

Each q_t is a nonzero polynomial of degree at most two in c.
Thus, for each fixed (a,b), at most 2(d-1) positive tails can
possibly be integral. Moreover c divides the positive integer

```text
H_t=t(d-t)[t(d-t)+at+a^2b],
```

and c<=Q(a,b). In particular, every c>Q(a,b) is nonintegral;
its second restricted eigenvalue is noninteger. No ordering between
a and b is required. These are necessary conditions for integrality,
not sufficient ones.

This improves the previous [effective large-tail bound](four-prime-large-tail.md)
R=24(M+a)^3(3M+a) by a factor greater than 128 uniformly.
At a=b=5 the cutoff falls from 186913752 to 111375. More usefully,
the remaining necessary tail candidates are obtained from 29 explicit
quadratics, rather than scanning that entire tail range.

**Corollary.** Every positive vector (5,5,5,c) is nonintegral.
The uniform reduction is a written unbounded argument. This specific
corollary also uses the complete finite arithmetic for its 29 candidate
quadratics, retained in the certificate, and an explicit cubic interval.

## A strict upper bound for the second restricted root

Use the established convention: nonzero proper ideals of Z_n are
adjacent precisely when their intersection is nonzero. The genuine
antisymmetric support restriction of the complement Laplacian is K-I,
where

```text
K = [(a+1)(b+1)(c+1)+a, ac,          ab,          abc]
    [a,                   (a+1)(b+1), ab,          0  ]
    [a,                   ac,          (a+1)(c+1), 0  ]
    [a,                   0,           0,          a+1].
```

The positive diagonal diag(1,c,b,bc) symmetrizes K. The
[previous tail proof](four-prime-large-tail.md) gives, for its real
eigenvalues in increasing order,

```text
1<=kappa_1<a+1<kappa_2<=M.
```

Interlacing supplies the upper bound; the shifted operator has a
positive two-dimensional block and a Schur complement of determinant
-a^2b^2c^2<0, giving strict separation at a+1. We now exclude the
remaining upper-endpoint equality. For p(x)=det(xI-K), direct expansion
gives

```text
p(M)=a^2bc{(c-1)[M^2-b(2a+1)]
           +(a+1)^2(b^2+1)-ab}>0.
```

Indeed c>=1, and both bracketed expressions are positive:

```text
M^2-b(2a+1)
 =(a+1)^2b^2+(2a^2+2a+1)b+(a+1)^2>0,
(a+1)^2(b^2+1)-ab>0.
```

Hence kappa_2<M, and any integer value of this actual restricted
root is a+1+t with 1<=t<=d-1. The support construction has weighted
sum zero and transfers kappa to the graph eigenvalue V+1-kappa,
where V=(a+1)^2(b+1)(c+1)-2. Therefore graph integrality forces
kappa_2 to be integer.

## Divisibility, quadratic candidates and the new cutoff

Only two rows of K depend on c, so q_t has degree at most two.
The constant-in-c coefficient of p is

```text
H(x)=(x-a-1)(x-M)
     [x^2-(ab+3a+b+2)x+2a^2+2ab+3a+b+1].
```

Substituting x=a+1+t gives the positive identity

```text
H(a+1+t)=H_t=t(d-t)[t(d-t)+at+a^2b]>0
```

for every 1<=t<=d-1. This also shows q_t is never identically zero.
Each such polynomial has at most two positive integer zeros, proving
the candidate-count bound. If q_t(c)=0 with integer c>0, reducing
that equation modulo c gives c dividing H_t. Thus c<=H_t.

For integer t in this interval,

```text
0<t(d-t)<=floor(d^2/4)=U,
t<=d-1.
```

Consequently H_t<=U[U+a(d-1)+a^2b]=Q(a,b). This proves the new
tail cutoff and shows that kappa_2 itself is noninteger above it.
The proof uses no estimates of floating-point eigenvalues.

For comparison with R, use d<M, a<M and a^2b<=ad to obtain

```text
Q <= (d^2/4)[d^2/4+2ad] < 9M^4/16,
R >= 72M^4 > 128Q.
```

The cutoff remains conservative. The quadratic candidate reduction
is stronger than the cutoff alone, and can be applied to a chosen
fixed pair without enumerating all tails up to Q.

## Completion of every (5,5,5,c)

Here M=36, d=30, and t=1,...,29. The complete candidate polynomial
is

```text
q_t(c)=A_t c^2+B_t c+C_t,
A_t=216t^2-1080t-6875,
B_t=t(-42t^2+1195t+575),
C_t=t(30-t)[t(30-t)+5t+125]>0.
```

For 9<=t<=28 all three coefficients are positive. To check this
whole interval, set u=t-9 for A_t and use

```text
A_t=216u^2+2808u+901>0,
B_t/t=7928-359(t-9)+42(t-9)(28-t)>=1107>0.
```

These polynomials have no positive tail root. The remaining nine
rows are fully specified below. Delta=B_t^2-4A_t C_t; each listed
square anchor h means h^2<Delta<(h+1)^2.

| t | A_t | B_t | C_t | Delta | Exclusion or remaining roots |
|---|---|---|---|---|---|
| 1 | -7739 | 1728 | 4611 | 145724100 | square anchor 12071 |
| 2 | -8171 | 5594 | 10696 | 380880900 | square anchor 19516 |
| 3 | -8171 | 11346 | 17901 | 713808000 | square anchor 26717 |
| 4 | -7739 | 18732 | 25896 | 1152524400 | square anchor 33948 |
| 5 | -6875 | 27500 | 34375 | 1701562500 | -6875(c-5)(c+1) |
| 6 | -5579 | 37398 | 43056 | 2359448100 | square anchor 48574 |
| 7 | -3851 | 48174 | 51681 | 3116828400 | square anchor 55828 |
| 8 | -1691 | 59576 | 60016 | 3955248000 | square anchor 62890 |
| 29 | 143461 | -2668 | 8671 | -4968683100 | no real root |

The seven nonsquare discriminants exclude integer roots; the last
row has negative discriminant. At t=5 the only positive integer
root is c=5, with kappa_2=11. Thus every c!=5 already has a
noninteger second restricted root.

At c=5 the complete quartic factors as

```text
p(x)=(x-11)(x^3-288x^2+14298x-41261).
```

The cubic has values -932 at three and 11387 at four, giving a
restricted root in (3,4). Its graph lift is noninteger. This handles
the sole remaining candidate and proves the corollary for every
positive c, including c<5.

## Verification and remaining scope

The [checker](../scripts/check_four_prime_tail_reduction.py) derives
the strict endpoint and positive constant-term identities, the full
fixed-pair quadratic formula, the positive-coefficient interval and
the exceptional cubic. The [certificate](../results/four-prime-tail-reduction.json)
retains all 29 candidate rows, not only the exceptional rows. Four
independent standard-library integer determinants per row reconstruct
the quadratic coefficients at c=0,1,2 and cross-check at c=3: 116
determinants in total. Here c=0 is solely an algebraic interpolation
value, not a positive graph exponent.

Seven specified support controls reconstruct 392 support-column
actions, weighted zero sums, symmetry and complement/universal
transfers. Forty-two additional independent integer determinants
reconstruct the quartics, and fourteen check the noninteger-witness
endpoints. Exact root isolation and Sturm counts verify the two
bounded roots and the witnesses. Six controls use c=Q+1, including
a control without a<=b; the seventh is the c=5 exception. The
uniform theorem has no finite exponent base; the triple-five
corollary uses the complete finite arithmetic described above.

No exponent rectangle, tail scan, expanded graph, floating eigensolver,
historical finite-base rerun or Lean validation is used. Previous
results, the focused three-prime main and all its finite inputs are
retained. The next structural question is the dependence of these
quadratic integer roots on unbounded a,b, or a sharper constraint on
their common divisibility data. Fixed-pair finiteness and the
triple-five corollary do not complete general single-pair, fully
unequal four-prime or higher-prime Q3. Final manuscript scope and
natural stopping/submission remain joint author decisions.
