# The exact span-only threshold for the balanced diagonal criterion

For ordered integer exponents `(a,a+d,a+r)`, `0<=d<=r`, the supporting
balanced-span corollary now requires

\[
a>r+4+\sqrt3(r+2),
\]

replacing `a>=3r+8`. At span ten the sufficient integer minimum drops
from 38 to 35; at span 100 it drops from 308 to 281.

The existing sufficient Schur condition for a complement quotient root
in `(2,3)` is `Delta=(a-2)(a+b+c-2)-2bc>0`. Its exact expansion is

\[
\Delta=W(a,r)+(r-d)(a+2r+2),\qquad
W=a^2-2ar-8a-2r^2-4r+4.
\]

The factorization

\[
W=[a-r-4-\sqrt3(r+2)][a-r-4+\sqrt3(r+2)]
\]

proves positivity at the new threshold. This also guarantees `a>4`,
so the existing balanced-interval corollary applies. The old bound
is larger by `(2-sqrt(3))(r+2)>0`.

At fixed positive real `a` and nonnegative real `r`, the minimum over
`0<=d<=r` occurs at `d=r`. The other zero of `W` is
`r+4-sqrt(3)(r+2)<2`; hence, for `a>=4`, `Delta>0` for every middle
parameter if and only if `a>r+4+sqrt(3)(r+2)`. At equality the
repeated-largest family `b=c=a+r` has `Delta=0`. This proves the
threshold exact for the strict diagonal criterion. It need not be
optimal for the existence of a quotient root in `(2,3)`, since the
criterion is only sufficient.

The newly covered fixed controls `(35,45,45)` and `(281,381,381)` have
`Delta=9` and `Delta=117`. Both fail the old linear bound. Exact direct
quotient determinants and root counts confirm no positive roots at or
below two and positive roots in `(2,3)`. The below-threshold control
`(34,44,44)` has `Delta=-32`; this tests the criterion sign, without
claiming spectral failure or graph integrality.

Run `python3 scripts/verify_balanced_span_threshold.py` with Python 3.10+
and SymPy 1.14.0; compare with `results/balanced-span-threshold.json`.
The checker verifies the generic expansion, factorization, boundary and
old-bound comparison, plus the two specified direct quotient root counts
with multiplicities. Its support constructor and SymPy backend are shared;
the original characteristic helper is not used. The infinite conclusion
uses the written proof. No parameter scan, new finite base, historical
finite-base rerun, floating point spectrum or Lean is involved.
The selected main classification manuscript is unchanged; the refinement
stays in the supporting collection.
