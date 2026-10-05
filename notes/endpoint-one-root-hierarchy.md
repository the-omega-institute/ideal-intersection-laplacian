# Higher coefficient tests, persistent real regimes and the equality equation

Use the endpoint-one notation

```text
F(x)=x^4-Ax^3+Bx^2-Dx+N,
N=rs(p+s), s=a+b+c, p=ab+ac+bc, r=abc.
```

This note answers the coefficient and regime questions after the
[root-congruence](endpoint-one-root-congruences.md) and
[middle-root](endpoint-one-middle-root.md) results. Full Q3 and integer
feasibility on the remaining fully distinct surface stay open.

## The higher coefficients supply further necessary congruences

An integer root d>0 must satisfy

```text
d divides N,
d^2 divides N-Dd,
d^3 divides N-Dd+Bd^2,
d^4 divides N-Dd+Bd^2-Ad^3.
```

Each follows by reducing F(d)=0 modulo the displayed power of d.
The linear stage genuinely uses D: after d|N it requires N/d=D modulo d,
not merely a condition that d divides N. The quadratic stage also uses B;
the cubic stage additionally uses A. If the linear stage passes, the next
test can be written as ((N/d-D)/d)+B=0 modulo d. An analogous next carry
then supplies the A test.

These are candidate-dependent divisibilities, not higher two-adic lifts
of the endpoint equation. No sufficiency theorem follows from them.
Algebraically they are still modular tests: the abstract monic polynomial
product_(j=2)^5(x-jd) has four positive integer roots, passes every displayed
congruence at d, but has value24d^4 there. This example is not an endpoint-one
quotient polynomial; it explains why a separate argument would be needed
to establish sufficiency on that surface.

On the same three established controls and same23window divisors:

| (a,b,c) | Candidates | Previous coefficient plus exponent survivors | Pass quadratic stage | Exponent plus quadratic survivors |
|---|---:|---|---|---|
| (8,8,105) | 5 | 15 | none | none |
| (9,9,136) | 5 | none | 14 | none |
| (20,20,741) | 13 | none | none | none |

The sole previous combined survivor d=15 at (8,8,105) fails the new stage:

```text
F(15)=-798518700=2925 modulo15^3,
15^3=3375.
```

Thus the exponent and quadratic congruences alone reject every candidate
in these three controls, without needing the final full-value zero test.
They do not prove sufficiency or global exclusion on an unbounded family.
All three graphs were already nonintegral by the repeated-exponent theorem.
Also b=a in these controls, with E>0; the newer middle-exponent window is
identical to the old one, so it did not change these23candidate lists.

## A uniform rejection of the earlier infinite candidate family

For a=6k,k>=1,b=a,c=(a-1)(2a-1), the candidate d=3a/2=9k divides N
and lies in (b,2a), the refined E>0 window. The earlier exact identity gives

```text
F(d)/d^2=-(4a^2-2a-1)T(a)/36,
T(a)=8a^5+48a^4-132a^3+95a^2-32a+4.
```

Since a is divisible by three, the numerator (4a^2-2a-1)T(a) is
(-1)*1=2 modulo three. The displayed quotient is therefore not an integer.
Thus d^2 does not divide F(d), and this candidate fails the linear
coefficient test for every k>=1.

This is a written unbounded exclusion of that particular candidate.
It is not an exclusion of every divisor in these windows, a new graph
nonintegrality family, or a result about fully distinct surviving triples.

## Both strict regimes occur for arbitrarily large real minima

Let H_(a,b)(c)=h_C(1), and c_0=b(b+2)-a, so E=0 at c=c_0.
The earlier [geometry theorem](endpoint-one-geometry.md) gives a unique
simple real root c>b whenever b<gamma(a), with gamma(a)>2a^2-a-2.
For every real a>=9 both b=a+3 and b=2a satisfy this feasibility bound.

At the threshold c_0, exact substitution gives

```text
b=a+3:
H(c_0)=-2(a+2)[a^7+11a^6+7a^5-479a^4-3210a^3
                       -9424a^2-13384a-7378]<0,
b=2a:
H(c_0)=(2a-1)[32a^7+352a^6+586a^5+305a^4-50a^3
                       -64a^2+16a-1]>0.
```

For a=9+m,m>=0, the complete descending coefficient vectors of -H(c_0)
in the first case and H(c_0) in the second case are

```text
[2,170,6232,128076,1602214,12344554,55958484,130053564,102699872],
[64,5280,188308,3800112,47536335,377906718,1866318180,5238888768,6403637656].
```

All entries are positive. The endpoint cubic has positive leading
coefficient and H(b)<0 on the feasible interval. Its unique root c>b
therefore lies above c_0 for b=a+3, giving E>0, and below c_0 for b=2a,
giving E<0. Thus neither regime eventually dominates the real endpoint
surface. Whether one regime dominates the fully distinct integer points
is a separate, unresolved Diophantine question.

Moreover feasibility holds for every b in [a+3,2a]. The unique simple
exponent root depends continuously on b. E has opposite signs at the
endpoints, so for each real a>=9 some b in (a+3,2a) has E=0.
This establishes real equality points, without claiming integer b or c.

## An exact Diophantine reduction for E=0

For integer4<=a<=b, impose c=b^2+2b-a. This c is automatically greater
than b. Direct substitution gives

```text
h_C(1)=-(b-1)G(a,b),
G(a,b)=g4(b)a^4+g3(b)a^3+g2(b)a^2+g1(b)a+g0(b),
g4=3b-1,
g3=-6b^3-10b^2+4b,
g2=3b^5+11b^4+7b^3-8b^2+b,
g1=b^5+6b^4+7b^3-2b^2,
g0=-b^7-8b^6-22b^5-21b^4+7b^3+16b^2-8b+1.
```

Because b-1 is nonzero, the integer equality subfamily is exactly G(a,b)=0
with this c. This exposes a separate Diophantine equation; it does not
classify its integer solutions. For fully distinct endpoint-one points
at minimum>=8, the earlier strict sum bounds give

```text
2a^2-a+1 < b^2+3b < 4a^2-a,
a<b<2a.
```

Indeed b+c=b^2+3b-a, so these follow by substitution in
2a^2-2a+1<b+c<4a^2-2a. In the surviving integer-spectrum region a>=9,
all earlier arithmetic and gap restrictions still apply. At any such
equality point, b is a residual integer root; the other factor need not
split integrally. Neither the root's index nor equality integer feasibility
is resolved here.

The [checker](../scripts/check_endpoint_one_root_hierarchy.py) reconstructs
the generic determinant, hierarchy, boundary candidate identity, both
complete positive coefficient vectors and all five G coefficients. It
retains exactly the existing3controls/23divisors and checks each new
remainder against exact F(d). The
[certificate](../results/endpoint-one-root-hierarchy.json) records all
remainders, identities and source/input hashes. Infinite statements have
written proofs; controls are finite diagnostics. No range/modulus scan,
higher endpoint two-adic lift, floating spectrum or Lean was used.
Prior manuscript/proofs/finite dependencies remain unchanged.
