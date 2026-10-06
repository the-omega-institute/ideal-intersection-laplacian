# Specializing the published quartic integral-point method

The remaining a=6 problem is covered by the quartic elliptic-logarithm
method of N. Tzanakis, *Solving elliptic diophantine equations by
estimating linear forms in elliptic logarithms. The case of quartic
equations*, Acta Arithmetica 75(2) (1996), 165-190,
[DOI:10.4064/aa-75-2-165-190](https://doi.org/10.4064/aa-75-2-165-190).
The original article's Sections 2-5 and 7 have been checked against
our curve, including the displayed formulas on the relevant pages.
This is an application of that existing method, with explicit initial
estimates and a proved choice of reduction case. It is not an
execution of the complete algorithm or a new general algorithm.

## Hypotheses and the same elliptic curve

The article's Equation (1), page 167, is

```text
V^2=aU^4+bU^3+cU^2+dU+e^2,
a,b,c,d,e integers, a>0, e>0, discriminant nonzero.
```

The leading coefficient need not be a square. Our original quartic
already has the required rational base point and square constant:

```text
W^2=f(b),
f(b)=alpha b^4+beta b^3+gamma b^2+delta b+h^2,
(alpha,beta,gamma,delta,h)=(43645,1152400,6640150,4524000,975),
(b,W)=(0,h).
```

The quartic discriminant is nonzero. To avoid colliding with the
article's coefficient b, our tail parameter remains b and its
coefficients are named alpha,beta,gamma,delta,h.

The article's short model has

```text
A0=-gamma^2/3+beta delta-4h^2alpha,
B0=2gamma^3/27-beta gamma delta/3-(8/3)h^2alpha gamma
   +h^2beta^2+alpha delta^2,
y^2=q(x)=x^3+A0 x+B0.
```

This is our cubic E0 after x=U+gamma/3,y=V. Scaling
(X,Y)=(9x/100,27y/1000) gives exactly the preceding
[integer-coefficient short equation](four-prime-a6-elliptic.md).
Thus a full rational Mordell-Weil basis on any of these rationally
isomorphic models supplies the required group input, provided its
model transformations and torsion points are retained. The method
does not require a full E0(K) basis.

## The positive branch has no monotonicity cutoff

For b>0 put

```text
F*(b)=[2h sqrt(f(b))+delta b+2h^2]/b^2.
```

This is the article's function on page 167 and our rational-chart
first coordinate R_U for W=+sqrt(f(b)). All five coefficients of f
are positive, so f(b)>alpha b^4>0. Exact differentiation gives

```text
b^3 sqrt(f(b)) (F*)'(b)
 =-h[beta b^3+2gamma b^2+3delta b+4h^2]
  -(delta b+4h^2)sqrt(f(b)) <0.
```

Hence F* is strictly decreasing for every b>0, with
F*(b)>2h sqrt(alpha) and limit 2h sqrt(alpha). Its range avoids
both of the article's forbidden values,

```text
-2h sqrt(alpha),
delta^2/(4h^2)-gamma=-1257750.
```

The article's sign is +1 and its monotonicity threshold u0 can
therefore be zero for our positive domain. The differential identity
R_V=-W dR_U/db verifies the vertical-coordinate orientation too.
This does not discard W<0: after finding the possible integer b,
both W signs must enter the original c-divisibility filter.

## The asymptotic logarithm is an independent term

The article's asymptotic point is

```text
P0=(1950s+gamma/3,1123590000+4524000s), s=sqrt(43645).
```

It is exactly Pstar on the shifted short model. The cubic q has
negative discriminant, so exactly one real root and a connected
real point group. Our P0 has positive second coordinate and lies
above that root. Thus the article's Equation (13) on page 172
applies, with its asymptotic elliptic logarithm retained.

The [infinite-order theorem](four-prime-nontorsion.md) proves that
Pstar-sigma(Pstar)=T is nontorsion. If the normalized real logarithm
of P0 were a rational combination of rational-group logarithms and
the real period, clearing denominators and applying the real group
isomorphism would make [n]P0 rational for some nonzero n. Its
Galois difference would be [n]T!=O, a contradiction. The constant
logarithm is therefore independent in precisely the sense needed
for Section 5's **Case 2**, the inhomogeneous reduction and
Proposition 4 on page 177. It cannot be removed by the article's
Case 3 simplification.

All rational basis coordinates and P0 lie in the common field
K=Q(sqrt(43645)), of degree two. Thus the field degree D in
the article's Section 7 may be two; it is not a requirement
to compute the full Mordell-Weil group over that field.

## Initial estimates available without a basis

The positive coefficient inequality directly gives

```text
0 < integral_b^infinity du/sqrt(f(u)) < 1/(sqrt(43645)*b), b>0.
```

We may take the article's c9=1/sqrt(43645).

For integer b>=1, f(b)<=f(1)b^4 and

```text
f(1)=13310820 <3649^2.
```

An integer quartic point therefore has |W|<3649b^2. The rational
chart numerator N=2h(W+h)+delta b obeys

```text
|N| <=2h|W|+2h^2+delta b <=13540800b^2.
```

After reducing N/b^2 to lowest terms, its numerator and denominator
can only decrease. For the logarithmic rational height this proves

```text
h(R_U)<=log(13540800)+2log(b).
```

Since E0 already has integer Weierstrass coefficients, the article's
Equation (18) may use this horizontal coordinate, with
c10=log(13540800). These are initial analytic estimates, not a
bound on the Mordell-Weil coefficients or on all tail parameters.

## Inputs still needed to execute the complete method

The verified published route requires the following remaining work:

1. Certify the full rational Mordell-Weil basis and torsion subgroup,
   with exact transformations to E0 and its quartic recovery map.
2. Certify a positive regulator lower bound c1, a global canonical-
   versus-naive height correction c11, and the David/logarithm
   constants of Sections 4 and 7, including the algebraic point P0.
3. Derive a proved initial coefficient bound, then perform the
   inhomogeneous lattice reduction with certified rounding and
   an independently verified lattice-distance inequality.
4. Exhaust the resulting proved coefficient range and all torsion
   sectors, recover integer b,W, and recover c for both W signs with
   divisibility and positivity; repeated minimum needs b,c>=6.

No step can be replaced by an arbitrary group-coefficient search.
The original page 177 prints a 2^(r/2) factor in Equation (26),
while the subsequent reduction expressions use 2^(-r). Before
implementation the distance bound must be derived from the actual
reduced basis and checked independently; we have not implemented
or adopted those printed numerical formulas here.

The [checker](../scripts/check_four_prime_quartic_method.py) and
[certificate](../results/four-prime-quartic-method.json) verify the
exact model identification, discriminants, asymptotic point,
differentiation, excluded values and integer height constant. The
case selection and inequalities also have the written arguments
above. SymPy 1.14.0 is used without floating arithmetic.

No full basis, numeric elliptic logarithms, regulator/c11/David
constants, initial coefficient bound, LLL reduction or complete
integral-point enumeration is supplied. Prior rank lower bounds,
original integrality filters and manuscript decisions retain their
scopes. This adds no graph-integrality or nonintegrality classification,
graph expansion, historical finite-base rerun or Lean verification.
