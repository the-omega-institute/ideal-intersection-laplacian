# Two low complement eigenvalues and four complete unequal-exponent families

We prove nonintegrality for every positive exponent triple of one of the forms

```
(a,a+1,a+2), (a,a+1,a+3), (a,a+2,a+3), (a,a+3,a+4), a>=1.
```

Consequently **every three-prime triple whose maximum minus minimum is
at most three is nonintegral**, including arbitrarily large distinct exponents.
The proof uses an inertia criterion for the general complement quotient and
four complete root-free modular certificates. It does not enumerate a range
of minimum exponents.

Read [the manuscript](../paper/paper.pdf),
[the complete proof source](../paper/sections/low-spectrum.tex), and
[the exact certificate](../results/low-spectrum.json).
Full Q3 and the remaining unequal-exponent and higher-prime cases stay open.
The subsequent [requested finite-region diagnostic](open-region-diagnostic.md)
certifies every remaining pair for minima4through7 under the uniform cutoff.
Together with earlier proofs this settles every minimum-entry<=7 triple,
using an explicitly complete finite discriminant certificate.

## Why endpoint signs alone are insufficient

An interval containing two roots need not give a sign change. At equal
exponents the complement quintic has the exact factorization

```
h_(a,a,a)(x) = (x-a^2-a) [x^2-(a^2+4a)x+3a^2]^2.
```

The low quadratic root has multiplicity two. The following symmetric
Schur complement counts eigenvalues without requiring a sign change.

## General inertia criterion

For ordered positive exponents `a<=b<=c`, let `s=a+b+c`, `P=abc`.
Symmetrize the [six-support complement quotient](one-unit-exponent.md)
by the square roots of its cell sizes and order the classes as
`1,2,3,23,13,12`. The symmetric matrix has blocks

```
C_sym = [[A, -sqrt(P)I], [-sqrt(P)I, D]],   D=diag(a,b,c),
A_ii = (b+c+bc, a+c+ac, a+b+ab)_i,
A_ij = -sqrt(a_i a_j), i!=j.
```

For `0<x<a`, the lower block `D-xI` is positive definite. Its Schur
complement is

```
K(x) = diag(k_a(x),k_b(x),k_c(x)) - v v^T,
v = (sqrt(a),sqrt(b),sqrt(c))^T,
k_t(x) = s-x-xP/[t(t-x)].
```

Here `k_t(x)` increases with `t>x`; its derivative is
`xP(2t-x)/[t^2(t-x)^2]>0`. Sylvester's law of inertia now proves:

- If the integer `m` satisfies `2<=m<a` and
  **`(c-m)(s-m)<mab`**, all three `k_t(m)` are negative. Hence
  `C_sym-mI` has three negative and three positive eigenvalues.
  The connected complement quotient has a simple zero eigenvalue,
  so **exactly two nonzero complement eigenvalues lie in `(0,m)`**.
- If also **`(a-m+1)(s-m+1)>(m-1)bc`**, all three `k_t(m-1)` are
  positive. After diagonal congruence, `K(m-1)` becomes `I-zz^T`,
  where `||z||^2 = a/k_a+b/k_b+c/k_c>1`, since each `k_t<s`.
  Thus `C_sym-(m-1)I` has just one negative eigenvalue, corresponding
  to zero. **Both low positive eigenvalues lie in `(m-1,m)`** and
  lift to noninteger graph eigenvalues in `(V-m,V-m+1)`.

All the relevant complement eigenvalues are less than `a<N`, so the
reflection and universal-vertex lift apply. The general criterion itself
has a written proof; it is not an inference from representative examples.

## Four complete families

At `m=3`, substitute `(b,c)=(a+d,a+e)`. The upper condition minus its
right side is respectively

| (d,e) | (c-3)(s-3)-3ab |
| --- | --- |
| (1,2) | -6a |
| (1,3) | -2a |
| (2,3) | -4a |
| (3,4) | 4-2a |

Every expression is negative for `a>=4`. Therefore each family has two
positive complement roots in `(0,3)`. We exclude the only possible integers
in this interval, 1 and 2.

Write `h_(a,a+d,a+e)(1)=-4M_(d,e)(a)P_(d,e)(a)`. These exact identities
prove `h(1)<0` for `a>=4`:

| (d,e) | M(a) | Descending coefficients of P(4+u) |
| --- | --- | --- |
| (1,2) | a(a+1) | 1,18,116,314,294 |
| (1,3) | a(a+1)(a+3) | 1,13,51,57 |
| (2,3) | a+2 | 1,25,242,1126,2484,2022 |
| (3,4) | a+3 | 1,28,302,1550,3699,3126 |

Every multiplier and every shifted coefficient is strictly positive.
At 2, the endpoint factorizations are

```
h_(a,a+1,a+2)(2) = -a F_12(a),
F_12(a) = a^5-9a^4-14a^3+93a^2+67a+6;

h_(a,a+1,a+3)(2) = -(a-2)(a+1) F_13(a),
F_13(a) = a^4-6a^3-42a^2-39a-10;

h_(a,a+2,a+3)(2) = -a F_23(a),
F_23(a) = a^5-5a^4-48a^3-59a^2-39a-54;

h_(a,a+3,a+4)(2) = -F_34(a),
F_34(a) = a^6-a^5-74a^4-375a^3-967a^2-1220a-340.
```

The four factors have no integer roots, as the following **complete**
modular residue lists show:

| Factor | Prime | Values at residues 0,...,p-1 |
| --- | --- | --- |
| F_12 | 7 | 6,4,1,5,6,5,1 |
| F_13 | 11 | 1,3,9,8,2,6,4,4,5,8,5 |
| F_23 | 7 | 2,6,5,3,5,4,3 |
| F_34 | 13 | 11,1,3,4,3,1,9,9,11,11,6,1,8 |

No residue value is zero. The accompanying multipliers are nonzero for
`a>=4`, so `h(2)!=0`. Both low positive roots are therefore noninteger.
Their graph lifts are noninteger as well. For `a=1,2,3`, use the previously
proved [minimum-three theorem](distinct-tail.md). This exhausts each family.

If a positive triple has maximum minus minimum at most3, repeated entries
are handled by the [complete repeated-exponent theorem](repeated-exponent-completion.md).
For distinct entries, its ordered gaps must be `(1,2),(1,3)` or `(2,3)`.
This proves the stated maximum-minus-minimum corollary.

## Exact verification

With Python 3.10+ and SymPy 1.14.0, run

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_low_spectrum.py
```

Compare with [results/low-spectrum.json](../results/low-spectrum.json).
The checker reconstructs the general weighted symmetric quotient, verifies
its block form, Schur complement and determinant identities, the monotonicity
derivative, all four upper-condition expressions, and both endpoint
factorizations. It checks the positive shifted coefficients and all
**38 modular residues**, using separate integer Horner arithmetic.

Eight explicitly chosen representatives, the four families at `a=4` and
`a=20`, also have independently reconstructed quotient polynomials and
exact Sturm counts of two roots in `(0,3)`. At `a=20` each meets the lower
condition and has two roots in `(2,3)`. These finite examples check the
formulas; the infinite claims use the written inertia proof and complete
modular exclusions. No parameter scan, floating-point spectrum or Lean
formalization is used. Earlier certificates keep their recorded scopes.

The remaining three-prime problem lies within `8<=a<b<c<4a^2-2a`, outside
the four families above and any triples settled by the general inertia
criterion. A uniform obstruction for the rest remains to be proved.

[Return to the project entrance](../README.md).
