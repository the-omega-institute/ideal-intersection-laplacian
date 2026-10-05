# A global gap between the two smallest and three largest positive roots

Let C be the six-support complement quotient in support order
1,2,3,12,13,23, and let 2<=a<=b<=c be real exponents. Its eigenvalues,
counted with multiplicity, satisfy

```text
0=lambda_1<lambda_2<=lambda_3<=lambda_4<=lambda_5<=lambda_6.
```

**Theorem.** Throughout this real domain,

```text
lambda_3<a+b<=b+c<lambda_4.
```

There is no endpoint, parity, integrality or equality-curve hypothesis.
This extends the earlier [pair-sum upper bound](endpoint-one-pair-sum-window.md)
and strengthens the [equality-only lower bound](endpoint-one-equality-second-root.md).
The proof is written, using principal interlacing and an exact determinant sign.

## The quotient and its symmetric similarity

In this support order,

```text
C = [[b+c+bc, -b, -c, 0, 0, -bc],
     [-a, a+c+ac, -c, 0, -ac, 0],
     [-a, -b, a+b+ab, -ab, 0, 0],
     [0, 0, -c, c, 0, 0],
     [0, -b, 0, 0, b, 0],
     [-a, 0, 0, 0, 0, a]].
```

With W=diag(a,b,c,ab,ac,bc), WC is symmetric and
S=W^(1/2)CW^(-1/2) is real symmetric. The weighted Laplacian quadratic
form is positive semidefinite. Its support graph is connected, so zero
is simple and the other five eigenvalues are positive. Diagonal
similarity restricts to principal blocks, permitting computations with C.

## Three eigenvalues below a+b

The principal block on supports 3,12,13,23 has eigenvalues a,b,rho_-,rho_+,
where rho_- and rho_+ are the roots of

```text
Q(x)=x²-(ab+a+b+c)x+c(a+b).
Q(a+b)=-ab(a+b)<0.
```

Its symmetric similarity gives real roots; the sign places
rho_-<a+b<rho_+. Since a,b<a+b, its third ordered eigenvalue is
max(b,rho_-)<a+b. Cauchy interlacing gives lambda_3<a+b.
This part holds for all ordered positive real exponents.

## Two eigenvalues above b+c

Delete support 3. The remaining five-dimensional principal block splits
as the scalar c on support 12 and a four-dimensional block T on
1,2,13,23. The symmetric principal block of T on 1,2 is

```text
K = [[b+c+bc, -sqrt(ab)],
     [-sqrt(ab), a+c+ac]].
K-(b+c)I = [[bc, -sqrt(ab)],
            [-sqrt(ab), a(c+1)-b]].
```

The first leading principal minor is bc>0. The determinant is

```text
b[a(c²+c-1)-bc]>0,
```

because a>=2 and b<=c imply

```text
a(c²+c-1)-bc >= 2(c²+c-1)-c² = c²+2c-2 > 0.
```

Sylvester's criterion therefore puts both eigenvalues of K above b+c.
Interlacing puts both largest eigenvalues of T above b+c, then both
largest eigenvalues of the five-dimensional block, and finally
lambda_5 and lambda_6 strictly above b+c.

## The determinant locates the fourth eigenvalue

Write h_C(x)=det(xI-C)/x. Direct expansion gives, for any selected
pair of exponents u,v and remaining exponent w,

```text
h_C(u+v)=-uvw(u+v+1)V_{u,v;w},
V_{u,v;w}=uv(u+v)(w-1)+w[uv-u-v+w].
```

For u=b,v=c,w=a, both terms in V are positive: a-1>0 and
bc-b-c+a=(b-1)(c-1)+a-1>0. Consequently

```text
det((b+c)I-S)=(b+c)h_C(b+c)<0.
```

No eigenvalue equals b+c. At least three eigenvalues lie below it,
and the two high eigenvalues just proved leave at most four below it.
In dimension six the negative determinant requires an odd number of
eigenvalues below b+c, counting multiplicity. Thus exactly three lie
below it, and lambda_4>b+c. This proves the theorem, including repeated
exponents and repeated eigenvalues.

## Consequence for the residual endpoint-one quartic

On h_C(1)=0 with real 4<=a<=b<=c, the
[minimum-root theorem](endpoint-one-minimum-root.md) gives lambda_2=1
simple and all four residual roots above a. Combining the earlier
strict c bound and the present theorem, their ordered roots satisfy

```text
a<mu_1<min(c,a+b),
b+c<mu_2<=mu_3<=mu_4.
```

In particular, the three larger roots are separated from the smallest
by the entire pair-sum interval [a+b,b+c]. At an integer endpoint-one
triple, integral splitting would require mu_2,mu_3,mu_4>=b+c+1, alongside
the existing smallest-root equation and divisor window. This necessary
condition does not yet exclude every integer spectrum.

The next concrete question is whether these stronger three-root bounds,
combined with the quartic's exact coefficients and the smallest-root
equation, force a noninteger root in the remaining endpoint-one region.
The general three-prime classification remains open. Closing that
classification would still leave nonsquarefree exponent vectors with
more than three prime factors in the full Q3 question.

## Exact supplementary verification

The [checker](../scripts/check_global_pair_sum_separation.py) reconstructs
the quotient, weighted symmetry, both principal decompositions, shifted
two-dimensional determinant, and the generic pair-sum identity. It checks
five specified controls: (2,2,3), (4,4,4), (9,9,136), (9,12,159), and
(9,30,951), with independent 6x6 Bareiss evaluations at both pair sums.

Sturm counts are summed over squarefree factors with their multiplicities.
The repeated control (4,4,4) has characteristic polynomial
x(x-20)(x²-32x+48)²: it has three eigenvalues below eight, although only
two distinct roots there. On the established endpoint-one control
(9,9,136), the quartic has one root below b+c and three above it.
The [certificate](../results/global-pair-sum-separation.json) records these
finite diagnostics and source hashes. They supplement the written theorem;
there is no parameter scan, floating spectrum or Lean verification.
Existing manuscript and historical certificates retain their scopes.
