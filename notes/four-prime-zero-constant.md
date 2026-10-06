# The zero-constant endpoint family

**Theorem.** For four distinct primes, every positive exponent vector

```text
(a,a,(a-1)(2a-1),c), a>=2, c>=a,
```

has noninteger Laplacian spectrum. Its smallest genuine restricted
root lies in (1,3) and is not 2. There is no ordering or coprimality
condition on the two tails. The result is an unbounded written proof
with no finite exponent base.

## The constant factor that selects the family

Use p(x)=det(xI-K) and the
[genuine repeated-pair restriction](four-prime-single-pair-balanced.md).
For a prospective integer restricted root s, set h=a+1-s.
The exact constant term in the tail c is

```text
p(s)|c=0=-h[(a+1)b+h]
             [b((s-1)^2+(s-2)h)-h(2h+s-1)].
```

At s=2 the final factor becomes b-(a-1)(2a-1). Thus the tail
equation loses its constant term precisely at the positive smaller-
parameter relation b=(a-1)(2a-1). This structural degeneration,
rather than a selected finite parameter table, motivates the family.
The word "smaller" refers to this chosen parameter, not an ordering
between b and the free tail c. Zero tail here is a polynomial
specialization, not a positive graph exponent.

Put

```text
N=(a-1)(2a+1)(2a^3-a^2+a-1)
 =4a^5-4a^4+a^3-2a^2+1,
D=2a^3-5a^2+3a+1.
```

At b=(a-1)(2a-1), the entire tail equation factors as

```text
p(2)=2a(a-1)c(N-Dc).
```

For positive c, the only possible root-two tail is therefore N/D.
Both N and D are positive for a>=2. We show that this rational
candidate is never an integer.

## A uniform coprimality identity

The integer polynomial identity

```text
(3a^2-9a+7)N
 +(-6a^4+9a^3-2a^2+6a+1)D=8
```

implies gcd(N,D) divides 8 at every integer a. But

```text
D=1+a(a-1)(2a-3)
```

is odd, since a(a-1) is even. Hence gcd(N,D)=1. Writing a=2+v,

```text
D=2v^3+7v^2+7v+3>=3.
```

Thus the positive candidate N/D has a nontrivial denominator even
in lowest terms. Root 2 is excluded for every positive integer c,
without a residue search, discriminant test or parameter cutoff.

## The low-root interval for every c>=a

The established tensor positivity proof gives kappa_min(K)>1 for
all positive a,b,c. For the upper bound, use the empty/full principal
minor of the symmetric matrix similar to K-3I. It is

```text
J3=-(a+2)bc+(a+1)(a-2)(b+c)+2(a-1)(a-2).
```

Substituting b=(a-1)(2a-1) and c=a+u with u>=0 gives

```text
J3=-(2a^3-4a+4)u-(5a^3-6a^2+5a-2)<0.
```

For a=2+v, the complete coefficient lists of the relevant positive
polynomials, in descending powers of v, are:

| Polynomial | Coefficients |
|---|---|
| b-a | 2,4,1 |
| D | 2,7,7,3 |
| 2a^3-4a+4 | 2,12,20,12 |
| 5a^3-6a^2+5a-2 | 5,24,41,24 |

The minor stays strictly negative at c=a, and b>=a for every a>=2.
A negative trial direction gives kappa_min(K)<3. Since its only
possible integer value in (1,3) is 2, already excluded, this root
is noninteger. The actual graph eigenvalue is V+1-kappa_min,
with V=(a+1)^2(b+1)(c+1)-2, proving the theorem. This also places
that graph eigenvalue in (V-2,V).

## A simple resonance passing the prior local tests

Take (a,a,b,c)=(6,6,55,75). At root 2, the good prime 5 has
e=v_5(a-1)=1, v_5(b)=1 and v_5(c)=2. The previous permitted
branch e=r<t holds. With scaled H=1,B=11,C=15, its first
cubic resonance factor B-2C-H vanishes modulo 5, while the second
2B-C+H is nonzero. Both coarse endpoint divisibilities hold.

The only prime dividing a+1 is 7. Its tail factor quadratics are
(x-3)(x+2) and (x-4)^2, so the prior modular splitting test also
passes. The preceding double-resonance discriminant test does not
apply: v_5(b+h)=v_5(60)=1<2v_5(h).

The exact tail equation now supplies a global obstruction:

```text
p(2)=-60c(271c-26065).
```

The sole positive candidate is 26065/271, in lowest terms and
noninteger. At c=75 the independent characteristic values are
p(2)=25830000 and p(3)=-1681145000. This compares the named
local tests only, not every prior sufficient criterion or priority.

## Verification and remaining scope

The [checker](../scripts/check_four_prime_zero_constant.py) verifies
the generic constant factorization against an independent symbolic
permutation determinant, the full root-two factorization, integer
Bezout identity, odd-denominator identity and strict minor. All four
written coefficient lists are retained and independently matched to
the [certificate](../results/four-prime-zero-constant.json).
Six specified positive controls verify 336 support-column actions,
weighted zero sums and symmetry, and the actual graph transfer.
Twenty-four independent integer determinants at algebraic c=0,1,2,3
reconstruct and cross-check six tail quadratics. Thirty more integer
determinants reconstruct six genuine quartics; six exact Sturm counts
verify one root in (1,3). The controls include two c=a boundaries
and tails on both sides of the noninteger rational candidate.

The certificate is reproducible with SymPy 1.14.0 using
`python3 scripts/check_four_prime_zero_constant.py`.
The unbounded proof does not depend on these six fixed controls.
No exponent/tail scan, expanded graph, historical finite-base rerun,
floating eigenvalues or Lean validation is used.

For c<a this particular minor argument is not asserted. Other
simple resonances and nonzero constant terms retain their unresolved
integer-root questions. General single-pair, fully unequal four-prime
and higher-prime classification remain open. All previous proofs and
finite inputs, the three-prime main and joint manuscript decisions
retain their scopes.
