# Three-prime classification manuscript and supporting material

The [26-page main manuscript](../paper/classification-core.pdf) makes
the completed three-prime classification the central result. It preserves
the proof chain and its finite dependencies while setting aside the
auxiliary arithmetic and higher-prime results. Reza Nikandish's
[coauthor review](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/9#issuecomment-6001734445)
endorses this organization and the retained evidence. The user has delegated
the structure decision; we select the focused classification as the main-paper
direction. The full collection is supporting research material, with no second
submission inferred. The alphabetical author order and Reza Nikandish as
corresponding author are now agreed; the confirmed tool uses are included
for a final coauthor wording review. Final title, venue, disclosure wording,
freeze and submission arrangements still require the coauthors' confirmation.

The existing `paper/paper.tex`, every original section source and
`paper/paper.pdf` are untouched. The default PDF remains 61 pages and the
previous optional detailed build remains 67 pages. The new candidate is
35 pages shorter than the default, with the same 11pt font, one-inch
margins and article layout. It revises the earlier 25-page candidate with
the confirmed author arrangement, tool-use declaration, precise proof
roadmap, real-weight interpretation and quotient-transfer explanation.
The essential evidence remains summarized in Appendix A, with complete
coefficient/base appendices in B and C.
The page count is a measured consequence of the selected scope, not a journal
page limit or a substitute for mathematical review.

## The retained route

The following numbers are read from the compiled candidate. The old
numbers refer to the original manuscript proof sources at `7be8459`,
which are still unchanged at the candidate's base `0806533`.

| Input | Original | Candidate | Role |
| --- | --- | --- | --- |
| Universal-vertex lift | Lemma 2.1 | Lemma 2.1 | Transfers every nonzero support eigenvalue |
| Repeated entries | Theorem 7.1 | Theorem 3.7 | Settles every `(a,a,b)` |
| Minimum through seven | Corollary 11.4 | Corollary 5.1 | Retains the complete 27,562-triple base |
| Uniform positive root below three | Theorem 12.2 | Theorem 5.3 | Forces an integer root to be one or two |
| Endpoint-one sum bound | Part of Theorem 14.2 | Part of Theorem 6.1 | Gives `b+c>=2a^2-2a+1` |
| Endpoint-two completion | Theorem 14.8 | Theorem 7.2 | Retains the complete 8,658-triple base |
| Largest-root unit interval | Theorem 16.1 | Theorem 8.1 | Supplies a noninteger root when `b-a>=3` |
| Endpoint-one gaps one and two | Lemma 16.2 | Lemma 8.2 | Excludes integer `c>b` in the two remaining gaps |
| Global classification | Theorem 16.3 | Theorem 8.3 | Assembles all positive exponent triples |

The repeated-entry section retains the full boundary proof supplied by
Reza Nikandish, the factor-pair and factor-index reductions, all first
three index cases, and the uniform cubic interval. The small-minimum
section retains the six-support quotient, unit/minimum-two proofs,
uniform cutoff and the complete 325-pair minimum-three input. The
27,562-triple certificate follows these inputs; it is not replaced by
a statement about a few small examples.

The symmetric Schur construction remains available before its uniform
comparison at three. The endpoint-one theorem is retained in full,
including its spectral-separation proof, so that the symmetric quotient
and the required sum comparison are explicit. Endpoint two retains the
whole rectangle proof, the real `(4,5)` interval argument and all smaller
finite inputs. Its 84/44/112 coefficient vectors and every base count
remain in Appendix B. Appendix C retains all 36/170 largest-root terms
and the six small-gap sign vectors.

For `8<=a<b<c`, a hypothetical integral spectrum therefore forces a
positive low quotient root to be one or two. Theorem 7.2 excludes two.
At one, gaps one and two are excluded by Lemma 8.2. Every larger middle
gap has `c>a^2-a` by Theorem 6.1; Theorem 8.1 then puts the largest root
between the consecutive integers `bc+a+b+c` and `bc+a+b+c+1`.
This is the same mathematical assembly as the original classification.

## Material outside this candidate

All these sources remain in the original manuscript or the supporting
research branch. The table records their selected placement; it does not
designate the supporting collection as an approved companion paper.

| Material | Current source | Placement and reason |
| --- | --- | --- |
| Squarefree composite classification | `squarefree.tex` | Supporting result; the candidate proves only the three-prime classification |
| Three successive repeated-family cutoffs; fixed-small-a results | Parts of `aa-bounds.tex`; `aa-small.tex` | Supporting refinements; their needed factor-index arguments are retained in the candidate |
| Four bounded-gap families and balanced-region corollaries | Parts of `low-spectrum.tex`, `mixed-inertia.tex` | Supporting spectral consequences; the needed Schur construction and low-root proof remain |
| Gcd, all-odd and common 2-adic valuation exclusions | `arithmetic-obstructions.tex` | Supporting arithmetic; not invoked in the completed core |
| Mixed residue classes and successive root shifts | `mixed-parity-congruence.tex`, `two-adic-lifting.tex` | Supporting arithmetic; endpoint classification no longer needs these filters |
| Modulo-five and local equality-cubic splitting, including prime thirteen | `mod-five-splitting.tex` | Supporting local arithmetic; not a global classification dependency |
| Earlier linear endpoint bound, middle-at-most-fifteen certificate and modulo-three tests | `endpoint-reduction.tex`, `endpoint-details.tex` | Supporting earlier reductions; the stronger rectangle and completion proofs remain in the candidate |
| Residual quartic divisor/reciprocal windows, equality-curve geometry and equality spectrum | Later parts of `endpoint-one-spectrum.tex`, `open.tex` | Supporting arithmetic/spectral questions independent of global nonintegrality |
| Arbitrary-prime-count Rayleigh families and four-prime pairs two/three | Later parts of `unit-exponent.tex` | Supporting higher-prime results; no new expansion is added this round |
| Four-prime pair four | PR9 `2e7d022`, `notes/four-prime-pair-four.md` | Remains in the supporting package, as discussed in Reza's comment |
| Full historical checker catalogue | `verification.tex`, `verification-details.tex` | Supporting reproducibility record; candidate Appendix A summarizes the dependencies it actually uses |

The original manuscript remains the full collection, so it can still be
read and reviewed alongside the main article. A polished companion document
is a separate possible editorial step if the coauthors identify a coherent
additional contribution. The higher-prime nonsquarefree classification remains
open, including the currently unclosed four-prime case `(2,3,4,5)`.

## Editorial direction

The working title is *Laplacian nonintegrality of three-prime ideal
intersection graphs*. It identifies the proved domain without implying
the general higher-prime classification. The title and venue can be adapted
to the corresponding coauthor's preference. JAC and EJC were mentioned in
the collaboration discussion; no specific expansion of EJC or journal
page limit is assumed here.

Keep the finite-domain summaries and full coefficient appendices with the
main article for referee access. The repository remains the reproducibility
package for exact checker sources and complete finite rows. Auxiliary
congruence refinements, equality-curve geometry and the four-prime pair-four
theorem do not lengthen the classification argument. A separate companion
should be assessed on its own mathematical contribution rather than created
solely to accommodate material removed from the main article.

## Source concordance and validation

`paper/core/body.tex` is assembled from explicitly selected contiguous
source spans by `scripts/check_classification_core.py`. This avoids silent
proof edits during rearrangement. The saved
[source receipt](../results/classification-core-source-review.json)
records the source files, line intervals and SHA256 hashes, plus the
shared coefficient appendices. It verifies that all 23 proof bodies and
23 theorem/lemma/proposition/corollary bodies selected for the candidate
are byte-identical to the original sources; the statements comprise
11 theorems, six lemmas, four propositions and two corollaries.
All explicit `ref`/`eqref` targets and all 18 bibliography entries/citations
resolve. The receipt is a source-integrity and explicit-reference check;
it is not an independent mathematical proof audit or a transitive
dependency theorem.

The selected dependencies were also read in their new order: the factor
indices, small-minimum reduction, Schur construction, both endpoint
arguments and final classification have their required definitions,
hypotheses, finite inputs and coefficient vectors present. No new
mathematical theorem or certificate-free replacement is claimed.

The manuscript builds with pdfTeX/TeX Live 2026 without LaTeX warnings,
undefined references or overfull/underfull boxes. All 26 pages were
rendered and visually inspected, including the classification page and
dense coefficient tables. The original default PDF retains SHA256
`f2b3a845f3e04879943471c21eaa556dfddf81dd54e1568db6be09156508aa3f`.
The historical finite certificates were not rerun; no new exponent scan,
floating-point eigensolver or Lean validation was performed.

From the repository root, check the committed fragments and receipt:

```sh
python3 scripts/check_classification_core.py
```

From `paper/`, compile the main classification manuscript without replacing
the supporting collection PDF:

```sh
pdflatex -interaction=nonstopmode -halt-on-error classification-core.tex
pdflatex -interaction=nonstopmode -halt-on-error classification-core.tex
```

The generator's `--emit-patch` mode emits an explicit initial or update
patch for the fragments and receipt. Editorial explanatory paragraphs
are kept outside the preserved statement and proof bodies. Future source
revisions must update the source selections and receipt together; the normal
checking command fails on a mismatch instead of silently refreshing files.

The [certificate manifest](classification-certificate-manifest.md) gives
the fixed source/data revisions, hashes and expected results. Fresh symbolic
checks in `scripts/check_classification_transfer.py` verify the weighted
energy identity, complement identity and both repeated-entry embeddings
used by the added explanations. No historical finite base was rerun for
this revision. The external model review's reported recalculations are
not counted as independently reproduced repository evidence.
