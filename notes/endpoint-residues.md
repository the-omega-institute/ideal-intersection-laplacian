# Endpoint residues and two modulo-three families

Every positive three-prime exponent triple with residues **(2,2,2)** or
a permutation of **(1,2,2) modulo 3** gives a nonintegral ideal intersection
graph. These infinite classes follow from the written low-root argument
and the two polynomial identities below. The complete residue tables also
answer Reza's parity question and delimit the proposed covering method.

## Parity of both endpoints

For the complement quintic `h_C(x)=det(xI-C)/x`, the complete binary table is:

| Number of odd exponents | h_C(x) modulo 2 | h_C(1) modulo 2 | h_C(2) modulo 2 |
| --- | --- | --- | --- |
| 0 | x^5 | 1 | 0 |
| 1 | x^2(x+1)^3 | 0 | 0 |
| 2 | x^2(x+1)^3 | 0 | 0 |
| 3 | x(x^2+x+1)^2 | 1 | 0 |

The factor x in the all-odd quintic is necessary; it does not alter the
value at one. Parity excludes endpoint one for all-even and all-odd triples,
but excludes endpoint two in none of the eight parity classes.
To use the uniform root in (0,3), both integer endpoints must be excluded.
Exclusion of just one surface is insufficient for that argument.

## Complete pair/root table modulo three

The entries are all residues c for which the indicated endpoint vanishes.
Zero residues are included, and a zero polynomial has every field element
as a root. Symmetry gives the omitted transposed pairs.

| (a,b) modulo 3 | c roots of h_C(1) | c roots of h_C(2) |
| --- | --- | --- |
| (0,0) | {1} | {2} |
| (0,1) | {0,1,2} | {1,2} |
| (0,2) | {1,2} | {0,1,2} |
| (1,1) | {0,2} | {0,1,2} |
| (1,2) | {0,1} | {0,1} |
| (2,2) | {0} | {0} |

Thus the triples with **both endpoints nonzero modulo 3** are exactly
(0,0,0), (2,2,2), and the three permutations of (1,2,2).
The first class is already covered by the common-divisor theorem.
The other two patterns add infinite classes. Direct reduction gives

```text
(2,2,2): h_C(x) = x^5 modulo 3,
(1,2,2): h_C(x) = (x^2+1)(x^3+x^2-x+1) modulo 3.
```

For (2,2,2), the endpoint values are 1 and 2 modulo 3. For (1,2,2),
both values are 1. If the minimum exponent is at most three, the earlier
small-minimum results apply. Otherwise the written uniform comparison
provides a positive complement root in (0,3); it cannot be either one
or two, so it and its graph lift are noninteger. In the second pattern,
the irreducible factor x^2+1 gives an alternative direct proof.

For example, (8,17,22) and (8,17,23) meet these criteria, have gcd one
and unequal 2-adic valuations, and lie beyond the second-smallest-at-most-15
certificate. The checker verifies their endpoints by integer determinants
and their low roots by exact Sturm counts.

Every pair (a,b) modulo 2 or 3 has at least one c root on **each** surface.
Consequently a script that retains only pairs with no c root would return
no exclusions for these primes and miss the new triple-level classes.
Retaining the full c-root sets is essential.

## What a finite congruence covering can establish

Neither surface is empty on all positive triples: the already settled
repeated triples (9,9,136) and (10,10,12) lie on endpoints one and two,
respectively. The possible fully distinct triples remain the relevant question.

There is also a limitation even after excluding actual repeated triples.
Fix any finite collection of congruence moduli and let M be their least
common multiple. Every triple congruent to (9,9,136) modulo M passes the
endpoint-one zero test at every chosen modulus. For any sufficiently large
integer k, the triple

```text
(9+kM, 9+(k+1)M, 136+(k+2)M)
```

is positive, strictly ordered and has middle exponent greater than 15.
It passes all those endpoint-one congruence tests. Likewise

```text
(10+kM, 10+(k+1)M, 12+(k+2)M)
```

passes every endpoint-two test. These are modular survivors, not asserted
integer zeros or integral examples. Thus endpoint tests at a fixed finite
set of moduli alone cannot establish global emptiness on fully distinct
positive triples. A proof must use further arithmetic or spectral information,
such as the existing interval restrictions or another-root obstruction.
This observation does not preclude combining congruences with those restrictions.

## Verification and a specification for Reza's script

The bounded [checker](../scripts/check_endpoint_residues.py) reconstructs
the symbolic quintic from the direct complement quotient. It records all
26 pair/endpoint rows for primes 2 and 3 and all eight parity classes in
the [certificate](../results/endpoint-residues.json). Both endpoint values
at every one of the 35 positive residue representatives are independently
checked by a 720-term integer determinant expansion. This includes endpoint
two modulo two: divide the integer characteristic value by two **before**
reducing, rather than dividing by zero in the field.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_residues.py
```

For an extended script, retain the full root sets for **both** endpoints,
including zero residues and degree drops; distinguish a zero polynomial
from a nonzero constant. A triple is excluded by the low-root test at a
prime only if both endpoint values are nonzero there. Alternatively, track
the forbidden residues for each surface separately: exclusion of endpoint
one at one prime and endpoint two at another also rules out integrality.
Use the corrected shift N=a+b+c+ab+ac+bc, or construct C directly.
The two known endpoint-zero controls and the values -23520/1656 at (4,5,6)
provide regression fixtures. Another-root evidence, such as a nonlinear
irreducible factor of the quintic modulo a prime, can settle an endpoint
survivor without proving that the surface itself is empty.

The infinite modulo-three result is a written proof with finite identity
checks. No exponent search, floating-point spectrum or Lean was used.
The complete Q3 classification remains open.
