# An integrality-preserving quadratic-field reduction

**Proposition.** Put s=sqrt(43645) and K=Q(s). Every positive
integer tail pair satisfying p(2;6,b,c)=0 maps injectively to an
algebraic integer point on

```text
E0: V^2=U^3+6640150U^2+5047497487500U+1053718156603125000
```

over K. The map is polynomial in the original affine coordinates.
The explicit coefficient filter below recovers exactly the positive
integer tail pairs from a complete list of O_K-integral points on E0.
Thus the original integrality condition has a sufficient complete
enumeration target. No rank, group basis or point list is computed.

This uses the two geometric points at infinity of the
[a=6 quartic](four-prime-a6-elliptic.md), now defined over K.
The earlier rational chart and its denominator warning retain
their scope; the field and the choice of origin have changed.

## Polynomial coordinates

Retain the exact square completion

```text
A(b)=-13b^2+420b-35,
W=A(b)c+210b^2+2650b+950,
f(b)=alpha b^4+beta b^3+gamma b^2+delta b+e,
alpha=43645, beta=1152400, gamma=6640150,
delta=4524000, e=950625=975^2,
W^2-f(b)=A(b)p(2;6,b,c).
```

Define

```text
U=2alpha b^2+beta b+2sW,
V=s(4alpha b^3+3beta b^2+2gamma b+delta)
    +(4alpha b+beta)W.
```

Both coordinates are polynomials with coefficients in Z[s].
Their exact cubic identity follows from W^2=f(b) and s^2=alpha:

```text
V^2=U^3+gamma U^2+P U+R,
P=beta delta-4alpha e=5047497487500,
R=e beta^2+alpha delta^2-4alpha e gamma
 =1053718156603125000.
```

The checker verifies this identity in the quotient by
(W^2-f(b),s^2-alpha), without approximating s. This is the same
intermediate cubic as the preceding rational model, with a
different map into it. Its discriminant is

```text
16 disc_U(U^3+gamma U^2+P U+R)
 =-309476819336418859764366000000000000000 !=0.
```

For a coordinate derivation, reverse the quartic with t=1/b and
Z=W/b^2. Its constant term is alpha=s^2. The preceding
rational-point construction, now based at t=0,Z=s, gives
U=[2s(Z+s)+beta t]/t^2. This is the displayed polynomial U.
Its second coordinate initially contains a division by b;
using W^2=f(b) cancels that division and gives the polynomial V.
These formulas extend to finite b=0 as well. The positivity
domain b>0 is entirely in the affine chart.

## Why the images are algebraic integers

The factorization 43645=5*7*29*43 is squarefree and is 1 modulo
4. Consequently

```text
O_K=Z[(1+s)/2],
Z[s] subset O_K.
```

For an integer tail pair, W is an integer by its definition.
The polynomial map therefore has U,V in Z[s], hence in O_K.
It introduces no tail-dependent denominators.

If one uses the earlier short Weierstrass equation over K,
X=(9U+3gamma)/100 and Y=27V/1000, these images lie in
O_K[1/10]. Thus only primes above 2 and 5 are needed for that
particular S-integral target. The integral cubic E0 avoids those
fixed denominators entirely. This does not establish any such
prime restriction for the earlier chart on rational E-points.

## The exact conjugate-coefficient filter

Write a K-point uniquely as

```text
U=u0+u1 s, V=v0+v1 s, with u0,u1,v0,v1 in Q.
```

An O_K-integral coordinate can have half-integer coefficients in
this basis. A complete O_K list must therefore use the full ring
of integers, then apply the following filter; it must not discard
points merely because the initial coefficients are not in Z.

For images of the polynomial map,

```text
u0=2alpha b^2+beta b,
u1=2W,
v0=(4alpha b+beta)W,
v1=4alpha b^3+3beta b^2+2gamma b+delta.
```

For b>0 the polynomial f(b) is strictly positive, since all five
coefficients are positive. Hence W!=0 and u1!=0. Recover

```text
W=u1/2,
b=(2v0-beta u1)/(4alpha u1),
c=(W-210b^2-2650b-950)/A(b).
```

The last denominator never vanishes at a rational b: its
discriminant is 4*43645, which is nonsquare. These recoveries
prove injectivity on the positive rational domain. Both signs of
W must be retained; they usually give different c.

A complete O_K-integral E0-point list gives a complete root-two
tail list by this finite filter:

1. Discard u1=0; such a point cannot be an image with b>0.
2. Recover b,W and require b to be a positive integer and W an integer.
3. Check all four coefficient identities above and W^2=f(b).
4. Recover c, requiring A(b)|(W-210b^2-2650b-950) and c>0.

For repeated-minimum vectors, additionally require b,c>=6.
Necessity follows from the polynomial map and positive f.
Sufficiency follows from the checked quartic equation, the square
completion and A(b)!=0: the recovered pair has p(2;6,b,c)=0.
All checks are exact rational or integer operations. The four
coefficient identities retain the conjugation condition selecting
the original rational quartic inside the K-curve. A rank or point
computation on E0(Q) alone does not enumerate E0(K).

## The previously nonintegral image is retained

The integral quartic point (b,W)=(55,-781950) now maps to

```text
U=327434250-1563900s,
V=-8409324885000+40238718000s.
```

These coordinates are algebraic integers. Its recovered
c=26065/271 fails the final integer-tail filter, as before.
The companion W=781950 also has integral field coordinates,
but recovers c=0. The b=0,W=+/-975 controls remain polynomial
images and are rejected by b>0. None is a positive integer graph
example; they check both signs and the affine boundary.

## What remains for a complete computation

This is an exact integrality-preserving reduction. To execute it
one still needs a certified complete O_K-integral point algorithm
for E0 over this specific quadratic field. If that algorithm uses
a Mordell-Weil basis, its basis and completeness must be certified
over K. An S-integral implementation on the short model must
include both signs and every prime above 2 or 5. Arbitrary
coordinate or group-coefficient bounds cannot supply completeness.

The [checker](../scripts/check_four_prime_affine_integrality.py)
checks the cubic identity, square completion, nonsingularity,
field factorization, coefficient inverse, recovery denominators
and short-model scaling. Four specified integral quartic points
check algebraic integer coordinates and exact coefficient recovery,
including rejection by the final tail filter. The
[certificate](../results/four-prime-affine-integrality.json) is
reproducible with SymPy 1.14.0 using
`python3 scripts/check_four_prime_affine_integrality.py`.

No rank, group basis, complete integral-point algorithm, exponent
scan, graph expansion, historical finite-base rerun, floating
eigenvalues or Lean validation is used. An integer root two alone
does not imply integer graph spectrum. The previous finiteness
theorem, all nonintegrality results and finite inputs, the
three-prime main and joint manuscript decisions retain their scopes.
