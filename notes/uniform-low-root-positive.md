# The optimal uniform low-root bound for all positive real parameters

For every ordered real triple \(0<a\le b\le c\), the six-support
complement quotient has a positive eigenvalue strictly below three.
This strengthens the former real minimum-four statement. The uniform
constant three cannot be lowered, even when restricted to integer parameters.

For positive real parameters the support weights are positive and the
support graph is connected. The quotient is similar to a positive
semidefinite symmetric matrix with a simple zero eigenvalue. Set
\(s=a+b+c\), \(P=abc\). In the singleton/paired-support order it is

\[
\mathcal C=\begin{pmatrix}A&-\sqrt P I_3\\-\sqrt P I_3&D\end{pmatrix},
\quad D=\operatorname{diag}(a,b,c),
\]

where \(A_{11}=bc+b+c\), and its off-diagonal entries are
\(-\sqrt{ab},-\sqrt{ac},-\sqrt{bc}\). It suffices to show that
\(\mathcal C-3I\) has at least two negative eigenvalues, counted
with multiplicity. Its negative eigenvalues include the shift of zero;
at least one other quotient eigenvalue is then in \((0,3)\).

For \(a>3\), the existing comparison proof applies unchanged. With
\(v=(\sqrt a,\sqrt b,\sqrt c)^T\), define
\(L=\operatorname{diag}(s-3P/a^2,s-3P/b^2,s-3P/c^2)-vv^T\).
Then

\[
\det L=6[c(a-b)^2+b(a-c)^2+a(b-c)^2],\qquad
v^TLv=-3P(1/a+1/b+1/c)<0.
\]

For unequal parameters the positive determinant forces exactly two negative
eigenvalues; at equal parameters \(L=-vv^T\) has a two-dimensional
nonpositive subspace. The Schur complement at three subtracts the positive
diagonal \(3+9P/[t^2(t-3)]\) from \(L\), so it has at least two
negative eigenvalues in either case.

If \(b\le3\), take the principal block on the first two singleton
supports and their paired supports. In \(\mathcal C-3I\) it is

\[
\begin{pmatrix}A_0&-\sqrt P I_2\\-\sqrt P I_2&D_0\end{pmatrix},
\qquad D_0=\operatorname{diag}(a-3,b-3)\le0.
\]

On vectors \((z,tz)\) its quadratic form is at most
\(z^T(A_0-2t\sqrt P I_2)z\). For sufficiently large \(t\), this
is strictly negative for every nonzero \(z\), giving a two-dimensional
negative subspace. This includes \(a=b=3\).

The remaining case is \(a\le3<b\). Eliminate the strictly positive
paired diagonals \(b-3,c-3\). The singleton vector
\((0,\sqrt b,\sqrt c)\) has quadratic value

\[
q=(a-3)(b+c)-3P\left(\frac1{b-3}+\frac1{c-3}\right)<0.
\]

Compress the remaining four-dimensional matrix to singleton one, its paired
support, and that vector. The basis vectors are independent. The resulting
matrix is

\[
\begin{pmatrix}M&-\sqrt P&r\\-\sqrt P&a-3&0\\r&0&q\end{pmatrix},
\quad M=bc+b+c-3>0,\quad r=-\sqrt a(b+c).
\]

Its determinant is
\(M(a-3)q-Pq-(a-3)r^2>0\): the first and third terms are
nonnegative and the second is strictly positive. The positive and negative
diagonal entries force both a positive and a negative eigenvalue; determinant
parity gives exactly two negative eigenvalues. Interlacing and the Schur
congruence transfer that count to \(\mathcal C-3I\). This argument
includes \(a=3\) without dividing by \(a-3\).

To establish optimality, specialize \(a=b=c=t\). The exact quintic is

\[
h_{t,t,t}(x)=(x-t^2-t)\bigl[x^2-(t^2+4t)x+3t^2\bigr]^2.
\]

The smaller quadratic root is the smallest positive quotient root:
the quadratic is positive at zero and equals \(-t^3\) at \(x=t\),
while \(t^2+t>t\). Rationalizing gives this root as

\[
\lambda_2(t)=
\frac6{1+4/t+\sqrt{(1+4/t)^2-12/t^2}}\longrightarrow3.
\]

For large \(t\) it approaches three from below. The same limit holds
along integers, so any proposed uniform constant less than three fails.

Run `python3 scripts/verify_uniform_low_root_positive.py` with Python 3.10
or later and SymPy 1.14.0. The saved result is
`results/uniform-low-root-positive.json`. The checker reconstructs the
weighted symmetric block from set disjointness, verifies the trial-subspace
and compression identities and the retained comparison identities, and
checks the equal-parameter factorization and limit. Seven fixed exact
controls cover the three branches, equal parameters, \(b=3\), \(a=3\)
and a root exactly at three. Root counts include multiplicities and remove
the upper endpoint explicitly; for \((3,6,9)\) there is one positive root
strictly below three and a separate root exactly at three.

This is a written all-positive-real proof supported by symbolic identities
and fixed controls. The support constructor and SymPy backend are shared;
the original characteristic-polynomial helper is not imported. There is no
parameter scan, new finite exponent base, floating-point eigenvalue calculation
or Lean verification. The integer classification still retains its historical
finite inputs and the balanced-interval corollary keeps its stated scope.
