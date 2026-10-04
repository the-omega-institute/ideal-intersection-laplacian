# A sharper maximum-exponent bound for endpoint two

For ordered exponent triples **`4<=a<=b<=c`**, we prove

```text
c>=3a-4  =>  h_C(2)>0.
```

The complement quotient therefore has a positive eigenvalue in `(0,2)`.
This proves nonintegrality for all-even triples and permutations of
`(1,3,2)` or `(3,3,0)` modulo four, using the prior conditional exclusion
of the integer root one for the mixed patterns.

Consequently **every endpoint-two zero requires `c<3a-4`**, irrespective
of parity. Together with the [middle-exponent bound](endpoint-two-middle-tail.md),
the remaining endpoint-two region is

```text
4<=a<=b<=c,  b<2a-2,  c<3a-4.
```

The earlier maximum bound was `R(a)=7a-16+40/(a+2)`. The improvement is
strict for every a>=4:

```text
R(a)-(3a-4)=4(a^2-a+4)/(a+2)>0.
```

For example, at minimum a=20 the old upper bound was `1384/11`, whereas
the new bound is `c<56`. This is a uniform restriction on the whole
endpoint-two surface, not a bound only for one fixed middle exponent.

## Positivity on a bounded middle interval

Let `C` be the established six-support complement quotient and
`h_C(x)=det(xI-C)/x`. The [previous endpoint reduction](endpoint-reduction.md)
gives the exact cubic `h_C(2)=A(a,c)b^3+B(a,c)b^2+D(a,c)b+E(a,c)`.
Its coefficients are independently reconstructed from C by the new checker.

The preceding full determinant theorem already proves `h_C(2)>0` for
`b>=2a-2`. It remains to consider `a<=b<2a-2`. Parameterize this bounded
interval by

```text
t=(b-a)/(2a-2-b)>=0,
b=(a+(2a-2)t)/(1+t).
```

Set `a=4+m` and `c=3a-4+v`, with m,v>=0. Clearing the positive denominator
gives the polynomial

```text
G(m,t,v)=(1+t)^3*h_C(2)
        =sum_{i=0}^3 sum_{j=0}^3 P_ij(m)t^i v^j.
```

The following table gives all coefficients explicitly. A vector
`[q0,q1,...]` denotes `P_ij(m)=q0+q1*m+...`, in ascending powers of m.

| i | j=0 | j=1 | j=2 | j=3 |
|---|---|---|---|---|
| 0 | [17568,45392,41600,18120,3986,413,15] | [13008,22464,14200,4120,545,26] | [2616,3108,1286,219,13] | [156,116,27,2] |
| 1 | [59072,155168,144464,63824,14180,1466,51] | [45792,80528,52120,15548,2120,104] | [9552,11704,5036,898,56] | [584,460,114,9] |
| 2 | [74496,194048,181536,80912,18096,1856,60] | [55360,98880,65336,19948,2778,137] | [11672,14716,6554,1213,78] | [724,600,157,13] |
| 3 | [36864,93696,88064,40096,9296,1008,36] | [23424,42560,28816,9064,1304,66] | [4784,6200,2852,546,36] | [296,256,70,6] |

Every listed coefficient is positive. In particular G has 88 nonzero
terms, all positive, and constant term 17568. Thus `G>0` for m,t,v>=0,
and division by `(1+t)^3>0` proves `h_C(2)>0` on the entire remaining
middle interval. The coefficient of t cubed also reproduces the boundary
value at `b=2a-2`. The preceding middle-tail theorem covers that boundary
and every larger b. This completes the proof for all ordered triples.

The table is a finite algebraic identity proving an infinite inequality.
It enumerates coefficients of one polynomial, not parameter values or
endpoint-zero candidates.

## The spectral conclusion and its parity scope

The established identity

```text
h_C(0)=-abc(a+b+c)(a+b+c+ab+ac+bc)<0
```

and `h_C(2)>0` give a root in `(0,2)` by the intermediate value theorem.
For all-even exponents C/2 is an integer matrix, so a hypothetical integer
spectrum of C could contain only even roots. For the two stated mixed
patterns, the existing [shifted-root identity](mixed-endpoint-roots.md)
forces hypothetical odd integer roots to be three modulo four. The only
integer in the interval, one, is therefore excluded under the
integer-spectrum hypothesis. The complement and universal-class lifts
transfer this nonintegrality to the ideal intersection graph.

The endpoint-two zero restriction is unconditional for every parity
pattern in the theorem. This proof does not exclude the integer root one
in the other mixed-parity classes, and does not settle their endpoint-one
surface. Neither endpoint compatibility nor failure of this sufficient
tail criterion establishes integrality.

## Exact checks and the remaining question

Run with SymPy 1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_maximum_tail.py
```

Compare with [the exact certificate](../results/endpoint-two-maximum-tail.json).
The checker reconstructs the generic 6x6 quotient and endpoint cubic,
verifies the interval transformation and its inverse, and checks all 88
positive coefficients and the boundary identity. Five fixed direct
integer quotient/Horner/Sturm fixtures cover the equality `c=3a-4`, a
strict tail, a mixed-parity example, the repeated-middle boundary b=a,
and an outside-tail control. In `(20,34,56)`, `(20,34,58)` and `(19,31,56)`,
both principal-block sufficient tests fail, the middle-tail bound does
not apply, and the maximum is below the old R(a) tail; the new endpoint
is positive. No claim is made that these examples escape every earlier
arithmetic theorem. `(20,22,32)` lies outside the tail and has no positive
root below two; it is not claimed integral. The retained endpoint-zero
control `(10,10,12)` satisfies the new strict maximum bound.

The infinite result is the written coefficient-positivity proof; the
selected fixtures are finite checks. No exponent/modulus scan, floating
spectrum or Lean verification is used. Manuscript files remain unchanged
pending review and integration. The surviving endpoint-two region has
unbounded minimum exponent, and full Q3, other endpoint-one cases and
higher-prime nonsquarefree vectors remain open. The next structural
question is the endpoint equation and the other quotient roots inside
`b<2a-2,c<3a-4`, combined with the existing arithmetic restrictions.

The subsequent [root-geometry theorem](endpoint-two-surface-geometry.md)
gives an exact real-feasibility test for each fixed a>=8,b>=a and a
unique real c>b solution when feasible. Integer feasibility remains open
in general; selected pairs can now be excluded by a single root bracket.

[Return to the project entrance](../README.md).
