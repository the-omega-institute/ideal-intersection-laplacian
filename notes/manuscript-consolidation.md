# Combined residue and endpoint statements

The main text now has two combined statements: Theorem 13.5 lists all
mixed-parity exclusions and restrictions, and Theorem 14.1 collects the
endpoint bound, divisor conditions, middle-exponent certificate and
modulo-three classes. One worked shifted-root example remains in the main
text. Appendix B has the residue/modulus/condition table and complete case
proofs; Appendix C has the complete endpoint arguments.

Appendix A groups the verification scopes and retains every finite-domain
count needed for the main conclusions. The complete per-checker catalogue
is preserved in paper/sections/verification-details.tex. The optional detailed
build includes it using a separate job name; see paper/README.md.

For positive exponent residue roles a=1, b=3, c=2 modulo four, the
main manuscript now collects the established necessary conditions in
one theorem. If the ideal intersection graph is Laplacian integral,

```text
a+c = b(b+2) modulo 128,
b = 11 or 15 modulo 16.
```

Put u=(a-1)/4 and t=(a+c-b(b+2))/128. The further conditions are

```text
t+u+v is odd if b=16v+11,
t+v is odd if b=16v+15.
```

If m=min(a,b,c)>=4 and M=max(a,b,c), integrality also requires

```text
h_C(2)=0,
M < 7m-16+40/(m+2).
```

The exponent letters identify residue roles; m and M identify size order.
Every violation proves nonintegrality. The arithmetic conditions have no
size or ratio bound; the endpoint and maximum conditions use m>=4.
This consolidation combines existing results and introduces no additional
congruence test or exponent search.

## How the proof is organized

The [main mixed-parity statement](../paper/sections/mixed-parity-congruence.tex)
is Theorem 13.5. The root cluster, the exact identity
h_C(b)=a^2*b^2*c^2*(a+c-b(b+2)), the endpoint-two deduction and all
intermediate calculations are retained in
[Appendix B](../paper/sections/two-adic-lifting.tex).
The [combined endpoint statement](../paper/sections/endpoint-reduction.tex)
is Theorem 14.1, with its complete arguments in
[Appendix C](../paper/sections/endpoint-details.tex).

The earlier weaker conditions are consequences of the displayed pair:
a+c=15mod16 and a+c+4b=27mod32. Substituting b=16v+11 or16v+15
into b(b+2) gives the first congruence; adding4b gives the second.
Their staged proofs remain in Appendix B because they establish the
odd-root cluster needed for the stronger conditions.

All prior derivative thresholds, complete lifting proofs, diagnostic
limitations and examples are retained. The sources and saved exact
certificates under scripts/ and results/ have identical contents to
revision 295a54c33689c212e2b99149882b1dadf31f6b10. Moving proofs changes
the numbering, so previous PR comments retain their original references.
This table maps the latest pre-reorganization version:

| At revision 295a54c | Current manuscript |
| --- | --- |
| Theorem 13.6, six mixed-parity classes modulo eight | Theorem 13.5; complete case proof Proposition B.2 |
| Theorem 13.8, all (3,3,2) modulo-four permutations | Theorem 13.5; complete case proof Proposition B.4 |
| Theorem 13.9, clustered-root conditions and endpoint/linear restrictions | Theorem 13.5; complete case proof Proposition B.5 and final lifting calculation |
| Lemma 13.10, exclusion of endpoint one | Lemma B.6 |
| Theorem 13.11, all (3,0,0) modulo-four permutations | Theorem 13.5; complete case proof Proposition B.7 |
| Lemma B.1, derivative thresholds | Lemma B.8 |
| Proposition B.2, sum modulo sixteen | Proposition B.9 |
| Proposition B.3, weighted sum modulo thirty-two | Proposition B.10 |
| Theorem 14.1, strict linear endpoint-two bound | Theorem 14.1; complete case proof Proposition C.1 |
| Corollary 14.2, all-even linear tail | Theorem 14.1; complete case proof Proposition C.2 |
| Corollary 14.3, mixed linear tail | Theorems 13.5/14.1; complete case proof Proposition C.3 |
| Proposition 14.4, endpoint divisor conditions | Theorem 14.1; complete case proof Proposition C.4 |
| Corollary 14.5, second-smallest exponent through fifteen | Theorem 14.1; complete case proof Proposition C.5 |
| Theorem 14.6, modulo-three endpoint classes | Theorem 14.1; complete case proof Proposition C.6 |
| Remark 14.7, finite endpoint-test covering scope | Remark C.7 |

The summary and introduction present the combined restrictions once,
while the appendices give their full derivations. This implements Reza's
specific final-pass reorganization suggestion. It does not decide when to
freeze the research scope, finalize authors/disclosure, submit or publish.

## The remaining research question

No finite closure of the (1,3,2) role has been established. Further
two-adic shifts remain paused. The structural target is the endpoint-two
surface h_C(2)=0 inside the linear maximum bound, using its cubic/divisor
constraints and the remaining quotient roots. There are finitely many
candidates for each fixed minimum, but the minimum itself is unbounded.
Full Q3 and nonsquarefree higher-prime exponent vectors remain open.
The Laplacian manuscript has no Lean formalization.
