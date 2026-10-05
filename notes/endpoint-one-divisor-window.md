# The endpoint-one constant and smallest quartic-root window

Let C be the six-support complement quotient in support order
1,2,3,12,13,23, with positive real exponents a<=b<=c. Put

```text
h_C(x)=det(xI-C)/x,
F(x)=[h_C(x)-x h_C(1)]/(x-1),
s=a+b+c, p=ab+ac+bc, r=abc.
```

The residual is continued polynomially at x=1. It is a monic quartic
for every triple, and is a spectral factor only when h_C(1)=0.

**Constant term.** F retains the strictly positive constant

```text
F(0)=-h_C(0)=rs(p+s)>0.
```

This follows from the generic quotient determinant, or directly from
the [symmetric quartic formula](endpoint-one-spectral-gap.md).
Imposing h_C(1)=0 does not introduce a factor x. The zero eigenvalue of
C has already been removed in h_C; division by x-1 then removes root one.

**Upper bound.** Write the eigenvalues of C, with multiplicity, as
0=lambda_1<lambda_2<=lambda_3<=...<=lambda_6. For all ordered positive
real exponents, the second smallest nonzero root satisfies

```text
lambda_3<c.
```

For the proof, use W=diag(a,b,c,ab,ac,bc). The matrix
S=W^(1/2) C W^(-1/2) is symmetric positive semidefinite: WC is symmetric
and its quadratic form is the sum of w_i w_j(z_i-z_j)^2 over unordered
disjoint support pairs. The support graph is connected, so the zero
kernel is one-dimensional. The principal block of S on supports
12,13,23 is diagonal(c,b,a), just as for C; these three supports have
no disjoint pair. Its ordered eigenvalues are a,b,c. Cauchy interlacing
for this three-dimensional principal block of a six-dimensional
symmetric matrix gives lambda_i<=beta_i<=lambda_(i+3), i=1,2,3.
Taking i=3 gives lambda_3<=c.

Equality is excluded by the exact generic identity

```text
h_C(c)=-a²b²c²(c²+2c-a-b)<0.
```

Indeed a+b<=2c and c>0 make the final factor at least c²>0.
Thus c is not any quotient eigenvalue, and lambda_3<c. This proof
does not require integer exponents, endpoint one, or minimum eight.

**Endpoint-one divisor window.** If also a>=8 and h_C(1)=0, the
[spectral-gap theorem](endpoint-one-spectral-gap.md) identifies
lambda_2=1 as simple and places all four roots of F above four.
Consequently its smallest root mu_1=lambda_3 satisfies

```text
4<mu_1<c.
```

For integer exponents and a hypothetical integer spectrum, the rational
root theorem for the monic integer quartic therefore forces

```text
mu_1 in {d>0 : d divides rs(p+s), 5<=d<=c-1}.
```

For a fixed integer endpoint-one triple, enumerate these positive
divisors and evaluate F(d) exactly. If none vanishes, mu_1 is noninteger,
so the quotient and the original graph cannot have an integer spectrum.
The original graph and complement quotients are related by the
established integral reflection on nonzero roots. A surviving candidate
does not by itself prove integrality; the remaining factors still need
checking. The finite divisor procedure decides this particular necessary
condition for each fixed triple. It does not decide the entire unbounded
endpoint-one surface without an additional uniform argument. Full Q3
and the previously recorded surviving exponent region remain open.

## Exact diagnostics on the established controls

Only the three previously used repeated-exponent endpoint-one controls
are tested; no parameter or modulus range is expanded.

| (a,b,c) | F(0) | Divisors in [5,c-1] | Zeros among candidates |
|---|---:|---:|---:|
| (8,8,105) | 1516468800 | 38 | 0 |
| (9,9,136) | 4551612912 | 39 | 0 |
| (20,20,741) | 7134703976400 | 197 | 0 |

The exact factorizations are

```text
(8,8,105): F=(x-968)(x³-1138x²+177145x-1566600),
(9,9,136): F=(x-1386)(x³-1604x²+322939x-3283992),
(20,20,741): F=(x-15620)(x³-16762x²+18415981x-456767220).
```

Each has exactly one quartic root in (4,c) by exact Sturm counts and no
integer root in that window by independent rational factorization.
The roots 968,1386,15620 lie above the window and do not provide its
smallest root. These examples already follow from the repeated-exponent
nonintegrality theorem; the diagnostics demonstrate the requested
divisor procedure rather than establish a new family.

Run `python3 scripts/check_endpoint_one_divisor_window.py` to reconstruct
the generic quotient, constant identity, weighted symmetry, principal
block and strict-bound determinant identity, then check every candidate
with integer Horner evaluation and rational factorization, with exact
Sturm counts on the three controls. The
[certificate](../results/endpoint-one-divisor-window.json) records all
candidate divisors, evaluations and source hashes. The infinite constant
and upper-bound results have written proofs; the three diagnostics are
finite exact checks. No Lean verification is claimed.
