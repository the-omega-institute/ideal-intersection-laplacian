# Structure of the proof: review and integration

Reza Nikandish proposed this section in PR9 comment
[6109400247](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/9#issuecomment-6109400247)
and supplied its LaTeX in comments
[6109409470](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/9#issuecomment-6109409470)
and [6109476193](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/9#issuecomment-6109476193).
The two source comments are identical. The reviewed section is inserted after
the graph section in both the focused main paper and the supporting collection.
It explains localization, sharpness and the differing endpoint scales.

## Mathematical disposition

The localization argument is valid. Existence of a positive quotient root
below three implies that the smallest positive root is below three; it need
not identify the originally supplied witness as the smallest root. For integer
exponents, noninteger quotient roots transfer to graph roots by complement
reflection and the universal-class lift. This necessary implication suffices;
the overview does not need an unproved converse about the full graph spectrum.

The balanced factorization and both proposed bounds are correct for m>=1.
We replace the squaring argument by q_m(m)=-m^3, q_m(3)=9-12m and the
rationalized root formula. The proposed upper-bound squaring difference is
48m-36, not 36m; the positive-root ordering is also made explicit. The lower
bound follows immediately from sqrt((m+4)^2-12)<m+4. The limit along integer
m establishes optimality of the uniform constant three, as already recorded
in the uniform-low-root theorem.

The endpoint-two middle bound needs its stated minimum hypothesis. The
overview uses the remaining classification range 8<=a<b<c, where both the
middle and maximum bounds apply. Finite rectangles at each fixed a do not
make the total endpoint-two domain finite: its proof retains the real
(4,5) root argument for a>=40 and the complete 8,658-triple base at minima
eight through thirty-nine.

The endpoint-one sum lower bound gives c>=a^2-a+1/2. It does not by itself
prove a two-sided c asymptotic or a dimension/density statement about integer
points. The section states the lower scale and its exact role in the
largest-root theorem. It does not claim that a common alternative method
is impossible or that either endpoint surface has been enumerated.

All supplied fixed-gap expansion coefficients through a^-2 are correct.
An analytic implicit-function proof upgrades the formal statement to a
fixed-d asymptotic with O_d(a^-3): t=1/a and y=t^2c give a polynomial
F_d(t,y), with F_d(0,y)=2y^2(y-2) and partial_y F_d(0,2)=8. The analytic
branch near y=2 has the stated Taylor coefficients. Since Q(0)>0,
Q(a+d)=-4a^6+O_d(a^5)<0 and the leading cubic coefficient is positive,
two other roots lie below b, proving uniqueness of the branch above b
for sufficiently large a at fixed d.

The remainder has no effective constant or explicit minimum and is not
uniform for growing d. No transition at d approximately sqrt(a), impossibility
of a uniform bracket, or author-reported numerical experiment is used as a
proved result. The exact d=1,2 brackets and largest-root interval remain the
classification inputs; the new fixed-gap proposition is supplementary.

## Exact checks and numbering

Run `python3 scripts/verify_proof_structure.py`. It reconstructs the generic
six-support determinant using the set-disjointness quotient constructor,
checks the balanced factorization and root anchors, derives the endpoint-one
cubic, proves the rescaling and nonzero derivative identities, and solves
the three successive Taylor coefficient equations exactly. The rescaled
residual vanishes through degree four; its degree-five coefficient is
d^2(4d^3-6d+7). These are generic symbolic identities supporting a written
analytic proof, not a finite exponent search or numerical root experiment.
The support constructor and SymPy backend are shared with prior diagnostics;
the original characteristic-polynomial helper is not imported.

The main and supporting PDFs are now 29 and 65 pages. All manuscript
references use labels. The insertion shifts later section numbers by one;
the new propositions are 3.1 and 3.2 in both builds.

| Result | Main | Supporting |
| --- | --- | --- |
| Repeated entries | Theorem 4.7 | Theorem 8.1 |
| Minimum through seven | Corollary 6.1 | Corollary 12.4 |
| Uniform low root | Theorem 6.3 | Theorem 13.2 |
| Endpoint-one sum and spectrum | Theorem 7.1 | Theorem 15.2 |
| Endpoint-two rectangle | Lemma 8.1 | Lemma 15.7 |
| Endpoint-two completion | Theorem 8.2 | Theorem 15.8 |
| Largest-root interval | Theorem 9.1 | Theorem 17.1 |
| Gaps one and two | Lemma 9.2 | Lemma 17.2 |
| Three-prime classification | Theorem 9.3 | Theorem 17.3 |

`scripts/check_classification_core.py` checks source concordance, label and
citation closure, and preservation of the selected proof bodies. The original
classification sections, finite certificate data, authors, disclosure and
bibliography are preserved. The historical detailed PDF is retained. No
historical finite-base determinant rerun, Lean, new Oracle review, merge,
publication or submission accompanies this integration.
