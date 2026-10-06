# Completion of the coprime repeated-minimum region

**Theorem.** Every positive four-prime exponent vector (a,a,b,c) with

```text
a>=5, b,c>=a, gcd((a-1)(a-2),bc)=1
```

has a noninteger Laplacian eigenvalue. There are no exceptional values
of a. This completes the coprime corollary of the preceding
[low-root divisibility theorem](four-prime-low-root-divisibility.md),
which left a=6,7,12,22.

The proof combines an unbounded spectral reduction with eleven complete
quadratic discriminant calculations. The finite rows are exactly the
cases required by that reduction; no tail interval is enumerated.
The general noncoprime repeated-minimum and single-pair regions remain open.

## The existing reduction

Use the genuine repeated-pair operator K, with characteristic polynomial
p(x)=det(xI-K) and actual graph eigenvalue transfer V+1-kappa.
The [preceding proof](four-prime-low-root-divisibility.md) gives
1<kappa_min(K)<4 throughout the domain and

```text
p(2)=-3b^2c^2 modulo a-1,
p(3)=-20b^2c^2 modulo a-2.
```

Coprimality excludes the integer value 2 for every a>=5. The only
remaining integer value, 3, requires a-2 to divide 20, giving
a=6,7,12,22. For every other a the earlier theorem applies directly.

When a=7, coprimality with (a-1)(a-2)=30 forces both tails
to be odd. The [modular repeated-pair theorem](repeated-pair-modular.md)
then excludes graph integrality: the characteristic polynomial modulo
two is (x+1)^2(x^2+x+1), with an irreducible quadratic factor.
This branch uses the full restriction's modular obstruction; it does
not require an additional claim about which real root is noninteger.

## A finite bound on the smaller tail

The empty/full-support principal minor of the symmetric similar matrix
K-3I is

```text
J3=-(a+2)bc+(a+1)(a-2)(b+c)+2(a-1)(a-2).
```

For b=2a-2+u,c=2a-2+v with u,v>=0 it becomes

```text
J3=-(a+2)uv-(a^2+3a-2)(u+v)-2(a-1)(3a+2)<0.
```

A negative trial direction gives kappa_min(K)<3. Together with
the general lower bound and exclusion of 2, this already proves
nonintegrality whenever both tails are at least 2a-2.

For the remaining a=6,12,22, permute the two tails so b<=c.
It is therefore enough to consider a<=b<=2a-3. Coprimality leaves
exactly these smaller-tail values:

| a | Complete necessary b list |
|---|---|
| 6 | 7,9 |
| 12 | 13,17,19,21 |
| 22 | 23,29,31,37,41 |

The larger tail c remains unbounded. It is handled by a quadratic
equation, not a finite tail search.

## Complete quadratic arithmetic

For each listed (a,b), write p(3)=h(Ac^2+Bc+C), with positive
integer content h. The following table is complete. Each discriminant
D=B^2-4AC satisfies z^2<D<(z+1)^2, so no quadratic has a rational
tail root. In particular p(3) cannot vanish at an integer c.

| a | b | h | A | B | C | D | z |
|---|---|---|---|---|---|---|---|
| 6 | 7 | 4 | -1085 | 8417 | -848 | 67165569 | 8195 |
| 6 | 9 | 4 | -1847 | 11381 | -2144 | 113687289 | 10662 |
| 12 | 13 | 10 | -4238 | 121085 | 6802 | 14776884729 | 121560 |
| 12 | 17 | 90 | -874 | 18581 | -462 | 343638409 | 18537 |
| 12 | 19 | 10 | -10100 | 192017 | -11822 | 36392919489 | 190769 |
| 12 | 21 | 10 | -12614 | 217949 | -20942 | 46445117049 | 215511 |
| 22 | 23 | 180 | -2001 | 142585 | 17568 | 20471096497 | 143077 |
| 22 | 29 | 180 | -3551 | 188573 | 10992 | 35715906697 | 188986 |
| 22 | 31 | 60 | -12491 | 614283 | 23456 | 378515559673 | 615236 |
| 22 | 37 | 60 | -18869 | 767703 | -13936 | 588316062673 | 767017 |
| 22 | 41 | 180 | -7947 | 292141 | -15408 | 84856574377 | 291301 |

Both possible integer values of the smallest root are now excluded for
a=6,12,22. Combining these rows, the tail cutoff, the a=7 modular
branch and the previous general reduction proves the theorem.

In particular, the entire previously exceptional families
(a,a,a+1,(a+1)^m), with a in {6,12,22} and m>=2, are now
excluded. Their tails are coprime to both endpoint divisors and are
zero modulo every p dividing a+1, so they pass the earlier modular
splitting tests. Passing those tests remains only a necessary condition.

## Verification and remaining question

The [checker](../scripts/check_four_prime_coprime_completion.py)
derives the generic principal-minor and negative-shift identities,
both low-endpoint residues, all four exceptional a values, the a=7
binary factorization and the complete finite b lists. It verifies every
quadratic row and strict square bracket. Forty-four independent integer
determinants reconstruct the eleven tail quadratics at algebraic
c=0,1,2 and cross-check at c=3; these zero representatives are
interpolation values, not positive graph exponent examples.

Six specified positive controls reconstruct 336 support-column actions
and verify weighted symmetry, zero sums and the actual graph transfer.
Thirty further independent integer determinants check their quartics;
six exact Sturm counts verify the low-root intervals. There are 74
independent integer determinants in total. Both complete written tables
are independently matched against the certificate.

The [certificate](../results/four-prime-coprime-completion.json)
is reproducible with SymPy 1.14.0 using
`python3 scripts/check_four_prime_coprime_completion.py`.
The conclusion uses the written unbounded reduction and the complete
eleven-row finite arithmetic. No arbitrary exponent rectangle, tail
scan, expanded graph, historical finite-base rerun or Lean validation
is used. All earlier results and their finite inputs are retained.

Next consider noncoprime repeated minima satisfying at least one of
the low-root divisibilities. Combine their endpoint equations with the
unique-tail integer-root conditions or the modular restrictions; a
passing divisibility alone does not make its endpoint a root. General
single-pair, fully unequal four-prime and higher-prime classification
remain open. The focused three-prime main and joint manuscript-scope
decisions are retained.
