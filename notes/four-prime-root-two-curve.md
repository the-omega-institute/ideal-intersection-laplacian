# The root-two tail curve and fixed-minimum finiteness

**Theorem.** Fix an integer a>=2. The equation

```text
p(2;a,b,c)=det(2I-K(a,b,c))=0
```

has only finitely many positive integer tail pairs (b,c). Its
smooth projective normalization is a geometrically irreducible
genus-one curve with a rational point. No tail ordering or
coprimality condition is needed for this assertion.

**Corollary.** Fix an integer a>=5. Only finitely many positive
tail pairs b,c>=a can give integer Laplacian spectrum for the
four-prime exponent vector (a,a,b,c). This gives finiteness with
only the repeated minimum a fixed; both tails are free.

These are written deductions from exact polynomial identities,
Riemann-Hurwitz and Siegel's theorem. They give no effective tail
bound, enumeration of integral points, or emptiness assertion.
General repeated-minimum classification remains open.

## The entire root-two equation

Use p(x)=det(xI-K) and the
[genuine restriction and graph transfer](four-prime-single-pair-balanced.md).
Write p(2)=A_a(b)c^2+B_a(b)c+C_a(b), where

```text
A_a(b)=-(2a+1)b^2+2a(a^2-1)b-(a^2-1),
B_a(b)=(a-1)[2a(a+1)b^2+(4a^3+6a^2-3a-2)b
                      +(a-1)(2a^2+a-2)],
C_a(b)=(a-1)[(a-1)(2a-1)-b][(a+1)b+a-1].
```

This keeps the nonzero constant term. For a>=2 and b>=1,
B_a(b)>0: all three displayed coefficients inside its bracket
are positive. In particular this tail polynomial is never
identically zero, even when A_a(b)=0.

Put F_a(b)=B_a(b)^2-4A_a(b)C_a(b). Its full quartic is

```text
F_a(b)=L b^4+M b^3+Q b^2+R b+T,
L=4(a-1)(a+1)(a^2-a-1)(a^2+a+1),
M=4(a-1)^2(a^2+a+1)(4a^3+6a^2-a-2),
Q=(a-1)^2(16a^6+40a^5+8a^4-20a^3-31a^2-8a+4),
R=2a(a-1)^3(2a+1)(4a^3+2a^2-a-2),
T=a^2(a-1)^4(2a+1)^2.
```

Its leading coefficient L is nonzero for every integer a>=2.
The exact quartic discriminant is

```text
disc_b(F_a)=-4096 a^8(a-1)^15(a+1)^2(2a+1)^6
                  (a^2+a+1)^2 H(a),
H(a)=64a^9+128a^8+48a^7-192a^6-196a^5-44a^4
     +119a^3+58a^2+4a+8.
```

For a=2+v the complete coefficients of H(2+v), in descending
powers v^9 through v^0, are

```text
64,1280,11312,57824,187900,401324,561527,494500,247744,53616.
```

Every coefficient is positive, so H(a)>0 for a>=2. Thus F_a
has four distinct geometric roots for every a in the theorem;
there are no exceptional integer specializations in this range.

## A genus-one model and its integer recovery condition

The identity

```text
(2A_a(b)c+B_a(b))^2-F_a(b)=4A_a(b)p(2;a,b,c)
```

gives the curve model y^2=F_a(b), with y=2A_a(b)c+B_a(b).
On A_a(b)!=0 its inverse is

```text
c=(y-B_a(b))/(2A_a(b)).
```

Consequently an integer point (b,y) yields an integer tail exactly
when 2A_a(b) divides y-B_a(b), with positivity imposed separately.
Both signs of y must be retained. At the finitely many roots of A_a,
the original equation is linear with B_a(b)>0 for positive b, and
must be checked as c=-C_a(b)/B_a(b).

The degree-two map to the b-line branches simply at the four
distinct roots of F_a. It has no branch at infinity because the
degree is four. Riemann-Hurwitz gives 2g-2=-4+4=0, so the
smooth projective model has genus one. The squarefree quartic
is not a square in the geometric rational function field, proving
geometric irreducibility. A vertical component of p(2)=0 would
force a common factor in A_a,B_a,C_a and a squared factor in F_a;
the squarefree discriminant excludes it.

There is an explicit rational point. Set

```text
b0=(a-1)(2a-1),
N=(a-1)(2a+1)(2a^3-a^2+a-1),
y0=B_a(b0)=2a(a-1)N.
```

Then (b,y)=(b0,y0) lies on y^2=F_a(b), corresponding to c=0.
Here y0>0, so the point is nonsingular. Choosing it as origin
makes the smooth genus-one curve an elliptic curve over Q.
The zero tail supplies a rational base point, not a positive graph
exponent; its positive-tail branch was already
[settled](four-prime-zero-constant.md).

Siegel's theorem says that an affine curve over a number field
whose smooth projective normalization has positive genus has only
finitely many integral points. Apply it to y^2=F_a(b) over Q.
Every positive integer root-two pair maps to an integer (b,y).
Where A_a(b)!=0 the inverse determines c uniquely. At each of
the at most two remaining b values, the positive-domain linear
equation has at most one c. This proves the theorem.

## Consequence for the graph spectrum

Fix a>=5 and order the tails b<=c. If both are at least 2a-2,
the [strict cutoff minor](four-prime-coprime-completion.md) gives
1<kappa_min(K)<3. Integer graph spectrum requires every genuine
restricted root to be integer, because its graph lift is
V+1-kappa with integer V. Thus the smallest root must be 2,
and the theorem leaves only finitely many tail pairs here.

The remaining strip has a<=b<=2a-3, exactly a-2 values of b.
The [repeated-minimum bound](four-prime-low-root-divisibility.md)
gives 1<kappa_min(K)<4, so integer spectrum requires p(2)=0
or p(3)=0. For fixed a,b, each is a nonzero quadratic or
linear polynomial in c. The coefficient of c in p(3) is

```text
(a-2)[(a^2-1)b^2+(4a^3+3a^2-8a-2)b
                     +(a-2)(2a^2-a-4)]>0.
```

Its bracket coefficients are positive for a>=3; B_a(b)>0 was
already checked for p(2). Thus at most four integer tails per b
pass this necessary endpoint test. There are at most 4(a-2)
ordered representatives in this strip, before other exclusions.
Together with the finite large-tail set, this proves the corollary.
It does not bound the repeated minimum a.

## The explicit a=6 model

At a=6 the quartic equation is

```text
y^2=20 G(b),
G(b)=8729b^4+230480b^3+1328030b^2+904800b+190125.
```

For integer points y is divisible by 10, since y^2 is divisible
by 20. With y=10z the integral model is 5z^2=G(b), and the
rational base point is (b,z)=(55,156390). Recover c with
the original coefficients and the divisibility condition above.
No elliptic rank or complete integral-point list is asserted.

For a concrete nonzero-constant simple resonance, take b=105,c=75.
At the good root-two prime 5, e=r=1<t=2; scaled H=1,B=21,C=15
give B-2C-H=-10 and 2B-C+H=28. Both coarse endpoint
divisibilities hold. At the only prime 7 dividing a+1, the tail
quadratics split as x(x-1) and (x-4)^2. The preceding
double-resonance hypothesis fails because v_5(b+a-1)=1<2.

The complete tail equation is

```text
p(2;6,105,c)=-20(4963c^2-259445c+9250).
```

It has two positive real roots, but its discriminant
26851230810000 lies strictly between 5181817^2 and 5181818^2.
Hence it has no integer tail root. At c=75,
p(2)=-169355000 and p(3)=-6225682400. This illustrates the
global curve condition after the named local tests pass; it is
not a comparison with every prior sufficient spectral region.

## Verification and next question

The [checker](../scripts/check_four_prime_root_two_curve.py) checks
the characteristic equation against an independent symbolic
permutation determinant, all five quartic coefficients, and the
quartic discriminant using both a resultant and the binary quartic
invariants I,J. It checks the complete ten-term positive expansion,
the inverse identity, rational point, positive coefficients of the
root-three linear term, both prior cutoff minors and the strip count.

Three specified graph controls check 168 support-column actions,
12 independent tail determinants and 15 quartic determinants,
with three exact Sturm counts in (1,4). Three integer Sylvester
determinants additionally check the discriminant specializations.
All 30 determinants are exact. The controls are implementation
checks; geometric genus and Siegel finiteness come from the written
argument, not these three examples.

The [certificate](../results/four-prime-root-two-curve.json) is
reproducible with SymPy 1.14.0 using
`python3 scripts/check_four_prime_root_two_curve.py`.
No parameter scan, expanded graph, historical finite-base rerun,
floating eigenvalues or Lean validation is used. Finiteness is
ineffective here: the next arithmetic step needs a verified elliptic
model and a justified method for complete integral points, retaining
the recovery divisibility and exceptional A_a=0 fibers. An integer
root two alone does not give integer graph spectrum. All earlier
proofs and finite inputs, the three-prime main and joint manuscript
decisions retain their scopes.
