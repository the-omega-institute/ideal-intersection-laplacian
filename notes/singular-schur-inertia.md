# Exact quotient root counts at zero Schur diagonal entries

The supporting inertia lemma now includes the boundaries excluded by
its reciprocal formula. For ordered positive real parameters and
`0<x<a`, write

\[
K(x)=\operatorname{diag}(k_a,k_b,k_c)-vv^T,\quad
k_t=a+b+c-x-\frac{xabc}{t(t-x)},\quad
v=(\sqrt a,\sqrt b,\sqrt c)^T.
\]

Let `q` be the number of negative `k_t` and let `z>0` be the number
that vanish. Then

\[
n_-(K)=q+1,\qquad n_+(K)=3-q-z,\qquad\dim\ker K=z-1.
\]

Consequently the six-support complement quotient has exactly `q`
positive eigenvalues strictly below `x`, and its eigenvalue `x` has
multiplicity `z-1`. A single zero diagonal does not make `x` an
eigenvalue of the quotient. Two or three zeros give multiplicity one
or two. Root counts include multiplicities.

Choose any index `j` with `k_j=0`. The coordinate change
`w_j=v^T y`, `w_i=y_i` for `i!=j` is invertible because `v_j>0`.
The quadratic form becomes

\[
y^TKy=-w_j^2+\sum_{i\ne j}k_iw_i^2.
\]

This congruence proves the inertia and nullity formulas without a limit
or division by a zero diagonal. The lower paired-support block `D-xI`
is positive definite when `x<a`. Its Schur congruence transfers the
negative count and nullity to the full symmetric quotient shifted by
`x`. The quotient is positive semidefinite with a simple zero, so
subtracting the shift of zero gives the asserted positive-root count.
Symmetry ensures that nullity equals algebraic multiplicity.

The nonsingular formula involving `F=1-sum(t/k_t)` is retained.
The new branch completes that lemma; the assumption `x<a` remains.
It does not treat a singular paired-support block at `x=a`.

Five specified rational/integer controls cover single-zero positions
and both possible two-zero counts:

| Parameters | Endpoint | Negative diagonal entries | Zero diagonal entries | Positive roots strictly below endpoint | Endpoint multiplicity |
| --- | --- | --- | --- | --- | --- |
| `(10,76/7,11)` | 2 | 0 | 1 | 0 | 0 |
| `(8,15,20)` | 3 | 1 | 1 | 1 | 0 |
| `(8,8,11)` | 3 | 2 | 1 | 2 | 0 |
| `(8,8,42/5)` | 2 | 0 | 2 | 0 | 1 |
| `(5,6,6)` | 2 | 1 | 2 | 1 | 1 |

The sixth control uses `(8,8,8)` at the exact algebraic endpoint
`x=48-8sqrt(33)`, between zero and eight. All three diagonal entries
are zero. Its direct quintic is

\[
(u-72)(u^2-96u+192)^2,
\]

so no positive root lies strictly below `x`, and `x` has multiplicity
two. The other quadratic root is `48+8sqrt(33)>x`, and `72>x`.

Run `python3 scripts/verify_singular_schur_inertia.py` with Python 3.10+
and SymPy 1.14.0; compare with `results/singular-schur-inertia.json`.
The checker verifies a generic three-dimensional congruence, constructs
the weighted symmetric and Schur blocks directly from set disjointness,
and checks the five rational endpoint multiplicities and strict root
counts. Endpoint factors are removed before counting roots. The equal
control uses exact algebraic factorization and ordering, with no floats.
The support constructor and SymPy backend are shared; the original
characteristic-polynomial helper is not imported. The written proof
establishes the general result; the fixed controls verify the formulas.
There is no scan, new finite classification input, historical finite-base
rerun or Lean verification. The selected main classification is retained;
this extension belongs to the supporting collection.
