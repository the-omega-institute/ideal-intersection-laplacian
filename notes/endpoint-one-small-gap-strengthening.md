# Endpoint-one small-gap brackets at real minimum two

For every real \(a\ge2\), put \(b=a+d\), with \(d=1\) or \(2\),
and view \(Q(c)=h_{a,b,c}(1)\) as a polynomial in the maximum
exponent. Its unique real root above \(b\) lies in

\[
(L_d,L_d+1),\qquad
L_1=2a^2-a-2,\quad L_2=2a^2+a-6.
\]

This strengthens Lemma 8.2 of the focused manuscript from minimum eight
to minimum two and states the real root bracket explicitly. For integer
\(a\), the anchors are integers, so no integer \(c>b\) in either gap
family satisfies the endpoint-one equation. The global three-prime
classification and its historical finite inputs retain their scopes.

The determinant's cubic has leading coefficient
\(a^2+b^2-1>0\) and constant
\((a-1)(b-1)(a+b-1)(ab+a+b-1)>0\). The six sign expressions have
the following complete coefficient vectors in ascending powers of
\(m=a-2\):

| Gap | Expression | Coefficients |
|---|---|---|
| 1 | \(-Q(b)\) | 64, 480, 848, 664, 264, 52, 4 |
| 1 | \(-Q(L_1)\) | 48, 376, 768, 648, 264, 52, 4 |
| 1 | \(Q(L_1+1)\) | 120, 412, 592, 456, 196, 44, 4 |
| 2 | \(-Q(b)\) | 57, 1689, 2513, 1516, 456, 68, 4 |
| 2 | \(-Q(L_2)\) | 57, 1009, 2119, 1140, 232, 16 |
| 2 | \(Q(L_2+1)\) | 160, 360, 640, 892, 476, 104, 8 |

All 41 coefficients are strictly positive. Thus
\(Q(0)>0>Q(b)\) and \(Q(L_d)<0<Q(L_d+1)\). The anchors obey

\[
L_1-b=1+6m+2m^2>0,\qquad
L_2-b=2m(m+4)\ge0.
\]

For gap two at \(a=2\), the lower anchor equals \(b=4\), and
\(Q(4)=-57\), \(Q(5)=160\). The open bracket still lies strictly
above \(b\). For gap one at \(a=2\), \(b=3\), \(L_1=4\), and
the three signed values are 64, 48 and 120, respectively.

Since the cubic tends to a negative value at negative infinity, the
intermediate value theorem gives one root in each of
\(( -\infty,0)\), \((0,b)\) and \((L_d,L_d+1)\).
These intervals are disjoint even when \(L_d=b\). Three distinct roots
exhaust the cubic's degree, proving uniqueness above \(b\) and the
bracket on the entire real domain. No finite exponent base is needed.

Run from the repository root with Python 3.10 or later and SymPy 1.14.0:

```sh
python3 scripts/verify_largest_root_coefficients.py
```

The checker reconstructs the quintic by a direct determinant of the
set-disjointness quotient, compares every vector with the current shared
LaTeX appendix, and verifies the leading/constant signs and exact anchor
differences. Its saved output is
`results/largest-root-coefficient-verification.json`. The support model,
table parser and SymPy backend are shared with earlier checks; the
original characteristic-polynomial helper is not imported. This written
real-domain strengthening uses generic identities, with no parameter
scan, historical finite-base rerun, expanded graph calculation or Lean.
