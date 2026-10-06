# At most one positive tail root per candidate offset

**Theorem.** For positive integer exponents (a,a,b,c) on four distinct
primes with b<c, each fixed (a,b) has at most b-1 possibly integral
tails c. This halves the preceding bound 2(b-1). No ordering between
a and b is required. The equal-tail case remains settled by the
double-pair theorem.

More precisely, the [harmonic root window](four-prime-harmonic-tail.md)
forces any integral graph to have its second genuine restricted root
kappa_2=a+1+t, with b+1<=t<=2b-1. Write

```text
q_t(c)=det((a+1+t)I-K)=A_t c^2+B_t c+H_t.
```

For all these integer offsets B_t>0 and H_t>0. Thus A_t>=0
excludes every positive c, whereas A_t<0 gives exactly one positive
real tail root. That root need not be integer or exceed b, and even
an integer second root does not establish graph integrality.

## The leading and constant coefficients

Retain the genuine repeated-pair restriction K-I and graph transfer
from the preceding notes; a graph eigenvalue is V+1-kappa. Direct
expansion of its characteristic polynomial gives

```text
A_t=(a+1)^2(b+1)t^2
    +(a+1)(b+1)[a^2-(2a+1)b]t-a^2b^2(2a+1),
H_t=t(d-t)[t(d-t)+at+a^2b], d=(a+1)b.
```

Since a>=1 implies d>=2b, H_t is strictly positive throughout
b<t<2b. We prove the less immediate positivity of B_t next.

## A complete positive identity for B_t/t

Set

```text
w=a-1>=0, u=t-b-1>=0, v=2b-t-1>=0.
```

Equivalently a=1+w, b=2+u+v, t=b+1+u. These substitutions
cover every admissible integer offset; when b=1 the domain is empty.
The exact polynomial identity is

```text
B_t/t = sum_(i,j) w^i u^j C_(i,j)(v).
```

Each row lists coefficients in increasing powers of v; all unlisted
pairs (i,j) are zero. A leading zero is an actual zero coefficient.

| i | j | Coefficients of C_(i,j)(v) |
|---|---|---|
| 0 | 0 | 13,28,14,2 |
| 0 | 1 | 17,26,6 |
| 0 | 2 | 4,4 |
| 1 | 0 | 33,53,24,3 |
| 1 | 1 | 62,58,11 |
| 1 | 2 | 30,12 |
| 1 | 3 | 4 |
| 2 | 0 | 10,21,10,1 |
| 2 | 1 | 27,25,4 |
| 2 | 2 | 15,5 |
| 2 | 3 | 2 |
| 3 | 0 | 0,2,1 |
| 3 | 1 | 2,2 |
| 3 | 2 | 1 |

All 34 nonzero coefficients are positive, including constant term
13. Hence B_t/t>0, and t>0 gives B_t>0.

If A_t>=0, all nonzero coefficients of q_t are positive, so no
positive c can be a root. If A_t<0, the discriminant is
B_t^2+4|A_t|H_t>0 and the root product H_t/A_t<0. There is
exactly one positive real root and one negative real root. The
positive root is

```text
c=(B_t+sqrt(B_t^2+4|A_t|H_t))/(2|A_t|).
```

An integer candidate requires a square discriminant and divisibility
of the numerator by 2|A_t|. There is at most one candidate per
offset, proving the theorem without a finite exponent base.

## A contiguous smaller offset domain

The leading coefficient is strictly increasing for t>=b, since

```text
A'_b=(a+1)(b+1)(a^2+b)>0
```

and A''_t=2(a+1)^2(b+1)>0. Its endpoint values are

```text
A_b=-ab(a+b+1)[a(b-1)+b]<0,
A_(2b)=b[2a^3+a^2b+2a^2+2ab^2+2ab+2b^2+2b]>0.
```

Therefore the unique positive zero tau of A_t lies in (b,2b),
and only integer offsets b<t<tau need be retained. This cutoff can
be decided by exact integer coefficient signs, without approximating
tau. For a=b=5, A_t=216t^2-1080t-6875 is negative at t=6,7,8
and positive at t=9; only three unequal-tail quadratics remain.
The earlier complete triple-five proof and all historical candidate
rows are retained.

## Verification and remaining scope

The [checker](../scripts/check_four_prime_unique_tail.py) derives
the generic A_t and H_t identities, all 34 positive linear-coefficient
terms, the derivative and both endpoint signs. The
[certificate](../results/four-prime-unique-tail.json) records six
specified quadratic controls. Twenty-four independent standard-library
integer determinants reconstruct their coefficients at c=0,1,2 and
cross-check at c=3; twelve exact Sturm counts verify the positive
and negative root counts. The c=0 value is algebraic interpolation,
not a positive graph exponent. The complete written coefficient table
is independently matched against the certificate.

This is a written unbounded proof with exact controls. No exponent
rectangle, tail scan, expanded graph, historical finite-base rerun or
Lean validation is used. The next question is to exclude square
discriminants or enforce numerator divisibility uniformly on the
remaining A_t<0 domain, or combine these conditions with a second
restricted root. General single-pair, fully unequal four-prime and
higher-prime classification remains open. The focused three-prime
main, earlier finite inputs and joint manuscript-scope decisions
remain retained.
