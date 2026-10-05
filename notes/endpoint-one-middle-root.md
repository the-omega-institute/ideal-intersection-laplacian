# Locating the smallest residual root relative to the middle exponent

Let C be the six-support complement quotient. Assume real 4<=a<=b<=c
and h_C(1)=0, where h_C(x)=det(xI-C)/x=(x-1)F(x). Write the quotient
eigenvalues, with multiplicity, as

```text
0=lambda_1<lambda_2=1<lambda_3<=lambda_4<=lambda_5<=lambda_6,
mu_i=lambda_(i+2), i=1,2,3,4.
```

The [minimum-root theorem](endpoint-one-minimum-root.md) gives mu_i>a,
and the [pair-sum bound](endpoint-one-pair-sum-window.md) gives
mu_1<min(c,a+b). Put E=c+a-b(b+2). Then:

- If E>0, mu_1>b.
- If E<0, exactly one residual root lies below b, and
  a<mu_1<b<mu_2.
- If E=0, the subsequent [equality theorem](endpoint-one-equality-root.md)
  identifies mu_1=b as simple, with all other residual roots greater than b.

These are written statements on the unbounded real endpoint-one surface,
not a finite computation or an integer-feasibility theorem.

## Determinant sign and interlacing

Put s=a+b+c and r=abc. The existing generic exponent identity gives

```text
h_C(b)=-r^2(b^2+3b-s)=r^2 E,
F(b)=r^2 E/(b-1).
```

The denominator is positive. Work with the symmetric similarity S of C;
its principal blocks have the same eigenvalues as the corresponding
diagonally similar blocks of C.

First, the three-support block on 12,13,23 is diag(c,b,a).
Its second eigenvalue is b, so principal interlacing gives lambda_5>=b,
and hence mu_3>=b. If E<0, F(b)<0, and no residual root equals b.
At most two residual roots can lie below b. For the monic quartic with
four real roots, its negative value at b means an odd number of roots
lies below b. Therefore exactly one does: mu_1<b<mu_2. The earlier
lower bound supplies a<mu_1.

For E>0, use the four-support block on 3,12,13,23 from the earlier
pair-sum proof. Its eigenvalues are a,b,rho_-,rho_+, with the last two
the roots of

```text
Q(x)=x^2-(ab+a+b+c)x+c(a+b).
```

They are the eigenvalues of the symmetric two-dimensional block

```text
[[ab+a+b, -sqrt(abc)],
 [-sqrt(abc), c]].
```

Its larger eigenvalue satisfies rho_+>=ab+a+b>b. Also

```text
Q(b)=a(c-b^2-b)=a(E+b-a)>0.
```

Since b<rho_+ and Q(b)>0, it follows that b<rho_-. Thus the ordered
four-support eigenvalues are a,b,rho_-,rho_+ (allowing a=b), and their
second eigenvalue is b. Interlacing gives lambda_4>=b, or mu_2>=b.
The positive value F(b) excludes equality with any residual root. At
most one residual root is below b, and the positive monic quartic value
requires an even number. There are therefore none, giving mu_1>b.

Finally, E=0 gives F(b)=0 directly. Its index and simplicity are proved
in the equality theorem by a double principal eigenvalue and the nonzero
coupling to the deleted coordinate. Integer endpoint feasibility and
integer splitting of the other residual factor remain separate questions.

## Refined integer divisor windows

For an integer endpoint-one triple with an integer spectrum, its smallest
residual root must divide N=rs(p+s). The strict regimes refine the window:

```text
E>0: b<d<min(c,a+b),
E<0: a<d<b.
```

The second upper bound is sharper than both c and a+b. The first improves
the lower endpoint from a to b when a<b. The existing coefficient and
exponent congruences can be applied inside these smaller windows. At E=0,
b itself is an integer residual root, but the other roots still need
checking. No uniform exclusion of all surviving triples is claimed.

## Exact controls on real endpoint points

For two selected fully distinct fixed pairs, exact cubic signs and Sturm
counts locate the unique real c>b with h_C(1)=0:

| (a,b) | Exact bracket for c | Threshold b(b+2)-a | Branch | New mu_1 window | Previous window |
|---|---|---:|---|---|---|
| (9,12) | (177,178) | 159 | E>0 | (12,21) | (9,21) |
| (9,30) | (247,248) | 951 | E<0 | (9,30) | (9,39) |

Each endpoint cubic has exactly one root on c>b and exactly one in its
displayed bracket. These c values are real algebraic exponent parameters,
not integer triples. They demonstrate that both strict regimes occur on
the real endpoint surface and that each improves a different side of
the window. The unbounded proof does not depend on these controls.

The [checker](../scripts/check_endpoint_one_middle_root.py) verifies the
generic six-support determinant, residual identity, weighted symmetry,
both principal blocks, characteristic factorization and Q(b) identity,
then the two selected exponent cubics with exact signs and Sturm counts.
The [certificate](../results/endpoint-one-middle-root.json) records all
identities, controls and source hashes. Full Q3, integer feasibility and
uniform integer splitting remain open. No exponent/modulus scan, higher
two-adic lifting, floating spectrum or Lean verification is used; prior
manuscript, proofs and finite dependencies remain unchanged.
