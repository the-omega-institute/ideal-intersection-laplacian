# A modulo-five splitting obstruction and the equality problem

**Theorem.** Every positive exponent triple that is a permutation of
`(1,1,2)` or `(1,4,4)` modulo five has a nonintegral ideal intersection
graph. There is no size, gap, parity or endpoint-zero hypothesis.

This follows from the monic integer complement quotient polynomial
`h_C(x)=det(xI-C)/x`. An integer spectrum would make its reduction modulo
five a product of linear factors. The complete reductions are

```text
(1,1,2): h_C(x)=(x-1)^2(x-3)(x^2+3x+4) mod5,
(1,4,4): h_C(x)=(x-1)^2(x^3+x^2+4x+3) mod5.
```

The quadratic discriminant is three, a nonsquare modulo five. The cubic
takes the values `3,4,3,1,4` at `0,1,2,3,4`, so it has no field root
and is irreducible. The quotient polynomial is symmetric in the exponents,
which supplies all permutations. Both reductions therefore contradict an
integer quotient spectrum, and the complement/universal-class lifts give
noninteger graph eigenvalues. This is a written finite-field proof for
unbounded integer exponent classes, rather than an exponent search.

## Consequence for the elementary equality system

On `c=b(b+2)-a`, put `q=ac`. The established identity is

```text
h_C(x)=(x-1)(x-b)P3(x)+x(x-b)G(a,b),
G=(3b-1)q^2+b(b^2+4b-1)q
  -(b^2+2b-1)(b^2+3b-1)(b^3+3b^2+3b-1).
```

At an integer equality point `G=0`, an integral spectrum requires P3 to
split over every finite field. For `b=1mod5`, the curve condition reduces to
`G=2(q-1)(q-2)mod5`, with `q=a(3-a)mod5`. It permits precisely
`a=1,2,4mod5`. For q=2 the cubic is
`(x-3)(x^2+3x+4)`; for q=1 it is `x^3+x^2+4x+3`. Neither splits, so
**an integral equality spectrum requires b!=1mod5**.

The q=1 cubic has discriminant one modulo five and is irreducible. Thus
the necessary square-discriminant congruence genuinely misses this row;
the integer-root equation in the elementary system remains essential.
This does not contradict square discriminant plus an actual integer root
being sufficient for integral splitting in characteristic zero.

All equality residues satisfying G=0 modulo five are:

| a | b | c | Cubic discriminant mod5 | Cubic splits mod5 |
|---:|---:|---:|---:|:---|
| 0 | 2 | 3 | 0 | yes |
| 1 | 0 | 4 | 0 | yes |
| 1 | 1 | 2 | 2 | no |
| 2 | 0 | 3 | 1 | yes |
| 2 | 1 | 1 | 2 | no |
| 3 | 0 | 2 | 1 | yes |
| 3 | 2 | 0 | 0 | yes |
| 4 | 0 | 1 | 0 | yes |
| 4 | 1 | 4 | 1 | no |

Consequently the remaining elementary system must have

```text
(a,b)mod5 in {(1,0),(2,0),(3,0),(4,0),(0,2),(3,2)}.
```

These six rows are necessary compatibility conditions. They neither assert
integer points on the equality curve nor prove integral spectra. The
comparison at modulo three has six G=0 rows, all with split cubics, so
it provides no additional equality splitting obstruction.

## Exact validation and scope

The checker verifies the generic equality identity and all six exponent
permutations from the six-support quotient. It checks every one of the
34 residue pairs at the fixed primes three and five, with separate
root-multiset enumeration and polynomial factorization. Independent
720-term integer determinant expansions check every endpoint residue,
both complete global residue polynomials at seven interpolation points,
and five fixed positive controls, for 83 determinants in total.

The controls `(9,16,19)` and `(11,16,22)` illustrate the two global
classes. `(14,21,469)` and `(26,41,1737)` lie on E=0 but not on G=0;
they are not integer endpoint-one solutions. The established repeated
endpoint-one zero `(9,9,136)` is retained and matches the global
`(1,4,4)mod5` reduction after permutation. Its nonintegrality was already
settled by the repeated-exponent theorem.

With Python 3.10+ and SymPy1.14.0, run

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_one_equality_mod_five.py
```

Compare with [the certificate](../results/endpoint-one-equality-mod-five.json).
The certificate records every curve row, all source hashes and the fixed
controls. No exponent scan, higher two-adic shift, integer-point enumeration,
rank calculation or Lean verification is used. This theorem needs no finite
exponent base; earlier global theorems retain their own dependencies.
The endpoint-one integer classification and full Q3 remain open.

[Return to the project entrance](../README.md).
