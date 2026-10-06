# Low-root divisibility for repeated minima

**Theorem.** For four distinct primes with positive exponents (a,a,b,c),
a>=5 and b,c>=a, Laplacian integrality requires at least one of

```text
(a-1) divides 3b^2c^2,
(a-2) divides 20b^2c^2.
```

If neither divisibility holds, the smallest genuine restricted root is
noninteger and gives a noninteger graph eigenvalue in (V-3,V), where
V=(a+1)^2(b+1)(c+1)-2. The tails need not be ordered or unequal.

Consequently, if gcd((a-1)(a-2),bc)=1, every such vector is
nonintegral unless a is one of 6,7,12,22. These are exceptions to
this sufficient arithmetic criterion, not assertions of integral graphs.

In particular, every vector

```text
(a,a,a+1,(a+1)^2), a=6s, s>=3,
```

is nonintegral. This entire unbounded family passes the preceding
modular splitting test at every prime divisor of a+1.

## The complementary low restricted root

Use the genuine repeated-pair operator K and weighted-zero-sum graph
transfer from the [balanced single-pair proof](four-prime-single-pair-balanced.md).
The general tensor positivity argument gives kappa_min(K)>1.
The empty/full-support principal minor of the symmetric similar matrix
K-4I is

```text
J4=-(2a+3)bc+(a^2-2a-3)(b+c)+2a^2-9a+9.
```

Writing b=a+v,c=a+w with v,w>=0 yields

```text
J4=-(2a+3)vw-(a^2+5a+3)(v+w)-5a^2-15a+9<0.
```

Thus a negative trial direction gives kappa_min(K)<4. For our domain,
1<kappa_min(K)<4, and its only possible integer values are 2 and 3.
This low root complements the second-root/unique-tail conditions used
in the preceding notes; it is a different eigenvalue.

## Endpoint residues

Put p(x)=det(xI-K). The established generic anchor identity is

```text
p(a+1)=-a^2b^2c^2(2a+1).
```

Since p(x) has integer polynomial coefficients in a,b,c, reducing
p(2) modulo a-1 is equivalent to substituting a=1, and reducing
p(3) modulo a-2 is equivalent to substituting a=2. Therefore

```text
p(2)=-3b^2c^2 modulo a-1,
p(3)=-20b^2c^2 modulo a-2.
```

If the smallest restricted root were 2, its characteristic value would
vanish and the first divisibility would hold. A smallest root equal
to 3 would force the second. Excluding both leaves a noninteger
root in (1,4), whose actual graph lift is V+1-kappa_min. This
proves the theorem without a parameter search.

For coprime tails, bc is invertible modulo both a-1 and a-2.
The first divisibility would force a-1 to divide 3, impossible for
a>=5. The second would force a-2 to divide 20. The divisors of
20 at least three are 4,5,10,20, giving exactly a=6,7,12,22.

## An infinite family passing every earlier modular test

Let a=6s with s>=3, b=a+1 and c=(a+1)^2. Both tails are at
least a. Since a is even,
gcd(a-1,a+1)=gcd(a-1,2)=1. Also
gcd(a-2,a+1)=gcd(a-2,3)=1. As bc=(a+1)^3, the coprime
corollary applies. None of 6,7,12,22 is a multiple of six at least
18, so the family is nonintegral.

For every p dividing a+1, both tails reduce to zero. Their factor
quadratics are x(x-1), and hence split. The
[modular repeated-pair theorem](repeated-pair-modular.md) therefore
does not exclude this family. The low-root arithmetic supplies the
additional obstruction.

This family also lies outside the preceding sufficient spectral regions.
Its tail gap r=a(a+1) is even and at least 342, it has no exponent
one through four or second equal pair, and c>2a-6 excludes the
balanced region. The product-tail and even-gap weighted criteria fail
with margins a^4+2a^3-9a-2 and
2a^5+5a^4+4a^3-7a^2-8a respectively. The latter also excludes
the earlier weaker weighted and midpoint criteria. The complete
positive coefficient lists after a=z+18 are:

| Comparison | Coefficients in descending powers of z |
|---|---|
| product tail | 1,74,2052,25263,116476 |
| even-gap weighted | 2,185,6844,126569,1170028,4324932 |
| small exponent m=a | 2,186,6916,128513,1193353,4429852 |
| small exponent m=a+1 | 2,189,7144,135012,1275697,4821138 |
| small exponent m=(a+1)^2 | 3,341,16149,407853,5793630,43889582,138523644 |

For the small-exponent comparison, the margin is
(m^2-1)B_m-(m-1)-A_m, where
A_m=product_(i!=m)k_i and B_m=product_(i!=m)(k_i+1)-1-A_m.
These three rows check every coordinate choice. The large-tail cutoff
also exceeds c: with M=(a+1)(a+2)>c, its value
24(M+a)^3(3M+a)>72M^4>c. The earlier finite-candidate reductions
remain applicable but do not by themselves exclude the entire family.
This is a comparison with the recorded criteria, not a priority claim.

## Verification and remaining scope

The [checker](../scripts/check_four_prime_low_root_divisibility.py)
verifies the generic anchor, both exact remainder identities and
integer polynomial quotients, the negative upper minor, all exceptional
divisors and five positive comparison polynomials. Six specified
controls reconstruct 336 support-column actions and check weighted
zero sums, symmetry and the actual complement-to-graph transfer.
Thirty independent integer determinants verify the six quartics at
x=0,1,2,3,4; six exact Sturm counts check the low-root interval.
The a=6 and a=22 controls deliberately pass one necessary divisibility,
illustrating the test's limitation without asserting integrality.

The [certificate](../results/four-prime-low-root-divisibility.json)
is reproducible with SymPy 1.14.0 using
`python3 scripts/check_four_prime_low_root_divisibility.py`.
The unbounded conclusion rests on the written argument; the fixed
controls check the algebra and implementation. No exponent/tail scan,
expanded graph, historical finite-base rerun or Lean validation is used.

For remaining repeated minima, combine the necessary disjunction of
these two low-root divisibilities with the unique-tail conditions and
modular residue restrictions. Holding one divisibility does not make
its endpoint a root. General single-pair, fully unequal four-prime and
higher-prime classification remain open. The focused three-prime main
and joint manuscript-scope decisions are retained.
