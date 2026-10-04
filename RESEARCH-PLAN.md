# First task: Laplacian integrality

**Status:** graph convention reviewed; the [working manuscript](paper/paper.tex)
consolidates the squarefree classification, `(1,1,k)`, Reza's boundary family,
the successive linear cutoffs, all `(a,a,b)` with `a,b>=1`, and all
`(1,b,c)` and `(2,b,c)` with `b,c>=1`.
The corrected repeated-exponent diagnostic and exact certificates remain
available. Full Q3 remains open.

Read [the exact diagnostic and finite-reduction proof](notes/aa-b-diagnostic.md).
With SymPy 1.14.0, reproduce the requested output using:

```sh
python3 scripts/check_aa_b.py
python3 scripts/check_aa_b.py --json
python3 scripts/check_fixed_repeated_exponents.py
python3 scripts/check_second_cutoff.py
python3 scripts/check_factor_index_reduction.py
python3 scripts/check_repeated_exponent_completion.py
python3 scripts/check_six_support_quotient.py
python3 scripts/check_fully_distinct.py
python3 scripts/check_minimum_two.py
```

The [completion proof](notes/repeated-exponent-completion.md) settles the
remaining factor indices using a uniform cubic sign interval. The next
focused question is the six-support quotient for three pairwise distinct
exponents all at least3. The [complement interval proof](notes/one-unit-exponent.md)
and [positive expansions](notes/minimum-two.md) now settle every triple
with minimum exponent at most2. Derive an exact obstruction for a stated subfamily;
the coordinate-swap decomposition is specific to repeated exponents.
Do not replace the open classification by an arbitrary finite scan.

Reza proposes the Laplacian integrality question, Q3 in his
[public source preprint](https://doi.org/10.5281/zenodo.23134979),
as the first follow-on task.

## First deliverable

The first note fixes the graph definition and Laplacian convention, gives
the squarefree classification and an unequal-exponent infinite family, and
includes a public reference for the originating graph. Reza's source
preprint is now linked via its verified Zenodo DOI.

Read [Reza's integrated extension](notes/repeated-exponent-family.md).
Next, address exponent triples outside the two proved families and nonsquarefree
vectors with more prime factors. The `(2,2,3)` example has an integral
antisymmetric block but a nonintegral remaining block, so a general proof
must handle this distinction. Use small, exact checks to diagnose stated
conjectures; numerical approximations do not establish integrality.

## Reproduce the checks

The infinite-family block checker uses Python 3.10 or later and its standard
library:

```sh
python3 scripts/check_integrality_obstructions.py
```

For the exact `(2,2,3)` characteristic-polynomial diagnostic, install the
pinned SymPy dependency in your own environment:

```sh
python3 -m pip install -r requirements-verification.txt
python3 scripts/check_remaining_case.py
python3 scripts/check_repeated_exponent_family.py
```

Compare outputs with `results/integrality-obstructions.json` and
`results/remaining-case-2-2-3.json` and `results/repeated-exponent-family.json`.
The new checker also verifies exact polynomial identities; its direct graph
checks cover 34, 174 and 548 vertices. These are finite independent checks;
the infinite-family claims use the written proofs. No Lean run is reported.

## Contribution checklist

1. State the graph convention, hypotheses and result.
2. Provide the readable proof, or clearly label the finite scope of a computation.
3. Record exact input identities, commands and verification range.
4. Give the source and attribution for existing results.
5. Identify the unresolved step and next mathematical question.

If Lean is used, record its toolchain, dependency revision and theorem axioms.
Select the execution machine and check available resources before a run.
Independent finite checks and formal verification retain separate scopes.

## Later directions

Vertex connectivity may accompany Q3 if the arguments connect naturally.
Other spectral invariants and the unequal-exponent matrix problem remain
separate follow-ups.

The source manuscript is linked rather than copied into this repository.
Attribute its earlier spectral results and keep its reported computations
separate from our independently checked claims.

[Return to the project entrance](README.md).
