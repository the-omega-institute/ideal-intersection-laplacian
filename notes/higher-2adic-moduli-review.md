# Review of the fixed-divisor higher-modulus diagnostic

Reza's PR7 script was run unchanged at exactly the requested exponent
moduli 8,16,32. Its reflection uses the correct count
N=a+b+c+ab+ac+bc, and its necessary condition is correctly the union
32|h_C(1) **or** 32|h_C(3). No correctness correction was needed.
The [original output](../results/higher-2adic-moduli-original.txt) is retained.

| Exponent modulus | Ordered mixed-parity classes | Excluded by endpoint divisibility | Survivors |
| --- | ---: | ---: | ---: |
| 8 | 384 | 36 | 348 |
| 16 | 3072 | 288 | 2784 |
| 32 | 24576 | 2304 | 22272 |

The modulus-eight exclusions are exactly the permutations of the six
patterns already in Theorem13.6. At moduli sixteen and thirty-two each
base residue triple has eight and sixty-four lifts, respectively.
The higher tables contain no additional endpoint-divisibility exclusions.

## Why the test stabilizes

On every mixed-parity exponent class, both h_C(1) and h_C(3) modulo32
already have coordinate period eight. To verify the polynomial identity,
substitute (a,b,c)=(2u+e1,2v+e2,2w+e3), using parity representatives
(1,0,0) and (1,1,0). In each coordinate replace its shift by shift+4z.
Every coefficient of the difference in u,v,w,z is divisible by32, for
both endpoints. Permutation symmetry covers all six mixed parity patterns.
There are twelve symbolic identities with560coefficients in total.

Consequently increasing the exponent modulus alone while keeping the
endpoint divisor32 fixed cannot strengthen this test. This conclusion
does not rule out stronger necessary divisibilities or further root
information. The saved384base rows encode the complete higher tables
by lifting, including zero and equal residues.

## Independent verification

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_2adic_higher_moduli.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_2adic_higher_moduli.py
```

The [independent verifier](../scripts/verify_2adic_higher_moduli.py) first
reconstructs the general direct disjoint-support complement quotient and
checks both reflected endpoint polynomials. At every one of the28032
ordered mixed-parity residue triples in the three requested domains,
separately written integer Bareiss determinants check both endpoint
values:56064determinants in all. At endpoint three, integer division by
three precedes reduction modulo32. The known (9,9,136) endpoint-one zero
is also recovered. All counts and the six excluded base patterns agree
with the original script. The
[certificate](../results/higher-2adic-moduli-verification.json) saves the
full base table, symbolic period checks, counts and source hashes.

## Additional root-distribution information

The new [written theorem for all permutations of (3,3,2) modulo four](https://github.com/the-omega-institute/ideal-intersection-laplacian/blob/35ac15620742477a408f4ada31050004cacfe486/notes/odd-root-distribution.md)
uses the shifted quintic and its derivative. It therefore excludes some
classes that pass this endpoint-divisor test. Combining the two results
gives48excluded base classes and336survivors modulo eight; the higher
counts are384/2688 at sixteen and3072/21504 at thirty-two.
These combined counts concern these two results alone, without applying
all the manuscript's other restrictions.

No new exponent range or modulus was added. These residue survivors do
not assert endpoint zeros or integral spectra. Full Q3 and nonsquarefree
higher-prime vectors remain open; no numerical spectrum or Lean was used.
