# One statement for the remaining mixed-parity restrictions

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

The [main statement](../paper/sections/mixed-parity-congruence.tex) is
Theorem 13.9. Its proof records the root cluster, the exact identity
h_C(b)=a^2*b^2*c^2*(a+c-b(b+2)), and the endpoint-two deduction.
The full derivative and shifted-cubic calculations are grouped in
[Appendix B](../paper/sections/two-adic-lifting.tex), following the detailed
verification scopes in [Appendix A](../paper/sections/verification.tex).

The earlier weaker conditions are consequences of the displayed pair:
a+c=15mod16 and a+c+4b=27mod32. Substituting b=16v+11 or16v+15
into b(b+2) gives the first congruence; adding4b gives the second.
Their staged proofs remain in Appendix B because they establish the
odd-root cluster needed for the stronger conditions.

All prior derivative thresholds, complete lifting proofs, diagnostic
limitations and examples are retained. The sources and saved exact
certificates under scripts/ and results/ have identical contents to
revision 1b7b2bd506f3be85ba04216f2eed6f355e66f911. Moving proofs changes
the numbering, so previous PR comments retain their original references:

| At revision 1b7b2bd | Current manuscript |
| --- | --- |
| Lemma 13.9, derivative thresholds | Lemma B.1 |
| Theorem 13.10, sum modulo sixteen | Proposition B.2 |
| Theorem 13.11, weighted sum modulo thirty-two | Proposition B.3 |
| Theorem 13.12, clustered-root arithmetic conditions | Theorem 13.9, now also includes the established endpoint/linear restrictions |
| Lemma 13.13, exclusion of endpoint one | Lemma 13.10 |
| Theorem 13.14, all (3,0,0) modulo-four permutations | Theorem 13.11 |
| Corollary 14.3, mixed linear tail | Corollary 14.3 |

The summary and introduction present the combined restrictions once,
while the appendix gives their full derivation. This implements the
planned manuscript reorganization after Reza's scope and closure questions.

## The remaining research question

No finite closure of the (1,3,2) role has been established. Further
two-adic shifts remain paused. The structural target is the endpoint-two
surface h_C(2)=0 inside the linear maximum bound, using its cubic/divisor
constraints and the remaining quotient roots. There are finitely many
candidates for each fixed minimum, but the minimum itself is unbounded.
Full Q3 and nonsquarefree higher-prime exponent vectors remain open.
The Laplacian manuscript has no Lean formalization.
