# A divisibility obstruction for mixed parity

Six further infinite residue classes give nonintegral three-prime ideal
intersection graphs. Relabel the two odd exponents as a,b and the even
exponent as c. Any row of this table, or exchange of a and b, suffices:

| a modulo 8 | b modulo 8 | c modulo 8 | h_C(1) modulo 32 | h_C(3) modulo 32 |
| --- | --- | --- | --- | --- |
| 1 | 3 | 2 | 8 | 16 |
| 1 | 7 | 2 | 24 | 16 |
| 3 | 7 | 2 | 16 | 8 |
| 3 | 5 | 6 | 8 | 16 |
| 3 | 7 | 6 | 16 | 24 |
| 5 | 7 | 6 | 24 | 16 |

The exponent sizes, ratios and differences are unrestricted. Examples
are (10,17,19) and (14,19,21), whose middle exponents exceed fifteen,
whose gcd is one, and whose 2-adic valuations differ. The proof rules out
a completely integer quotient spectrum without identifying its lowest root.
Read [the manuscript source](../paper/sections/mixed-parity-congruence.tex)
and [the exact certificate](../results/mixed-parity-congruence.json).

## Three odd roots force a stronger divisor

For either mixed exponent parity, the general complement quintic satisfies

```text
h_C(x) = x^2(x+1)^3 modulo 2.
```

If its five roots were integers, precisely two would be even and three
odd, counted with multiplicity. Among the three odd roots, at least two
share a residue r modulo four, where r is one or three. At x=r, the
corresponding two factors are divisible by four, and the third odd-root
factor is divisible by two. The two even-root factors are odd. Hence

```text
32 divides h_C(1) OR 32 divides h_C(3).
```

The reasoning includes coincident roots and a zero evaluation. It applies
to every monic integer quintic with binary reduction x^2(x+1)^3.

Now substitute a=8u+r1, b=8v+r2, c=8w+r3 in the exact complement
quintic. For each of the six rows, expansion gives the displayed constant
residues at one and three modulo 32; all nonconstant coefficients are
divisible by 32. Neither value is divisible by 32, contradicting the
necessary condition. Thus a complement quotient root is noninteger.
The quotient is similar to a real symmetric matrix, and the graph lift
V-mu gives a noninteger graph eigenvalue.

This proof uses three odd roots forced by the **quintic's** binary
factorization. It does not confuse them with the number of odd exponents.
The test also works for a triple with exactly one odd exponent whenever
the same two evaluations fail the necessary condition; the six displayed
rows have exactly two odd exponents.

## Why the first binary checks do not suffice

With two even and three odd hypothetical roots, evaluation at an even
integer must be divisible by four and evaluation at an odd integer by
eight. Symbolic substitution for both mixed exponent parities shows that
these initial divisibilities hold identically and supply no obstruction.

The complete lower-modulus checks also find a product of five monic
linear factors for every mixed-parity residue triple modulo four and
eight: all 12 and 80 unordered classes, respectively. These are compatible
factorizations over finite rings, not evidence of actual integer spectra.
The additional distribution of three odd roots modulo four supplies the
stronger divisor 32 used in the theorem.

## Exact verification

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_mixed_parity_congruence.py
```

The [checker](../scripts/check_mixed_parity_congruence.py) reconstructs
the general complement quintic. It verifies the two mixed binary
reductions, the four initial symbolic divisibility identities, and all
558 coefficients in the twelve substitutions for the six rows. Six
positive residue representatives and the two examples above have both
values independently reconstructed by 720-term integer determinant
expansions and separate integer Horner evaluations. The examples retain
nonlinear rational factors. The lower-modulus tables save explicit
compatible root multisets for each of the 92 unordered residue triples.

The infinite result follows from the written pigeonhole and divisibility
argument; the symbolic checks verify its algebraic table. No exponent
scan, floating-point spectrum or Lean is used. Full Q3 remains open.
Reza's proposed fixed-prime endpoint-root script remains a separate
complementary direction; it has not been replaced by this investigation.
