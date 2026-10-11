# Modular endpoint candidates are a union

Reza's PR6 script uses the correct complement reflection
`h_C(x)=-g_B(N-x)` with `N=a+b+c+ab+ac+bc`. Its candidate-set logic
needed correction: the uniform positive root in (0,3) requires

```text
h_C(1)=0 OR h_C(2)=0,
```

for a possibly integral graph. It does not require both endpoints to vanish.
Thus the surviving c-root set is the **union** of the endpoint-one and
endpoint-two sets. A residue triple is excluded by this low-root test
when **both values are nonzero**. The intersection is retained as a
separate diagnostic with no claim that it represents all candidates.

The known repeated triple (9,9,136) illustrates the distinction:
`h_C(1)=0`, but `h_C(2)=3660018448`. It is already nonintegral by the
repeated-exponent proof. An empty intersection would not establish that
neither endpoint can occur. At prime two the correction is also visible:
all eight residue triples survive the union, whereas only six lie in
the intersection.

## Complete results at the contributor's six fixed primes

| Prime | Surviving union | Both nonzero, excluded | Both zero, intersection only |
| --- | --- | --- | --- |
| 2 | 8 | 0 | 6 |
| 3 | 22 | 5 | 15 |
| 5 | 78 | 47 | 27 |
| 7 | 142 | 201 | 39 |
| 11 | 371 | 960 | 37 |
| 13 | 505 | 1692 | 39 |

For each prime, a positive exponent triple with minimum at least four
and both endpoint values nonzero modulo that prime is nonintegral by
the uniform low-root proof. Smaller minima are already settled.
The [full root-set JSON](../results/modular-endpoints.json) therefore
specifies checked congruence exclusions, with no upper bound on the
exponents. No prime in this fixed list settles the entire remaining region.

All residue coordinates, including zero and equal coordinates, are
retained: distinct positive integers can have equal residues. Degree drops
and zero endpoint polynomials are evaluated correctly by checking every
field element. The original contributor's quotient construction is preserved.
The [original output](../results/modular-endpoints-original.txt) is kept
alongside the [corrected output](../results/modular-endpoints-corrected.txt).

## Independent verification

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_modular_endpoints.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_modular_endpoints.py --json
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_modular_endpoints.py
```

The [verifier](../scripts/verify_modular_endpoints.py) starts from the
direct disjoint-support complement matrix and checks the generic quotient
reflection identity. Independent determinants check both endpoint values
at all **4,031 residue triples**, giving **8,062 endpoint checks**.
There are 8,054 modular Gaussian determinant calculations and eight
integer determinant expansions for endpoint two modulo two, where field
division is unavailable. Every root set at all **377 pairs** agrees with
the corrected reflected-H script. The regression values at (4,5,6) are
-23520 and 1656, and both known repeated endpoint-zero controls are retained.
See [the verification receipt](../results/modular-endpoints-verification.json).

Fixed finite congruence tests still have survivors obtained by lifting
the known endpoint-zero controls; those are not asserted actual integer
zeros or integral graphs. Further interval/divisor restrictions or another
noninteger-root obstruction are needed. The separate manuscript PR3
contains a three-odd-root divisor argument that supplies six further
mixed-parity classes modulo eight. No exponent scan, floating-point
spectrum or Lean is used here; full Q3 remains open.
