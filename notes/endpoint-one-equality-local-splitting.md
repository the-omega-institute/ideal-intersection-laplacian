# Local splitting at odd prime divisors of the middle exponent

Fix an integer equality point c=b(b+2)-a, q=ac, G(q,b)=0, and let P3
be the established monic equality cubic. The previous
[local discriminant theorem](endpoint-one-equality-local-discriminant.md)
excluded its negative branch when 13 is a nonresidue. The following
result completes that local test, including the remaining positive branch.

**Theorem.** Let p be any odd prime dividing b. Then q is either1 or-1
modulo p.

- If q=1modp, P3 has three distinct roots in Z_p. This includes p=13.
- If q=-1modp and p!=13, P3 splits into three distinct Z_p roots exactly
  when 13 is a quadratic residue modulo p. Otherwise it has exactly one
  Q_p root and an irreducible quadratic factor.

In the split negative branch, write e=v_p(b). The two roots reducing
to-1 have difference of valuation exactly e, while their differences
from the root reducing to0 are units.

Thus, away from p=13 on the negative branch, the normalized
discriminant condition is both necessary and sufficient for **local**
splitting. Local splitting does not give an integer equality point or
an integer spectrum.

## The positive branch already splits at every prime power

At p|b, the curve equation reduces to G=1-q². Also q=-a²modp.
For q=1, this forces a²=-1modp, and the cubic reduction is

```text
P3(x)=x(x²+1)modp.
```

Its three distinct roots are0,+a,-a. Their derivatives are respectively
1,-2,-2 modulo p, all nonzero because p is odd. Hensel's simple-root
lemma lifts each to a unique root in Z_p. The monic degree-three
polynomial therefore splits into three distinct linear factors over Z_p.

In particular, every actual equality point in the surviving
(a,b)=(2,0) or(3,0)mod5 rows has a cubic that splits over Z_5 and
over Z/5^kZ for every k>=1. Increasing the power of five in a splitting
table cannot exclude those rows. This conclusion follows from a written
lifting theorem, without enumerating any power or exponent range.
Other equations or primes can still obstruct integer spectra.

## The negative branch has a complete ordinary local criterion

For q=-1modp, P3=x(x+1)²modp. The root0 is simple, since P3'(0)=1modp.
Hensel gives a unique root d0 in pZ_p and an exact factorization

```text
P3(x)=(x-d0)Q(x),
Q(x)=x²+(d0-A)x+d0²-A d0+B,
delta_Q=A²+2A d0-3d0²-4B.
```

Here A,B are the cubic's established root sum and pair sum. These
formulas use polynomial division and do not divide by d0; they also
apply if the lifted root is zero. Reducing Q modulo p gives (x+1)².
Since d0 is simple, P3'(d0) is a unit. The discriminants satisfy

```text
Delta=P3'(d0)² delta_Q.
```

The earlier anchor argument gives, for e=v_p(b),
Delta=13b²modp^(3e). If p!=13, its valuation is2e and its normalized
unit is13(b/p^e)²modp. An odd-prime-adic unit is a square exactly when
its reduction modulo p is a nonzero square, by Hensel's lemma applied
to z²-unit. Therefore delta_Q is a square in Q_p exactly when 13 is a
residue modulo p.

For odd p, the quadratic formula now gives both Q roots in Z_p in
the square case: its coefficients and its square-root discriminant
are integral, and2 is a unit. They are distinct because Delta!=0,
and both reduce to-1. Their difference has valuation e. In the
nonsquare case Q is irreducible over Q_p, so d0 is the only Q_p root.
The root differences to d0 are units because0 and-1 are distinct modulo p.

At p=13 the normalized leading unit vanishes; the negative branch
requires a further mathematical reduction. The positive branch proof
still applies there. No assertion about the prime two is added.

## Exact verification and the remaining question

The [checker](../scripts/check_endpoint_one_equality_local_splitting.py)
verifies both reductions, the simple-root derivative identities, generic
polynomial division and the discriminant identity modulo P3(d)=0.
It reruns the established direct six-support characteristic identity,
independent5x5Sylvester discriminant and local anchor identities. The
specified examples at3,5,7 illustrate a split negative branch, a positive
branch and an excluded negative branch. They are residue examples,
not asserted integer equality points.

Run with SymPy1.14.0 and Python3.10+:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_one_equality_local_splitting.py
```

Compare with [the certificate](../results/endpoint-one-equality-local-splitting.json).
The prime-power conclusion is a written proof using Hensel's lemma;
no prime/power/exponent scan or finite exponent base is used. The
integer-root equation and global square discriminant remain necessary
for integer splitting. The four necessary modulo-five pairs, the7/11
divisibility exclusions, and the unresolved equality classification and
full Q3 are retained. No new nonintegrality family or Lean result is claimed.

[Return to the project entrance](../README.md).
