# Every three-prime graph with an exponent two is nonintegral

**Theorem.** For distinct primes p,q,r and every b,c≥1, the ideal
intersection graph of `Z_(p^2 q^b r^c)` is not Laplacian integral.
Together with the unit-exponent theorem, this settles every triple whose
minimum exponent is at most2. The repeated-exponent theorem also covers
equal entries of any size. Fully distinct triples with all entries at
least3 and nonsquarefree vectors with more than three prime factors remain open.

This is a written infinite-family proof, with exact symbolic checks and
one rational endpoint certificate. No larger diagnostic range or Lean is used.

## The same complement quotient

Use the six-support complement matrix C and its polynomial
`det(xI-C)=x h_(a,b,c)(x)` from the
[unit-exponent proof](one-unit-exponent.md). If h has a root μ in an
interval containing no integer and not containing0 orN, the quotient
reflection and universal-vertex lift give a noninteger graph eigenvalue
V−μ. Here N=a+b+c+ab+ac+bc and V=N+abc−1.

When a=2, h(0)<0. Put s=b+c and t=bc. Direct substitution gives

$$h_{2,b,c}(1)=(s-13)t^2-(2s+6)t+3s^3+s^2-3s-1.$$

The symmetric formula allows us to order b≤c. If either is1, the previous
unit-exponent theorem applies. If either is2 or b=c, the repeated-exponent
theorem applies. It remains to consider 3≤b<c.

## Positive expansions exhaust the infinite range

For b=3 and c=5+v, v≥0,

$$h_{2,3,5+v}(1)=12v^3+112v^2+268v+120>0.$$

For b≥4 and c>b, write b=4+u and c=5+u+v, with integers u,v≥0.
The second exact expansion is

$$\begin{aligned}
h_{2,4+u,5+u+v}(1)
={}&(u^2+8u+19)v^3\\
&+(4u^3+38u^2+128u+170)v^2\\
&+(5u^4+62u^3+271u^2+502u+368)v\\
&+2u^5+32u^4+190u^3+504u^2+552u+160>0.
\end{aligned}$$

All displayed coefficients are positive. In both regions h(0)<0<h(1),
so a root μ∈(0,1) gives a graph eigenvalue in(V−1,V).
These two parameterizations cover every 3≤b<c except(b,c)=(3,4).

## The single exception has a rational sign certificate

For(a,b,c)=(2,3,4), the complement quintic is

$$h(x)=x^5-53x^4+953x^3-6523x^2+13134x-7560.$$

It has h(1)=−48 and h(3/2)=13437/32>0. Hence a real root lies strictly
between1 and3/2, an interval with no integer. Since V=58, its lifted
graph eigenvalue lies in(113/2,57), also with no integer. This settles
the last case and proves the theorem for every positive b,c.

## Exact validation

[The targeted checker](../scripts/check_minimum_two.py) verifies the
general h(0) expression at a=2, the symmetric h(1) formula, both positive
expansions and all their coefficients. It reconstructs the exceptional
quintic from the complement quotient and checks the two rational endpoint
values with separate Horner evaluation. It enumerates no parameter range.

[The saved certificate](../results/minimum-two.json) contains exact
expressions, the exception and source hashes. The earlier direct ideal
embedding check at(2,3,4) remains part of the six-support evidence; it is
not represented as a new run here. The infinite conclusion uses the
written positivity argument, not the35case diagnostic.
