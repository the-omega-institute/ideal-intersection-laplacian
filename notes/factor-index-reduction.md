# A finite divisor reduction for each factor index

The square-discriminant condition admits a second exact finite reduction:
instead of fixing the repeated exponent a, fix the index j in
$d=1+(a+1)j$. Then d must divide the constant $(j+1)^3(j+2)$,
independent of a. This makes each fixed index a finite problem over all a.

We use this reduction to settle j=2 completely and prove nonintegrality
for every a≥2 and

$$b>T(a)=\frac{2(a-4)(a-2)}{3a+4}.$$

It also completes the all-positive-b families a=7,8,9. Together with
earlier proofs, every repeated exponent a=2 through9 is settled.
The remaining arbitrary-index and full Q3 questions are open.

## Exact reduction in the other parameter

For a≥2, put h=a+1, M=a³(2a+1), C=(a−1)(2a−1).
The [proved discriminant reduction](aa-b-diagnostic.md) gives positive
factors d≤e with de=M, d≡e≡1 mod h and
d+e=h²b+a(3a+1). The case d=1 is the settled boundary family.
For every other pair write d=1+hj, with j≥1.

**Proposition.** Fix j≥1 and let K_j=(j+1)³(j+2).
Every nonboundary square-discriminant pair of index j is obtained exactly
as follows. For each positive divisor d of K_j satisfying

$$a=\frac{d-1}{j}-1\in\mathbb Z_{\geq2},$$

set M=a³(2a+1), e=M/d and v=(e−1)/(a+1). Retain exactly those
candidates with d≤e and b=C−jv≥1. Both e and v are automatically integers;
the discriminant is D=(v−j)². Conversely every retained candidate is
an admissible square-discriminant pair of index j.

**Proof.** Modulo d=j(a+1)+1, we have ja≡−(j+1), so

$$j^4 M=(ja)^3\,j(2a+1)\equiv(j+1)^3(j+2)=K_j\pmod d.$$

Since gcd(d,j)=1, d divides M if and only if d divides K_j. Thus e is an
integer, and M≡d≡1 mod h implies e≡1 mod h, making v integral.
From

$$M=1+h(3a-2)+h^2C=(1+hj)(1+hv)$$

we obtain j+v+h jv=3a−2+hC. Setting b=C−jv gives
d+e=h²b+a(3a+1), while e−d=h(v−j). The positivity and ordering conditions
then give exactly the earlier factor criterion. This proves both directions.

The exact polynomial identity behind the congruence is

$$j^4M-K_j=(j(a+1)+1)
\bigl(2j^3a^3-j^2(j+2)a^2+j(j+1)(j+2)a-(j+1)^2(j+2)\bigr).$$

There is no truncation in a in this criterion. Arbitrary j is still an
infinite family of finite divisor problems.

## The complete second-index case

For j=2, K_2=108. The admissible shape is d=2a+3, an odd divisor
of108 with d≥7. The only candidates are d=9,27, giving a=3,12.
At a=3, e=21, v=5 and b=0, which is excluded.
At a=12, e=1600, v=123 and b=7, with sqrt(D)=121.
Thus (a,b)=(12,7) is the only positive-b pair of index2 over all a.

Its symmetric cubic is

$$f_{12,7}(x)=x^3-751x^2+180348x-13829760.$$

The values modulo13 at all residues are
4,7,9,3,8,4,10,6,11,5,7,10,7, with no zero. The monic cubic is therefore
irreducible over the rationals, and its real nonzero roots lift to
noninteger graph eigenvalues. This settles the entire index2 case.

## A third cutoff and three more complete families

Index0 is Reza's boundary family; [index1](second-linear-cutoff.md) is
already settled. After index2, every unresolved square-discriminant pair
has d≥Q=3a+4. Since e≥d≥Q,

$$\frac MQ+Q-(d+e)=(d-Q)\left(\frac eQ-1\right)\geq0.$$

Therefore

$$b\leq\frac{M/Q+Q-a(3a+1)}{(a+1)^2}
=\frac{2(a-4)(a-2)}{3a+4}=T(a).$$

Every b>T(a) is consequently nonintegral for all a≥2. For a≥3 this is
strictly below S(a), since

$$S(a)-T(a)=\frac{2a^3-a^2-5a-12}{(2a+3)(3a+4)}>0.$$

With z=a−3≥0, its numerator is 2z³+17z²+43z+18.
The leading term of T(a) is 2a/3.

At a=7,8,9, the bounds are 6/5,12/7,70/31. Only the following
four positive-b cases remain, each with nonsquare discriminant:

| (a,b) | D | Consecutive square roots bounding D |
| --- | --- | --- |
| (7,1) | 421 | 20,21 |
| (8,1) | 545 | 23,24 |
| (9,1) | 685 | 26,27 |
| (9,2) | 1489 | 38,39 |

Thus every positive b is nonintegral for a=7,8,9 too. These four checks
exhaust the proved remaining ranges, rather than sample a larger b interval.

[The checker](../scripts/check_factor_index_reduction.py) verifies the
general polynomial identities, every divisor of108, the unique cubic
certificate and all four discriminants. [Its saved certificate](../results/factor-index-reduction.json)
records the source hashes. No parameter-range expansion or Lean is used.
Next: the symmetric cubic on admissible j≥3 pairs, with
b≤floor(T(a)); the all-a classification is not yet proved.
