# Sharp real cutoff for the endpoint-two middle bound

Put \(\alpha=(7+\sqrt{13})/3\), so \(3<\alpha<4\). For ordered
real parameters \(\alpha\le a\le b\le c\) on \(h_C(2)=0\),

\[
b\le2a-2,
\]

with equality exactly at
\(a=\alpha,\ b=c=2\alpha-2\). Thus \(b<2a-2\) whenever
\(a>\alpha\). This strengthens the previous real assumption \(a\ge4\)
and gives the optimal uniform cutoff for the strict bound. The integer
bound still starts at four; the maximum bound \(c<9a/4-8\) still starts
at eight. The three-prime classification retains its finite inputs.

To exclude \(b\ge2a-2\), write \(b=2a-2+u\), \(c=b+v\),
with \(u,v\ge0\). The established quotient determinant identity is

\[
h_C(2)=A_0(u)B_0(u)+\tfrac12(A_0B_0)'(u)v+D_0(u)v^2+E_0(u)v^3.
\]

The first factor is

\[
A_0(u)=2u^2+7(a-2)u+6(a-\alpha)(a-(7-\sqrt{13})/3).
\]

For \(a\ge\alpha\), it is nonnegative and vanishes only when
\(a=\alpha,u=0\). Its derivative \(4u+7(a-2)\) is strictly
positive. To see positivity of the other three factors, set \(a=3+m\).
Their complete expansions are

\[
\begin{aligned}
B_0={}&(m+5)u^3+(4m^2+34m+54)u^2\\
&+(4m^3+61m^2+210m+201)u+26m^3+178m^2+382m+262,\\
D_0={}&4(m+5)u^3+(20m^2+143m+187)u^2\\
&+(33m^3+317m^2+803m+583)u\\
&+18m^4+228m^3+872m^2+1276m+614,\\
E_0={}&(m+5)u^2+(5m^2+33m+44)u+6m^3+52m^2+134m+104.
\end{aligned}
\]

All 13, 14 and 9 coefficients are strictly positive. Hence
\(B_0,B_0',D_0,E_0>0\), and \((A_0B_0)'>0\).
The determinant is positive except at \(a=\alpha,u=v=0\), where
it is zero. This gives the bound, the equality case and sharpness.
The equality point is ordered because \(2\alpha-2>\alpha\).

With Python 3.10 or later and SymPy 1.14.0, run:

```sh
python3 scripts/verify_endpoint_two_middle_cutoff.py
```

The saved result is `results/endpoint-two-middle-sharp-cutoff.json`.
The checker reconstructs the generic endpoint from the direct six-support
set-disjointness quotient determinant, verifies the cubic identity and all
36 positive shifted coefficients, and checks the ordered equality point
exactly over \(\mathbb Q(\sqrt{13})\). Three specified rational controls
give

| \((a,b,c)\) | \(h_C(2)\) |
|---|---:|
| \((7/2,5,5)\) | \(-2003/8\) |
| \((15/4,11/2,11/2)\) | \(569889/256\) |
| \((15/4,6,7)\) | \(330295/16\) |

Their endpoint values also agree with separately evaluated direct
determinants over the rational numbers. The two positive controls
lie in the newly admitted real range; the negative control shows why the
original proof cannot be extended uniformly to minimum three. The real
result is a written proof, not an inference from these controls. The
support constructor and SymPy are shared; the original characteristic
helper is not imported. No parameter scan, new finite exponent base,
historical finite-base rerun, floating-point computation or Lean check
is claimed.
