# A uniform low eigenvalue and a balanced region of nonintegrality

For **every ordered exponent triple `4<=a<=b<=c`**, the six-support
complement quotient has a nonzero eigenvalue in **`(0,3)`**. The diagonal
of its Schur complement may have any sign pattern. This gives a uniform
bound throughout the three-prime region left by the earlier results.

If also **`(a-2)(a+b+c-2)>2bc`**, a nonzero complement eigenvalue lies
in **`(2,3)`**, so the ideal intersection graph is not Laplacian integral.
In particular, if `r=c-a`, **every triple with `a>=3r+8` is nonintegral**.
The span can grow without bound; this result is a written proof, without
enumerating exponents or using modular endpoint certificates.

Read [the manuscript proof](../paper/sections/mixed-inertia.tex),
[the PDF](../paper/paper.pdf), and
[the exact identity and representative checks](../results/mixed-inertia.json).

## Counting roots with a mixed-sign diagonal

Use the symmetric quotient and Schur complement from
[the preceding inertia proof](low-spectrum.md). Put `s=a+b+c`, `P=abc`,
`v=(sqrt(a),sqrt(b),sqrt(c))^T`, and, for `0<x<a`,

```text
K(x)=diag(k_a(x),k_b(x),k_c(x))-vv^T,
k_t(x)=s-x-xP/[t(t-x)].
```

When none of the `k_t(x)` is zero, let `q` be the number of negative
diagonal values and set `F(x)=1-a/k_a-b/k_b-c/k_c`. Then

```text
n_minus(K(x))=q+indicator(F(x)<0),
nullity(K(x))=indicator(F(x)=0).
```

Indeed the bordered matrix `[[diag(k),v],[v^T,1]]` is congruent both
to `K(x) direct_sum [1]` and to `diag(k) direct_sum [F(x)]`.
The lower block `diag(a,b,c)-xI` of the full quotient is positive
definite, so the number of positive quotient eigenvalues strictly below
`x` is `n_minus(K(x))-1`, subtracting the simple zero eigenvalue.
This formula applies to mixed signs. The following comparison also covers
zero diagonal values, where the reciprocal formula cannot be used.

## A general comparison at three

Define the real symmetric matrix

```text
L=diag(s-3P/a^2,s-3P/b^2,s-3P/c^2)-vv^T.
```

Two identities determine enough of its inertia:

```text
det(L)=6[c(a-b)^2+b(a-c)^2+a(b-c)^2],
v^T L v=-3P(1/a+1/b+1/c)<0.
```

For unequal exponents the determinant is strictly positive. The negative
Rayleigh value supplies a negative eigenvalue; a positive determinant in
dimension three then forces exactly two negative eigenvalues. At equal
exponents, `L=-vv^T`, with one negative and two zero eigenvalues.
Thus in every case **at least two eigenvalues of L are nonpositive**.

For `a>3`, the exact comparison is

```text
K(3)=L-diag(3+9P/[t^2(t-3)]), t=a,b,c.
```

The subtracted diagonal is positive definite. A two-dimensional subspace
where L is nonpositive becomes strictly negative for K(3). Therefore
K(3) has at least two negative eigenvalues, independently of its diagonal
signs. Sylvester's law of inertia gives at least two quotient eigenvalues
below three. One is zero; another is positive because the complement
support graph is connected. This proves the universal root in `(0,3)`.
For example, `(8,100,10000)` has only one negative `k_t(3)`; the bound
still applies. The proof also includes equal exponents and zero-diagonal
boundaries such as `(8,8,11)` and `(8,15,20)`.

## An integer-free interval and a growing balanced region

The inequality `(a-2)(s-2)>2bc` is exactly `k_a(2)>0`. Since `k_t(2)`
increases with `t`, all three values are positive. Congruence turns K(2)
into `I-zz^T`, with `||z||^2=a/k_a+b/k_b+c/k_c>1`, since each `k_t<s`.
It consequently has one negative and two positive eigenvalues and is
nonsingular. The only quotient eigenvalue at or below two is zero.
The universal positive root below three therefore lies in `(2,3)`.
Its graph lift lies in `(V-3,V-2)`, which contains no integer.

For an explicit sufficient region write `b=a+d`, `c=a+r`, `0<=d<=r`.
Then

```text
(a-2)(s-2)-2bc
 = a^2-2ar-8a-2r^2-4r+4+(r-d)(a+2r+2).
```

At `a=3r+8+u`, `u>=0`, the first part becomes

```text
(r+2)^2+(4r+8)u+u^2>0.
```

The remaining term is nonnegative. This proves every triple with
minimum exponent at least three times its span plus eight is nonintegral.
Examples outside the earlier four fixed-gap families include
`(20,21,24)`, `(38,43,48)` and `(308,350,408)`.

## What remains

For `a>=4`, a Laplacian integral graph would require its smallest
positive complement quotient eigenvalue to equal 1 or 2. Therefore
`h_C(1)h_C(2)=0` is a **necessary condition**, not an integrality
classification. If both endpoints are nonzero, the uniform low-root
bound already proves nonintegrality, regardless of endpoint signs.
The endpoint-zero triples still need an argument about the other roots.

After the earlier minimum-through-seven and tail results, unresolved
three-prime triples lie within `8<=a<b<c<4a^2-2a`, outside the proved
families and the new interval criterion. In particular they must satisfy
`a<3(c-a)+8` and `(a-2)(a+b+c-2)<=2bc`. A possible integral example must
also lie on one of the two endpoint-zero surfaces. Full Q3 and the
nonsquarefree higher-prime vectors remain open.

## Exact verification

Run with Python 3.10+ and SymPy 1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_mixed_inertia.py
```

The checker verifies the determinant, negative Rayleigh, equal-exponent,
comparison-gap and span identities symbolically using a rational
three-dimensional congruence. Six exact fixtures cover every nonsingular
Schur sign/secular combination possible here: `(q,sign(F))` equal to
`(0,-1),(1,1),(1,-1),(2,1),(2,-1),(3,1)`. Independent quotient polynomials and
Sturm counts check the inertia predictions. Nine explicitly selected
quotient/Sturm fixtures check the low-root and interval statements,
including equal exponents, two zero-diagonal boundaries, a strongly
unbalanced triple and chosen spans up to 1000. These examples validate
the formulas; the infinite statements follow from the written proof.
The earlier 27,562-case certificate is retained, not rerun or enlarged.
No numerical eigensolver or Lean formalization is used.

[Return to the project entrance](../README.md).
