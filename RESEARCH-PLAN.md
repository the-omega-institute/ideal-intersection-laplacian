# First task: Laplacian integrality

**Status:** graph convention and Q3 scope reviewed. Written nonintegrality
proofs cover all squarefree integers with at least three prime factors and
the exponent families `(1,1,k)` and `(a,a,(a-1)(2a-1))`, `a >= 2`.
Reza has reviewed the first note and supplied the latter extension, now
integrated with independent exact checks. The full general-exponent
characterization remains open.

Read [the mathematical note](notes/integrality-obstructions.md). Independent
integer checks validate the invariant blocks in 14 finite cases. An exact
34-vertex characteristic-polynomial calculation also settles `(2,2,3)` and
shows why a repeated-exponent block alone is insufficient in general.

Reza proposes the Laplacian integrality question, Q3 in his privately shared
preprint on ideal intersection graphs of `Z_n`, as the first follow-on task.

## First deliverable

The first note fixes the graph definition and Laplacian convention, gives
the squarefree classification and an unequal-exponent infinite family, and
includes a public reference for the originating graph. Reza's unannounced
preprint is kept outside the public repository.

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

The confidential source manuscript is not part of this repository. Until a
public reference is available, do not publish its contents or assert its
reported partial results as independently verified.

[Return to the project entrance](README.md).
