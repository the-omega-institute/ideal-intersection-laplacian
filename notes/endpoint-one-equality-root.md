# The equality root is simple and second smallest nonzero

**Unconditional equality theorem.** For real4<=a<=b and c=b(b+2)-a,
the six-support complement quotient has b as its simple second smallest
nonzero eigenvalue:

```text
0=lambda_1<lambda_2<lambda_3=b<lambda_4<=lambda_5<=lambda_6.
```

No endpoint-one hypothesis is needed; c>b holds automatically.
If also h_C(1)=0, the earlier [minimum-root theorem](endpoint-one-minimum-root.md)
gives lambda_2=1. Therefore mu_1=b is simple, and all three other residual
roots exceed b. Together with the [strict regimes](endpoint-one-middle-root.md),
this completes the real endpoint-one partition:

```text
sign(mu_1-b)=sign(c+a-b(b+2)); in every regime mu_2>b.
```

These statements have written unbounded proofs. They do not classify
integer equality points or prove integer spectra.

## A double principal eigenvalue determines the full index

Use the symmetric similarity S=W^(1/2)CW^(-1/2), with
W=diag(a,b,c,ab,ac,bc). Connectedness and positive support weights make
S positive semidefinite with a one-dimensional kernel whose vector has
every coordinate nonzero. Every proper principal block is positive definite.

Delete singleton support2. The five-support block B on 1,3,12,13,23
is the direct sum of the scalar b on support13 and the four-support block
T on 1,3,12,23. Support13 is only coupled to the deleted singleton2.
On c=b^2+2b-a, exact factorization gives

```text
det(xI-T)=(x-b)K(x),
K(x)=x^3-Lx^2+Mx-abc(b+3),
L=b(b^2+4b+5),
M=ac(b^2+1)+b^2(b+2)(b^2+3b+3).
```

K has three positive real roots with multiplicity, since T is symmetric
positive definite and b>0. Its value at b is

```text
K(b)=b(b+1)R>0,
R=a(b-a)(b-2)+ab(b-2)(b+1)+b^2(b+1)(b+2).
```

All terms of R are nonnegative and the last two are positive. Thus b
is simple in T. The pair-support block on 12,23 is diag(c,a), so
interlacing puts the largest eigenvalue of T at least c>b. At least
one K root therefore exceeds b. A positive monic cubic value K(b)
requires an odd number of roots below b; it cannot be three. Exactly
one K root lies below b and the other two lie above.

B consequently has ordered eigenvalues

```text
beta_1<b=beta_2=beta_3<beta_4<=beta_5.
```

Five-support interlacing in S gives beta_2<=lambda_3<=beta_3,
which forces lambda_3=b.

## The nonzero coupling proves simplicity

Put the deleted singleton2 coordinate last and write

```text
S-bI=[[B-bI,u],[u^T,tau]].
```

The kernel of B-bI has dimension two. The unit vector v on support13
belongs to that kernel, and v^T u=-sqrt(abc) is nonzero. For a full
eigenvector (z,t), the equation (B-bI)z+ut=0, multiplied by v^T,
forces t=0. The remaining equations are z in ker(B-bI) and u^Tz=0.
The second is a nonzero linear condition on a two-dimensional kernel,
so the full eigenspace has dimension one. Symmetry equates geometric
and algebraic multiplicities. Thus b is simple and lambda_2<b<lambda_4.

This argument uses a coupling uniformly nonzero throughout the domain;
it is not inferred from generic symbolic rank or finite examples.

## Remaining integer questions and exact diagnostics

On endpoint one, b=lambda_3=mu_1 and F(x)=(x-b)P_3(x), where P_3 is
monic and its three roots exceed b. At an integer equality point P_3 has
integer coefficients. The earlier [G(a,b)=0 equation](endpoint-one-root-hierarchy.md)
still controls whether such an integer endpoint-one point exists.
If it does, integer spectra still require P_3 to split into three integer
roots greater than b. This note resolves b's index and simplicity; integer
feasibility and the remaining cubic splitting stay open.

| (a,b,c) | Other nonzero quotient roots below b | Above b | Full multiplicity of b | Endpoint one? |
|---|---:|---:|---:|---|
| (4,4,20) | 1 | 3 | 1 | no |
| (9,12,159) | 1 | 3 | 1 | no |
| (9,30,951) | 1 | 3 | 1 | no |

These three selected integer triples have E=0 but are off endpoint one.
Exact Sturm counts on h_C(x)/(x-b), nonzero derivatives at b and direct
matrix ranks agree with the unconditional theorem. They do not demonstrate
integer solutions of G(a,b)=0. The written theorem has no finite base.

The [checker](../scripts/check_endpoint_one_equality_root.py) verifies generic
weighted symmetry, both characteristic factors, positive K(b) identity,
pair block and nonzero scalar coupling, then exact counts and ranks on
the controls. It also checks the residual's synthetic-division remainder,
which vanishes under E=0,h_C(1)=0. The
[certificate](../results/endpoint-one-equality-root.json) retains identities,
controls and source hashes. No parameter/modulus scan, higher two-adic
lift, floating spectrum or Lean was used. Prior manuscript and finite
dependencies remain unchanged; full Q3 remains open.
