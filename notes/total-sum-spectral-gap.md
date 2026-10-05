# A total-sum spectral gap and a coefficient window for the smallest root

Let C be the six-support complement quotient in support order
1,2,3,12,13,23, with real 2<=a<=b<=c. Put s=a+b+c, p=ab+ac+bc,
r=abc and h_C(x)=det(xI-C)/x. Order eigenvalues with multiplicity as
0=lambda_1<lambda_2<=...<=lambda_6.

**Theorem.** If (a,b,c)!=(2,2,2), then

```text
lambda_3<a+b<s<lambda_4.
```

At (2,2,2), lambda_4=s=6. Thus lambda_4>=s throughout the stated
real domain, with equality only at that single boundary point. This
strengthens the [pair-sum gap](global-pair-sum-separation.md) by a in
the lower bound for all three larger roots.

## Written proof of the global gap

Use the symmetric similarity S=W^(1/2)CW^(-1/2), where
W=diag(a,b,c,ab,ac,bc). The earlier four-support proof gives
lambda_3<a+b. The principal block on singleton supports 1,2, shifted
now by s, is

```text
K-sI = [[bc-a, -sqrt(ab)],
        [-sqrt(ab), ac-b]].
```

Its first leading minor bc-a>=a(a-1)>0. Its determinant is
c(abc-a²-b²), whose bracket has the ordered nonnegative decomposition

```text
abc-a²-b²
 =ab(c-b)+(a-1)(b-a)(b+a)+(a-2)a².
```

It is positive unless a=b=c=2. Away from that point both principal
eigenvalues exceed s, so interlacing gives lambda_5,lambda_6>s.

The full determinant has the symmetric identity

```text
h_C(s)=-rs V,
V=r(s+3)-sp
 =a²(bc-b-c)+b²(ac-a-c)+c²(ab-a-b).
```

Every bracket is nonnegative for exponents at least two. All three
vanish simultaneously only at (2,2,2), so V>0 elsewhere. Therefore
det(sI-S)=s h_C(s)<0. At least three eigenvalues lie below s and
at most four; its negative sign requires an odd number below it,
counting multiplicity. Exactly three lie below s, proving lambda_4>s.

At the remaining boundary the exact characteristic polynomial is
x(x-6)(x²-12x+12)². Its two quadratic roots are 6-2sqrt(6) and
6+2sqrt(6), each double. The fourth ordered eigenvalue is exactly six.
This also proves that the boundary exception cannot be dropped.

## A smallest-root interval from the quartic coefficients

On h_C(1)=0 at real 4<=a<=b<=c, write

```text
F(x)=h_C(x)/(x-1)=x⁴-Ax³+Bx²-Dx+N,
A=p+3s-1,
D=r²+(s²-s+1)r+s²p+p²+(s-1)³,
N=rs(p+s)>0,
U=min(c,a+b).
```

The earlier minimum-root and upper-window theorems, and the new gap,
give a<mu_1<U and mu_2,mu_3,mu_4>s. Define the positive rational
expression

```text
R=2/s+1/(A-U-2s)=2/s+1/(p+s-1-U).
```

**Coefficient window.** Throughout this real endpoint-one domain,

```text
N/D < mu_1 < N/(D-NR),
D-NR>0.
```

These combine with the earlier interval: every hypothetical smallest
integer root d must divide N, satisfy F(d)=0, and lie strictly between
max(a,N/D) and min(U,N/(D-NR)). There is no E-sign condition.

To prove the interval, Vieta gives

```text
D/N=1/mu_1+1/mu_2+1/mu_3+1/mu_4.
```

For three numbers x_i>s with sum T, convexity of 1/(s+y) on the
simplex y_i>=0, sum y_i=T-3s, gives the strict upper bound

```text
sum 1/x_i < 2/s+1/(T-2s).
```

Indeed the maximum on the closed simplex occurs at a vertex, where
two y_i vanish; all three are positive here. With T=A-mu_1 and
mu_1<U, the right side is less than R. The three reciprocal terms
are positive, giving 1/mu_1<D/N and 1/mu_1>D/N-R.

All denominators are positive. First A-U-2s=p+s-1-U>s because
p>1+U: for a,b,c>=4, p>=4c+ab and U<=c. Hence R<3/s.
Also r/s=1/(1/(ab)+1/(ac)+1/(bc))>=16/3>4, and

```text
D-3N/s
 =r(r-4s)+r(s²-3p+1)+s²p+p²+(s-1)³>0,
s²-3p=((a-b)²+(a-c)²+(b-c)²)/2>=0.
```

Thus D-NR>D-3N/s>0, justifying inversion and proving the claimed
strict upper bound. The proof uses exact coefficients, rather than
candidate-dependent congruence lifts.

## Supplementary fixed controls and the unresolved step

Only the three established endpoint-one controls and their existing
23 divisor candidates are filtered by the coefficient window:

| (a,b,c) | New lower endpoint | New upper endpoint | Surviving old candidates |
|---|---|---|---|
| (8,8,105) | 18955860/2163037 | 37911720/3678919 | 10 |
| (9,9,136) | 252867384/25048747 | 389837217/33407662 | 11 |
| (20,20,741) | 10492211730/423697633 | 566579433420/21410357153 | 25,26 |

All four remaining exact F values are nonzero. These controls already
follow from the repeated-exponent theorem; the reduction from 23 to
four candidates is a finite diagnostic, not a new nonintegrality family.

The [checker](../scripts/check_total_sum_spectral_gap.py) reconstructs
the generic quotient, shifted principal determinant, symmetric total-sum
identity, and coefficient identities. Six specified spectral controls,
including the exact (2,2,2) boundary and the repeated (4,4,4) control,
use direct 6x6 Bareiss determinants and Sturm counts with multiplicity.
The three endpoint-one coefficient controls use exact rational arithmetic
and direct Horner evaluation. The
[certificate](../results/total-sum-spectral-gap.json) records source hashes
and the complete checks. No parameter scan, floating spectra or Lean is used.

The next structural question is whether this coefficient window, together
with the smallest-root equation, has a uniform integer exclusion on the
remaining fully distinct endpoint-one region. Neither the global gap nor
the real coefficient window proves that exclusion. The three-prime
classification and higher-prime nonsquarefree part of full Q3 remain open.
