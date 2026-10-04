# A second linear cutoff from the first nonboundary factor

For distinct primes and exponents `(a,a,b)`, with `a>=2`, we prove
nonintegrality whenever

$$b>S(a)=\frac{(a-3)(2a-3)}{2a+3}=a-6+\frac{27}{2a+3}.$$

This improves the [previous cutoff](aa-b-diagnostic.md)
$R(a)=2(a-1)(a-2)/(a+2)$. The complete positive-b families now include
every repeated exponent $a=2,3,4,5,6$. The general classification remains open.

## The first nonboundary factor is a finite problem over all a

Use the proved square-discriminant reduction, with
$M=a^3(2a+1)$, $h=a+1$, and positive factors $d\leq e$ satisfying
$de=M$, $d+e=h^2b+a(3a+1)$, and $d\equiv e\equiv1\pmod h$.
The case $d=1$ is Reza's settled boundary family.

For the next possible value $d=a+2$, the identity

$$M=(a+2)(2a^3-3a^2+6a-12)+24$$

implies $a+2\mid24$. This leaves $a=2,4,6,10,22$.
Substitution into the exact factor criterion gives $b=0,2,5,12,35$,
respectively. Since $b\geq1$, the complete list is:

| $(a,b)$ | $(d,e)$ | Symmetric cubic | Root-free prime |
| --- | --- | --- | --- |
| $(4,2)$ | $(6,96)$ | $x^3-86x^2+2304x-18816$ | 5 |
| $(6,5)$ | $(8,351)$ | $x^3-245x^2+19266x-488160$ | 7 |
| $(10,12)$ | $(12,1750)$ | $x^3-842x^2+230160x-20534400$ | 13 |
| $(22,35)$ | $(24,19965)$ | $x^3-4919x^2+7887858x-4132479120$ | 17 |

Each monic cubic has no root modulo its listed prime, so it is irreducible
over the rationals. The symmetric quotient has real, nonzero eigenvalues,
and extension through the universal vertices shifts each by the integer
$a^2b-1$. Thus all four graphs are nonintegral. These are all possible
positive-b pairs with $d=a+2$, not a bounded search in a or b.

## The improved uniform bound

After settling $d=1$ and $d=a+2$, the congruence forces
$d\geq T=2a+3$. Since $e\geq d\geq T$,

$$\frac MT+T-(d+e)=(d-T)\left(\frac eT-1\right)\geq0.$$

Substituting the sum condition gives

$$b\leq\frac{M/T+T-a(3a+1)}{(a+1)^2}
=\frac{(a-3)(2a-3)}{2a+3}=S(a).$$

Therefore every $b>S(a)$ has either a nonsquare discriminant, the settled
boundary pair, or one of the four settled first-factor pairs. This proves
the second cutoff for every $a\geq2$.
It is strictly below the previous cutoff, since

$$R(a)-S(a)=\frac{2a^3-a^2-a-6}{(a+2)(2a+3)}>0.$$

For $z=a-2\geq0$, the numerator is $2z^3+11z^2+19z+4$.

## Two further complete fixed-exponent families

At $a=5,6$, the new bounds are $S(5)=14/13$ and $S(6)=9/5$.
Only $b=1$ remains in each case. Their discriminants are respectively
$221$, between $14^2$ and $15^2$, and $313$, between $17^2$ and $18^2$.
Thus every positive b is nonintegral for these two repeated exponents too.
Together with the earlier theorem, this covers $a=2,3,4,5,6$.

[The exact checker](../scripts/check_second_cutoff.py) verifies the polynomial
identities, every divisor of24, the four modular residue lists, and these
two remaining discriminants. [The saved certificate](../results/second-cutoff.json)
records its source hashes. No larger parameter scan or Lean run is used.
Next: control the symmetric cubic on admissible square-discriminant pairs
with $d\geq2a+3$ and $b\leq\lfloor S(a)\rfloor$; full Q3 remains open.
