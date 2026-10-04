# Working manuscript

Read [the PDF](paper.pdf), or edit [paper.tex](paper.tex) and the section
files it includes. This is a growing mathematical draft, not a submission
package. Author metadata and any manuscript disclosure are for joint agreement.

The section names follow Reza's proposed layout. At the time of integration,
his announced `paper/` files were not yet present on any of the three remote
branches. The introduction and open section here are short temporary texts;
`aa-family.tex` is reconstructed from his already public PR #2 proof. His
own versions can be integrated when uploaded, preserving the five expanded
sections and their shared graph/lifting definitions.

| Section | Contents |
| --- | --- |
| [graph.tex](sections/graph.tex) | Ideal encoding, support classes, universal-vertex lift and both repeated-exponent blocks |
| [squarefree.tex](sections/squarefree.tex) | Complete squarefree composite classification, with odd and even tensor arguments |
| [pqrk.tex](sections/pqrk.tex) | Explicit irrational eigenvalues for `(1,1,k)` |
| [aa-family.tex](sections/aa-family.tex) | Reza's public boundary-family proof |
| [aa-bounds.tex](sections/aa-bounds.tex) | Exact divisor criterion, quadratic bound, two linear cutoffs and complete first-factor certificates |
| [aa-small.tex](sections/aa-small.tex) | All-b theorem for a=2,3,4,5,6, divisor/modular certificates and cubic-test scope |
| [verification.tex](sections/verification.tex) | Actual scope of the exact checkers |
| [open.tex](sections/open.tex) | Remaining square-discriminant and unequal-exponent cases |

## Build

From this directory, with a standard TeX installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

## Evidence

The initial notes and checkers are retained from PR #2 at
`f1284407b418979e8d3973805c85518489cab201`; the strengthened diagnostic,
factor certificates and cutoff are retained from PR #3 at
`fd8cffe184c0fff34647299fe6e08cdd1caac442`. The manuscript presents their
proofs in dependency order. No new parameter search or Lean validation is
needed to reproduce this consolidation.

From the repository root, use Python 3.10+ and SymPy 1.14.0:

```sh
python3 scripts/check_integrality_obstructions.py
python3 scripts/check_remaining_case.py
python3 scripts/check_repeated_exponent_family.py
python3 scripts/check_aa_b.py --json
python3 scripts/check_fixed_repeated_exponents.py
python3 scripts/check_second_cutoff.py
```

Compare with the corresponding JSON files under `results/`. The full text
output for the 90 diagnostics is also retained there. A separate direct
check for the cubic-scope example `(1,1,2)` is:

```sh
python3 - <<'PY'
from itertools import product
import sympy

bounds = (1, 1, 2)
vertices = [vertex for vertex in product(*(range(bound + 1) for bound in bounds))
            if vertex not in ((0, 0, 0), bounds)]
laplacian = sympy.zeros(len(vertices))
for first_index, first_vertex in enumerate(vertices):
    for second_index in range(first_index + 1, len(vertices)):
        second_vertex = vertices[second_index]
        if any(max(first, second) < bound
               for first, second, bound in zip(first_vertex, second_vertex, bounds)):
            laplacian[first_index, first_index] += 1
            laplacian[second_index, second_index] += 1
            laplacian[first_index, second_index] = -1
            laplacian[second_index, first_index] = -1
variable = sympy.Symbol('x')
expected = (variable * (variable - 10) * (variable - 9) ** 3
            * (variable - 7) ** 2 * (variable - 4)
            * (variable ** 2 - 13 * variable + 34))
assert sympy.expand(laplacian.charpoly(variable).as_expr() - expected) == 0
print(sympy.factor(expected))
PY
```

The bibliography contains the verified original graph reference. Reza's
source-preprint citation will be finalized when a public identifier is
available; its confidential PDF is not included in this repository.

[Return to the project entrance](../README.md).
