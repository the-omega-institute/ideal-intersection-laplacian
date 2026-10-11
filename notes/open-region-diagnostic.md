# Reza's requested open-region diagnostic and complete minimum-through-seven certificate

Reza requested the region `4<=a<=7`, `a<b<c<4a^2-2a` in his
[PR comment](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/3#issuecomment-5979680229).
His source commits `56c8d97557311704de1d86697e5a38ddaee38fa5` and
`f8c810fbef544362fcae727ae7bd9bccb5467ce5` are preserved in this PR.

The corrected run exhausts **all 27,562 triples**. Every H-quotient quintic
has a positive nonsquare integer discriminant and hence a noninteger root.
The [full console output](../results/open-region-diagnostic.txt),
[summary and first sign-pattern witnesses](../results/open-region-diagnostic.json),
[complete discriminant/square-bracket CSV](../results/open-region-discriminants.csv),
and [independent verification receipt](../results/open-region-certificate-check.json)
are saved.

Because the [written uniform cutoff](distinct-tail.md) already settles
`c>=4a^2-2a`, this particular finite run exhausts every remaining pair for
minimum exponent4,5,6,7. With the earlier repeated/minimum-three results,
it therefore gives a **complete computer-assisted proof for every triple
with minimum exponent at most seven**. It does not bound the minimum
exponent in general; full Q3 remains open. Read the proof and explicit
finite-certificate dependence in [the manuscript](../paper/paper.pdf).

## Script corrections and polynomial identity

The original first run stopped at `Integer(disc).is_square`, which is
not an available property in SymPy1.14.0. We use the exact standard-library
integer square root. Exact rational factorization replaces the fallback
divisor/root-removal loop; in the requested run every case already has a
nonsquare discriminant. The generic characteristic polynomial is computed
once, then its integer coefficients are specialized for every triple.
The requested bounds are unchanged. The duplicate older filename remains
a compatibility entrypoint.

The source script constructs the quotient **B of H**, not the complement C.
Its original variable `h` is therefore denoted `g_B` in the output:

```
g_B(x)=det(xI-B)/x,
h_C(x)=det(xI-C)/x=-g_B(N-x),
N=a+b+c+ab+ac+bc.
```

The earlier low-endpoint arguments use `h_C`. The two sign reports differ:

| a | c exclusive bound | Cases | Noninteger root | g_B --- | h_C -+- | h_C -++ | h_C +++ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 56 | 1275 | 1275 | 1275 | 14 | 367 | 894 |
| 5 | 90 | 3486 | 3486 | 3486 | 13 | 1189 | 2284 |
| 6 | 132 | 7750 | 7750 | 7750 | 13 | 2890 | 4847 |
| 7 | 182 | 15051 | 15051 | 15051 | 13 | 5925 | 9113 |

For `g_B`, the pattern at1,2,3 is `---` in every case. This gives no
sign change at these endpoints. For `h_C`, all three listed nonzero
patterns occur at every requested minimum. Different patterns do not imply
that a uniform proof is impossible: an inertia argument can count two
roots in one interval even when endpoint signs agree. The
[new inertia theorem](low-spectrum.md) proves four unequal-exponent
families for every positive minimum exponent without scanning that exponent.

## Complete exact certificate

If all roots of a monic integer polynomial were integers, its discriminant,
the product of squared root differences, would be an integer square.
The CSV gives every triple, its discriminant Delta and an integer q with
`q^2<Delta<(q+1)^2`. These strict brackets exclude square discriminants.
The quotient is similar to a real symmetric Laplacian, so its noninteger
root is a real nonzero eigenvalue and lifts across the universal vertices.

The independent checker derives its quintic from the support quotient and
recomputes **every** discriminant with an integer9x9Sylvester determinant
using a separate Bareiss implementation. It checks exact division at every
elimination step, all square brackets, the lexicographically ordered full
domain, and absence of extra rows. The16diagnostic representatives additionally
check direct matrix characteristic polynomials, complement endpoint reflection
and rational factorization. No floating-point spectrum or Lean is used.

Run with Python3.10+ and SymPy1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_open_region2.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_open_region2.py --json --certificate-csv results/open-region-discriminants.csv
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_open_region_certificate.py
```

Compare the second and third command outputs with the saved JSON files.
The remaining three-prime problem lies within `8<=a<b<c<4a^2-2a`, outside
the proved bounded-gap families and the general inertia criterion.

[Return to the project entrance](../README.md).
