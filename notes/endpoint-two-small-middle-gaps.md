# Excluding endpoint two when the two smallest exponents are close

Let C be the six-support complement quotient and `h_C(x)=det(xI-C)/x`.
All exponent labels below are in **size order**, independently of residue roles.

**Theorem.** Every integer triple

```text
(a,a+d,c),  a>=8,  1<=d<=4,  c>a+d
```

has **`h_C(2)!=0`**. There is no bound on c. The [gap-two theorem](endpoint-two-gap-two.md)
already handles d=2. Here we prove the remaining gaps d=1,3,4 with written
infinite tails and a complete exact finite base for 76 fixed pairs.
The combined statement down to a=8 depends on that finite computation.

Together with the [growing-gap theorem](endpoint-two-growing-gap.md), this
gives a structural necessary condition for **every fully distinct integer
endpoint-two zero** with minimum a>=8:

```text
d=b-a>=5  and  a<2d^2+20.
```

This condition is independent of parity. The minimum middle gap must grow
at least on the square-root scale as a grows. It does not assert that all
triples passing this necessary condition have an endpoint zero.

## Written tails for the three new gaps

Put `Q_d(c)=h_C(2)` at b=a+d. Its cubic coefficients, in descending powers
of c, are as follows; they follow from the generic quotient identity.

```text
d=1:
[2a^3+6a^2-4,
 -5a^4-2a^3-14a^2-21a+14,
 2a^5+5a^4-12a^3-36a^2+55a-14,
 4a^5-2a^4-32a^3+52a^2-26a+4]

d=3:
[2a^3+12a^2+14a+8,
 -5a^4-22a^3-22a^2+25a-6,
 2a^5+15a^4+20a^3-66a^2-91a-18,
 4a^5+18a^4-16a^3-56a^2-30a-4]

d=4:
[2a^3+15a^2+24a+20,
 -5a^4-32a^3-38a^2+96a+8,
 2a^5+20a^4+48a^3-60a^2-224a-80,
 4a^5+28a^4+16a^3-104a^2-128a-32].
```

Set `L_d=2a+d-10` and `U_d=L_d+1`. For the following thresholds A_d,
substitute a=A_d+m, m>=0. The vectors below give the complete coefficients
of the indicated endpoint values in **descending powers of m**.

| d | A_d | -Q_d(L_d) coefficient vector | Q_d(U_d) coefficient vector |
|---|---|---|---|
| 1 | 20 | [136,9192,228898,2482218,9856980] | [6,414,10596,119754,519138,212220] |
| 3 | 16 | [72,3528,61002,422694,881604] | [6,388,10256,140678,1016228,3116304] |
| 4 | 64 | [16,3104,206080,5010048,21802496] | [6,1899,241104,15348219,489818496,6268561524] |

Every coefficient, including the constant, is positive. Therefore
`Q_d(L_d)<0<Q_d(U_d)` on the entire real tail a>=A_d.
Both endpoints lie above b=a+d, since `L_d-b=a-10>0` there.
The intermediate value theorem gives a real solution between L_d and U_d.
The [root-geometry theorem](endpoint-two-surface-geometry.md) applies at
a>=8,b>=a and makes it the unique real solution c>b. For integer a,
the endpoints are consecutive integers, so no integer c>b can solve
the endpoint equation. Uniqueness and simplicity concern the polynomial
in the exponent c; no new spectral-multiplicity claim is made.

## Complete base computation

The remaining fixed pairs are precisely those listed below.

| d | Base minima a | Number of pairs | Integer roots c>a+d |
|---|---|---|---|
| 1 | 8 through 19 | 12 | none |
| 3 | 8 through 15 | 8 | none |
| 4 | 8 through 63 | 56 | none |

For each pair, divide Q_d by the gcd of its integer coefficients to obtain
a primitive cubic with nonzero constant. Every integer root c divides
that constant. The checker enumerates **all** positive constant divisors
above b, evaluates each by integer Horner arithmetic, and finds no root.
Exact rational-factor extraction independently gives the same empty set
of integer roots above b. The primitive cubics, complete candidates and
every evaluated value are saved in [the certificate](../results/endpoint-two-small-middle-gaps.json).

This finite base covers every integer c>b for all 76 necessary pairs;
it does not impose an arbitrary cutoff on c. The all-a>=8 result uses
these finite computations in addition to the written tails. The earlier
gap-two proof, including its own finite base, is preserved separately.
Repeated `(10,10,12)` remains a genuine endpoint-two zero outside the
fully distinct hypotheses; there is no assertion that the entire symmetric
endpoint polynomial is free of integer zeros.

## Nonintegrality and the remaining region

For all-even triples and permutations of `(1,3,2)/(3,3,0)` modulo four,
an integer spectrum cannot contain one by the earlier root-distribution
arguments. The uniform positive quotient root in `(0,3)` would have to
be two, contradicting the theorem. Thus every triple in these classes
with a>=8 and `1<=b-a<=4` is nonintegral, for every c>b.
The earlier minimum-through-seven result handles the smaller minima.

The exclusion of one in the mixed classes is conditional on integer
spectra; this does not assert that h_C(1) is always nonzero. Other
endpoint-one cases remain separate. For integer endpoint-two zeros with
minimum a>=8, the remaining region now requires all of

```text
d=b-a>=5,  a<2d^2+20,  b<beta(a)<2a-2,  b<c<3a-4.
```

These are necessary restrictions, not a characterization of the remaining
integer points. General endpoint-two integer feasibility, other quotient
roots on that surface, the other endpoint-one cases and full Q3 remain open.

## Verification

With SymPy 1.14.0, run

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_small_middle_gaps.py
```

The checker reconstructs the generic six-by-six quotient quintic, all three
family cubics and the six complete positive endpoint expansions. The note's
coefficient vectors are checked against the certificate. It checks all 76
base pairs by complete integer-divisor reduction and independent rational
factor extraction. Six selected tail pairs have exact Sturm counts of one
exponent root in their bracket and one on the whole c>b interval; twelve
direct quotient/Horner/Sturm fixtures check the bracket endpoints. The
repeated endpoint-zero control is retained.

The finite base is required by the stated theorem and its tail thresholds;
no unrelated parameter or modulus range is expanded. No floating spectra
or Lean verification are claimed. Manuscript files are unchanged while
the standalone results on PR9 await review and integration.

[Return to the project entrance](../README.md).
