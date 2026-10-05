# A pair-sum upper bound on the second nonzero quotient root

Let C be the six-support complement quotient in support order
1,2,3,12,13,23, with positive real exponents a<=b<=c. Write its
eigenvalues, counted with multiplicity, as
0=lambda_1<lambda_2<=...<=lambda_6.

**Universal upper bound.** For every such positive real triple,

```text
lambda_3<a+b.
```

There is no endpoint, integer or minimum hypothesis in this bound.
Together with the [previous strict bound](endpoint-one-divisor-window.md),
lambda_3<min(c,a+b). The proof uses only a four-dimensional principal
block and Cauchy interlacing, with no finite computation.

## The four-dimensional principal block

Use the symmetric similarity S=W^(1/2)CW^(-1/2), where
W=diag(a,b,c,ab,ac,bc). On supports 3,12,13,23 its principal block is

```text
P = [[ab+a+b, -sqrt(abc), 0, 0],
     [-sqrt(abc), c,     0, 0],
     [0,             0, b, 0],
     [0,             0, 0, a]].
```

The two-dimensional block has characteristic polynomial

```text
Q(x)=x²-(ab+a+b+c)x+c(a+b).
Q(a+b)=-ab(a+b)<0.
```

It is real symmetric with positive trace and determinant, so it has
two positive eigenvalues rho_-<rho_+. The negative value at a+b proves
rho_-<a+b<rho_+. The other two principal eigenvalues are a and b,
both strictly below a+b. Thus exactly three eigenvalues of P lie
below a+b. In ordered notation its third eigenvalue is
beta_3=max(b,rho_-)<a+b. Interlacing between dimensions six and four
gives lambda_3<=beta_3, proving the theorem.

For a more precise bound, the same argument gives

```text
lambda_3<=max(b,rho_-),
rho_-=[ab+a+b+c-sqrt((ab+a+b-c)²+4abc)]/2.
```

The inequality here can be non-strict; the simpler upper bound a+b is
strict. The nonsymmetric principal block of C has the same spectrum:
diagonal similarity restricts to the selected supports.

## Endpoint-one integer candidates

On h_C(1)=0 at 4<=a<=b<=c, the
[minimum-dependent theorem](endpoint-one-minimum-root.md) makes root one
simple and smallest positive, with the smallest quartic root
mu_1=lambda_3>a. Combining the written bounds gives

```text
a<mu_1<min(c,a+b).
```

For integer exponents and a hypothetical integer spectrum, the positive
constant F(0)=rs(p+s), s=a+b+c,p=ab+ac+bc,r=abc, therefore requires

```text
mu_1 in {d>0 : d divides rs(p+s), a+1<=d<=min(c,a+b)-1}.
```

This strengthens the previous [a+1,c-1] window. It remains a finite
necessary test for each fixed triple; a surviving root would still
require checking the other factors. The full unbounded endpoint-one
surface and Q3 are not decided by this bound.

Only the three established endpoint-one controls are checked:

| (a,b,c) | New upper endpoint | Candidate divisors | Number |
|---|---:|---|---:|
| (8,8,105) | 16 | 10,11,12,14,15 | 5 |
| (9,9,136) | 18 | 11,12,14,16,17 | 5 |
| (20,20,741) | 40 | 21,22,24,25,26,28,30,33,34,35,37,38,39 | 13 |

All 23 exact integer Horner values are nonzero. Independent rational
factorization agrees, and exact Sturm counts give one quartic root in
(a,min(c,a+b)) in each control and no quartic roots on [0,a]. The
previous wider window had 34,35,183 candidates. These controls were
already nonintegral by the repeated-exponent theorem; no new
nonintegrality family is claimed.

The [checker](../scripts/check_endpoint_one_pair_sum_window.py) reconstructs
the generic quotient, weighted symmetry, principal block, factored
principal characteristic polynomial, discriminant and strict sign identity.
The [certificate](../results/endpoint-one-pair-sum-window.json) includes
all candidate divisors, evaluations and source hashes. Infinite bounds
have written proofs; the three controls are finite exact diagnostics.
No parameter/modulus scan, floating spectra or Lean verification is used.
