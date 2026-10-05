# Explicit equality cubic and the remaining arithmetic problem

On c=b(b+2)-a, put q=ac and use the equality curve

```text
G=(3b-1)q^2+b(b^2+4b-1)q
  -(b^2+2b-1)(b^2+3b-1)(b^3+3b^2+3b-1).
```

Define the integer-coefficient cubic P3=x^3-Ax^2+Bx-N by

```text
A=q+b^3+5b^2+8b-1,
B=qb(b^2+5b+5)+2b^5+12b^4+25b^3+16b^2-8b+1,
N=qb(b+3)[q+b(b^2+3b+3)].
```

These are explicit polynomials in a,b after q=a[b(b+2)-a]. Direct
determinant expansion gives the generic identity

```text
h_C(x)=(x-1)(x-b)P3(x)+x(x-b)G.
```

Thus h_C(1)=(1-b)G, and on the endpoint-one equality curve G=0 this
is exactly the remaining spectral cubic. At real 4<=a<=b there, the
[pair-sum theorem](endpoint-one-equality-second-root.md) puts all three
roots strictly above a+b. Off G=0 the displayed P3 is an algebraic
extension of those coefficients; its roots are not asserted quotient roots.

## Discriminant and a complete test for each fixed integer point

The explicit discriminant is

```text
Delta=A^2B^2-4B^3-4A^3N-27N^2+18ABN.
```

As a polynomial in q,b it has degree five in q, degree sixteen in b,
and 61 terms. The [certificate](../results/endpoint-one-equality-cubic.json)
retains its full expansion. It is independently checked both by the cubic
discriminant routine and by the negative of the 5x5 Sylvester determinant
of P3 and its derivative.

Integral splitting requires Delta to be an integer square, including
zero if roots repeat. Square discriminant alone does not imply splitting:
x^3-3x+1 has discriminant81, but its only possible rational roots +/-1
both fail. This is an abstract counterexample, not an endpoint triple.
For an irreducible cubic a nonzero square discriminant can instead give
a cyclic cubic extension.

At a fixed admissible integer equality point, N>0 and each integer root
d>a+b must divide N. For any such divisor test P3(d)=0. If it vanishes,

```text
P3(x)=(x-d)[x^2+(d-A)x+N/d].
```

All three roots are integers exactly when some such divisor passes the
root test and the quadratic discriminant (A-d)^2-4N/d is a nonnegative
integer square with its square root congruent to A-d modulo two. This
also covers repeated roots. It is a finite exact test for each known
integer point, rather than a bound on the unbounded equality curve.

## Finiteness does not supply a candidate list

The genus-ten result and Siegel's theorem prove finitely many integer
points. They supply no effective height bound or complete list here.
Finitely many rational points is a separate consequence of Faltings for
the smooth projective curve; it also supplies no enumeration in this work.
One cannot turn either finiteness statement into a complete answer by
checking a presumed finite set without proving that it is exhaustive.

Riemann-Roch spaces for specified divisors on the normalization are
computable in principle. Their bases provide functions and embeddings,
not an enumeration of all rational or integer points. Effective point
methods need additional certified arithmetic information, such as a
suitable Mordell-Weil rank bound and generators, a justified height bound,
or a covering computation with a completeness argument. None has been
established for this curve. The genus-three quotient and dimension-seven
Prym remain possible arithmetic directions, as described in the
[descent diagnostic](endpoint-one-equality-quotient.md).

The [checker](../scripts/check_endpoint_one_equality_cubic.py) verifies
generic characteristic-polynomial, endpoint, discriminant/Sylvester and
divisor-factor identities, and the abstract square-discriminant example.
It does not search exponent triples, enumerate curve points or compute
Jacobian ranks. Equality integer feasibility and global cubic splitting
remain open; no new nonintegrality family or Lean verification is claimed.
