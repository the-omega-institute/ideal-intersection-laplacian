# Integer feasibility when the two smallest exponents differ by two

For every **integer `a>=8` and integer `c>a+2`**, the ordered gap-two
triple `(a,a+2,c)` satisfies **`h_C(2)!=0`**.

The unbounded part, a>=20, has a written proof: the unique real endpoint-two
solution lies strictly between **`2a-8` and `2a-7`**, which are consecutive
integers. The extension through a=8,...,19 uses a complete exact computation
for twelve fixed pairs and every integer c>a+2. These verification scopes
are distinct; the full statement is not claimed as a purely written proof.

Consequently every all-even triple in this family is nonintegral. The same
holds for gap-two triples with residue pattern `(1,3,2)` modulo four, using
the earlier conditional exclusion of one. Other mixed-parity endpoint-one
cases are not settled by this result. Full Q3 remains open.

## The exact cubic for the gap-two family

Set b=a+2 and write `h_C(2)=aP_a(c)`. Direct quotient expansion gives

```text
P_a(c)=(2a^2+9a+6)c^3-(5a^3+12a^2+14a+12)c^2
       +(2a^4+10a^3-56a)c+4a^4+8a^3-32a^2.
```

The [root-geometry theorem](endpoint-two-surface-geometry.md) says that
for a>=8 and fixed b>=a there is at most one real endpoint-two solution
with c>b. If there is a sign-changing bracket above b, that bracket
contains the only solution. This turns a unit-width bracket into an
integer-feasibility proof for the entire unbounded c interval.

## A uniform bracket for every a>=20

The two exact endpoint identities are

```text
h_C(2)atc=2a-8 = -16a(7a^3-84a^2+148a+240),
h_C(2)atc=2a-7 = 3a(2a^4-49a^3+356a^2-427a-882).
```

At a=20+m, m>=0, their signs are explicit:

```text
-h_C(2)atc=2a-8
 =112m^4+7616m^3+190528m^2+2069760m+8192000,

h_C(2)atc=2a-7
 =6m^5+453m^4+13308m^3+189999m^2+1323714m+3658680.
```

All coefficients are positive, so the lower value is negative and the
upper positive for every a>=20. Both endpoints lie above b=a+2 because
`2a-8-(a+2)=a-10>0`. The intermediate value theorem gives a root in
`(2a-8,2a-7)`, and the preceding uniqueness theorem excludes every other
real c>b root. No integer lies in this interval, proving the infinite tail.

## Complete finite base at minima eight through nineteen

For each remaining a, divide P_a by the gcd of its integer coefficients
to obtain a primitive cubic. The table lists its coefficients in
descending powers of c and every integer root with c>a+2.

| a | Primitive cubic coefficients | Integer roots c>a+2 |
|---|---|---|
| 8 | [103,-1726,6432,9216] | none |
| 9 | [83,-1585,6636,9828] | none |
| 10 | [37,-794,3680,5600] | none |
| 11 | [347,-8273,41976,65340] | none |
| 12 | [67,-1758,9680,15360] | none |
| 13 | [461,-13207,78364,126412] | none |
| 14 | [131,-4070,25872,42336] | none |
| 15 | [197,-6599,44720,74100] | none |
| 16 | [331,-11894,85568,143360] | none |
| 17 | [737,-28283,215220,364140] | none |
| 18 | [17,-694,5568,9504] | none |
| 19 | [899,-38905,328168,564604] | none |

Any integer root c of a primitive cubic divides its nonzero constant
term. The checker enumerates all positive divisors greater than a+2
using integer trial division and evaluates every candidate by integer
Horner arithmetic. It independently cross-checks the complete root set
with exact rational-factor extraction. All candidate divisors and values
are retained in [the certificate](../results/endpoint-two-gap-two.json).
Thus the finite calculation covers every integer c>a+2 for these twelve
pairs, without an arbitrary cutoff on c.

The a=10 cubic does have the integer root c=10:

```text
P_10(c)/content=(c-10)(37c^2-424c-560).
```

It lies below b=12 and corresponds to the permutation `(10,12,10)` of
the retained repeated endpoint-zero control `(10,10,12)`. It is not an
ordered gap-two counterexample. No polynomial-wide root-free claim is
made where only the c>b interval is relevant.

## Nonintegrality and remaining scope

The established uniform low-root theorem supplies a positive quotient
root in `(0,3)`. An integer spectrum of an all-even triple cannot contain
one; for the stated mixed pattern, hypothetical odd integer roots must
be three modulo four, also excluding one. Such an integer spectrum would
therefore require endpoint two, which has just been excluded. The
complement and universal-class lifts give nonintegrality of the original
ideal intersection graph.

The absence of endpoint two holds for every parity pattern in the ordered
family. Its nonintegrality consequence additionally requires exclusion of
one. In particular the other mixed-parity patterns that can use endpoint
one remain separate. This result does not settle arbitrary middle gaps
or the general integer-feasibility problem on the endpoint-two surface.

## Reproducibility

With SymPy 1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_gap_two.py
```

The checker reconstructs the generic direct6x6quotient and verifies the
family cubic and both sign identities coefficientwise. The finite base
uses complete divisor enumeration and independent rational-factor extraction.
Seven selected direct quotient/Horner fixtures check the endpoints, with
exact Sturm counts and the real-exponent brackets at a=20 and a=40.
The unordered endpoint-zero control is retained. The note tables and
sign coefficients are checked against the saved certificate.

The computation is limited to the twelve necessary base pairs for this
one specified family, plus the selected identity fixtures. It does not
enlarge an unrelated exponent range or modulus range. No floating spectrum
or Lean verification is used. Manuscript files remain unchanged pending
review and integration; full Q3 and the general surviving endpoint cases
remain open.

[Return to the project entrance](../README.md).
