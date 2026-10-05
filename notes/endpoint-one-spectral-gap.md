# A spectral gap after the endpoint-one root

Let C be the six-support complement quotient and h_C(x)=det(xI-C)/x.

**Residual positivity theorem.** For all real exponents a,b,c>=8, define
the polynomial

```text
F(x)=[h_C(x)-x h_C(1)]/(x-1),
```

with its polynomial continuation at x=1. Then F(x)>0 throughout the
closed interval **0<=x<=4**. No ordering or parity hypothesis is needed.

**Endpoint-one spectral theorem.** If a,b,c>=8 and h_C(1)=0, then the
quotient root one is simple and is the smallest positive quotient root.
All four other quotient roots are **strictly greater than four**.

The simplicity here is actual spectral simplicity of root one, distinct
from the earlier simplicity of an exponent c solving the endpoint cubic.
Both new theorems have written proofs on their entire unbounded real
domains, with no finite base or exponent scan.

Under an integer-spectrum assumption on endpoint one, the four other
quotient roots must consequently be integers at least five. This location
result alone does not produce a noninteger root or exclude integer points
on endpoint one. Full Q3 remains open.

## The exact residual quartic

The numerator vanishes at x=1 for every parameter triple, so F is always
a monic quartic. Put s=a+b+c, p=ab+ac+bc, r=abc. The generic quotient gives

```text
F(x)=x⁴+(1-p-3s)x³+(sr+2sp+3s²-3s+1)x²
     -[r²+(s²-s+1)r+s²p+p²+s³-3s²+3s-1]x+rs(p+s).
```

In particular,

```text
h_C(x)=x h_C(1)+(x-1)F(x),
F(1)=h_C'(1)-h_C(1).
```

F is a spectral factor of h_C only on h_C(1)=0. Outside that surface,
the residual positivity identity still holds, but its roots need not be
quotient roots; no such identification is made.

## A complete positive identity on the closed low interval

F is symmetric in a,b,c, so sort the real exponents a<=b<=c and set

```text
a=8+m, b=8+m+t, c=8+m+t+u,
x=4v/(1+v), m,t,u,v>=0.
```

The inverse interval substitution is v=x/(4-x), with positive denominator
at 0<=x<4. Clearing the denominator gives

```text
G(m,t,u,v)=(1+v)⁴ F(4v/(1+v))
         =sum_(i,j,k) m^i t^j u^k sum_(ell=0)^4 g_(i,j,k,ell) v^ell.
```

The following is the complete coefficient table. Each vector gives
**ascending powers of v** in the coefficient of m^i t^j u^k. All350
coefficients in the70vectors are strictly positive; omitted monomials
are zero. The constant is2654208.

| i | j | k | Ascending v coefficient vector |
|---|---|---|---|
| 0 | 0 | 0 | [2654208,7797220,7836988,2882316,188596] |
| 0 | 0 | 1 | [651264,2000436,2147180,896892,98884] |
| 0 | 0 | 2 | [48640,158956,186612,90916,14620] |
| 0 | 0 | 3 | [1088,4028,5556,3380,764] |
| 0 | 1 | 0 | [1302528,4000872,4294360,1793784,197768] |
| 0 | 1 | 1 | [248320,796560,909936,423408,61712] |
| 0 | 1 | 2 | [13568,46408,57976,31000,5864] |
| 0 | 1 | 3 | [200,764,1092,692,164] |
| 0 | 2 | 0 | [248320,796560,909936,423408,61712] |
| 0 | 2 | 1 | [34176,115056,140592,72720,13008] |
| 0 | 2 | 2 | [1192,4328,5832,3448,752] |
| 0 | 2 | 3 | [8,32,48,32,8] |
| 0 | 3 | 0 | [22784,76704,93728,48480,8672] |
| 0 | 3 | 1 | [1984,7128,9480,5512,1176] |
| 0 | 3 | 2 | [32,128,192,128,32] |
| 0 | 4 | 0 | [992,3564,4740,2756,588] |
| 0 | 4 | 1 | [40,160,240,160,40] |
| 0 | 5 | 0 | [16,64,96,64,16] |
| 1 | 0 | 0 | [1953792,6001308,6441540,2690676,296652] |
| 1 | 0 | 1 | [399360,1275208,1446648,664984,94184] |
| 1 | 0 | 2 | [23872,80732,99284,51860,9436] |
| 1 | 0 | 3 | [400,1528,2184,1384,328] |
| 1 | 1 | 0 | [798720,2550416,2893296,1329968,188368] |
| 1 | 1 | 1 | [121792,404076,483620,242180,40844] |
| 1 | 1 | 2 | [4992,17580,22804,12836,2620] |
| 1 | 1 | 3 | [49,192,282,184,45] |
| 1 | 2 | 0 | [121792,404076,483620,242180,40844] |
| 1 | 2 | 1 | [12576,43572,55308,30204,5892] |
| 1 | 2 | 2 | [293,1088,1506,920,209] |
| 1 | 2 | 3 | [1,4,6,4,1] |
| 1 | 3 | 0 | [8384,29048,36872,20136,3928] |
| 1 | 3 | 1 | [488,1792,2448,1472,328] |
| 1 | 3 | 2 | [4,16,24,16,4] |
| 1 | 4 | 0 | [244,896,1224,736,164] |
| 1 | 4 | 1 | [5,20,30,20,5] |
| 1 | 5 | 0 | [2,8,12,8,2] |
| 2 | 0 | 0 | [599040,1912812,2169972,997476,141276] |
| 2 | 0 | 1 | [97920,323344,384336,190320,31408] |
| 2 | 0 | 2 | [4392,15288,19528,10760,2128] |
| 2 | 0 | 3 | [49,192,282,184,45] |
| 2 | 1 | 0 | [195840,646688,768672,380640,62816] |
| 2 | 1 | 1 | [22392,76464,95152,50480,9400] |
| 2 | 1 | 2 | [612,2208,2952,1728,372] |
| 2 | 1 | 3 | [3,12,18,12,3] |
| 2 | 2 | 0 | [22392,76464,95152,50480,9400] |
| 2 | 2 | 1 | [1542,5472,7164,4080,846] |
| 2 | 2 | 2 | [18,68,96,60,14] |
| 2 | 3 | 0 | [1028,3648,4776,2720,564] |
| 2 | 3 | 1 | [30,112,156,96,22] |
| 2 | 4 | 0 | [15,56,78,48,11] |
| 3 | 0 | 0 | [97920,323344,384336,190320,31408] |
| 3 | 0 | 1 | [12000,40784,50416,26480,4848] |
| 3 | 0 | 2 | [359,1280,1686,968,203] |
| 3 | 0 | 3 | [2,8,12,8,2] |
| 3 | 1 | 0 | [24000,81568,100832,52960,9696] |
| 3 | 1 | 1 | [1829,6400,8226,4568,913] |
| 3 | 1 | 2 | [25,92,126,76,17] |
| 3 | 2 | 0 | [1829,6400,8226,4568,913] |
| 3 | 2 | 1 | [63,228,306,180,39] |
| 3 | 3 | 0 | [42,152,204,120,26] |
| 4 | 0 | 0 | [9000,30588,37812,19860,3636] |
| 4 | 0 | 1 | [735,2560,3270,1800,355] |
| 4 | 0 | 2 | [11,40,54,32,7] |
| 4 | 1 | 0 | [1470,5120,6540,3600,710] |
| 4 | 1 | 1 | [56,200,264,152,32] |
| 4 | 2 | 0 | [56,200,264,152,32] |
| 5 | 0 | 0 | [441,1536,1962,1080,213] |
| 5 | 0 | 1 | [18,64,84,48,10] |
| 5 | 1 | 0 | [36,128,168,96,20] |
| 6 | 0 | 0 | [9,32,42,24,5] |

Thus G>0 for every m,t,u,v>=0, proving F(x)>0 throughout 0<=x<4.
The coefficient of v⁴ in G is exactly F(4). The last entry of every
vector is positive, including the constant188596, so the same table
also proves F(4)>0. This supplies the closed endpoint rather than
inferring strict positivity from a limiting nonnegative value.

## Real roots, the spectral derivative and the gap

Let W=diag(a,b,c,ab,ac,bc), in the established support order
1,2,3,12,13,23. For disjoint supports i,j, C_ij=-w_j; the diagonal is
the sum of adjacent support weights. Hence WC is symmetric and

```text
zᵀWCz=sum_(unordered disjoint support pairs i,j) w_i w_j(z_i-z_j)²>=0.
```

All weights are positive. The disjoint-support graph is connected: its
three singleton supports form a triangle, and every two-element support
is adjacent to its complementary singleton. Therefore WC has a
one-dimensional kernel, and C is similar to the symmetric positive
semidefinite matrix W^(-1/2)(WC)W^(-1/2). Its five nonzero quotient roots
are real and strictly positive, counted with multiplicity.

On endpoint one, h_C(x)=(x-1)F(x). Residual positivity gives F(1)>0, so

```text
h_C'(1)=F(1)>0.
```

The root one is therefore spectrally simple. All four remaining quotient
roots are roots of F, hence positive and real by the preceding weighted
selfadjoint argument. Since F is strictly positive on[0,4], none can lie
there; all four are strictly greater than four. This proves both the
smallest-root statement and the asserted spectral gap. Multiplicities of
the other four roots are not constrained by this argument.

## Consequence for the remaining problem

The earlier [endpoint-one geometry](endpoint-one-geometry.md) described
real exponent feasibility and exponent-root uniqueness. The present result
adds the spectral structure on that surface: exactly one positive root
at or below four, namely the simple root one. Finding another root in a
smaller interval below four cannot close the remaining endpoint-one cases.
The relevant remaining factor is the explicit quartic F, with all roots
above four; one must instead obstruct its splitting into integer roots,
locate a noninteger root above four, or exclude integer exponent points.

The [minimum-eight result](minimum-eight.md) retains its108pair finite
certificate. Earlier global endpoint-two completion retains its8658triple
base and earlier small-minimum certificates. This new written spectral
theorem does not remove those dependencies or change the surviving region
a>=9,d=b-a>=3,a<2d²+20,b<=2a²-a-2,b<c,b+c<4a²-2a.

Repeated endpoint-one controls(8,8,105),(9,9,136),(20,20,741)retain one
as a genuine root, with the other four above four. They remain nonintegral
by the existing repeated-exponent theorem; no new nonintegrality family is
claimed from the gap alone. Full Q3 and higher-prime nonsquarefree vectors
remain open. Manuscript integration awaits coauthor review.

## Reproduction and verification scope

With SymPy1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_one_spectral_gap.py
```

Compare with [the certificate](../results/endpoint-one-spectral-gap.json).
The checker reconstructs the generic6x6quotient, verifies the monic quartic,
its symmetric formula, derivative identity, inverse interval substitution
and closed-boundary identity. The complete350termpositive polynomial is
reconstructed from all70note vectors. Eight direct quotient/Horner/Sturm
fixtures have no residual root on[0,4]; three genuine endpoint-one controls
have exactly one quotient root there, positive derivative at one and four
remaining quotient roots above four. JSON reproduces byte-for-byte.

These finite fixtures supplement the written unbounded proofs; they are
not a finite base or parameter scan. No floating spectra or Lean verification
is claimed. All earlier notes, scripts, certificates and manuscript files
remain unchanged; the old orthogonality n=7scope is separate.

[Return to the project entrance](../README.md).
