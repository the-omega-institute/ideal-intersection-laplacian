# Integer exclusion with a growing middle gap

Let C be the six-support complement quotient and `h_C(x)=det(xI-C)/x`.
Throughout this note, a,b,c are in **size order**, not labelled by their
residue classes.

**Theorem.** For real `d>=5,a>=2d^2+20,b=a+d`, there is exactly one real
solution c>b of `h_C(2)=0`, and it satisfies

```text
2a+d-11 < c < 2a+d-10.
```

Consequently, for **integer `d>=5,a>=2d^2+20,c>a+d`**, the triple
`(a,a+d,c)` has no endpoint-two zero. The middle gap is allowed to grow
with a; this is an unbounded family, not a fixed-gap statement.

This theorem has a written proof for its entire domain. It needs no finite
base calculation. The quadratic threshold is sufficient; optimality is
not claimed. The earlier [gap-two theorem](endpoint-two-gap-two.md) has a
different bracket and a complete finite base, and remains unchanged.

## Endpoint polynomial

Write `Q(c)=h_C(2)=Ac^3+Bc^2+Dc+E`, with a,b fixed. The generic quotient gives

```text
A=ab(a+b-1)+2a(a-1)+2b(b-1)-4,
B=b^2[(a+2)b-(7a^2-2a+8)]
  +(a^3+2a^2-6a-4)b+2(a-2)(a^2-2a-6),
D=(a-2)(b-2)[a^2b+a^2+ab^2+6ab+4a+b^2+4b-12],
E=2(a-2)(b-2)(a+b-2)(ab+a+b-2).
```

At b=a+d, put `L=2a+d-11` and `U=L+1`. Direct substitution gives

```text
Q(L)=-6a^5+(8d^2-15d-65)a^4
 +(16d^3-78d^2-130d+2052)a^3
 +(10d^4-102d^3-285d^2+3078d-8203)a^2
 +(2d^5-25d^4-220d^3+3458d^2-8203d-676)a
 +4d^5-122d^4+1216d^3-4004d^2-338d+8788,
Q(U)=(8d^2-144)a^4+(16d^3-56d^2-288d+2016)a^3
 +(10d^4-84d^3-392d^2+3024d-6336)a^2
 +(2d^5-20d^4-248d^3+3056d^2-6336d-1152)a
 +4d^5-112d^4+1024d^3-3072d^2-576d+6912.
```

## Two strict signs on the entire domain

Set `d=5+r` and `a=2d^2+20+u`, so r,u>=0. In the table below each vector
lists the coefficient of the indicated power of u, in **ascending powers
of r**. These are the complete expansions of -Q(L) and Q(U).

| u power | -Q(L) coefficient vector | Q(U) coefficient vector |
|---|---|---|
| 0 | [8176563072,10702072308,6533887336,2441182410,617575888,110647964,14260434,1312164,83144,3312,64] | [1722564592,3898674344,3488957044,1763855732,574749536,127937904,19858260,2132724,152168,6528,128] |
| 1 | [617529036,647593173,312876344,90388708,17077611,2166606,181376,9248,224] | [93388278,190152594,138386892,54033548,12904374,1966050,188360,10432,256] |
| 2 | [18517518,14575402,5172183,1044682,127178,8904,288] | [1888094,3435084,1874344,504308,74458,5856,192] |
| 3 | [275748,144710,32718,3624,176] | [16856,27232,9272,1296,64] |
| 4 | [2040,535,52] | [56,80,8] |
| 5 | [6] | [0] |

Every nonzero coefficient is positive, including both constant terms.
Therefore `Q(L)<0<Q(U)` for every real r,u>=0, including the boundary.
Moreover, `L-b=a-11>0`, since a>=70. The intermediate value theorem
produces an endpoint-two solution in `(L,U)`, wholly above b.

The [real-root geometry theorem](endpoint-two-surface-geometry.md) applies
because a>=8 and b>=a. It proves that whenever an endpoint-two solution
c>b exists, that solution is unique and simple as a root of the polynomial
in the exponent c. Hence the root just bracketed is the only such real
solution. For integer a,d, L and U are consecutive integers, proving the
integer exclusion. Simplicity here concerns the exponent polynomial;
no new spectral-multiplicity statement is made.

## Spectral consequence and open scope

The integer exclusion itself has no parity hypothesis. For all-even
triples and permutations of `(1,3,2)` or `(3,3,0)` modulo four that satisfy
the size-ordered theorem hypotheses, it proves **Laplacian nonintegrality**.
Indeed, a hypothetical integer spectrum cannot contain one by the prior
root-distribution arguments. The uniform positive quotient root in `(0,3)`
would then have to be two, which this theorem excludes.

The mixed-pattern exclusion of one is conditional on an integer spectrum;
we do not assert that h_C(1) is always nonzero in those classes. Other
endpoint-one cases, arbitrary middle gaps outside the stated threshold,
general integer feasibility of the endpoint-two surface and full Q3 remain
open. No conclusion about the old binary-subspace n=7 problem is drawn.

## Exact verification

With SymPy 1.14.0, run

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_growing_gap.py
```

Compare with [the certificate](../results/endpoint-two-growing-gap.json).
The checker reconstructs the generic six-by-six quotient quintic, verifies
the endpoint cubic and both complete sign identities, and reconstructs
the two-variable positive expansions. The note's full vectors are checked
against the certificate. These identities support the written infinite
proof; no exponent range is scanned and no finite base is required.

Five selected pairs `(70,75),(92,98),(148,156),(100,105),(182,191)` have
exact Sturm counts of one exponent root in the indicated bracket and one
on the whole c>b tail. Ten direct quotient, integer-Horner and Sturm checks
at the bracket endpoints provide finite cross-checks. The earlier gap-two
pair `(20,22)` and repeated endpoint-zero triple `(10,10,12)` are retained
as outside-hypothesis controls. No floating spectra or Lean verification
are claimed. Manuscript files are unchanged pending review of PR9.

[Return to the project entrance](../README.md).
