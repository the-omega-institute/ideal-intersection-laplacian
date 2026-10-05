# A valuation obstruction at the exceptional prime thirteen

Fix an integer equality point c=b(b+2)-a, q=ac, G(q,b)=0, with b>0.
The established monic cubic P3 has discriminant Delta(q,b). The
[ordinary local splitting theorem](endpoint-one-equality-local-splitting.md)
leaves the negative branch at p=13 exceptional because its leading
normalized discriminant is divisible by13. Its next term gives a new
uniform obstruction.

**Theorem.** Suppose13 divides b and q=-1mod13, equivalently a²=1mod13.
If b is not104mod169, then P3 does not split over Q_13, and the ideal
intersection graph has a noninteger Laplacian eigenvalue. Thus an integral
equality spectrum on this negative branch requires b=104mod169.
In particular,13² cannot divide b on that branch.

This condition leaves the positive branch q=1mod13 unchanged: it splits
over Z_13 by the earlier three simple-root lifts. It does not exclude
all equality points with13 dividing b.

## Exact anchor and proof

Put e=v_13(b)>=1 and choose the refined anchor

```text
w=-1+2b+3b²+(7/2)b³.
```

The coefficient1/2 is integral at13. Direct substitution into the
established curve and discriminant formulas gives identities in Z[1/2][b]:

```text
G(w,b)=b⁴ S(b),
S(b)=(143/4)b³+(185/4)b²+43b-37/2,
Delta(w,b)=13b²-18b³+b⁴ T(b),
T(b) in Z[1/2][b].
```

The complete coefficients of T are in the exact certificate. The curve
difference identity remains

```text
G(q,b)-G(w,b)=(q-w)[(3b-1)(q+w)+b(b²+4b-1)].
```

Both q and w reduce to-1mod13, so the bracket is2mod13, a unit.
Since G(q,b)=0, the anchor identity implies q-w is divisible by13^(4e)
in Z_13. Delta is an integer polynomial in q,b; its difference at q,w
is divisible by q-w. Consequently

```text
Delta(q,b)=13b²-18b³ mod13^(4e).
```

If e>=2, the two displayed terms have valuations2e+1 and3e,
respectively, and the remainder has valuation at least4e. The first
valuation is strictly smaller than both others, so
v_13(Delta)=2e+1, which is odd. A nonzero square in Q_13 has even
valuation, hence Delta is nonsquare.

If e=1, write b=13u with u a13-adic unit. The same congruence gives

```text
Delta=13³ u²(1-18u) mod13⁴.
```

Unless u=8mod13, the parenthesis is a unit:18u=1mod13 has the unique
solution u=8. Thus v_13(Delta)=3 in every other unit class, again odd.
The sole remaining condition is b=13*8=104mod169, which already implies
e=1. On that class Delta is divisible by13⁴; this argument does not
decide its square status.

A split monic cubic has discriminant equal to the square of the product
of its root differences. Therefore nonsquare Delta rules out splitting
over Q_13 and, in particular, over the integers. The established equality
factorization h_C=(x-1)(x-b)P3 and the complement/universal-vertex lifts
give the graph's Laplacian nonintegrality.

## Verification and next question

The [checker](../scripts/check_endpoint_one_equality_thirteen.py) verifies
both anchor identities, the coefficient ring, the curve difference unit,
discriminant difference divisibility and the unique linear residue8.
It independently reconstructs the generic cubic from the six-support
quotient and its discriminant from a5x5Sylvester determinant through the
existing cubic checker. This is exact symbolic validation of the identities
used by the written valuation argument. No prime/power/exponent table or
finite exponent base is used, and no integer equality point is asserted.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_one_equality_thirteen.py
```

Compare with [the certificate](../results/endpoint-one-equality-thirteen.json).
The focused remaining local case is q=-1mod13, b=104mod169. Deriving the
next discriminant term there can distinguish its valuation and unit;
the positive branch's local compatibility, four necessary modulo-five
pairs, and7/11divisibility exclusions are retained. Global integer equality
classification and full Q3 remain open. No Lean verification is claimed.
