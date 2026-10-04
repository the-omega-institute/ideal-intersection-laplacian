# Finite endpoint tests and the geometric restrictions

The endpoint-covering observation in Remark 14.7 concerns a fixed finite
collection of tests of the form h_C(1)=0 or h_C(2)=0 modulo an integer.
It does not establish that every congruence method is exhausted. In
particular, another quotient root or an integer divisor condition can
still exclude a triple passing these tests.

The original equal-step constructions have fixed span and unbounded
minimum. Their tails therefore satisfy the established balanced-region
criterion minimum >= 3*span+8. They establish the endpoint-only limitation
on all fully distinct triples, without demonstrating survival of the
geometric restrictions. The following construction supplies that additional
scope for the explicitly listed restrictions.

Let L be the least common multiple of eight and the selected moduli. Choose
any positive multiple d of L with d>=32. Consider

```text
T1(d) = (9+d, 9+2d, 136+4d),
T2(d) = (10+d, 10+2d, 12+4d).
```

Both triples are strictly ordered and have minimum at least eight and
middle exponent greater than fifteen. Since the complement quotient has
integer polynomial entries in its exponents, its monic quintic h_C and
both endpoint evaluations have integer polynomial coefficients. The known
zeros at (9,9,136) and (10,10,12) show that T1 passes every selected
endpoint-one test and T2 every selected endpoint-two test, respectively.

Put I=(a-2)(a+b+c-2)-2bc for an ordered triple (a,b,c). Exact substitution
gives

| Quantity | T1(d) | T2(d) |
| --- | --- | --- |
| I | -9d^2-415d-1384 | -9d^2-42d |
| 4a^2-2a-c | 4d^2+66d+170 | 4d^2+74d+368 |
| (a+2)(7a-16-c)+40 | 3d^2-56d-939 | 3d^2+78d+544 |

The first row is negative, so the sufficient inertia inequality I>0 does
not exclude either construction. The second row is positive. For the first
entry in the third row, writing d=32+e gives 3e^2+136e+341>0 for e>=0;
the other entry is positive already. Thus both constructions satisfy

```text
c < 4a^2-2a,
c < 7a-16+40/(a+2).
```

The gcd is exactly one for T1: a common divisor divides b-2a=-9 and
c-4a=100. For T2 it is exactly two: it divides -10 and -28, and every
entry is even. Since d is divisible by eight, T1 has residues (1,1,0)
modulo eight, while T2 has residues (2,2,4), with valuations (1,1,2).
Hence neither is all odd, neither has gcd at least three, and neither
has common 2-adic valuation. They have distinct exponents and large spans,
and do not enter the balanced-region exclusion.

This proves that finitely many endpoint-value congruence tests, even with
the stated ordering, small-exponent, gcd, valuation and geometric filters,
cannot eliminate every candidate. It does not assert that these triples
pass every other arithmetic or spectral restriction in the manuscript,
that either endpoint actually vanishes, or that their spectra are integral.
The fully distinct endpoint surfaces and full Q3 remain open.

The [exact checker](../scripts/check_endpoint_congruence_scope.py) verifies
the six substitution identities, the positive boundary shift and both
known zero endpoints by integer six-by-six determinants. Its
[saved output](../results/endpoint-congruence-scope.json) is a finite identity
check supporting the written all-moduli argument; it performs no exponent
search, numerical spectrum or Lean verification.
