# An infinite family extending the (2,2,3) obstruction

**Theorem.** Let $a\geq2$, put $c=(a-1)(2a-1)$, and let $p,q,r$ be
distinct primes. The ideal intersection graph of $n=p^a q^a r^c$ has a
noninteger Laplacian eigenvalue. Its two-dimensional antisymmetric block
has integer eigenvalues, while its symmetric block supplies the obstruction.

Reza Nikandish supplied this theorem and its proof in
[the public PR discussion](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/2#issuecomment-5977154129).
This note integrates his argument with the
[earlier definitions and results](integrality-obstructions.md), making the
spectral lifting step explicit. The first exponent triples are $(2,2,3)$,
$(3,3,10)$ and $(4,4,21)$. The general integrality classification remains open.

## Equitable partition and the universal vertices

First allow arbitrary integers $a,c\geq1$. A nonempty support $S$ corresponds
to a clique of size $\prod_{i\in S}k_i$, except that the full support has one
vertex removed for the whole-ring ideal. Two distinct vertices are adjacent
exactly when their supports intersect. Here $(k_1,k_2,k_3)=(a,a,c)$.

The full-support class consists of $u=a^2c-1$ universal vertices. Removing
it gives a graph $H$ on the six supports $1,2,3,12,13,23$, of respective
sizes $a,a,c,a^2,ac,ac$. Swapping coordinates 1 and 2 gives the four cells

$$X=\mathcal C_1\cup\mathcal C_2,\quad Y=\mathcal C_3,\quad
Z=\mathcal C_{12},\quad W=\mathcal C_{13}\cup\mathcal C_{23}.$$

Their sizes are $2a,c,a^2,2ac$. The neighbor counts in $H$ are

| Cell | $X$ | $Y$ | $Z$ | $W$ |
| --- | --- | --- | --- | --- |
| $X$ | $a-1$ | $0$ | $a^2$ | $ac$ |
| $Y$ | $0$ | $c-1$ | $0$ | $2ac$ |
| $Z$ | $2a$ | $0$ | $a^2-1$ | $2ac$ |
| $W$ | $a$ | $c$ | $a^2$ | $2ac-1$ |

These counts depend on the cell, not the vertex, so the partition is
equitable. Acting on cell-constant functions, $L(H)$ has the quotient

$$B=\begin{pmatrix}
a^2+ac&0&-a^2&-ac\\
0&2ac&0&-2ac\\
-2a&0&2a+2ac&-2ac\\
-a&-c&-a^2&a^2+a+c
\end{pmatrix}.$$

If $T$ assigns a cell value to every vertex, equitability gives $L(H)T=TB$.
With $M=\operatorname{diag}(2a,c,a^2,2ac)$, the matrix $MB$ is symmetric.
Thus $B$ is similar to a real symmetric matrix and has real eigenvalues.

For any nonzero eigenvalue $\lambda$ of $B$, an eigenvector $v$ lifts to
$Tv$, a nonzero eigenvector of $L(H)$. Since $\lambda\ne0$ and Laplacian
row sums vanish, $Tv$ has total sum zero. Extend it by zero on the removed
universal vertices. Every old vertex gains $u$ edges to those vertices;
every universal vertex sees total value zero. Hence the extended vector is
an eigenvector of $L(G_n)$ with eigenvalue $\lambda+u$. This proves the
lifting statement directly, including $u=0$.

## The cubic and a root between consecutive integers

Expansion gives $\det(xI-B)=x f(x)$, where

$$f(x)=x^3-E_1x^2+E_2x-E_3,$$
$$E_1=2a^2+5ac+3a+c,$$
$$E_2=a^4+7a^3c+3a^3+8a^2c^2+11a^2c+2a^2+3ac^2+2ac,$$
$$E_3=2a^2c(a+c+1)(a^2+2ac+2a+c).$$

Since $E_3>0$, each root of $f$ is nonzero, and the preceding lifting
argument applies to all three roots.

Now specialize to $c=(a-1)(2a-1)$. For $a=2$, the cubic is

$$f(x)=x^3-47x^2+702x-3312.$$

Its values modulo 5 at $0,1,2,3,4$ are $3,4,2,3,3$. It has no root in
$\mathbb F_5$, so this monic cubic is irreducible over $\mathbb Q$ and
has no integer root. It is the earlier $(2,2,3)$ obstruction before the
universal-vertex shift: $u=11$ and

$$f(z-11)=z^3-80z^2+2099z-18052.$$

For $a\geq3$, put $n_1=2a^3-2a^2+2a-1$. Exact polynomial identities give

$$f(n_1)=2(5a^4-10a^3+7a^2-1),$$
$$f(n_1-1)=-2(a-1)(a+2)(2a^4-7a^3+7a^2-a-3).$$

The first value is positive, since
$5a^4-10a^3+7a^2-1=5a^3(a-2)+7a^2-1>0$ for $a\geq2$.
For the final factor in the second value, writing $b=a-3\geq0$ gives

$$2a^4-7a^3+7a^2-a-3
=2b^4+17b^3+52b^2+68b+30>0.$$

Thus $f(n_1-1)<0<f(n_1)$. The intermediate value theorem supplies a root
$\lambda\in(n_1-1,n_1)$. After the integer shift $u$, it gives an
eigenvalue of $L(G_n)$ strictly between $n_1-1+u$ and $n_1+u$.
For $a=2$, a real noninteger root likewise lies between its integer floor
and the next integer. This proves the theorem for every $a\geq2$.

## Why the antisymmetric block misses this family

The cell-constant functions with values $s,-s$ on $1,2$ and $t,-t$ on
$13,23$, zero elsewhere, form an invariant subspace for $L(H)$ with matrix

$$B_- =\begin{pmatrix}a^2+ac&-ac\\-a&a^2+a+c+2ac\end{pmatrix}.$$

Its characteristic discriminant is

$$D=(a+1)^2c^2+2a(3a+1)c+a^2.$$

On our family this equals $(2a^3-a^2+a-1)^2$, and the two eigenvalues are

$$4a^3-3a^2+a,\qquad 2a^3-2a^2+1.$$

Both are integers. Their shifts by $u$ remain integers. At $a=2$, they are
$22,9$ for $H$ and $33,20$ for $G_n$, matching the earlier diagnostic.
The cubic in the symmetric block is essential for this infinite family.

## Independent verification

[The exact checker](../scripts/check_repeated_exponent_family.py) verifies
the quotient characteristic polynomial, both sign identities and the
antisymmetric eigenvalues as polynomial identities in SymPy 1.14.0. It
checks the displayed positive-coefficient expansion and the shifted
$(2,2,3)$ cubic.

It separately constructs the original ideal graph from exponent tuples for
$(a,c)=(2,3),(3,10),(4,21)$, giving 34, 174 and 548 vertices. Integer neighbor
counts verify the equitable partition, both invariant blocks, and the
universal-vertex lifting on the nonconstant quotient space. The full
seven-support quotient characteristic polynomial also agrees with the cubic,
antisymmetric block and join factors. These checks do not compute the full
548-by-548 characteristic polynomial or use numerical eigenvalues.

The [saved result](../results/repeated-exponent-family.json) records the
finite cases and checker hash. The infinite result follows from the written
argument; no Lean verification is claimed.
