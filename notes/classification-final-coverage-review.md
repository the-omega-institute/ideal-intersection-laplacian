# Final case coverage of the three-prime manuscript

This review reads the focused manuscript at `1c467a59457c0384f4903e4225e8d5070c68631e`
after the October 10 proof strengthenings. The main PDF is 27 pages and the
supporting PDF is 63 pages. It checks the final case assembly, eigenvalue
transfer and exact archived finite domains. It establishes no new theorem
and does not replace the component proofs or their determinant computations.

## Transfer and the final alternatives

For integer exponents, put `N=a+b+c+ab+ac+bc` and `u=abc-1`. The complement
quotient satisfies `B+C=N I-1 w^T`, with `w^T C=0`. A nonzero quotient root
`mu` reflects to `N-mu` on the graph with the universal class removed. If
`mu` is noninteger, then `N-mu` is nonzero; Lemma 2.1 lifts it to
`N+u-mu`, also noninteger. Conversely, an integral full graph spectrum
forces every nonzero complement quotient root to be integral: `mu=N` is
already an integer, and every other root has this lift. The integer-root
alternative in Theorem 8.3 therefore respects the join lemma's nonzero
hypothesis, including the exceptional value where reflection gives zero.

Sort the positive integer exponents. These branches exhaust them.

| Branch | Required current input | Conclusion |
| --- | --- | --- |
| Any repeated entries | Theorem 3.7, including its boundary and factor-index subproofs | A noninteger graph eigenvalue |
| Fully distinct, minimum at most seven | Corollary 5.1 and its unit/minimum-two/minimum-three dependencies | A noninteger graph eigenvalue |
| `8<=a<b<c` | Theorem 5.3 gives a positive quotient root in `(0,3)` | An integral graph spectrum forces root one or two |
| Root two | Theorem 7.2 | Nonintegrality using its finite base and real tail |
| Root one and `b-a=1` or `2` | Lemma 8.2 | The unique endpoint-one zero above `b` lies between consecutive integer anchors, contradicting integer `c` |
| Root one and `b-a>=3` | Sum-bound part of Theorem 6.1, then Theorem 8.1 | A quotient root in `(bc+a+b+c,bc+a+b+c+1)` |

In the last branch, `b+c>=2a^2-2a+1` and `c>=b` imply
`c>=a^2-a+1/2>a^2-a`. This supplies Theorem 8.1's remaining hypothesis.
The classification branch has `a>=8`, the sum bound needs `a>=2`, and
the largest-root theorem needs `a>=2`, `b-a>=3` and `c>=a^2-a`.
The residual separation with cutoff `a>2+sqrt(3)` remains in Theorem 6.1;
the final implication uses only the sum bound. No equality-curve enumeration
or four-prime result is used.

## The three finite domains

| Input | Exact ordered integer domain | Archived rows |
| --- | --- | --- |
| Minimum three, Theorem 4.4 | `a=3`, `4<=b<c<30` | 325 |
| Minima four through seven, Corollary 5.1 | `4<=a<=7`, `a<b<c<4a^2-2a` | 27,562 |
| Endpoint two, Theorem 7.2 | `8<=a<=39`, `a<b<2a-2`, `b<c<9a/4-8` | 8,658 |

For minima four through seven, the fixed-`a` count is
`binomial(4a^2-3a-1,2)`, giving 1,275; 3,486; 7,750; and 15,051.
The strict boundary `c<4a^2-2a` complements the written cutoff
`c>=4a^2-2a`, so no integer boundary is omitted.

For endpoint two, the largest integer `c` is `(9a-33)//4`, from the
strict rational bound. With `C=(9a-33)//4`, `B=min(2a-3,C-1)` and
`n=max(0,B-a)`, the count is `n*C-n*(a+1+B)/2`. The 32 minima include
the zero-row case `a=8`. At `a>=40`, written positive-coefficient identities
give a root in `(4,5)` on the zero surface. Minima at most seven and
repeated triples use their earlier theorems. The finite base is neither a
scan of all endpoint-zero triples nor the entire endpoint-two proof.

The fresh archived-row audit compared every ordered tuple against these
exact domains, including order, uniqueness and exhaustion. All 325 JSON
cases, 27,562 discriminant CSV rows and 8,658 endpoint-two CSV rows match.
The endpoint-two CSV was read directly from public revision
`4afe151e1dc7193e6776cc1b08d3606aa804238e`. The stored discriminants obey
their strict consecutive-square brackets. The stored endpoint values are
nonzero, agree with half the stored Bareiss determinants, and have minimum
absolute value 8,208.

These checks validate domain coverage and relations between stored data.
They do not freshly reconstruct characteristic polynomials, discriminants
or endpoint determinants. The earlier reconstruction certificates remain
essential. The separate minimum-three independent checker was already run
earlier and was not rerun here. The [fixed input manifest](classification-certificate-manifest.md)
provides commands, algorithms, revisions and shared-input limits.

## Later real-domain refinements

The strengthened hypotheses have their own written proofs and targeted
exact checks; the older manifest checker alone verifies its pinned statement.

| Current refinement | Proof and exact-check note | Role in classification |
| --- | --- | --- |
| Positive root below three for all ordered positive reals; constant three optimal | [Uniform low root](uniform-low-root-positive.md) | Used at integer minimum at least eight |
| Endpoint-one sum bound at real minimum two | [Sum bound](endpoint-one-sum-bound.md) | Supplies the largest-root cutoff |
| Residual separation for `a>2+sqrt(3)` | [Sharp residual cutoff](residual-spectrum-sharp-cutoff.md) | Retained theorem; final assembly uses only the sum bound |
| Endpoint-two middle bound for `a>(7+sqrt(13))/3` | [Sharp middle cutoff](endpoint-two-middle-sharp-cutoff.md) | Integer minimum-four and maximum-bound minimum-eight scopes retained |
| Endpoint-one small gaps at real minimum two | [Small-gap brackets](endpoint-one-small-gap-strengthening.md) | Applied to the two integer gap cases |
| Largest-root interval at real minimum two | [Largest-root strengthening](largest-root-minimum-two.md) | Applied to the remaining integer gap case |

Supporting balanced-span, equality-surface and zero-Schur-diagonal refinements
add no dependency to Theorem 8.3. Their hypotheses remain as stated in their
notes. In particular, the zero-diagonal inertia lemma retains `0<x<a`;
completion at `x=a` is not required by the classification.

Fresh runs of `scripts/check_classification_transfer.py` and
`scripts/check_classification_core.py` passed: the first checks symbolic
energy/complement/embedding identities, and the second checks current source
concordance and explicit reference/citation closure. Neither independently
proves the global theorem. This review does not rebuild a PDF, add a finite
base, use floating-point eigenvalues, run Lean or perform a new Oracle review.
Journal, title, metadata, final disclosure and submission arrangements remain
for the coauthors.
