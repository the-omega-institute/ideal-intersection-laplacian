# Nonintegrality when the minimum exponent is eight

Let C be the six-support complement quotient, h_C(x)=det(xI-C)/x, and
write the positive integer exponents in size order a<=b<=c.

**Theorem.** Every three-exponent vector with minimum exactly eight has
a nonintegral ideal intersection graph. The proof combines written
reductions with a complete **108-pair finite certificate** for endpoint
one. It is not a purely written theorem.

Together with the preserved minimum-through-seven results, this certifies
every triple with minimum at most eight. The cumulative statement retains
the earlier27562triple finite discriminant certificate. The new minimum-eight
argument does not need the8658triple global endpoint-two completion base.
Full Q3 and higher-prime nonsquarefree vectors remain open.

## The written reduction

Repeated exponents are already covered by the
[complete repeated-exponent theorem](repeated-exponent-completion.md),
including cases where the repeated exponents are the two largest.
It remains to consider a=8<b<c. Then b>=9 and c>=10.

The [uniform low-root theorem](mixed-inertia.md) supplies a positive
quotient root in(0,3). If every quotient root were an integer, either one
or two would therefore be a root. The written
[nine-fourths maximum cutoff](endpoint-two-sharp-maximum.md) gives

```text
c>=9a/4-8=10  =>  h_C(2)>0.
```

Thus endpoint two is excluded for every fully distinct integer triple
with minimum eight, with no finite base required for this reduction.

On endpoint one, the written
[growing-gap theorem](endpoint-one-growing-gap.md) excludes b=9and10
for every integer c>b. The [real geometry theorem](endpoint-one-geometry.md)
excludes b>=119, since real c>b feasibility at a=8 holds exactly when
b<=2a²-a-2=118 for integer b. Therefore the entire unresolved endpoint-one
region has exactly108possible middle exponents:

```text
11<=b<=118,  c>b.
```

There is no arbitrary upper cutoff on c. For every one of these middle
values the same written geometry theorem gives exactly one real exponent
root above b, and the sum bound places it below240-b.

## Complete finite unit brackets

At a=8 the generic endpoint-one cubic is

```text
Q_b(c)=(b²+63)c³+(b³-241b²+133b+427)c²
       +7(b-1)(19b+21)c+7(b-1)(b+7)(9b+7).
```

The checker reconstructs this formula from the exact6x6quotient and verifies
the diagonal factorization

```text
Q_b(b)=(7-2b²+3b)(-b³+119b²-21b-49).
```

For each integer b=11,...,118, integer bisection starts with the written
bracket (b,240-b) and finds consecutive integers L_b,U_b=L_b+1 satisfying

```text
b<L_b<U_b<=240-b,  Q_b(L_b)<0<Q_b(U_b).
```

The complete [108-row CSV](../results/minimum-eight-base.csv) records every
b, both integer endpoints, both integer Horner values, and independent
fraction-free6x6Bareiss determinants of I-C at those exponents. All216
determinants equal the corresponding endpoint values. Exact Sturm counts
give one root on each complete interval c>b and on each unit bracket;
the cubics have no repeated polynomial root.

The written uniqueness theorem, or the independently checked full-interval
Sturm count for each pair, makes the root in(L_b,U_b) the only real root
above b. Since no integer lies strictly between L_b and U_b, every integer
c>b is excluded. The finite certificate therefore covers an unbounded
last exponent for all108necessary middle values, rather than certifying
only a bounded sample of triples.

## Spectral conclusion and scope

Every fully distinct minimum-eight integer triple has h_C(1)!=0 and
h_C(2)>0. Its positive quotient root in(0,3) is consequently noninteger.
The usual complement and universal-class lifts transfer nonintegrality to
the ideal intersection graph. The repeated-exponent theorem supplies the
remaining minimum-eight triples.

The new theorem depends on the108fixed-pair finite certificate. Its
endpoint-two part is written; no global endpoint-two base is used. The
cumulative minimum<=8result additionally depends on the earlier finite
minimum4through7certificate, which remains unchanged. Root simplicity here
concerns the exponent polynomial; no new spectral-multiplicity assertion
is made. Repeated endpoint-one zeros(8,8,105)and(9,9,136)are preserved as
controls outside the fully distinct hypotheses.

Any remaining fully distinct integer spectrum would now require

```text
a>=9,  d=b-a>=3,  a<2d²+20,
b<=2a²-a-2,  b<c,  b+c<4a²-2a,  h_C(1)=0.
```

These are necessary restrictions. This fixed-minimum certificate does not
establish a uniform bound on a or solve full Q3. Further work should target
a specified algebraic obstruction or another quotient root in this region;
no larger-minimum computation is part of this result.

## Reproduction

With SymPy1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_minimum_eight.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_minimum_eight.py --csv
```

Compare with [the JSON certificate](../results/minimum-eight.json) and the
complete CSV. Both outputs reproduce byte-for-byte; the JSON records the
CSV SHA256 and source hashes. All108unit brackets,216boundary determinants
and216Sturm counts pass. The boundary triple(8,9,10)has a positive endpoint
two, and both repeated endpoint-one controls retain their zero values.

This is exact finite verification combined with written reductions.
No new discriminant certificate, floating spectra or Lean verification is
claimed. All earlier notes, scripts, results and manuscript files remain
unchanged pending coauthor review and integration.

[Return to the project entrance](../README.md).
