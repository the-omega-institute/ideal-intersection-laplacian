# Direct verification of the displayed largest-root coefficients

The final three-prime classification uses the written largest-root interval
and the two small middle-gap brackets in Theorem 8.1 and Lemma 8.2 of the
focused manuscript. The new checker independently reconstructs
`det(x I-C)` from the set-disjointness quotient by a symbolic determinant,
rather than importing the original characteristic-polynomial helper.
It verifies the generic polynomial Schur identity and the lower endpoint
factorization, then parses the actual LaTeX tables in
`paper/sections/largest-root-identities.tex`.

All 9 lower rows (36 coefficients), 25 upper rows (170 coefficients)
and six small-gap vectors (41 coefficients) agree exactly with the
reconstructed polynomials. Their constants are 1404 and 513220, and all
247 displayed coefficients are strictly positive. The checker also verifies
the positive polynomial lower bounds for the two Schur diagonal entries,
the small-gap anchor above the middle exponent, and inclusion of the same
tables in both manuscript builds.

The mathematical root-location argument remains the written one. At the
upper endpoint the pair-support block is positive definite; the two
positive Schur diagonal lower bounds make its two-by-two principal block
positive definite. The positive full determinant makes the remaining
scalar Schur complement positive. At the lower endpoint the negative
determinant forces an eigenvalue above it. Hence the largest root lies
strictly between the consecutive endpoints. For each small gap, the
three disjoint root intervals exhaust the cubic's degree, so its sole
root above the middle exponent is in the specified open unit interval.

Run from the repository root with Python 3.10 or later and SymPy 1.14.0:

```sh
python3 scripts/verify_largest_root_coefficients.py
```

The saved output is `results/largest-root-coefficient-verification.json`.
This checks the current manuscript tables, not just an archived result.
It shares the mathematical support model and SymPy backend with other
checks; independence refers to the determinant reconstruction and source
table comparison. There is no parameter scan, historical finite-base
rerun, expanded graph calculation or Lean run. The original revision-pinned
checker and its seven fixed spectral controls retain their separate scope.
