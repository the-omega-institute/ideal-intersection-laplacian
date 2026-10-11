# A uniform mixed-parity family modulo four

Every positive exponent triple that is a permutation of **(3,3,2) modulo
four** gives a nonintegral three-prime ideal intersection graph. This is
a written proof for an infinite family, without size or ratio restrictions.
It strengthens two rows of the earlier [six-class theorem](mixed-parity-congruence.md)
and adds the cases where the two odd exponents share a residue modulo eight.

Relabel the odd exponents as a=4u+3 and b=4v+3, and the even exponent
as c=4w+2, with u,v,w nonnegative integers. For the general complement
quintic h(x)=det(xI-C)/x, expansion gives coefficientwise identities:

```text
h(x) = x^2(x+1)^3 modulo 2,
F(y) = h(2y+1)/8 belongs to Z[u,v,w,y],
F(y) = y^3 modulo 2,
h(1) = 16(u+v) modulo 32,
h'(1) = 8(u+v+1) modulo 16.
```

If all five roots of h were integers, precisely two would be even and
three odd, counted with multiplicity. Write the even roots as eta1,eta2
and the odd roots as 2r1+1,2r2+1,2r3+1. The exact factorization is

```text
F(y) = (2y+1-eta1)(2y+1-eta2)(y-r1)(y-r2)(y-r3).
```

The even-root factors reduce to one modulo two. Since F reduces to y^3,
each ri must be even. Thus all three odd roots are one modulo four.
Their three factors at x=1 each contribute a factor four, so 64 divides
h(1). Every term in the product-rule expansion of h'(1) retains at
least two of these factors, so 16 divides h'(1). This includes coincident
roots and evaluations equal to zero.

The endpoint congruence now forces u+v even, but the derivative congruence
forces u+v odd. This contradiction rules out an entirely integer quintic
spectrum. The complement quotient is similar to a real symmetric matrix;
the noninteger real root mu lifts to the noninteger graph eigenvalue V-mu.

## Relation to the previous result

The earlier six rows include (3,7,2) and (3,7,6) modulo eight. The new
theorem covers those rows and also (3,3,2), (7,7,2), (3,3,6), (7,7,6),
including all permutations. The examples (10,19,27) and (14,23,39) lie
in the latter group; they have gcd one, unequal 2-adic valuations and
middle exponent above fifteen. This comparison is with the earlier six
rows, rather than a claim that no other theorem can cover these examples.

## Exact checks

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_odd_root_distribution.py
```

The [checker](../scripts/check_odd_root_distribution.py) reconstructs the
generic quintic and verifies all six exponent permutations. It checks
160 coefficients for divisibility by eight, the 160 coefficients of the
shifted congruence modulo two, 42 endpoint coefficients modulo 32 and
51 derivative coefficients modulo 16. These are polynomial identities
in the shift variables, rather than values on a finite exponent range.

For four selected fixtures, a separately written integer matrix supplies
28 six-by-six permutation-expansion determinants. Six positive evaluation
points reconstruct each full quintic by interpolation; the determinant
at zero checks the omitted zero root. A further 24 five-by-five principal
cofactors reconstruct the derivative of det(xI-C) at one independently.
Since det(xI-C)=x h(x), subtracting h(1) gives h'(1). All polynomial
coefficients, endpoint and derivative congruences agree. Each fixture also
retains a nonlinear rational factor. The
[saved certificate](../results/odd-root-distribution.json) records the
coefficients, values, source hash and validation scope.

The [manuscript](../paper/sections/mixed-parity-congruence.tex) contains
the root-distribution lemma and the theorem. No exponent scan,
floating-point eigenvalue calculation or Lean formalization is used.
Full Q3 and nonsquarefree vectors with more than three prime factors
remain open.
