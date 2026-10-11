# Even exponents congruent to two modulo four

**Every positive three-prime exponent triple with `a=b=c=2 mod4`
gives a nonintegral ideal intersection graph.** Actual equality of the
exponents is unnecessary; their ratios and differences can be arbitrary.
Together with the earlier all-odd and common-divisor arguments, this
settles **every triple whose three exponents have the same 2-adic valuation**.

This proof resolves another whole part of the remaining even region,
including gcd-two triples below the linear tail bound. Examples are
`(10,14,18)`, `(14,22,34)` and `(18,26,42)`.
Read [the manuscript proof](../paper/sections/arithmetic-obstructions.tex),
[the PDF](../paper/paper.pdf), and [exact checks](../results/even-exponent-congruence.json).

## Scaling reveals an obstruction that modulo two misses

Write the exponents as `a=2A`, `b=2B`, `c=2D`, where A,B,D are odd,
and set `Q=C/2`. This is an integer matrix. Put
`f(x)=det(xI-Q)/x`, a monic integer quintic.

If every complement eigenvalue were an integer, division by two would
give rational eigenvalues of Q. The rational-root theorem makes them
integers as well. In the six-support order, reduction of Q modulo two
is block lower triangular: the top block is the three-by-three matrix
with zero diagonal and all off-diagonal entries one, and the bottom
block is the identity. Thus

```text
det(xI-Q) = x(x+1)^5 modulo2,
f(x) = (x+1)^5 modulo2.
```

All five hypothetical integer roots of f must therefore be odd.
For each odd integer t, every factor `t-root` is even, so **32 divides
f(t)**. This applies even when t is itself a root, giving f(t)=0.

Now write `A=2u+1`, `B=2v+1`, `D=2w+1`. Expansion of the exact quotient
quintic gives the polynomial congruence

```text
f(2y+1) = 8(u+v+w+y-1) modulo32.
```

At y=0 and y=1 it implies **`f(3)-f(1)=8 mod32`**, contradicting
divisibility of both values by 32. Consequently C has a noninteger
eigenvalue, which lifts to a noninteger graph eigenvalue. The argument
does not assume that the lowest root or either integer endpoint is
noninteger.

## A common 2-adic valuation

Let `v2(t)` be the exponent of two dividing a positive integer t. If
the three valuations agree, there are three cases:

- Valuation zero: all three exponents are odd, settled by the earlier
  irreducible quadratic modulo two.
- Valuation one: all exponents are congruent to two modulo four, settled
  by the scaled-quintic argument above.
- Valuation at least two: their common divisor is at least four, settled
  by the earlier common-divisor theorem.

Hence every possible integral triple has unequal 2-adic valuations.
In particular, the remaining all-even region has gcd two, at least one
exponent congruent to two modulo four and at least one divisible by four,
and still obeys the strict linear endpoint-two bound.
Mixed-parity endpoint-one cases and full Q3 remain open.

## Exact verification

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_even_exponent_congruence.py
```

The checker constructs Q directly from the general six-support quotient,
verifies its integer-polynomial entries and the characteristic scaling
identity, and checks both congruences symbolically coefficient by
coefficient. It also reconstructs the binary block matrix and its
characteristic polynomial independently. Three chosen gcd-two fixtures
below the earlier linear and quadratic bounds have direct quotient
polynomials, separate integer Horner values at one and three, and
nonlinear irreducible rational factors. These examples check the formulas;
the infinite theorem follows from the written divisibility contradiction.
No exponent scan, numerical spectrum or Lean is used.

[Return to the project entrance](../README.md).
