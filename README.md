# Laplacian integrality of ideal intersection graphs

Public workspace for the follow-on collaboration between **Haobo Ma,
Reza Nikandish and Wenlin Zhang**, studying ideal intersection graphs of
`Z_n` and their Laplacian spectra.

Our first question is the **Laplacian integrality characterization**:
which graphs in this family have only integer Laplacian eigenvalues?
This is a new research track; no complete characterization is claimed here.

## Start here

| What you want | Where to go |
| --- | --- |
| Understand the first task and current status | [Research plan](RESEARCH-PLAN.md) |
| Read the requested (a,a,b) diagnostic and fixed-a theorem | [Exact diagnostic and proof](notes/aa-b-diagnostic.md) |
| Read the earlier squarefree and infinite-family contributions | [PR #2](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/2) |
| Discuss a conjecture or share a checked argument | [Project issues](https://github.com/the-omega-institute/ideal-intersection-laplacian/issues) |
| Review proposed additions | [Pull requests](https://github.com/the-omega-institute/ideal-intersection-laplacian/pulls) |
| Read the previous joint paper | [Binary subspace orthogonality project](https://github.com/the-omega-institute/binary-subspace-orthogonality) |

## Current status

We have agreed to start with Q3, the integrality question proposed by Reza.
The graph convention has been reviewed, and the first proofs are in PR #2.
Reza's diagnostic request now has exact output for all 90 requested pairs.
A factor-pair argument proves nonintegrality for every `(a,a,b)` with
`a=2,3,4` and `b>=1`; the full characterization remains open.
For every `a>=1`, all `b>(a-1)(2a-1)` are also covered by the general
discriminant bound; Reza's earlier theorem covers equality for `a>=2`.
A congruence sharpens the remaining range to `b <= floor(R(a))`, with
`R(a)=2(a-1)(a-2)/(a+2)` for even `a` and
`R(a)=(2a-3)(4a-3)/(2(a+3))` for odd `a`. Every larger `b` is nonintegral;
read the linear cutoff proof in the note above.

The original preprint is awaiting public announcement. This repository begins
with public project navigation and the agreed research plan. Its confidential
PDF, correspondence and unannounced manuscript content are kept outside the
public repository. A public source link can be added when available.

## How we work

We use short cycles of conjecture, proof or counterexample, and independent
verification. Each contribution states its assumptions and separates written
proofs, exact finite computations and Lean verification.

The initial work is to fix the graph convention and spectral reduction,
then develop the integrality argument. Vertex connectivity may become a
companion result if it fits naturally; other invariants and unequal-exponent
matrix questions remain later directions.

Use one focused pull request for each checked contribution, with a readable
explanation and reproducible evidence where relevant. Existing collaborator
edits are preserved. See [rights and provenance](RIGHTS.md).
