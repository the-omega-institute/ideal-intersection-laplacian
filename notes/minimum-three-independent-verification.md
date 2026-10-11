# Exact verification of the minimum-three finite input

Theorem 4.4 of the focused three-prime manuscript reduces the case with
minimum exponent three to the pairs

\[
4\le b<c<30.
\]

The written cutoff covers larger exponents, and the earlier unit,
minimum-two and repeated-exponent theorems cover the other cases. The
remaining set contains exactly 325 pairs. The following check covers that
set without extending the parameter range.

From the six nonempty proper subsets of the three prime indices, give a
support class the weight equal to the product of its exponents. Construct
the complement quotient by putting minus the target weight in each
off-diagonal entry whose two supports are disjoint, and summing those
weights on the diagonal. This construction uses sets directly and does
not import the original quotient helper or checker.

The rows sum to zero. Thus the characteristic polynomial is
\(x h_{3,b,c}(x)\), where \(h\) has degree five. Integer Bareiss
determinants at the six distinct arguments 1 through 6 determine all
coefficients of \(h\) by exact rational interpolation. For every pair,
the recovered coefficients agree with the archived polynomial. Their
constant terms are negative; their endpoint-one values agree with the
cubic displayed in Theorem 4.4.

The endpoint-one counts are 257 positive, 68 negative and no zeros.
The negative ranges agree with the manuscript's complete table. All
257 positive cases have a strict sign change in \((0,1)\). Among the
68 negative cases, 67 have a strict sign change in \((1,2)\); the
remaining case \((3,4,5)\) has

\[
h(1)=-3792,\qquad h(3/2)=48825/32>0.
\]

The rational endpoint is evaluated directly by an integer determinant
of the scaled matrix. All 325 strict root intervals and their reflected
graph-eigenvalue intervals agree with the archived rows. Reflection uses
the manuscript's proved quotient transfer and vertex count
\(V=4(b+1)(c+1)-2\). This check does not enumerate the original graph.

Run from the repository root with Python 3.10 or later; no third-party
package is required:

```sh
python3 scripts/verify_minimum_three.py
```

The program reads `results/distinct-tail.json` and rejects missing,
duplicate or extra rows, coefficient disagreements, endpoint zeros,
failed strict sign changes and incorrect graph lifts. Its expected
summary is saved in
`results/minimum-three-independent-verification.json`.

The fresh run evaluated 2,018 exact Bareiss determinants and checked all
325 coefficient vectors and strict intervals. A separate Leibniz
permutation expansion also agreed with the endpoint-one determinant for
all 325 pairs. The verification shares the mathematical six-support
model and archived input with the original computation, but uses no
SymPy characteristic-polynomial routine or original checker imports.

This reproduces one finite input to the existing theorem. The other
finite bases of 27,562 and 8,658 triples and the written infinite-domain
arguments retain their separate evidence. No new classification theorem
or Lean validation is claimed.
