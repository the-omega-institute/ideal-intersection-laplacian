# A uniform unequal-exponent cutoff and every minimum exponent of three

For three distinct primes, the ideal intersection graph is nonintegral
whenever its positive exponents, ordered as `a <= b <= c`, satisfy
`a >= 2` and **`c >= 4a^2 - 2a`**. This is a written infinite-family proof.
It reduces the unresolved triples for each fixed minimum exponent to a
finite set. Combining the cutoff with the exact endpoint certificate below
also proves nonintegrality for **every `(3,b,c)`, b,c >= 1**.
Together with the earlier theorems, every triple with minimum exponent at
most three is now settled.

Read [the working manuscript](../paper/paper.pdf),
[the proof source](../paper/sections/distinct-tail.tex), and
[the exact certificate](../results/distinct-tail.json).
The general characterization remains open: in the three-prime case the
remaining ordered triples are `4 <= a < b < c < 4a^2 - 2a`.
Nonsquarefree vectors with four or more primes are also unresolved.

## The general endpoint and cutoff

Use the six-support complement quotient `C` defined in the
[unit-exponent note](one-unit-exponent.md), and write
`det(xI-C) = x h_(a,b,c)(x)`. Put

```
L = a^2 + b^2 - 1
Q = a^3 - 4a^2 b^2 + 2a^2 b - a^2 + 2ab^2 + ab - 3a
    + b^3 - b^2 - 3b + 3
R = (a-1)(b-1)(2ab + 3a + 3b - 3)
S = (a-1)(b-1)(a+b-1)(ab+a+b-1).
```

The exact identity is `h(1) = Lc^3 + Qc^2 + Rc + S`.
For `a,b >= 2`, the three coefficients `L,R,S` are positive.
Thus **`Lc+Q >= 0`** is already a sufficient nonintegrality condition:
`h(0)<0<h(1)` gives a complement eigenvalue in `(0,1)` and a graph
eigenvalue in `(V-1,V)`, where `V=(a+1)(b+1)(c+1)-2`.
In particular this condition holds at and above `T(a)=4a^2-2a`, because

```
Q + T(a)L = b^2(b-1) + (2a^2+a-3)b + K(a)
K(a) = 4a^4-a^3-5a^2-a+3
K(2+u) = 4u^4+31u^3+85u^2+95u+37 > 0, u >= 0.
```

All terms are positive when `a,b >= 2`. No range extrapolation is used.
The threshold also supplies an exact finite reduction for any fixed
minimum exponent: only the ordered pairs `a < b < c < T(a)` need remain,
since repeated entries and smaller minimum exponents are handled separately.

## Completion when the minimum is three

After the earlier unit, minimum-two and repeated-exponent theorems,
order the remaining entries as `4 <= b < c`. The tail `c >= 30` follows
from the cutoff. At `a=3`, the first endpoint becomes

```
h(1) = (b^2+8)c^3 + (b-1)(b^2-30b-12)c^2
       + 6(b-1)(3b+2)c + 4(b-1)(b+2)(2b+1).
```

There are exactly `choose(26,2)=325` pairs in `4 <= b < c < 30`.
Exact integer evaluation gives 257 positive values, 68 negative values,
and **no zero**. The negative values occur precisely in these ranges;
all other pairs in the derived finite domain are positive:

| b | c with h(1)<0 |
| --- | --- |
| 4 | 5–13 |
| 5 | 6–15 |
| 6 | 7–16 |
| 7 | 8–17 |
| 8 | 9–17 |
| 9 | 10–16 |
| 10 | 11–16 |
| 11 | 12–15 |
| 12 | 13–14 |
| 13 | 14 |

Positive first endpoints give a root in `(0,1)`. For negative endpoints,
the following written identities prove `h(2)>0`, except at `(b,c)=(4,5)`:

```
h_(3,4,6+v)(2) = 104v^3+1238v^2+4018v+2344

h_(3,5+u,6+u+v)(2)
 = (5u^2+54u+153)v^3
   + (20u^3+262u^2+1179u+1863)v^2
   + (25u^4+426u^3+2642u^2+7011u+6624)v
   + 10u^5+218u^4+1828u^3+7200u^2+12600u+6480.
```

Every coefficient is positive for `u,v>=0`; the two regions exhaust
`4<=b<c` except `(4,5)`. When `h(1)<0<h(2)`, a root lies in `(1,2)`.
Both lifted intervals contain no integer.

For the sole exception,

```
h_(3,4,5)(x) = x^5-83x^4+2327x^3-24133x^2+60576x-42480
h(1) = -3792
h(3/2) = 48825/32 > 0.
```

This yields a root in `(1,3/2)`, so the graph with 118 vertices has a
noninteger eigenvalue in `(233/2,117)`. All cases are covered.

## Verification scope

Run with Python 3.10+ and SymPy 1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_distinct_tail.py
```

Compare with [results/distinct-tail.json](../results/distinct-tail.json).
The checker reconstructs the symbolic six-support quintic and verifies the
general cubic endpoint, cutoff identity, positive remainder, and both
minimum-three positive expansions. For **every** pair in the theorem-derived
325-case domain, it independently reconstructs the integer quotient quintic,
matches the symbolic specialization, and verifies the signs with separate
Python `Fraction` Horner arithmetic. Each record includes the polynomial,
two endpoint values and the lifted graph interval. All cubic `h(1)` values
also match separate Horner evaluation in `c`. The sole rational exception
has an additional Sturm count of one in `(1,3/2)`.

The minimum-three theorem uses this exhaustive finite nonvanishing/sign
certificate alongside the written tail and endpoint-expansion proofs.
There is no arbitrary range expansion, numerical eigenvalue evidence or
Lean formalization. The previous 35-case diagnostic keeps its original scope.

[Return to the project entrance](../README.md).
