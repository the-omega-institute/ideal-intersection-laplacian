# A rational-group coset for the quadratic-field images

**Proposition.** Retain the integral cubic E0 and polynomial map
P=(U,V) from the [quadratic-field reduction](four-prime-affine-integrality.md).
Let s=sqrt(43645), K=Q(s), and let sigma be the nontrivial
automorphism of K/Q. Put

```text
Pstar=(1950s,1123590000+4524000s),
T=(196265550/203,-712421190000s/41209).
```

Both points lie on E0. Every positive rational quartic point
(b,W), W^2=f(b), satisfies P-sigma(P)=T. Moreover,

```text
{P in E0(K): P-sigma(P)=T}=Pstar+E0(Q).
```

If R is the point on the same cubic given by the preceding
rational chart, then P=Pstar-R. Thus the integral quadratic-field
target can be restricted to a translate of the rational group.
Parameterizing this coset does not require a full E0(K) basis.
Completeness of its integral-point enumeration is a separate step,
still not executed.

## The fixed Galois difference

Write alpha=43645, beta=1152400, gamma=6640150,
delta=4524000 and h=975. The curve is

```text
E0: V^2=U^3+gamma U^2+5047497487500U
          +1053718156603125000.
```

Its group identity is the point at infinity. For a positive
rational quartic point, f(b)>0, so W!=0. Consequently
U-sigma(U)=4sW!=0. The slope for adding P and -sigma(P) is

```text
m=(V+sigma(V))/(U-sigma(U))=(4alpha b+beta)/(2s).
```

The Weierstrass addition formulas give

```text
U_T=m^2-gamma-U-sigma(U)=beta^2/(4alpha)-gamma,
V_T=-V+m(U-U_T)
   =[beta(gamma-beta^2/(4alpha))-2alpha delta]/(2s).
```

The displayed coordinates simplify exactly to T above. The
checker verifies its curve equation and these identities with
s^2=alpha, retaining exact rational coefficients. Sigma(T)=-T
and T is nonzero. Substituting b=0,W=h in the polynomial map
gives Pstar, with Pstar-sigma(Pstar)=T as well.

For any P satisfying the Galois-difference equation, let Q=P-Pstar.
Then

```text
Q-sigma(Q)=(P-sigma(P))-(Pstar-sigma(Pstar))=O.
```

The fixed subgroup E0(K)^sigma is E0(Q): a finite fixed point has
rational coordinates, and the identity is rational. Hence Q is
rational. Conversely every rational Q makes Pstar+Q satisfy the
equation. This proves equality of the full coset, not merely an
inclusion for the four checked controls. The point at infinity
does not lie in this coset, since its Galois difference is O.

## Relation to the preceding rational chart

For b>0 the [rational a=6 construction](four-prime-a6-elliptic.md)
has cubic coordinates

```text
R_U=[2h(W+h)+delta b]/b^2,
R_V=[(R_U^2-4h^2alpha)b-delta R_U-2h^2beta]/(2h).
```

Adding Pstar and -R gives precisely the polynomial point P.
The checker verifies both coordinate identities modulo
(W^2-f(b),s^2-alpha). Its addition denominator R_U-1950s
cannot vanish for rational b,W, because R_U is rational and
1950s is irrational. The preceding short-model scaling gives

```text
R_U=(100X-3gamma)/9, R_V=1000Y/27,
P-Pstar=((100X-3gamma)/9,-1000Y/27).
```

The sign is essential: the translated rational point is -R.
At b=0,W=h the rational chart is O and P=Pstar. At b=0,W=-h,
the translated point is (-1257750,-1794390000), the negative
of the previous finite exceptional point. Both signs at b=55
also give the exact negatives of their previous rational-chart
coordinates. These four controls are coordinate verifications;
none is a positive integer tail example.

## Consequences for a complete computation

For any finite Q=(x,y) in E0(Q), its translate has explicit
coordinates

```text
m=(y-V_Pstar)/(x-U_Pstar),
U=m^2-gamma-x-U_Pstar,
V=-V_Pstar+m(U_Pstar-U).
```

The denominator is nonzero because x is rational and U_Pstar is
irrational. Q=O translates to Pstar, which fails the positive-b
filter. Therefore a sufficient complete target is now

```text
{Q in E0(Q): Pstar+Q has both coordinates in O_K},
O_K=Z[(1+s)/2].
```

Apply the full [conjugate-coefficient, quartic and integer-tail
filter](four-prime-affine-integrality.md) to each translate.
Both W signs are retained. A complete algorithm on this coset
may use a certified full rational Mordell-Weil basis, if its
method needs one; it need not enumerate the entire E0(K) group.
This does not establish such an algorithm or certify any basis.

Do not substitute the ordinary integral points Q on E0(Q) for
this target. The required integrality belongs to Pstar+Q.
For (b,W)=(55,-781950), the field point P is integral but

```text
Q=(-50963250/121,-234393705000/1331)
```

is nonintegral. Its recovered c=26065/271 still fails the final
tail filter; this is no missed graph example. The new result
refines the group search without removing the translated
integrality condition or the original rational-chart warning.

The [checker](../scripts/check_four_prime_galois_coset.py) and
[certificate](../results/four-prime-galois-coset.json) verify the
generic difference and translation identities, both fixed-point
curve equations, and four specified affine controls with SymPy
1.14.0. No rank, basis, complete point list, new nonintegrality
classification, arbitrary scan, graph expansion, historical
finite-base rerun, floating computation or Lean is used. The
earlier finiteness theorem, other results and manuscript scope
retain their stated ranges.
