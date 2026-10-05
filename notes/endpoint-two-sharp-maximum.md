# A uniform nine-fourths maximum bound on endpoint two

Let C be the six-support complement quotient and `h_C(x)=det(xI-C)/x`.
Exponents are in **size order**, independently of their residue roles.

**Theorem.** For ordered real exponents `8<=a<=b<=c`,

```text
c>=9a/4-8  =>  h_C(2)>0.
```

In particular, every endpoint-two zero in this domain requires
**`c<9a/4-8`**. This strictly improves the preceding bound c<3a-4, since

```text
(3a-4)-(9a/4-8)=3a/4+4>0.
```

The proof covers the entire unbounded real domain; it requires no finite
base or exponent scan. The threshold is sufficient, with no optimality
claim. The preceding a>=4 bound remains available below minimum eight.

## Positive transformation with two square expressions

The [middle-tail theorem](endpoint-two-middle-tail.md) already gives
h_C(2)>0 when b>=2a-2. It remains to consider a<=b<2a-2. Parameterize
that interval and the proposed maximum tail by

```text
a=8+m,  b=(a+(2a-2)t)/(1+t),  c=9a/4-8+v,
m,t,v>=0,  t=(b-a)/(2a-2-b).
```

The inverse is exact, and the denominator 1+t is positive. Clearing the
denominator of the generic endpoint polynomial and its quarter fractions
gives the following identity:

```text
H(m,t,v)=64(1+t)^3*h_C(2)
 =9m^6(1+2t)[14(1-t)^2+5t+t^2]
  +308m^5*t(t-1)^2+P(m,t,v).
```

Both displayed terms are nonnegative for m,t>=0. The residual P has
**84 nonzero coefficients, all strictly positive**, including constant
3014656. The following table gives the entire residual:

```text
P(m,t,v)=sum_{i=0}^3 sum_{j=0}^3 P_ij(m)t^i v^j.
```

Each vector lists the coefficients of P_ij in **ascending powers of m**.

| i | j=0 | j=1 | j=2 | j=3 |
|---|---|---|---|---|
| 0 | [3014656,4968448,2878080,766780,100060,6027] | [3489792,4092928,1603664,277392,21796,632] | [1124352,751424,170816,16144,544] | [75520,27392,3264,128] |
| 1 | [393216,3104768,2984064,974712,131516,6322] | [7569408,11273216,4914464,907536,74792,2252] | [4098048,2845312,670016,65568,2288] | [308736,115456,14208,576] |
| 2 | [19243008,14490880,5200064,995716,79824,1] | [6706176,11799040,5473584,1047616,88300,2684] | [5053440,3608768,872192,87472,3120] | [413952,158720,20032,832] |
| 3 | [44646400,39516672,14832512,2952456,316272,15946] | [6137856,7480320,3084384,563904,46760,1416] | [2217984,1597824,391424,39840,1440] | [180736,70656,9088,384] |

The positive constant gives P>0 even when some or all parameters are zero.
Thus H>0 throughout m,t,v>=0. Dividing by the positive factor64(1+t)^3
proves the theorem on a<=b<2a-2. The previously established middle-tail
theorem covers the boundary and larger b, completing the proof.

The two nonnegative terms account for the only negative monomials in
the raw expansion. For example its top m^6 coefficient is

```text
270t^3-279t^2+45t+126
 =9(1+2t)[14(1-t)^2+5t+t^2].
```

The m^5 coefficient at v=0 becomes a positive-coefficient cubic after
subtracting308t(t-1)^2. The full table verifies the residual identity
coefficientwise, not through sampling of parameter values.

## Spectral consequence and remaining region

The established quotient identity gives

```text
h_C(0)=-abc(a+b+c)(a+b+c+ab+ac+bc)<0.
```

Together with h_C(2)>0 this supplies a positive quotient root in `(0,2)`.
For all-even triples an integer spectrum cannot contain one. For permutations
of `(1,3,2)/(3,3,0)` modulo four, the earlier root-distribution arguments
also exclude one under the assumption of an integer spectrum. Consequently
all these triples with minimum>=8 and c>=9a/4-8 are nonintegral. Complement
and universal-class lifts transfer the conclusion to the ideal intersection
graph. This conditional exclusion does not assert that h_C(1) is always
nonzero in the mixed classes; other endpoint-one cases remain separate.

For fully distinct integer endpoint-two zeros with a>=8, combine the new
bound with [root geometry](endpoint-two-surface-geometry.md), the
[small-middle-gap theorem](endpoint-two-small-middle-gaps.md) and the
[growing-gap theorem](endpoint-two-growing-gap.md). The remaining region
must satisfy

```text
d=b-a>=5,  a<2d^2+20,  b<beta(a)<2a-2,  b<c<9a/4-8.
```

These conditions are necessary, not a characterization. General integer
endpoint-two feasibility, the other quotient roots, other endpoint-one
cases and full Q3 remain open. The repeated `(10,10,12)` endpoint zero
lies below the new cutoff14.5 and is preserved. The fixed pair `(20,22)`
has its real root in `(32,33)`, also below its new cutoff37.

## Exact verification

With SymPy 1.14.0, run

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_sharp_maximum.py
```

Compare with [the certificate](../results/endpoint-two-sharp-maximum.json).
The checker reconstructs the generic six-by-six quotient, transformed
polynomial, inverse substitution, both nonnegative expressions and complete
residual. All16note vectors match the certificate. It verifies the t^3
boundary coefficient against direct substitution at b=2a-2 and the strict
improvement over the preceding maximum bound.

Eight selected direct quotient/integer-Horner/Sturm fixtures check the
minimum boundary, a fractional cutoff rounded upward, the new maximum tail,
and the boundary/beyond-boundary middle branches. Two below-cutoff controls
retain a negative endpoint and a genuine repeated endpoint zero. The finite
fixtures supplement the written unbounded identity; they are not a finite
base. No exponent or modulus range is scanned, and no floating spectra or
Lean verification are claimed. Previous proofs, checkers, certificates and
manuscript files are unchanged pending standalone review and integration.

[Return to the project entrance](../README.md).
