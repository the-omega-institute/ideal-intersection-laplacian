# Direct verification of the endpoint-two proof inputs

Lemma 7.1 and Theorem 7.2 of the focused manuscript combine a written
real-tail proof with a historical finite base. This check reconstructs
`det(x I-C)` from the set-disjointness quotient by a symbolic determinant,
without importing the original characteristic-polynomial helper, and
reads the current appendix tables literally.

The generic middle-bound identity agrees, and its four factors have
6, 13, 14 and 9 positive shifted terms at `a=4+m`. The three rational
parameterizations have exact inverse identities. All 84 coefficients
in the maximum-bound residual, 44 in the difference at five, and 112
in the scaled difference at four match: all 240 nonzero coefficients
are strictly positive. Their constants are 3,014,656; 4,629,843; and
611,305,472. The displayed `[0]` row at `t^3 u^3` in the difference
at five is checked as an absent component. The two separately displayed
residual expressions are nonnegative on their stated real domain.

The written argument confines endpoint-two zeros at minimum at least
eight to a strict rectangle. At minimum at least forty the positive
differences give `h_C(4)>0>h_C(5)`, hence a noninteger root in `(4,5)`.
Repeated exponents and minima at most seven use the earlier theorems;
the remaining fully distinct minima eight through thirty-nine use the
historical finite input.

For that finite domain, put

\[
c_{\max}=\left\lfloor\frac{9a-33}{4}\right\rfloor,
\quad b_{\max}=\min\{2a-3,c_{\max}-1\},
\quad n=\max\{0,b_{\max}-a\}.
\]

Summing `c_max-b` over `a+1<=b<=b_max` gives

\[
n c_{\max}-\frac{n(a+1+b_{\max})}{2}.
\]

All 32 displayed per-minimum counts agree with this arithmetic formula;
the total is 8,658, including zero triples at minimum eight. The strict
integer maximum boundary is checked separately. This verifies domain
coverage and table transcription, not the nonzero endpoint values or
the reported minimum absolute value 8,208. Those remain supported by
the separate historical Horner/Bareiss certificate.

Run from the repository root with Python 3.10 or later and SymPy 1.14.0:

```sh
python3 scripts/verify_endpoint_two_coefficients.py
```

The output is saved in `results/endpoint-two-coefficient-verification.json`.
Both manuscript builds include the same checked appendix. The checker
shares the mathematical support model, table parser and SymPy backend
with the other direct checks. Independence refers to determinant
reconstruction and literal source comparison. It performs no endpoint
evaluation on the 8,658-triple base, historical finite-base rerun,
parameter scan, expanded graph calculation or Lean validation.
