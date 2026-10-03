# Laplacian integrality of ideal intersection graphs

Public workspace for the follow-on collaboration between **Haobo Ma,
Reza Nikandish and Wenlin Zhang**, studying ideal intersection graphs of
`Z_n` and their Laplacian spectra.

Our first question is the **Laplacian integrality characterization**:
which graphs in this family have only integer Laplacian eigenvalues?
This is a new research track; no complete characterization is claimed here.

## First results

We prove nonintegrality for every squarefree integer with at least three
distinct prime factors and for every exponent vector that is a permutation
of `(1,1,k)`, `k >= 1`. This completes the squarefree composite classification:
the integral case is exactly two prime factors, including the edgeless graph.
Read [the proofs and exact verification scope](notes/integrality-obstructions.md).
The full characterization for arbitrary exponent vectors remains open.

## Start here

| What you want | Where to go |
| --- | --- |
| Understand the first task and current status | [Research plan](RESEARCH-PLAN.md) |
| Read the first checked contributions | [Nonintegrality proofs](notes/integrality-obstructions.md) |
| Discuss a conjecture or share a checked argument | [Project issues](https://github.com/the-omega-institute/ideal-intersection-laplacian/issues) |
| Review proposed additions | [Pull requests](https://github.com/the-omega-institute/ideal-intersection-laplacian/pulls) |
| Read the previous joint paper | [Binary subspace orthogonality project](https://github.com/the-omega-institute/binary-subspace-orthogonality) |

## Current status

We have agreed to start with Q3, the integrality question proposed by Reza.
The privately shared preprint has been received and reviewed for the graph
definition and Q3 scope. The first follow-on proofs and independent exact
checks are now available above for coauthor review.

The original preprint is awaiting public announcement. This repository begins
with the agreed research plan and our follow-on contributions. Its confidential
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
