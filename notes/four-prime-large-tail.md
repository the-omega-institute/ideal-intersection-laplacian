# An effective large-tail obstruction for every repeated pair

**Theorem.** Let a,b,c be positive integer exponents on four distinct
primes, with vector (a,a,b,c). Put

```text
M=(a+1)(b+1),
L=M+a,
R(a,b)=24L^3(3M+a).
```

If c>R(a,b), the ideal intersection graph is Laplacian nonintegral.
No ordering between a and b is assumed. In particular, for each fixed
positive pair (a,b), only finitely many positive tails c can possibly
give an integral graph: all such c satisfy c<=R(a,b).

The cutoff is deliberately conservative. Its purpose is a uniform,
effective tail theorem, independent of the midpoint conditions and
without parameter scans. It does not complete the classification,
since a and b remain unbounded and the remaining finite tail ranges
have not been classified.

## Two distinct bounded restricted roots

Retain the graph convention: nonzero proper ideals of Z_n are adjacent
when their intersection is nonzero. The established
[antisymmetric support embedding](four-prime-pair-three.md) gives
the genuine complement restriction K-I, with

```text
K = [(a+1)(b+1)(c+1)+a, ac,          ab,          abc]
    [a,                   (a+1)(b+1), ab,          0  ]
    [a,                   ac,          (a+1)(c+1), 0  ]
    [a,                   0,           0,          a+1].
```

The positive diagonal D=diag(1,c,b,bc) symmetrizes K. Write its
real eigenvalues in increasing order as kappa_1,...,kappa_4.
Because K-I is an actual Laplacian restriction, kappa_i>=1.
The earlier tensor argument proves the stronger kappa_i>1, but
the weak inequality suffices here.

The principal submatrix of the symmetric similar operator on the
second and fourth coordinates is diag(M,a+1). Cauchy interlacing
therefore gives kappa_2<=M. To separate the two lower roots strictly,
consider the symmetric matrix D(K-(a+1)I). Its principal block on
the second and third coordinates is

```text
bc * [[a+1,a],[a,a+1]],
```

which is positive definite. Its Schur complement on the first and
fourth coordinates has the form

```text
[[E,abc],[abc,0]],
```

with determinant -a^2b^2c^2<0. Thus the complete shifted operator
has exactly one negative and three positive eigenvalues. Congruence
with the symmetric similar operator of K preserves this inertia,
so

```text
1<=kappa_1<a+1<kappa_2<=M.
```

In particular, the two lower roots are distinct and uniformly bounded
as c grows. This uses interlacing only for the bounds; all witnesses
remain eigenvalues of the genuine invariant restriction.

## The leading tail quadratic cannot have two integer roots

Put p(x)=det(xI-K). Only the first and third rows depend on c,
so there are integer-coefficient polynomials F,G,H with

```text
p(x)=F(x)c^2+G(x)c+H(x).
```

Direct determinant expansion gives

```text
F(x)=(a+1)^2(b+1)x^2
     -(a+1)(b+1)(a^2+2ab+4a+b+2)x
     +(2a+1)(a+b+1)(2ab+a+b+1).
```

This quadratic cannot have two integer roots, counted with
multiplicity. Indeed their sum would be

```text
a+2b+3-(b+1)/(a+1).
```

If both roots were integers, a+1 would divide b+1. Their product
would also be an integer, forcing a+1 to divide the constant term
of F. But modulo a+1 that constant term is b^2, which is congruent
to 1 when a+1 divides b+1. Since a+1>=2, this is impossible.

Consequently F has at most one distinct integer zero. The identity
F(a+1)=-a^2b^2(2a+1)<0 also confirms the separation of its two
real limiting roots, though the argument does not require taking a
limit or estimating their distances from integers.

## A uniform determinant bound excludes new integer roots

Write K=K_0+cK_1, where

```text
K_0 = [M+a, 0, ab, 0]
      [a,   M, ab, 0]
      [a,   0, a+1,0]
      [a,   0, 0, a+1],

K_1 = [M, a,   0,   ab]
      [0, 0,   0,   0 ]
      [0, a,   a+1, 0 ]
      [0, 0,   0,   0 ].
```

For any integer k in [1,M], every entry of kI-K_0 has absolute
value at most L=M+a, and every entry of K_1 has absolute value
at most M. The determinant has 24 signed permutation terms.
Each constant-in-c term is bounded by L^4. Each coefficient linear
in c has at most two contributions per permutation, since only
two rows depend on c. Hence, uniformly over all these k,

```text
|H(k)|<=24L^4,
|G(k)|<=48ML^3.
```

Their sum is bounded by

```text
24L^4+48ML^3=24L^3(3M+a)=R(a,b).
```

If F(k) is a nonzero integer and c>R(a,b), then c>=1 and

```text
|p(k)| >= c^2-|G(k)|c-|H(k)|
        >= c^2-R(a,b)c
        >0.
```

Thus every integer zero of p in [1,M] must also be a zero of F.
If both bounded roots kappa_1 and kappa_2 were integers, their
distinctness would force two distinct integer zeros of F, contrary
to the previous argument. At least one of these actual restricted
roots is therefore noninteger.

The support embedding has weighted sum zero. Complement reflection
and restoring the a^2bc-1 universal vertices transfer any restricted
root kappa to the graph eigenvalue V+1-kappa, where
V=(a+1)^2(b+1)(c+1)-2. This is noninteger whenever kappa is
noninteger, proving the theorem.

## Coverage beyond the midpoint regions

For any a>=5 take b=a and any c>R(a,a). This is a new unbounded
family (a,a,a,c) relative to our preceding sufficient regions.
The product-tail failure margin is

```text
(a^2-1)(a+c)+(a-1)(2a-1)-ac
  =(a^2-a-1)c+a^3+2a^2-4a+1>0.
```

Also R(a,a)>=24a^4>5a, so r=c-a>4a. Both midpoint conditions fail:
(2a+1)r^2>8a^2, regardless of gap parity. The balanced condition
c<=2a-6 fails; the prior general comparison excludes every coordinate
of the small-exponent criterion for these repeated minima. The vector
has no unit or repeated exponent two, three or four, no double pair,
and gap greater than four. These comparisons are with our recorded
criteria, not a literature-priority claim.

For a=b=5 the explicit cutoff is 186913752. Thus the theorem includes
(5,5,5,186913753) and every larger last exponent. Such large exponents
do not require constructing the graph: the proof and controls use
only the four-dimensional restriction and 14 support classes.

## Exact checks and remaining question

The [checker](../scripts/check_four_prime_large_tail.py) verifies the
generic tail decomposition, complete F, root-sum and modular identities,
Schur-complement determinant, coefficient majorant and coverage identity.
The [certificate](../results/four-prime-large-tail.json) records six
large-tail controls, including both integer and noninteger root sums
of F and a control without a<=b. A seventh control at (a,b,c)=(5,5,11)
lies below the cutoff and still has an independently certified noninteger
root. Being below the cutoff does not imply integrality.

The seven controls reconstruct 392 support-column actions, weighted
zero sums, symmetry and complement/universal lifts. Forty-two independent
standard-library integer determinants reconstruct and cross-check the
quartics; fourteen additional direct endpoint determinants check the
chosen unit-interval witnesses. Exact root isolation and Sturm counts
verify the two bounded roots and the noninteger witnesses. The fixed
controls validate the implementation; they are not a finite base for
the theorem.

No exponent scan, expanded graph, floating eigensolver, historical
finite-base rerun or Lean validation is used. The midpoint and
small-gap results remain available, and the focused three-prime main
and all of its finite inputs are retained. The next structural problem
is to sharpen the determinant majorant or control the remaining
intermediate tails below it and outside the other sufficient regions.
The unbounded single-pair, fully unequal four-prime and higher-prime
classification remains open. Final manuscript inclusion and a natural
stopping/submission decision remain joint author decisions.
