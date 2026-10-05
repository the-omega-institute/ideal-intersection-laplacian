# Real feasibility and a sum cutoff on endpoint one

Let C be the six-support complement quotient and `h_C(x)=det(xI-C)/x`.
Labels a,b,c are in **size order**, independently of residue roles.

**Theorem.** Fix real a>=8 and b>=a. The equation h_C(1)=0 has a
solution c>b if and only if

```text
R1_a(b)=-b^3+(2a^2-a-1)b^2-3(a-1)b-(a-1)^2 > 0.
```

When it exists, the exponent c is unique and simple as a polynomial root.
There is a unique threshold gamma(a) such that feasibility is b<gamma(a),
and it has the precise bracket

```text
2a^2-a-2 < gamma(a) < 2a^2-a-1.
```

Thus, for integer a>=8,b>=a, a real solution c>b exists exactly when
**b<=2a^2-a-2**. Whether its unique real c is an integer remains separate.

**Sum-tail theorem.** For ordered real8<=a<=b<=c,

```text
b+c>=4a^2-2a  =>  h_C(1)>0.
```

Every ordered endpoint-one zero with c>b therefore requires
**b+c<4a^2-2a**, sharpening the earlier maximum-only cutoff by subtracting
b from the allowed maximum c. For integer exponents this sum tail is
nonintegral without a parity hypothesis, since h_C(0)<0<h_C(1) gives a
positive quotient root in `(0,1)`. Both theorems have written proofs on
their full unbounded domains, with no finite base or parameter scan.

## The cubic and diagonal factors

The established generic endpoint cubic, with a,b fixed, is

```text
Q(c)=h_C(1)=Ac^3+Bc^2+Dc+E,
A=a^2+b^2-1,
B=a^3-4a^2b^2+2a^2b-a^2+2ab^2+ab-3a+b^3-b^2-3b+3,
D=(a-1)(b-1)(2ab+3a+3b-3),
E=(a-1)(b-1)(a+b-1)(ab+a+b-1).
```

For a,b>=8, A,D,E are positive. Direct substitution gives

```text
Q(b)=L1_a(b)R1_a(b),  L1_a(b)=a-2b^2+3b-1<0,
2S=(L1_a(b)R1_a(b))prime,
Q(b+v)=L1R1+Sv+Tv^2+Av^3,
T=b^2(4b-4a^2+2a-1)+(5a^2+a-6)b+(a-1)(a^2-3).
```

The prime differentiates in b with a fixed. The identity for S follows
from symmetry in b,c: along b=c the derivative is twice the partial
derivative in c. Since L1 decreases for b>=a and
L1(a)=-(2a^2-4a+1)<0, its sign is strictly negative on the whole domain.

## A unique middle threshold

Normalize R1 by b squared. Its derivative is

```text
(R1/b^2)prime=-1+3(a-1)/b^2+2(a-1)^2/b^3
             <=-1+5/a<0.
```

Put `B0=2a^2-a-1`. The exact boundary values are

```text
R1_a(a)=(a^2+a-1)(2a^2-4a+1)>0,
R1_a(B0)=-2(a-1)^2(3a+2)<0,
R1_a(B0-1)=4a^4-10a^3+a^2+9a-3>0.
```

The last polynomial has strictly positive coefficients at a=8+m.
Strict decrease and these signs give exactly one threshold gamma(a),
inside `(B0-1,B0)`. Below gamma R1 is positive, above it negative.

## Existence, uniqueness and nonexistence above b

If R1>0, then Q(b)<0. Since Q(0)=E>0 and its leading coefficient is
positive, there is one root in `(0,b)` and one in `(b,infinity)`.
There is also a negative root because Q tends to negative infinity to
the left and Q(0)>0. These three disjoint intervals contain all roots
of the cubic, so each root is simple and the solution c>b is unique.

If R1<=0, then b>=gamma(a)>B0-1>a^2. The last inequality is
`B0-1-a^2=(a-2)(a+1)>0`. The normalized derivative identity gives

```text
R1prime=b^2(R1/b^2)prime+2R1/b<0.
```

Since L1,L1prime<0, the derivative identity makes S>0. The displayed
formula for T is positive at b>a^2: all three summands are positive.
Therefore Q(b+v)>0 for every v>0, since its constant L1R1>=0 and
the other coefficients are positive. This excludes every solution c>b,
including the threshold case where c=b itself is a root. Simplicity
above concerns the exponent c, not a new spectral-multiplicity claim.

## The stronger sum bound

Put `T0=4a^2-2a`. For c>=T0-b,

```text
Ac+B >= A(T0-b)+B
       =P_a(b)=-b^2+(a^2+a-2)b+K(a),
K(a)=4a^4-a^3-5a^2-a+3.
```

For a<=b<=B0, P_a is concave in b, and both endpoints are positive:

```text
P_a(a)=4a^4-5a^2-3a+3,
P_a(B0)=2(a-1)(a^3+3a^2-a-2).
```

The complete positive vectors below, in **descending powers of m** at
a=8+m, verify the three polynomial signs used in this proof.

| Polynomial | Coefficient vector |
|---|---|
| R1_a(B0-1) | [4,118,1297,6297,11397] |
| P_a(a) | [4,128,1531,8109,16043] |
| P_a(B0) | [2,68,856,4734,9716] |

Concavity therefore makes P_a(b)>0 throughout that interval. If b<gamma,
then b<B0, so c>=T0-b makes `Q(c)=c^2(Ac+B)+Dc+E>0`. If b>=gamma,
the preceding positive shifted cubic already gives Q(c)>0 for c>b.
For the remaining diagonal c=b with b+c>=T0, one has
b>=T0/2=B0+1>gamma, so Q(b)=L1R1>0 as well. This proves the sum tail
for all ordered exponents, including the diagonal.

An endpoint-one zero above b must therefore have b+c<T0. Together with
h_C(0)<0, positivity in the sum tail yields a root in `(0,1)` and hence
Laplacian nonintegrality after the usual complement/universal-class lifts.

## Scope and verification

After the endpoint-two spectral completion, remaining integer spectra at
minimum>=8 must use endpoint one. Its fixed-pair real feasibility is now
explicit, with a unique real exponent root and a precise middle threshold.
The repeated control `(9,9,136)` has a genuine endpoint-one zero, below
the sum cutoff; it is already nonintegral by the repeated-exponent theorem.
There is no claim that the endpoint-one surface is empty or that its other
roots are integers. General integer feasibility and those other quotient
roots remain the next structural questions. Full Q3 and higher-prime
nonsquarefree vectors remain open.

With SymPy 1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_one_geometry.py
```

Compare with [the certificate](../results/endpoint-one-geometry.json).
The checker reconstructs the generic quotient and endpoint cubic; verifies
diagonal factors, symmetry derivative, normalized derivative, threshold
boundaries, shifted quadratic and concave sum-bound identities. The three
complete note vectors match the certificate. Eight selected exponent cubics
have exact Sturm counts on the whole c>b interval, and the feasible cases
also have exactly one positive root below b and one negative root. Seven
direct quotient/integer-Horner/Sturm fixtures verify tail signs and retain
the repeated endpoint-zero control. The certificate reproduces byte-for-byte.

These finite fixtures supplement written infinite proofs; no finite base,
exponent scan, floating spectrum or Lean verification is claimed. Earlier
proofs/certificates and manuscript files remain unchanged pending review.

[Return to the project entrance](../README.md).
