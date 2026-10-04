# Complete endpoint diagnostic for the requested pair range

For **every pair `4<=a<b<=15` and every integer `c>b`**, both complement
endpoints are nonzero:

```text
h_C(1) != 0 and h_C(2) != 0.
```

This is a complete exact certificate over **66 pairs and 132 cubics**.
There is no imposed cutoff on c. The previously proved
[positive complement root in (0,3)](https://github.com/the-omega-institute/ideal-intersection-laplacian/blob/f49f6334292f3955ca88859b269c0581a8677f47/notes/mixed-inertia.md)
therefore proves nonintegrality for every fully distinct exponent triple
in this pair range. The finite certificate includes 28 pairs with a at
least eight. It does not bound the minimum exponent in general or settle Q3.

## Review of Reza's diagnostic

Reza supplied `check_endpoint_surfaces.py` in commit
`4324bbcceae4bdd85e6f7b3ba1183d93173b8bd6` and requested its default
range through b=15. The original script was run unchanged before editing;
its [output](../results/endpoint-surfaces-original.txt) reported an empty list.
That output used the wrong reflection shift and actually stopped at b=14.

The quotient B in the script is the Laplacian quotient of H, after
deleting the universal class. Thus the reflected complement quintic is

```text
h_C(x) = -g_B(N-x),
N = |V(H)| = a+b+c+ab+ac+bc.
```

The full graph has `(a+1)(b+1)(c+1)-2` vertices, including `abc-1`
universal vertices. That full count cannot be used in this reflection.
For example, at `(4,5,6)` the original shift gives endpoint values
`-54772674264` and `-52833379392`; the correct values are `-23520`
and `1656`. The wrong endpoints are quintics in c, whereas the correct
ones are cubics.

The correction also includes b=15, as requested, and extracts integer
roots from exact rational linear factors using `ground_roots()`, avoiding
dependence on radical expressions. The original contributor's matrix
construction and diagnostic structure are retained.

The [corrected output](../results/endpoint-surfaces-corrected.txt) is:

```text
=== Surface h_C(1) = 0 ===
  Subtotal: 0 triples

=== Surface h_C(2) = 0 ===
  Subtotal: 0 triples

Total candidate triples: 0
```

## Independent completeness certificate

The separate [verifier](../scripts/verify_endpoint_surfaces.py) starts
from the direct disjoint-support complement matrix, reconstructs its
generic characteristic quintic, and specializes the two cubics for each
of the 66 pairs. It checks the quotient/reflection identity against
Reza's corrected H construction for every pair.

The endpoint cubics have nonzero constant terms

```text
K1 = (a-1)(b-1)(a+b-1)(ab+a+b-1),
K2 = 2(a-2)(b-2)(a+b-2)(ab+a+b-2).
```

An integer endpoint root c must divide its constant term, by reduction
of the equation modulo c. The verifier exhausts **all 8,527 positive
divisors**, evaluates each of the **7,585 divisors above b** by separate
integer Horner arithmetic, and finds no root. The resulting lists agree
with exact rational linear-factor extraction in the corrected script.
The [certificate](../results/endpoint-surfaces-verification.json) records
all 132 coefficient lists, divisor counts and root lists.

Two positive controls outside the fully distinct requested range are
retained: `(9,9,136)` has endpoint one and `(10,10,12)` has endpoint two.
The corrected root extraction recovers both; direct complement matrices
match the reflected quintics, and their full rational factorizations have
nonlinear factors. Both are previously settled repeated-exponent cases.

Reproduce the outputs with Python and SymPy 1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_surfaces.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_endpoint_surfaces.py
```

This certificate answers the requested finite diagnostic completely,
including unbounded integer c. For b beyond 15 the endpoint surfaces still
need a proof. The existing common-divisor, residue, valuation, balanced
and tail results are retained in [PR3](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/3).
No numerical spectrum or Lean verification is used.
