# Independent polynomial and certificate coverage audit

This audit checks the algebraic identities supporting the completed
three-prime nonintegrality proof. It adds independent verification evidence
to the existing result, without extending the exponent ranges or changing
the classification theorem.

## Determinants reconstructed from the graph

The verifier uses only the Python standard library. It represents
polynomials as integer coefficient dictionaries in the variables m,u,v,
and constructs the complement Laplacian quotient directly from the six
nonempty proper supports 1,2,3,12,13,23. Support weights are a,b,c,ab,ac,bc;
two supports are adjacent precisely when they are disjoint. Each diagonal
is the sum of adjacent support weights, and each off-diagonal entry is
minus the adjacent column weight.

For each determinant it enumerates all 720 Leibniz permutations. Exactly
16 products are nonzero. No characteristic-polynomial formula, Schur
determinant formula, original checker module, symbolic algebra package or
floating-point approximation is used in this reconstruction.

With a=3+m, b=a+3+u, c=a²-a+v and M=bc+a+b+c, the two reconstructed
determinants agree coefficientwise with

```text
det(MI-C) = -M a²bc T,
det((M+1)I-C) = (M+1) P.
```

Here T and P are reconstructed from the complete saved positive tables,
containing 36 and 170 terms. The full determinants contain 225 and 300
terms. Every table coefficient is checked to be a positive integer.
Thus the identities hold in the integer polynomial ring, for all values
of the variables, rather than only at selected exponent triples.

The verifier also independently reconstructs all six small-gap boundary
determinants at x=1: for b=a+d, d=1,2 and a=8+m, it checks the complete
positive vectors for -h_C(1) at c=b and c=L_d, and for h_C(1) at c=L_d+1.
The anchors are L_1=2a²-a-2 and L_2=2a²+a-6. These are another six generic
polynomial identities. Together with the written cubic-root argument,
they support exclusion of integer c>b in the two small-gap cases.

The optional manuscript comparison checks all 34 main coefficient rows
and all six small-gap rows. The saved audit used the Appendix E source at
manuscript revision aeb190caaa6a1dda8ef4e4275bc38b2171ac4081;
its SHA-256 is recorded in the report.

## Historical finite certificates

The audit independently constructs the exact finite domains

```text
4 <= a <= 7, a < b < c < 4a²-2a:                 27,562 triples;
8 <= a <= 39, a < b < 2a-2, b < c < 9a/4-8:     8,658 triples.
```

Both saved CSV files contain exactly those triples with no missing or
duplicate row, and their hashes match the historical manifests. Every
stored discriminant lies strictly between its stored consecutive square
bounds. Every endpoint-two row has a nonzero stored Horner value and a
stored determinant equal to twice that value. The a=8 endpoint-two
subdomain is empty.

These are integrity and coverage checks of the saved historical evidence.
They do not recompute the historical discriminants or determinants;
the original verifiers remain dependencies of the computer-assisted
classification. The separate 108-pair minimum-eight certificate is not
needed by this proof route.

## Reproduction and mathematical scope

From this repository root, run Python without optimization:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_three_prime_completion.py
```

To include the manuscript comparison, add
`--manuscript-table /path/to/paper/sections/largest-root-identities.tex`
from the pinned manuscript revision. The resulting report is saved at
[results/three-prime-independent-audit.json](../results/three-prime-independent-audit.json).

The audit verifies the eight determinant identities and certificate
coverage. The written Schur positive-definiteness proof, cubic-root
geometry, complement/universal-class lifts, repeated-exponent results,
small-minimum reduction and endpoint-two reduction remain explicit
mathematical dependencies; checking determinant signs alone does not
identify the largest eigenvalue. The complete classification remains
computer-assisted, with historical bases of 27,562 and 8,658 triples.
This is not Lean verification. The higher-prime nonsquarefree part of Q3
and the original orthogonality problem at n=7 remain open.
