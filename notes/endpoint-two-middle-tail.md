# A middle-exponent bound from the full endpoint-two determinant

For ordered exponents **`4<=a<=b<=c`**, we prove

```text
b>=2a-2  =>  h_C(2)>0.
```

Consequently the six-support complement quotient has a positive root in
`(0,2)`. This proves nonintegrality for all-even triples and permutations
of `(1,3,2)` or `(3,3,0)` modulo four. For the mixed patterns, exclusion
of the integer root one is conditional on an integer spectrum, as in
the existing [root-distribution proof](mixed-endpoint-roots.md).

In particular, **every endpoint-two zero with ordered minimum at least
four requires `b<2a-2`**. Combining this with the existing maximum bound,
the unresolved endpoint-two candidates satisfy

```text
4<=a<=b<=c,  b<2a-2,  c<7a-16+40/(a+2).
```

The subsequent [maximum-tail proof](endpoint-two-maximum-tail.md) strengthens
the last inequality to `c<3a-4`, using this bounded middle interval.

This settles the entire `b>=2a+2` branch left untouched by the preceding
[principal-block test](endpoint-two-middle-inertia.md), and extends the
exclusion down to `b=2a-2`. It does not close the surviving endpoint-two
surface or the other mixed-parity endpoint-one cases.

## The full determinant rather than one principal block

Let `C` be the established six-support complement quotient and
`h_C(x)=det(xI-C)/x`. At two, the Schur complement is

```text
K(2)=diag(k_a,k_b,k_c)-vv^T,
k_t=a+b+c-2-2abc/[t(t-2)],
v=(sqrt(a),sqrt(b),sqrt(c)).
```

The exact determinant relation is

```text
2h_C(2)=(a-2)(b-2)(c-2)det K(2).
```

The earlier principal a,b test can fail when the full determinant is
positive. For example, `(20,42,46)` has `k_b>0` and
`Delta_ab=k_a*k_b-a*k_b-b*k_a<0`. Both preceding sufficient tests fail,
but the polynomial positivity proved here still gives a root in `(0,2)`.
The result therefore uses the remaining block through the full determinant.

## A positive expansion at the boundary

Write `b=2a-2+u` and `c=b+v`, with `u,v>=0`. Define

```text
A(u)=2u^2+7(a-2)u+2(3a^2-14a+12),

B(u)=(a+2)u^3+(4a^2+10a-12)u^2
     +(4a^3+25a^2-48a+12)u+2(13a^3-28a^2+8a+8),

D(u)=2(a-2)(9a^3+24a^2-56a+16)
     +(33a^3+20a^2-208a+136)u
     +(20a^2+23a-62)u^2+4(a+2)u^3,

E(u)=2(3a^3-a^2-8a+4)+(5a^2+3a-10)u+(a+2)u^2.
```

Direct polynomial expansion gives the identity

```text
h_C(2)=A(u)B(u)+(A(u)B(u))prime*v/2+D(u)v^2+E(u)v^3.
```

Here the prime denotes differentiation with respect to u. One can also
obtain the linear coefficient from symmetry in b,c: the derivative of
`h_C(2)` along the diagonal `b=c` is twice the partial derivative in c.
The constant term factors as `A(u)B(u)` on that diagonal.

Every coefficient of A, B, D and E is strictly positive for `a>=4`.
For example, `3a^2-14a+12` equals four at a=4 and increases thereafter;
`13a^3-28a^2+8a+8=a^2(13a-28)+8a+8>0`.
The remaining coefficients have the same elementary positivity; equivalently,
substituting `a=4+m` gives positive constants and nonnegative coefficients
in m for each of them. The exact coefficient expansions are retained in
the [certificate](../results/endpoint-two-middle-tail.json).

Thus A and B are strictly positive for u>=0, while `(AB)prime`, D and E
are positive. The displayed formula proves `h_C(2)>0` for all u,v>=0,
including both boundary equalities. As an additional identity check, the
fully expanded polynomial in `(m,u,v)` has 69 nonzero terms, all with
positive coefficients, and constant term 6784.

## From the endpoint sign to nonintegrality

The established quotient identity gives

```text
h_C(0)=-abc(a+b+c)(a+b+c+ab+ac+bc)<0.
```

Together with `h_C(2)>0`, the intermediate value theorem gives a positive
quotient root strictly between zero and two. All-even triples cannot have
the integer eigenvalue one: C/2 is an integer matrix, so a hypothetical
integer spectrum of C has only even roots. For the two stated mixed
patterns, the prior shifted-quintic identity forces hypothetical odd
integer roots to be three modulo four, likewise excluding one.
The root in `(0,2)` therefore proves nonintegrality in these classes.
The established complement and universal-class lifts transfer the result
to the ideal intersection graph.

The positivity of `h_C(2)` and the bound on its zero surface hold for
every ordered triple in the theorem, regardless of parity. Nonintegrality
from this interval additionally uses exclusion of one; no such exclusion
is asserted here for the other mixed-parity classes.

## Exact checks and remaining scope

Run with SymPy 1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_middle_tail.py
```

The checker reconstructs the general 6x6 quotient, verifies its full Schur
determinant relation at two, the b,c symmetry, and the positive expansion
coefficientwise. Five selected direct integer quotient/Horner/Sturm fixtures
include `b=2a-2`, `b=2a+2`, a mixed-parity example outside the six mixed
modulo-eight rows, the equality `b=c`, and `(20,22,32)` outside the new tail.
The latter has no positive quotient root below two and is not claimed
integral. The retained endpoint-zero control `(10,10,12)` lies below the
middle bound; an endpoint zero does not imply integrality.

The infinite result follows from the written positivity proof. The fixed
fixtures are finite checks, with no enlarged exponent/modulus search,
floating spectrum or Lean verification. The manuscript remains unchanged
while this standalone deduction is reviewed. Full Q3, the surviving
endpoint-two region and the other endpoint-one cases remain open.

[Return to the project entrance](../README.md).
