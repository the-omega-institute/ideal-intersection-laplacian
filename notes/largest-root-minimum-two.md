# Largest quotient root at real minimum two

The largest-root theorem now holds for real

\[
2\le a\le b\le c,\qquad b-a\ge3,\qquad c\ge a^2-a.
\]

With \(M=bc+a+b+c\), it gives
\(M<\lambda_{\max}(C)<M+1\). This lowers the previous minimum-three
hypothesis. Integer exponents in this domain therefore give a nonintegral
ideal intersection graph by the established complement and universal-class
lifts. The complete three-prime classification retains its historical finite
inputs; this strengthening is a written real-domain proof with no finite base.

## The lower sign

The direct quotient determinant gives \(h_C(M)=-a^2bcT\), where

\[
T=(2b^2-ab+b-a)c^2-[(a-1)b^2+a^2]c-ab(a+b).
\]

The quadratic coefficient is at least \(b^2>0\). At \(c=b\),

\[
T(a,b,b)=2b[(b-a+1)b^2-ab-a^2]
\ge2b^3(b-a-1)>0.
\]

Here \(a(b+a)\le2b^2\). The derivative at this boundary is

\[
\partial_cT(a,b,b)=b^2(4b-3a+3)-2ab-a^2\ge b^3>0,
\]

because \(4b-3a+3\ge b+3\) and \(2ab+a^2\le3b^2\).
The upward quadratic thus remains positive for every \(c\ge b\).

## The upper sign

Put \(P=h_C(M+1)\). For \(a\ge3\), the existing complete
170-term positive expansion in the manuscript gives \(P>0\).
For \(2\le a\le3\), substitute

\[
a=2+m,\quad b=5+m+u,\quad c=b+v,
\qquad0\le m\le1,\quad u,v\ge0.
\]

Every ordered triple in the new slab has this form. It also automatically
satisfies the quadratic maximum bound, since
\(a+3-(a^2-a)=(3-a)(a+1)\ge0\).
Write the complete 143-term expansion as
\(P=\sum p_{kij}m^ku^iv^j\). Its 39 negative coefficients have
\(k\ge3\); all coefficients with \(k=0\) are positive. Define

\[
B(u,v)=\sum_{i,j}\left(p_{0ij}+
                 \sum_{k\ge1,\,p_{kij}<0}p_{kij}\right)u^iv^j.
\]

The exact difference is

\[
P-B=\sum_{k\ge1,\,p_{kij}>0}p_{kij}m^ku^iv^j
   +\sum_{k\ge1,\,p_{kij}<0}|p_{kij}|(1-m^k)u^iv^j\ge0.
\]

The complete ascending \(u\)-coefficient vectors of \(v^j\) in \(B\) are:

| \(j\) | Coefficient vector |
|---|---|
| 0 | 259876, 480352, 371193, 157834, 41170, 6792, 693, 40, 1 |
| 1 | 240176, 371193, 236751, 82340, 16980, 2079, 140, 4 |
| 2 | 77666, 100317, 52638, 14520, 2226, 180, 6 |
| 3 | 10700, 11468, 4800, 987, 100, 4 |
| 4 | 540, 468, 147, 20, 1 |

All 35 coefficients are strictly positive, so \(P\ge B\ge259876>0\).
The negative coefficients are bounded on the slab, rather than incorrectly
being treated as a counterexample or a positive expansion on all \(m\ge0\).

## Identifying the largest root

The symmetric quotient similarity and its Schur complement remain the
same as in the manuscript. At \(x=M+1\), the pair-support block is
positive definite and the Schur complement is

\[
H=\operatorname{diag}(\ell_a,\ell_b,\ell_c)+zz^T,
\qquad \ell_t=x-a-b-c-\frac{xabc}{t(x-t)}.
\]

Both \(x-b\) and \(x-c\) exceed \(bc\). Consequently
\(\ell_b>c(b-a)+1-a>0\) and
\(\ell_c>b(c-a)+1-a>0\), now using
\(c\ge b\ge a+3\) throughout. The \(b,c\) principal block is
positive definite. The positive full determinant \(xP\) makes its remaining
scalar Schur complement positive. Thus \(xI-S\) is positive definite
and every root lies below \(M+1\). The negative determinant at \(M\)
puts at least one root above \(M\), proving the asserted largest-root bracket.

## Reproduction and scope

From the repository root, with Python 3.10 or later and SymPy 1.14.0:

```sh
python3 scripts/verify_largest_root_minimum_two.py
python3 scripts/verify_largest_root_coefficients.py
```

The first checker reconstructs the generic determinant directly, verifies
the lower quadratic identities, every displayed lower-bound coefficient,
the exact nonnegative difference, and the Schur diagonal bounds.
Its saved output is `results/largest-root-minimum-two.json`.
Two fixed controls, \((2,5,5)\) and \((5/2,11/2,6)\), have exact
Sturm counts of one root in the bracket and none above it. They supplement
the proof; they are not a parameter scan or finite base. The second checker
retains its 247-coefficient scope for the original 36/170 tables and the
six current minimum-two small-gap vectors. The support constructor and
SymPy backend are shared, and the original characteristic-polynomial
helper is not imported. There is no Lean validation or rerun of the
27,562- and 8,658-triple historical bases. Four-prime classification and
integer-point enumeration retain their separate open scope.
