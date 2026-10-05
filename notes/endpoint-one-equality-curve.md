# The equality curve has geometric genus ten

The explicit plane curve G(a,b)=0 from the
[equality reduction](endpoint-one-root-hierarchy.md) has total degree seven,
degree four in a and degree seven in b. Its smooth projective model is
geometrically irreducible of genus ten. It is therefore neither rational
nor elliptic. The plane arithmetic genus fifteen is not its geometric genus.
No prior literature identification of this specific curve is established here.

## The involution and a genus-three quotient

Put t=b(b+2) and q=a(t-a)=ac. The involution a -> t-a exchanges a and c.
Direct substitution gives

```text
G=Aq^2+Bq+C,
A=3b-1,
B=b(b^2+4b-1),
C=-(b^2+2b-1)(b^2+3b-1)(b^3+3b^2+3b-1).
```

The quotient has the birational hyperelliptic model y=2Aq+B,

```text
y^2=D(b),
D=12b^8+92b^7+233b^6+172b^5-154b^4-172b^3+161b^2-44b+4.
```

The exact polynomial gcd(D,D') is one. Thus D is squarefree of degree
eight and this smooth quotient has genus three. Over the complex numbers
its two points above infinity are unramified for the b map; b has a simple
pole at each, y a pole of order four and q=(y-B)/(2A) a pole of order three.

## Ten branch points give genus ten

Recover a by adjoining a square root of f=t^2-4q:
2a=t+sqrt(f). Its norm down to the rational b field is

```text
Norm(f)=N(b)/(3b-1),
N=(b^3+5b^2+6b-2)
  (3b^6+8b^5-6b^4-36b^3-28b^2+40b-8).
```

This follows from Norm(f)=16R(t^2/4)/A, where R(q)=Aq^2+Bq+C.
Exact gcd computations give gcd(N,N')=gcd(N,D)=1 and
N(1/3)=368/729; also D(1/3)=16/729. The norm therefore has a simple
pole at b=1/3 and cannot be a square in the complex rational b field.
Consequently f cannot be a square on the quotient, so the double cover
is connected and G is geometrically irreducible.

Each of the nine distinct zeros of N is away from A=0 and D=0. The
two quotient points there are unramified for b, and exactly one has f=0,
of order one: the other factor is nonzero and the norm zero is simple.
These are nine branch points of the square-root cover.

At b=1/3 the two quotient points are also unramified. At one, q has a
simple pole; at the other q is regular. The simple pole of the norm and
the nonzero numerator ensure f has a simple pole at the former and is
nonzero at the latter. This gives the tenth branch point. Away from these
points and infinity, q and f are regular and the norm has no further zeros.
At both points at infinity, t^2 has pole order four and q pole order three,
so f has pole order four. These even orders give no further ramification.

Riemann-Hurwitz now gives

```text
2g-2=2(2*3-2)+10=18, hence g=10.
```

This computation concerns the normalization; no smoothness of the plane
septic is assumed. By Siegel's theorem, the affine curve has finitely many
integer points. This is a finiteness conclusion, not an effective list,
an emptiness proof, or a classification of admissible endpoint triples.
The ordered minimum>=9 region and all earlier arithmetic restrictions
must still be enforced in any effective integer-point computation.

## Separate arithmetic windows

The coefficient hierarchy and exponent-anchor tests already apply in each
strict regime, restricted to (b,min(c,a+b)) for E>0 and (a,b) for E<0.
Their necessary status does not change. The middle anchor can be written
(b-1)F(b)=r^2E, so an integer residual root d!=b necessarily satisfies

```text
d-b divides r^2 E, where r=abc.
```

This follows by reducing the integer polynomial (b-1)F at d modulo d-b.
It is a division-free, possibly weaker form of the earlier middle-anchor
test; its sign records the regime, but a signed divisor has no stronger
divisibility content than its absolute value. It does not establish
sufficiency or a new regime-specific exclusion. At E=0 the
[simple smallest root b](endpoint-one-equality-root.md) is already known;
the remaining spectral test concerns the cubic P_3 with all roots >b.

The [checker](../scripts/check_endpoint_one_equality_curve.py) verifies the
involution, quotient, discriminant, norm, degrees, gcds and special values
against the original six-support determinant. The
[certificate](../results/endpoint-one-equality-curve.json) records these exact
identities. The ramification argument and finiteness consequence are written
mathematics, not a computed integer-point list or Lean verification.
