# Exact inputs for the three-prime classification

The [machine-readable manifest](../results/classification-certificate-manifest.json)
records the theorem, exact domain, predicate, full Git revision, source and
data filenames, SHA256 hashes, command and expected result for every entry
below. This connects the focused manuscript to the historical evidence without
requiring a referee to infer which revision contains a supporting checker.

| Main-paper input | Fixed revision | Exact evidence |
| --- | --- | --- |
| Boundary family, Theorem 3.2 | [afe3999](https://github.com/the-omega-institute/ideal-intersection-laplacian/tree/afe3999071b81a71cb5aa559053b649b721929dc) | Written boundary identities and the separate minimum-two modular exception |
| Repeated completion, Theorem 3.7 | Same revision | Complete divisors of 24, 108, 320; eight root-free cubic certificates; later-index written interval |
| Minimum three, Theorem 4.4 | Same revision | All 325 pairs; endpoint-one signs 257 positive, 68 negative, no zeros; written endpoint-two regions and one rational/Sturm exception |
| Minima four through seven, Corollary 5.1 | Same revision | All 27,562 CSV rows; separate integer Sylvester/Bareiss discriminants and strict square brackets |
| Endpoint-two rectangle, Lemma 7.1 | [4afe151](https://github.com/the-omega-institute/ideal-intersection-laplacian/tree/4afe151e1dc7193e6776cc1b08d3606aa804238e) | Full 84-term residual and two nonnegative square expressions |
| Endpoint-two completion, Theorem 7.2 | Same endpoint-two revision | Full 44/112-term identities; all 8,658 finite rows with Horner/Bareiss agreement and no zeros |
| Largest root and small gaps, Theorem 8.1/Lemma 8.2 | [4471a5b](https://github.com/the-omega-institute/ideal-intersection-laplacian/tree/4471a5b4a02d97d3dcf78ea004298d5592924a95) | Full 36/170-term identities, Schur identity, all six small-gap sign vectors |

Use Python 3.10 or later and SymPy 1.14.0. Run each command from the root
of its exact revision checkout. For example, create three detached checkouts
from a clone of this repository:

```sh
git worktree add --detach /tmp/ideal-classification-inputs afe3999071b81a71cb5aa559053b649b721929dc
git worktree add --detach /tmp/ideal-endpoint-two-inputs 4afe151e1dc7193e6776cc1b08d3606aa804238e
git worktree add --detach /tmp/ideal-largest-root-inputs 4471a5b4a02d97d3dcf78ea004298d5592924a95
```

In the classification-input checkout, run:

```sh
python3 scripts/check_repeated_exponent_family.py
python3 scripts/check_repeated_exponent_completion.py
python3 scripts/check_distinct_tail.py
python3 scripts/check_open_region_certificate.py
```

The minimum-three finite input now also has a
[standalone independent check](minimum-three-independent-verification.md)
in the focused manuscript checkout:

```sh
python3 scripts/verify_minimum_three.py
```

It requires Python's standard library only and reconstructs all 325
characteristic polynomials by integer determinants and exact interpolation,
checking their strict root intervals and graph lifts against the archived
rows. This check has been run; its result is in
`results/minimum-three-independent-verification.json`. The two larger
historical finite bases were not rerun in this addition.

In the endpoint-two checkout, run:

```sh
python3 scripts/check_endpoint_two_sharp_maximum.py
python3 scripts/check_endpoint_two_completion.py
python3 scripts/check_endpoint_two_completion.py --csv > /tmp/ideal-endpoint-two-reproduced.csv
```

The last command regenerates the complete CSV; compare it with the pinned
`results/endpoint-two-completion-base.csv`. The strict integer upper cutoff
is `(9*a-33)//4`; the zero-row minimum-eight case is part of the complete
per-minimum counts. A repeated control such as `(10,10,12)` is assigned to
the repeated theorem, not to the fully distinct finite base or the
minimum-forty real tail.

In the largest-root checkout, run:

```sh
python3 scripts/check_largest_root_unit_interval.py
```

The source/data SHA256 values bind each file to its revision. A successful
checking command establishes its stated identities or finite predicates;
the classification additionally uses the written reductions in the paper.
Integer Horner evaluation, integer Bareiss determinants and symbolic
characteristic-polynomial calculations are distinct algorithms, but some
share the same displayed quotient/helper and SymPy. Their agreement should
be described with those shared inputs made explicit. The previously recorded
full and smaller-input audits retain their own validation scopes.

This manifest was constructed by reading the pinned Git blobs and parsing
the checker sources. It does not represent a fresh rerun of the historical
finite bases. The pinned endpoint-two checker parses successfully: the
apparent split scope string seen in browser rendering is not a literal
Python syntax defect. The separate GPT Pro review reported additional
computations, but its executable artifacts have not been retrieved here;
those reports are not substituted for the repository's certificates.
