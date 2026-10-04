# Existence and uniqueness on the endpoint-two surface

For fixed real exponents **`a>=8,b>=a`**, the equation `h_C(2)=0`,
viewed as a polynomial equation in c, has a solution **`c>b` if and only if**

```text
R_a(b)=-(a+2)b^3+2a(a-2)b^2-(a+6)(a-2)b-2(a-2)^2 > 0.
```

When this condition holds, the real solution is **unique and simple as
a root of the polynomial in c**. This is a statement about the exponent
parameter c, not an additional claim about spectral multiplicity at two.
Whether that unique real exponent is an integer remains a separate question.

The function `R_a(b)/b^2` strictly decreases for b>=a. It has a unique
zero `beta(a)` with `a<beta(a)<2a-2`. Every ordered endpoint-two zero
with c>b therefore requires the sharper middle condition **`b<beta(a)`**,
in addition to the [maximum bound `c<3a-4`](endpoint-two-maximum-tail.md).

Two concrete consequences are:

- `beta(8)` lies in `(8,9)`. No fully distinct integer triple with minimum
  eight has an endpoint-two zero. All-even and `(1,3,2)/(3,3,0)` modulo-four
  triples with this minimum are therefore nonintegral; other endpoint-one
  cases are not settled by this argument.
- `beta(20)` lies in `(32,33)`, so an integer middle exponent must be at
  most32, improving the preceding `b<38` condition. At the fixed pair
  `(a,b)=(20,22)`, the unique real solution in c lies in `(32,33)` as well.
  Thus there is no integer endpoint-two solution for this entire pair,
  and every all-even `(20,22,c)` with c>22 is nonintegral.

## The diagonal factorization

Write `Q(c)=h_C(2)` with a,b fixed and let `v=c-b`. The generic quotient
identity gives

```text
Q(b+v)=L_a(b)R_a(b)+S_a(b)v+T_a(b)v^2+U_a(b)v^3,
L_a(b)=ab+2a-2b^2+6b-4,
2S_a(b)=(L_a(b)R_a(b))prime.
```

Here the prime means differentiation in b with a fixed. The last identity
also follows from symmetry of the endpoint polynomial in b,c: the
derivative along b=c is twice the partial derivative in c.

For a=8+m,b=a+d with m,d>=0,

```text
-L_a(b)=m^2+3md+8m+2d^2+18d+4>0,
L_a(b)prime=-3a+6-4d<0.
```

Both T and U have strictly positive coefficients in m,d. The complete
coefficient vectors are given here in ascending powers of m; each row
is the coefficient of the indicated power of d.

| d power | T coefficient vector | U coefficient vector |
|---|---|---|
| 0 | [10488,4748,758,49,1] | [1180,428,51,2] |
| 1 | [4144,1400,150,5] | [214,51,3] |
| 2 | [682,151,8] | [10,1] |
| 3 | [40,4] | [0] |

Thus T,U>0 and `Q''(b+v)=2T+6Uv>0` for v>=0.

## A unique threshold for the middle exponent

Normalize `R=R_a(b)` by b squared:

```text
(R/b^2)prime=-(a+2)+(a+6)(a-2)/b^2+4(a-2)^2/b^3.
```

For b>=a>=8, the right side is at most `-a-1+8/a<0`.
The two exact boundary values are

```text
R_a(a)=(a-1)(a+2)(a^2-8a+4)>0,
R_a(2a-2)=-2(13a^3-28a^2+8a+8)<0.
```

The first is positive at eight and thereafter; the second is negative
since `13a^3-28a^2+8a+8=a^2(13a-28)+8a+8>0`.
Strict decrease of R/b squared and the intermediate value theorem give
exactly one threshold beta(a) in `(a,2a-2)`, with R>0 precisely below it.

## Existence, nonexistence and simplicity in c

If R>0, then L<0 makes `Q(b)<0`. As c tends to infinity, the positive
cubic coefficient gives Q(c) tending to infinity. The coefficients of
`Q(b+v)` in descending order have signs `+,+,sign(S),-`, exactly one sign
change regardless of S. Descartes' rule, together with the intermediate
value theorem, proves exactly one positive root in v. At that root v0,
strict convexity gives

```text
Q'(b+v0) > [Q(b+v0)-Q(b)]/v0 > 0.
```

The root in c is therefore simple.

If R<=0, then Q(b)>=0. The normalized derivative formula gives

```text
Rprime=b^2*(R/b^2)prime+2R/b<0.
```

Since L,Lprime<0, the identity `2S=Lprime*R+L*Rprime` makes S strictly
positive. Every coefficient of `Q(b+v)` is then nonnegative and S,T,U
are strictly positive. Thus Q(b+v)>0 for every v>0, proving nonexistence
of c>b solutions. This also handles R=0, where the diagonal c=b itself
is an endpoint zero but no strictly larger c is.

## Exact examples and spectral scope

The exact threshold evaluations are

```text
R_8(8)=280,    R_8(9)=-342,
R_20(32)=760,  R_20(33)=-22626.
```

For the pair `(20,22)`, direct quotient evaluation gives

```text
h_C(2)atc=32 = -8192000,
h_C(2)atc=33 = 3658680.
```

The theorem proves that this bracket contains the only real c>b zero.
It contains no integer, so there is no integer endpoint-two solution for
the pair. The same reasoning brackets the unique real solution for
`(20,32)` in `(32,33)`. The repeated control `(10,10,12)` has a genuine
endpoint zero and satisfies R>0; it is already known to be nonintegral.

For all-even triples and the two stated mixed modulo-four patterns, an
integer spectrum cannot contain one under the existing root-distribution
arguments. The uniform positive root in `(0,3)` would then force the
endpoint two. Nonexistence of that endpoint therefore proves nonintegrality
in these classes. The other mixed-parity endpoint-one cases remain separate.

The threshold and uniqueness statements themselves require no parity
condition. They do not prove the entire endpoint-two surface has no
integer points or that every endpoint-zero quotient has a noninteger
remaining root. The minimum exponent remains unbounded.

## Verification

The subsequent [gap-two argument](endpoint-two-gap-two.md) excludes every
integer endpoint-two solution for ordered `(a,a+2,c)` with a>=8,c>a+2.
Its uniform written bracket at a>=20 is supplemented by a complete finite
base for a=8,...,19. The [growing-gap proof](endpoint-two-growing-gap.md)
also excludes integer solutions for d=b-a>=5,a>=2d^2+20, using a written
unit-width bracket throughout that domain, with no finite base.
General integer feasibility outside these hypotheses stays open.

Run with SymPy 1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_surface_geometry.py
```

Compare with [the certificate](../results/endpoint-two-surface-geometry.json).
The checker reconstructs the generic direct6x6quotient, diagonal factors,
symmetry derivative, positive coefficient vectors, normalized derivative
and its bound, and threshold boundary identities. Five selected fixed-pair
cubics have exact Sturm counts over the whole interval c>b; seven selected
direct quotient/Horner fixtures independently check the endpoint values.
The note's coefficient vectors are checked against the saved certificate.

These fixed-pair diagnostics illustrate the written unbounded root theorem;
no pair range, exponent range or modulus range is scanned. No floating
spectrum or Lean verification is claimed. Manuscript files remain unchanged
while standalone results are reviewed. Full Q3, the general integer
endpoint-two feasibility problem, other endpoint-one cases and higher-prime
nonsquarefree vectors remain open.

[Return to the project entrance](../README.md).
