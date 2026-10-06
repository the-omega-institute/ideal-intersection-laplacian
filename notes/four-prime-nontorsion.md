# An infinite-order obstruction to rationalizing the coset

**Proposition.** The fixed Galois difference T in the
[coset theorem](four-prime-galois-coset.md) has infinite order.
Consequently, for every P in Pstar+E0(Q) and every nonzero integer n,
the point [n]P is not rational. More generally, a nonzero
Q-defined isogeny cannot send a point of this coset to a rational
point. There are also explicit independent infinite-order points
on E0(K), proving rank E0(K)>=2. These are lower bounds, not an
exact rank computation or a certified full basis.

## A rational twist witness

Use the preceding short equation and its rational scaling:

```text
E: Y^2=X^3+A X+B,
A=-78162568812, B=8433576786332241,
X=(9U+3gamma)/100, Y=27V/1000,
gamma=6640150.
```

Let d=43645 and s^2=d. The Galois difference on E0 is

```text
T=(196265550/203,-712421190000s/41209).
```

Its short-model image has rational X and Y a rational multiple
of s. The quadratic twist

```text
E_d: y^2=x^3+d^2 A x+d^3 B
```

has integer coefficients. The K-isomorphism
(X,Y)->(dX,dsY) sends T to the rational point

```text
T_d=(12492018795,-889155076709250).
```

The checker verifies the twist identity and this point's exact
curve equation. Its second coordinate is nonzero and divisible
by the prime 1201, whereas

```text
disc(E_d)=-16(4(d^2 A)^3+27(d^3 B)^2)
         =d^6 disc(E),
disc(E_d) mod 1201=4.
```

In particular 1201 does not divide the discriminant. The classical
Nagell-Lutz theorem says that a rational torsion point on a
nonsingular short Weierstrass equation with integer coefficients
has integer coordinates and either y=0 or y^2 dividing
4a^3+27b^2. The point T_d violates the latter divisibility at
1201 and has y!=0, so it has infinite order. The isomorphism
then proves that T has infinite order. No torsion-group
enumeration, height approximation or rank computation is needed.

## Multiplication and rational isogenies

The coset theorem gives P-sigma(P)=T, where sigma(s)=-s.
For a nonzero integer n,

```text
[n]P-sigma([n]P)=[n]T!=O.
```

Thus [n]P is not fixed by sigma, and is not rational. There is
no fixed nonzero multiplier that turns this coset into rational
points; in fact even an individual point cannot be rationalized
by any nonzero multiplier.

If phi:E0->E' is a nonzero isogeny defined over Q, it commutes
with sigma and has finite kernel. Hence phi(T) has infinite order,
and

```text
phi(P)-sigma(phi(P))=phi(T)!=O.
```

Its image is again nonrational. This assertion concerns Q-defined
isogenies. It does not restrict arbitrary functions on the curve
or change the rational-group parameterization Q=P-Pstar.

## Two independent infinite-order points

The [previous rational chart](four-prime-a6-elliptic.md) maps the
specified quartic control (b,W)=(55,-781950) to

```text
S=(19517052/121,6328630035/1331) in E(Q).
```

The checker verifies its curve equation. Its first coordinate is
not an integer, so Nagell-Lutz proves that S has infinite order
on the integer-coefficient short equation E. Transfer it to E0
by the rational isomorphism above. It is Galois invariant, while
sigma(T)=-T. If mS+nT=O, conjugation and subtraction give
2nT=O, forcing n=0; then m=0 as S has infinite order. This
proves independence and the lower bounds

```text
rank E0(Q)>=1,
rank E_d(Q)>=1,
rank E0(K)>=2.
```

The control S is not a positive integer graph example: the
original c=26065/271 fails tail integrality. Its use here is as
an infinite-order group witness. No full basis or exact rank
is asserted for any of the three groups.

## Consequence for the remaining computation

The exact coset Pstar+E0(Q) remains the relevant group target,
with integrality imposed on Pstar+Q rather than on Q itself.
The new obstruction excludes rationalization by multiplying
points or applying a Q-defined isogeny. It does not supply a
complete translated-integrality algorithm, a point list or a
new nonintegrality classification. Both W signs, full O_K and
the original conjugate/quartic/integer-tail filter remain required.

The [checker](../scripts/check_four_prime_nontorsion.py) and
[certificate](../results/four-prime-nontorsion.json) record the
exact twist and curve identities, Nagell-Lutz witnesses and
integer discriminant residue. The group consequences and
independence use the written argument. SymPy 1.14.0 supplies
exact arithmetic; there is no arbitrary point search, graph or
historical finite-base rerun, floating computation or Lean.
Previous results and joint manuscript decisions retain their
stated scopes.
