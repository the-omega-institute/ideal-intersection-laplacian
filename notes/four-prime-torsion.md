# The three torsion groups are trivial

**Proposition.** For the a=6 elliptic curve E, its quadratic twist
E_d with d=43645, and K=Q(sqrt(d)),

```text
E(Q)_tors={O}, E_d(Q)_tors={O}, E(K)_tors={O}.
```

The rational isomorphism to E0 transfers the first and third
statements to that integral cubic. Thus the torsion input for the
[published quartic method](four-prime-quartic-method.md) is fully
determined. The free Mordell-Weil basis remains uncomputed.

## Two specified good reductions

Use the short integer-coefficient equation

```text
E: Y^2=X^3+A X+B,
A=-78162568812, B=8433576786332241,
E_d: y^2=x^3+d^2 A x+d^3 B, d=43645.
```

The checker verifies nonzero discriminant residues at 11 and 17
for both equations, so these are good reductions. Including the
point at infinity, the exact orders are

| prime | E(F_p) | E_d(F_p) |
|---|---:|---:|
| 11 | 10 | 14 |
| 17 | 16 | 20 |

Each count is certified by a list of all cubic values and numbers
of corresponding vertical coordinates. A second calculation uses
the Legendre-symbol sum p+1+sum_x chi(x^3+Ax+B). The two
calculations agree for every horizontal coordinate.

At good reduction p, prime-to-p rational torsion injects into
E(F_p). For a torsion prime other than 11 or 17, its primary
subgroup order must therefore divide both displayed group orders.
The 11-primary subgroup is excluded by reduction at 17, since
neither 16 nor 20 is divisible by 11; the 17-primary subgroup
is excluded at 11, since neither 10 nor 14 is divisible by 17.
Thus the full rational torsion orders divide

```text
gcd(10,16)=2 for E,
gcd(14,20)=2 for E_d.
```

This argument uses only prime-to-p reduction injectivity and
accounts explicitly for both exceptional primary subgroups.

## Excluding rational two-torsion

A nonidentity two-torsion point on a short Weierstrass equation
has vertical coordinate zero. The cubic g(X)=X^3+AX+B reduces
modulo 23 to

```text
g(X)=X^3-X+15 mod 23.
```

Its complete list of values, for X=0,...,22, is

```text
15,15,21,16,6,20,18,6,13,22,16,1,6,14,8,17,1,12,10,1,14,9,15.
```

None is zero. A degree-three polynomial over a field is
irreducible exactly when it has no root. Since g is monic over Z,
irreducibility modulo 23 proves irreducibility over Q. In
particular it has no rational root, so E(Q) has no two-torsion.

The twist cubic obeys

```text
g_d(x)=x^3+d^2 A x+d^3 B=d^3 g(x/d).
```

It has no rational root either. Hence E_d(Q) has no two-torsion.
Combined with the order bounds, both rational torsion groups
are trivial.

## No additional torsion over the quadratic field

Let P be any torsion point in E(K), and let sigma(s)=-s.
Its trace P+sigma(P) is a rational torsion point, hence O by
the preceding result. Therefore sigma(P)=-P. A finite such
point has X in Q and Y a rational multiple of s. The
K-isomorphism

```text
E->E_d, (X,Y)->(dX,dsY)
```

sends it to a rational torsion point of E_d, also necessarily O.
An isomorphism cannot send a finite point to O. Thus P=O,
proving the full quadratic-field torsion statement. This is a
written Galois argument; no K-point enumeration is used.

## The remaining algorithm input

The Tzanakis method's rational torsion term s/t is now 0/1.
In its inhomogeneous Case 2, the normalized linear form therefore
has the simpler shape

```text
Phi=rho0+m0+sum_i(mi*rho_i),
```

where rho0 is the indispensable asymptotic-point logarithm and
the rho_i come from a full rational free basis. The previous
[infinite-order theorem](four-prime-nontorsion.md) still supplies
rank lower bounds one for E(Q) and E_d(Q), and two over K.
Trivial torsion does not certify an exact rank, saturation or
a full free basis, nor any regulator or logarithm bound.

The [checker](../scripts/check_four_prime_torsion.py) and
[certificate](../results/four-prime-torsion.json) use SymPy
1.14.0 to verify the four specified finite-field counts, their
Legendre-symbol checks, good reduction and the modulo-23
irreducibility and twist identities. These targeted counts
resolve the stated torsion input. They are not a parameter
scan or a graph-integrality test.

No remaining height/David constants, initial coefficient bound,
LLL reduction or complete integral-point list is computed.
Both W signs and the original c-divisibility filter remain
required. There is no new nonintegrality classification,
graph/historical finite-base rerun, floating computation or
Lean validation; earlier results and joint manuscript decisions
retain their stated scopes.
