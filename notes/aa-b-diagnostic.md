# Repeated exponents: exact diagnostics and three complete fixed-exponent families

**Theorem.** For $a\in\{2,3,4\}$, every $b\geq1$, and distinct primes
$p,q,r$, the ideal intersection graph of $p^a q^a r^b$ is not Laplacian integral.

This extends the requested diagnostic range $b=1,\ldots,30$ to every positive
$b$ for these three values of $a$. The argument reduces an infinite parameter
range to a complete finite list of possible square discriminants. The
classification with arbitrary exponents remains open.

The graph uses nonzero proper ideals, adjacency by nonzero intersection, and
$L=D-A$. Reza Nikandish supplied the general repeated-exponent quotient and
asked for the diagnostic in
[PR #3](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/3#issuecomment-5977353331).
The [integrated quotient proof](https://github.com/the-omega-institute/ideal-intersection-laplacian/blob/f1284407b418979e8d3973805c85518489cab201/notes/repeated-exponent-family.md)
fixes the two invariant blocks and the shift by $u=a^2b-1$ universal vertices.

## The requested 90 cases

The corrected [diagnostic](../scripts/check_aa_b.py) gives:

| $a$ | Range of $b$ | Cubics with noninteger roots | Certified consecutive-integer intervals | Reducible cubics |
| --- | --- | --- | --- | --- |
| 2 | 1–30 | 30/30 | 30/30 | $b=2,6$ |
| 3 | 1–30 | 30/30 | 30/30 | $b=3,12$ |
| 4 | 1–30 | 30/30 | 30/30 | $b=4,20$ |

Each reducible cubic has one linear and one irreducible quadratic factor.
All other tested cubics are irreducible and have an irreducibility witness
among the tested primes $2,3,5,7,11,13,17,19,23,29,31$.
See [the full text output](../results/aa-b-diagnostic.txt) and
[exact rational isolating intervals](../results/aa-b-diagnostic.json).

No prime makes all these cubics irreducible modulo that prime. This is a
structural obstruction, not a search-limit issue. In fact, for every $a\geq1$,

$$f_{a,a}(x)=(x-2a(a+1))
\bigl(x^2-(5a^2+2a)x+6a^4+3a^3\bigr).$$

Both factors remain monic of positive degree after reduction modulo any
prime. Thus the tested diagonal cases already rule out a uniform
whole-cubic irreducibility witness. A second general reducible family is

$$f_{a,a(a+1)}(x)=(x-2a(a+1)^2)
\bigl(x^2-(3a^3+4a^2+2a)x+2a^6+6a^5+7a^4+3a^3\bigr).$$

A noninteger root does not require the entire cubic to be irreducible.

## Finite reduction for each fixed repeated exponent

After removing the universal vertices, the antisymmetric block is

$$B_- =\begin{pmatrix}a^2+ab&-ab\\-a&a^2+a+b+2ab\end{pmatrix}.$$

Its discriminant is

$$D=(a+1)^2b^2+2a(3a+1)b+a^2.$$

If $D$ is not a square, this block has irrational eigenvalues, which remain
irrational after the integer shift $u$. Therefore it suffices to examine the
positive integers $b$ for which $D$ is a square.

Put $A=(a+1)^2b+a(3a+1)$. The identity

$$A^2-(a+1)^2D=4a^3(2a+1)$$

turns the square condition $D=s^2$ into

$$\ell r=4a^3(2a+1),\qquad
\ell=A-(a+1)s,\quad r=A+(a+1)s.$$

Since the product is positive and $A>0$, both $\ell,r$ are positive. Choose
$s\geq0$, so $\ell\leq r$. Conversely, a positive factor pair produces an
admissible square discriminant exactly when

$$\ell\equiv r\pmod2,\qquad
b=\frac{(\ell+r)/2-a(3a+1)}{(a+1)^2}\in\mathbb Z_{\geq1},\qquad
s=\frac{r-\ell}{2(a+1)}\in\mathbb Z_{\geq0}.$$

This is an exact finite arithmetic criterion for every fixed $a$, with no
bound on $b$. Enumerating the divisors of the three small constants gives:

| $a$ | $4a^3(2a+1)$ | Admissible $(\ell,r)$ | Exceptional $b$ | $\sqrt D$ |
| --- | --- | --- | --- | --- |
| 2 | 160 | $(2,80)$ | 3 | 13 |
| 3 | 756 | $(2,378)$ | 10 | 47 |
| 4 | 2304 | $(12,192)$ | 2 | 18 |
| 4 | 2304 | $(2,1152)$ | 21 | 115 |

The [finite-reduction checker](../scripts/check_fixed_repeated_exponents.py)
records every candidate factor pair and its admissibility, rather than
sampling a range of $b$.

## The four exceptional cubics

For those four pairs, the symmetric quotient supplies a noninteger root:

| $(a,b)$ | Cubic $f_{a,b}(x)$ | Prime with no root modulo that prime |
| --- | --- | --- |
| $(2,3)$ | $x^3-47x^2+702x-3312$ | 5 |
| $(3,10)$ | $x^3-187x^2+11220x-214200$ | 13 |
| $(4,2)$ | $x^3-86x^2+2304x-18816$ | 5 |
| $(4,21)$ | $x^3-485x^2+75492x-3721536$ | 5 |

Each monic cubic has no root over the indicated finite field and is therefore
irreducible over $\mathbb Q$. Its roots are real because the quotient is
similar to a symmetric matrix. They are nonzero because its constant term is
nonzero. Their shifts by $u$ are noninteger eigenvalues of the original graph.
Together with the nonsquare-discriminant case, this proves the theorem.

Three exceptions belong to Reza's earlier infinite family
$b=(a-1)(2a-1)$; the new factor-pair reduction shows that only one further
exception, $(4,2)$, is required to cover all $b$ for $a=2,3,4$.

## Verification scope and next question

The requested diagnostic initially stopped because the return values of
SymPy's `factor_list` were reversed. The revision fixes that error, uses
exact root isolation instead of a floating-point proximity test, and labels
the prime search as restricted to the displayed tested primes. It also
corrects the cubic test to a sufficient condition: integrality of the cubic
alone does not settle the antisymmetric block or the whole graph.

The finite-reduction checker independently reconstructs the symbolic cubic
from the four-cell quotient, verifies the discriminant factor-pair identity
and both general cubic factorizations, and certifies all factor pairs and
modular witnesses for $a=2,3,4$.
The [result](../results/fixed-repeated-exponents.json) records the source hash.
These are exact algebraic and arithmetic checks, with no numerical spectrum
or Lean verification.

The next focused task is to control the symmetric cubic on all admissible
factor pairs for arbitrary $a$. The factor-pair criterion eliminates an
unbounded search in $b$ for each fixed $a$, but does not settle arbitrary $a$
or triples with three distinct exponents.
