# An explicit elliptic model for the a=6 root-two equation

**Proposition.** The complete root-two tail equation p(2;6,b,c)=0
is birational over Q to the nonsingular Weierstrass curve

```text
E: Y^2=X^3-78162568812X+8433576786332241.
```

The maps and their rational exceptional points are explicit below.
For positive rational b,c the forward map is defined. Positive
integer tail pairs are recovered by requiring the inverse b and c
to be positive integers; repeated-minimum pairs also require b,c>=6.
No rank, Mordell-Weil basis, minimal-model assertion or complete
integral-point enumeration is made.

This supplies the coordinate step after the
[genus-one finiteness theorem](four-prime-root-two-curve.md).
The affine integrality conditions remain part of the problem:
the displayed Weierstrass model is a rational coordinate model.

## The affine equation and its square completion

The established genuine restriction gives

```text
p(2;6,b,c)=A(b)c^2+B(b)c+C(b),
A(b)=-13b^2+420b-35,
B(b)=420b^2+5300b+1900,
C(b)=5(55-b)(7b+5).
```

Put

```text
W=A(b)c+210b^2+2650b+950,
f(b)=43645b^4+1152400b^3+6640150b^2+4524000b+950625.
```

The exact identity W^2-f(b)=A(b)p(2;6,b,c) shows that the
tail curve is equivalent to W^2=f(b). This is the preceding
model 5z^2=G(b) with W=5z and f=5G. At integer b,W,
the equation forces 5|W. The discriminant of A is
174580=4*43645. Since 208^2<43645<209^2, A has no rational
root. Thus the inverse

```text
c=(W-210b^2-2650b-950)/A(b)
```

has no missing rational A=0 fiber in this a=6 case. For integer
b,W it imposes the additional divisibility
A(b)|(W-210b^2-2650b-950), and positivity is separate.

## Derivation of the Weierstrass coordinates

Write

```text
alpha=43645, beta=1152400, gamma=6640150, delta=4524000,
q=975,
f(b)=alpha b^4+beta b^3+gamma b^2+delta b+q^2.
```

For b!=0 define

```text
U=[2q(W+q)+delta b]/b^2,
L=U^2-4q^2 alpha,
V=[Lb-delta U-2q^2 beta]/(2q).
```

Substituting W=(Ub^2-delta b)/(2q)-q in W^2=f(b), and
dividing by b^2, gives

```text
Lb^2+(-2delta U-4q^2 beta)b+(delta^2-4q^2U-4q^2gamma)=0.
```

Completing this quadratic yields

```text
V^2=U^3+gamma U^2+P U+R,
P=beta delta-4q^2 alpha=5047497487500,
R=q^2 beta^2+alpha delta^2-4q^2 alpha gamma
 =1053718156603125000.
```

Now set

```text
X=(9U+3gamma)/100,
Y=27V/1000.
```

Direct substitution gives the displayed curve E. Its Weierstrass
discriminant is

```text
-16[4(-78162568812)^3+27(8433576786332241)^2]
 =-164468670344965775252034431406000 !=0.
```

No minimality claim is needed for this rational equivalence.

## The inverse and all rational exceptions

For a finite rational point (X,Y) on E set

```text
U=(100X-3gamma)/9,
V=1000Y/27,
b=[2qV+delta U+2q^2 beta]/[U^2-4q^2 alpha],
W=(Ub^2-delta b)/(2q)-q.
```

Equivalently the first inverse coordinate is the compact formula

```text
b=(2340Y+1628640X-253444000680)
       /[(2X-398409)^2-5377107645].
```

Here 5377107645=351^2*43645 is not a rational square, so the
denominator is nonzero at every rational X. Likewise L never
vanishes at a rational U, because L=0 would make alpha a rational
square. The inverse therefore exists at every finite rational
Weierstrass point. It gives a point on the quartic, and the two
maps compose to the identity wherever b!=0.

There are two quartic points at b=0:

```text
(b,W)=(0,975), corresponding to c=-5/7;
(b,W)=(0,-975), corresponding to c=55.
```

The first maps to the Weierstrass point at infinity O: U has a
double pole there, hence X has a double pole. The second maps to

```text
P0=(86007,48448530).
```

Indeed U=delta^2/(4q^2)-gamma=-1257750 and
V=(-delta U-2q^2 beta)/(2q)=1794390000 at this point. The
inverse b is zero only at P0 among finite rational E-points:
setting its numerator to zero in the cubic equation forces
U=delta^2/(4q^2)-gamma, and then fixes V.

The two points at infinity of the smooth quartic have leading
coordinates W/b^2=+/-sqrt(alpha). Since alpha is not a rational
square, neither is rational. Thus there are no additional rational
points at infinity to account for. Positive integer tail pairs
correspond exactly to finite rational E-points other than P0 whose
recovered b,c are positive integers. Both choices of W must be
retained; they encode different tail roots.

## The remaining computational requirement

The birational maps have denominators depending on b. In
particular the integral quartic point (b,W)=(55,-781950) maps to

```text
(X,Y)=(19517052/121,6328630035/1331).
```

Its recovered tail is c=26065/271, so the final integer-tail
filter rejects it. It is still an integral quartic point, and a
routine listing only integral X,Y would omit it. The companion
(55,781950) maps to (252030,68869359), with c=0. Neither point
is a positive integer graph example.

A complete computation must establish completeness for integral
points on the original affine quartic, or directly for integer
values of the inverse functions b(P),c(P). Integrality of X,Y
is an additional condition that has not been justified for all
positive integer tail solutions. Choosing a finite set of allowed
denominator primes also needs a proof; the displayed denominators
alone do not give that set.

The [official Sage documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html#sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.integral_points)
specifies that `integral_points` lists integral points on the
chosen elliptic model, with `both_signs=False` by default. It also
states that an incomplete supplied Mordell-Weil basis can omit
points outside its generated subgroup. Consequently both the
affine integrality condition and a certified complete group basis
must be addressed before using such a computation as an exhaustive
tail certificate. No such computation is performed here.

## Verification and scope

The [checker](../scripts/check_four_prime_a6_elliptic.py) independently
reconstructs the a=6 characteristic value by a symbolic permutation
determinant, checks the square completion, derives the cubic by
the quadratic discriminant, and checks both maps and their two
compositions as polynomial identities modulo the curve equations.
It checks the exact nonsingularity discriminant, compact inverse,
nonsquare denominators, both b=0 branches and P0. Four specified
rational points check both signs and exact round trips, including
the nonintegral Weierstrass image above.

The [certificate](../results/four-prime-a6-elliptic.json) is
reproducible with SymPy 1.14.0 using
`python3 scripts/check_four_prime_a6_elliptic.py`.
These are exact coordinate and exceptional-point checks. No
exponent scan, graph expansion, historical finite-base rerun,
elliptic rank or integral-point algorithm, floating eigenvalues or
Lean validation is used. Previous fixed-minimum finiteness and
nonintegrality results retain their scopes. An integer root two
alone does not give integer graph spectrum; the three-prime main
and joint manuscript decisions remain unchanged.
