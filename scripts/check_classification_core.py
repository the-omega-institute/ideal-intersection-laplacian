import argparse
import difflib
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "paper/sections"


def digest(content):
    return hashlib.sha256(content.encode()).hexdigest()


def select(filename, start=None, stop=None):
    content = (SECTIONS / filename).read_text()
    start_index = content.index(start) if start else 0
    stop_index = content.index(stop, start_index) if stop else len(content)
    selected = content[start_index:stop_index]
    return selected, {
        "source": "paper/sections/" + filename,
        "source_sha256": digest(content),
        "start_line": content[:start_index].count("\n") + 1,
        "exclusive_end_line": content[:stop_index].count("\n") + 1,
        "selected_sha256": digest(selected),
    }


def bodies(content, environment):
    return re.findall(
        r"\\begin\{" + environment + r"\}(.*?)\\end\{" + environment + r"\}",
        content,
        re.DOTALL,
    )


def assemble():
    pieces = []
    selections = []

    def heading(content):
        pieces.append(content + "\n\n")

    def fragment(filename, start=None, stop=None):
        content, record = select(filename, start, stop)
        pieces.append(content)
        selections.append(record)

    fragment("graph.tex")
    heading(r"""\section{Repeated exponents}
\label{sec:bounds}
\label{sec:completion}
Coordinate interchange gives the two invariant blocks above. The
antisymmetric discriminant handles most parameters; exact factor indices
and the symmetric cubic settle every square-discriminant exception.

\subsection{Two unit exponents}""")
    fragment("pqrk.tex", r"\begin{theorem}")
    heading(r"""\subsection{The boundary family}
The following argument was supplied by Reza Nikandish in the public
collaboration discussion. It is the index-zero case in the factor
reduction below.""")
    fragment("aa-family.tex", r"\begin{theorem}")
    heading(r"\subsection{Exact factor pairs and the first indices}")
    fragment("aa-bounds.tex", "Fix $a,b", r"\begin{theorem}[Unified linear cutoff]")
    fragment("aa-bounds.tex", "The first possible value after", r"\begin{theorem}[Second linear cutoff]")
    fragment("aa-bounds.tex", r"\subsection{A finite reduction for each factor index}", r"\begin{theorem}[Third linear cutoff]")
    heading(r"\subsection{Completion by a cubic interval}")
    fragment("aa-completion.tex", r"\begin{theorem}", "The preceding cutoffs and fixed-exponent")
    heading(r"""\section{The complement quotient and small minima}
\label{sec:unit}
For unequal exponents the complement quotient retains all six support
classes. Its positive roots reflect to graph eigenvalues by the complement
identity and the universal-vertex lift.

\subsection{A unit exponent}""")
    fragment("unit-exponent.tex", r"\begin{theorem}", "The unit-exponent obstruction extends")
    heading(r"\subsection{A minimum exponent of two}\label{sec:minimum-two}")
    fragment("minimum-two.tex", r"\begin{theorem}")
    heading(r"\subsection{The uniform cutoff and minimum three}\label{sec:distinct-tail}")
    fragment("distinct-tail.tex", r"\begin{proposition}")
    heading(r"""\section{Small-minimum certificates and a uniform low root}
\label{sec:low-spectrum}
The complement quotient also makes sense for positive real support weights.
With $W=\operatorname{diag}(w)$ and disjointness edges on the six supports,
\[
 z^TWCz=\sum_{\{S,T\}:\,S\cap T=\varnothing}w_Sw_T(z_S-z_T)^2.
\]
Thus $W^{1/2}CW^{-1/2}$ is positive semidefinite. The singleton triangle
and the three complementary-pair edges connect this support graph, so
its kernel is one-dimensional. This justifies the real-parameter spectral
arguments below as well as their integer specializations.

The uniform cutoff leaves a complete finite domain at minima four through
seven. A symmetric Schur complement then supplies a positive root below
three at every larger minimum, including when an endpoint sign change
misses a pair of low roots.

\subsection{The complete minimum-through-seven certificate}""")
    fragment("low-spectrum.tex", "The uniform cutoff makes the requested", "The signs of $(g_B")
    heading(r"\subsection{The symmetric Schur complement}")
    fragment("low-spectrum.tex", r"\begin{proposition}", r"\begin{theorem}")
    heading(r"\subsection{The uniform comparison at three}")
    fragment("mixed-inertia.tex", r"\begin{theorem}", r"\begin{corollary}")
    heading(r"""\section{The endpoint-one sum bound and spectral separation}
On endpoint one the sum of the two larger exponents is quadratic in the
minimum. We retain the full spectral statement and its written proof;
the sum bound and the symmetric quotient are the inputs used in the
largest-root completion.""")
    fragment("endpoint-one-spectrum.tex", r"\begin{theorem}", r"\begin{corollary}")
    heading(r"""\section{The endpoint-two alternative}
For integer exponents, every noninteger quotient root $\mu$ transfers to
the graph eigenvalue $N+abc-1-\mu$: the exception $N-\mu=0$ in
Lemma~\ref{lem:join} is impossible because $N$ is an integer. Conversely,
the earlier repeated-entry and small-minimum proofs exhibit noninteger
roots in the six-support space itself. The repeated-entry invariant blocks
lie in that space, and~\eqref{eq:complement} reflects their roots from $B$
to $C$. These are the quotient obstructions used for the smaller cases
in the endpoint-two theorem.""")
    fragment("endpoint-two-completion.tex", "The endpoint-two surface admits", r"\begin{corollary}")
    fragment("three-prime-classification.tex")
    return "".join(pieces), selections


def audit(body, selections, bibliography):
    top = (ROOT / "paper/classification-core.tex").read_text()
    appendices = "\n".join(
        (SECTIONS / filename).read_text()
        for filename in ("endpoint-two-identities.tex", "largest-root-identities.tex")
    )
    combined = top + body + bibliography + appendices
    labels = re.findall(r"\\label\{([^}]+)\}", combined)
    references = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", combined)
    assert len(labels) == len(set(labels)), "Duplicate labels"
    assert set(references) <= set(labels), sorted(set(references) - set(labels))
    citation_keys = set()
    for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", combined):
        citation_keys.update(group.split(","))
    bibliography_keys = set(re.findall(r"\\bibitem\{([^}]+)\}", bibliography))
    assert citation_keys <= bibliography_keys
    original = "\n".join(path.read_text() for path in sorted(SECTIONS.glob("*.tex")))
    environment_counts = {}
    preservation = {}
    for environment in ("proof", "theorem", "lemma", "proposition", "corollary"):
        originals = Counter(digest(value) for value in bodies(original, environment))
        selected = Counter(digest(value) for value in bodies(body, environment))
        assert not selected - originals, environment
        environment_counts[environment] = sum(selected.values())
        preservation[environment] = dict(sorted(selected.items()))
    required = {
        "thm:repeated", "cor:minimum-seven", "thm:uniform-low-root",
        "thm:endpoint-one-spectrum", "thm:endpoint-two-completion",
        "thm:largest-root-unit-interval", "lem:endpoint-one-small-gaps",
        "thm:three-prime-classification",
    }
    assert required <= set(labels)
    return {
        "source_base_commit": "08065334917ac0bacc965e4c447e2b2aa5c421d1",
        "original_proof_source_revision": "7be84599097fdff320b196cb4f84a2dfe505bd77",
        "scope": "Source concordance, explicit-reference closure and selected statement/proof bodies matching the current source sections; not an independent proof validation or certificate rerun.",
        "written_proof_update": "Endpoint-one sum bound and small-gap1/2 exponent-root brackets hold at real minimum a>=2; residual spectral claims retain a>=4. Small-gap sign vectors use a=2+m with the L2=b boundary explicit.",
        "generated_body_sha256": digest(body),
        "generated_bibliography_sha256": digest(bibliography),
        "selections": selections,
        "shared_appendices": {
            "paper/sections/" + filename: digest((SECTIONS / filename).read_text())
            for filename in ("endpoint-two-identities.tex", "largest-root-identities.tex")
        },
        "environment_counts": environment_counts,
        "preserved_body_hashes": preservation,
        "explicit_references_resolve": True,
        "labels": sorted(labels),
        "citations_resolve": True,
        "finite_bases_retained": [27562, 8658],
        "earlier_minimum_three_base_retained": 325,
        "new_mathematical_theorem": False,
        "lean_run": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-patch", action="store_true")
    arguments = parser.parse_args()
    body, selections = assemble()
    original = (ROOT / "paper/paper.tex").read_text()
    start = original.index(r"\begingroup")
    stop = original.index(r"\endgroup", start) + len(r"\endgroup")
    bibliography = original[start:stop] + "\n"
    report = audit(body, selections, bibliography)
    generated = {
        "paper/core/body.tex": body,
        "paper/core/bibliography.tex": bibliography,
        "results/classification-core-source-review.json": json.dumps(report, indent=2) + "\n",
    }
    if arguments.emit_patch:
        print("*** Begin Patch")
        for filename, content in generated.items():
            path = ROOT / filename
            if path.exists():
                if path.read_text() == content:
                    continue
                print("*** Update File: " + str(path))
                for line in list(difflib.unified_diff(path.read_text().splitlines(), content.splitlines(), n=3))[2:]:
                    print("@@" if line.startswith("@@") else line)
            else:
                print("*** Add File: " + str(path))
                print("\n".join("+" + line for line in content.splitlines()))
        print("*** End Patch")
    else:
        for filename, content in generated.items():
            assert (ROOT / filename).read_text() == content, filename
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
