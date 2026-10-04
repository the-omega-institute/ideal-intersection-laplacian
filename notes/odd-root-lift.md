# The remaining sum class and roots modulo eight

For positive exponent residue roles a=1, b=3, c=2 modulo four, an
integer Laplacian spectrum requires

```text
a+c+4b = 27 modulo 32.
```

Every triple violating this condition is nonintegral, including all
permutations, with no size or ratio bound. The variables identify the
residue roles, not the increasing order of the exponents.
This strengthens the previous necessary condition a+c=15mod16.

## Proof

Suppose all five complement quotient roots are integers. The previous
shifted-root argument forces precisely two even roots and three odd
roots, all three congruent to three modulo four. The endpoint condition
forces a+c=15mod16, so write

```text
a=4u+1, b=4v+3, c=16t-4u-2.
```

These integer parameters cover every positive triple satisfying that
sum condition, subject to the original exponent positivity constraints.
Coefficientwise expansion of the complement quintic gives

```text
H(z)=h_C(4z+3)/64 belongs to Z[u,v,t,z],
H(z) = z^3 + v*z^2 + v*z + t+1 modulo 2.
```

Write its hypothetical odd roots as 4r_i+3. Then

```text
H(z) = product_j(4z+3-eta_j) * product_i(z-r_i),
```

where eta_j are the two even roots. Their factors reduce to one modulo
two. Thus the displayed binary cubic must split into three linear factors.

If v is even, the cubic is z^3+t+1. It splits exactly when t is odd;
otherwise it is (z+1)(z^2+z+1). If v is odd, it is
z^3+z^2+z+t+1. It splits exactly when t is even; otherwise it is
z(z^2+z+1). The quadratic z^2+z+1 is irreducible over the binary field.
In both cases, splitting requires t+v odd. Since

```text
a+c+4b = 16(t+v)+11,
```

this is exactly the asserted congruence modulo thirty-two. The noninteger
real complement root has a noninteger lift to the ideal intersection graph.

In the compatible cases the binary cubic is z^3 or (z+1)^3. Thus all
three odd roots, if integers, would be b modulo eight, and 512 would
divide h_C(b). This is further root information, not a claim that any
compatible triple is integral.

The [subsequent clustered-root proof](clustered-odd-roots.md) converts
this value condition into a+c=b(b+2)mod128, restricts b by its derivative,
and derives additional exclusions from the third shifted binary cubic.

## Additional range and exact checks

There are eight residues modulo thirty-two in each of the three roles,
giving 512 role-ordered triples. The previous sum condition leaves 128.
The new condition removes half of those, adding 64 exclusions, or 384
after all six permutations. The remaining 64 classes are compatible
with this argument. These counts follow the congruence, not an exponent scan.

Examples (13,18,19) and (9,31,38), ordered by size, have residue-role
triples (13,19,18) and (9,31,38). They obey the previous sum condition
but have a+c+4b=11mod32. Their shifted binary cubics contain the
irreducible quadratic. Both have minimum above seven, middle exponent
above fifteen, gcd one and unequal two-adic valuations.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_odd_root_lift.py` and
compare with [the certificate](../results/odd-root-lift.json).
The checker matches the direct complement quintic to Reza's reflected
source, verifies all exponent permutations and the arbitrary-shift
coefficient identities, and displays all eight shift-parity patterns.
Four fixtures, two newly excluded and two compatible controls, reconstruct
the full quintic by six independent integer determinants and a zero-root
check each: 28 determinants in total. The compatible controls also have
nonlinear rational factors, illustrating that congruence compatibility
does not imply integrality. No numerical eigenvalues or Lean are used.
Full Q3 and nonsquarefree higher-prime vectors remain open.
