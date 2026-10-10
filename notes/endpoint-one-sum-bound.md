# The sharp endpoint-one sum bound at real minimum two

For real \(2\le a\le b\le c\), the endpoint equation
\(h_C(1)=0\) implies

\[
b+c\ge 2a^2-2a+1.
\]

Equality holds exactly when \(b=a\) and
\(c=(a-1)(2a-1)\). This strengthens the minimum assumption in the
sum-bound part of Theorem 6.1 of the focused manuscript. Its later
residual-root separation retains the hypothesis \(a\ge4\).

Put \(q=b+c\), \(z=bc\), \(Q=2a^2-2a+1\) and
\(K=4a^2-2a+1\). The quotient determinant has the form

\[
h_C(1)=(q-K)z^2-a(a-1)(q+2a-1)z+P_a(q),
\]

where

\[
P_a(q)=(a^2-1)q^3+(a^3-a^2-3a+3)q^2
       -3(a-1)^2q-(a-1)^3.
\]

Ordering gives \(z\ge z_0=a(q-a)\), since
\(z-z_0=(b-a)(c-a)\ge0\). If \(q\le Q\), then
\(q-K\le-2a^2\), and subtracting the value at \(z_0\) gives

\[
(z-z_0)\bigl[(q-K)(z+z_0)-a(a-1)(q+2a-1)\bigr]\le0,
\]

strictly unless \(z=z_0\). Thus the largest possible endpoint value
at fixed \(q\le Q\) occurs on the repeated boundary.

Write \(t=q-a\ge a\). On that boundary,

\[
h_C(1)\big|_{z=z_0}=\bigl[(a-1)(2a-1)-t\bigr]B(a,t),
\]

with

\[
B=a^3-2a^2t^2+a^2t+a^2+3at-3a+t^2-2t+1.
\]

For \(t=a+u\), \(u\ge0\), the short identity

\[
\begin{aligned}
-B(a,a+u)={}&(2a^2-1)u^2\\
 &+\bigl[(a-2)(4a^2+7a+9)+20\bigr]u\\
 &+(a-2)\bigl[2a^3+a(2a-1)+3\bigr]+5
\end{aligned}
\]

has strictly positive coefficients for every \(a\ge2\).
Consequently \(B<0\). When \(q<Q\), the other factor is positive,
so \(h_C(1)<0\), contradicting the endpoint equation. At \(q=Q\)
the boundary factor vanishes; equality requires \(z=z_0\), hence
\(b=a\) by ordering, and then \(c=(a-1)(2a-1)\). Conversely this
family makes the determinant zero. It is ordered throughout the stated
domain because \(c-a=2(a-1)^2-1>0\).

The generic six-by-six determinant, product bound, difference identity,
boundary factorization, positive quadratic and equality family are
checked with exact symbolic arithmetic by
`scripts/check_endpoint_one_sum_bound.py`. Run it from the repository
root with Python 3.10 or later and SymPy 1.14.0:

```sh
python3 scripts/check_endpoint_one_sum_bound.py
```

The recorded result is `results/endpoint-one-sum-bound.json`. The two
specified controls \((2,2,3)\) and \((3,3,10)\) verify equality below
the former minimum assumption. No parameter scan or finite base is
needed for this real-domain proof, and no Lean validation is claimed.
