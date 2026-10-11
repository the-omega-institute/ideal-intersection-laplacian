# Mixed-parity root distributions and the low integer endpoints

Every positive exponent triple that is a permutation of **(3,0,0) modulo
four** has a nonintegral ideal intersection graph, without a size or ratio
bound. This settles a class with exactly one odd exponent.

There is also a linear tail for two further mixed-parity patterns. For a
permutation of **(1,3,2)** or **(3,3,0) modulo four**, an integral spectrum
with minimum exponent m at least four requires

```text
maximum exponent M < R(m) = 7m - 16 + 40/(m+2).
```

In particular, for minimum at least eight, M>=7m-12 proves nonintegrality.
The minimum and maximum here refer to size order, not residue roles.

## The common root-distribution argument

For each of the three residue patterns, substitute
(a,b,c)=(4u+r_a,4v+r_b,4w+r_c) into the complement quintic. Exact
coefficientwise identities give

```text
h_C(x) = x^2(x+1)^3 modulo two,
F(y)=h_C(2y+1)/8 is an integer polynomial,
F(y) = (y+1)^3 modulo two.
```

Suppose every quotient root were an integer. The first identity forces
three odd roots and two even roots, counted with multiplicity. Write the
odd roots as 2r_i+1 and the even roots as eta_j. Then

```text
F(y) = product_j(2y+1-eta_j) product_i(y-r_i).
```

The even-root factors reduce to one modulo two. The binary cubic forces
each r_i to be odd, so every odd root is three modulo four. Therefore one
cannot be a quotient root under the integer-spectrum assumption. This is
a conditional root exclusion; it does not by itself assert h_C(1)!=0 for
every triple in these patterns.

## Complete one-odd-exponent class

For residue roles (3,0,0), a further identity is

```text
h_C(2) = 4 modulo eight.
```

Thus two is never a root. If the minimum exponent is at least four,
the already proved uniform comparison supplies a positive complement
root in (0,3). Were all roots integers, that root would be one or two.
The two preceding exclusions give a contradiction. The possible smaller
minimum is three, already covered by the minimum-three theorem.
This proves the entire positive residue class, including all permutations.

The triples (19,36,100) and (35,52,120) illustrate this class beyond the
minimum-through-seven and middle-through-fifteen certificates. The claim
for every exponent follows from the identities and the low-root proof,
not from these examples.

## A linear mixed-parity tail

For the patterns (1,3,2) and (3,3,0), the same conditional exclusion of
one leaves two as the only possible integer low root. Therefore an
integer spectrum with minimum m>=4 would require h_C(2)=0. The existing
endpoint-two theorem then gives M<R(m). Equivalently, M>=R(m) makes
h_C(2)>0 and proves nonintegrality. For m>=8, R(m)<=7m-12.

This extends the previous linear tail, which used all-even exponents to
exclude one. For example, the residue-role triples (25,27,758) and
(29,27,882) satisfy all three necessary conditions of the preceding
clustered-odd-root theorem but lie beyond this linear bound. The new
argument excludes them without a further congruence lift. The triple
(19,27,140) illustrates the other mixed pattern.

The remaining mixed triples in these two patterns must lie below the
linear bound as well as satisfy all applicable earlier restrictions.
Other mixed-parity patterns and the full Q3 characterization remain open.

## Exact verification

The [checker](../scripts/check_mixed_endpoint_roots.py) matches the direct
quintic with Reza's reflected formula and verifies all six exponent
symmetries. It proves the three arbitrary-shift identities and the
endpoint congruence coefficientwise. Eight selected full quintics are
independently reconstructed using 56 integer 6-by-6 determinant expansions.
Exact Sturm counts check the low-root fixtures. The known endpoint-zero
controls (9,9,136) and (10,10,12) are retained to check scope and the
direction of the cutoff. The latter is already nonintegral by the
repeated-exponent theorem; an endpoint zero is not integrality evidence.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_mixed_endpoint_roots.py
```

Compare with [the saved certificate](../results/mixed-endpoint-roots.json).
No exponent/modulus range scan, floating spectra or Lean formalization
is used. Nonsquarefree exponent vectors with more prime factors remain open.
