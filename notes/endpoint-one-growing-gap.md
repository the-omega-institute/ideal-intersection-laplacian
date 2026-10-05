# Endpoint-one integer exclusion with an unbounded middle gap

Let C be the six-support complement quotient and h_C(x)=det(xI-C)/x.
Write a,b,c in **size order**, independently of residue roles, and d=b-a.

**Endpoint-one theorem.** For integer d>=1,a>=2d²+20,b=a+d, the unique
real solution c>b of h_C(1)=0 lies strictly between consecutive integers

```text
L=2a²+(2d-3)a-d²-ceil(3d/2)+1,  L<c<L+1.
```

Thus no integer c>b solves endpoint one on this entire unbounded family.
For **d=1 or2**, the same brackets hold for every integer a>=8, improving
the minimum threshold to eight. These endpoint-one statements have written
proofs throughout their domains, with no finite base or parameter scan.

**Written spectral family.** Every integer triple (a,a+d,c) with
**d>=5,a>=2d²+20,c>a+d** is nonintegral, without any parity hypothesis.
The new endpoint-one exclusion and preserved written endpoint-two growing-gap
exclusion rule out both possible integer values of the uniform root in(0,3).
This family uses only written proofs, with no finite base.

**Broader consequence.** Every triple with d>=1,a>=2d²+20,c>a+d, and every
triple with d=1or2,a>=8,c>a+d, is also nonintegral. This broader conclusion
was first obtained using the earlier global endpoint-two theorem or
small-gap certificates. The [structural review](structural-closure-review.md)
now gives a written proof with no finite base for the entire
d>=1,a>=2d²+20 region. The additional d=1or2,a>=8 conclusion retains
its earlier finite dependencies. Consequently any fully
distinct integer spectrum at minimum>=8 would require

```text
d=b-a>=3,  a<2d²+20,
b<=2a²-a-2,  b<c,  b+c<4a²-2a,  h_C(1)=0.
```

These are necessary restrictions, not a classification. Full Q3 and
higher-prime nonsquarefree vectors remain open.

## The endpoint cubic and the integer bracket

The established generic quotient gives Q(c)=h_C(1)=Ac³+Bc²+Dc+E, where

```text
A=a²+b²-1,
B=a³-4a²b²+2a²b-a²+2ab²+ab-3a+b³-b²-3b+3,
D=(a-1)(b-1)(2ab+3a+3b-3),
E=(a-1)(b-1)(a+b-1)(ab+a+b-1).
```

Set b=a+d and define the real anchor

```text
M=2a²+(2d-3)a-d²-3d/2+1.
```

For even d, L=M and U=M+1. For odd d, L=M-1/2 and U=M+1/2.
Both pairs are consecutive integers when a,d are integers. We prove four
boundary signs on larger real domains, so the parity labels select the
integer bracket but impose no congruence condition on the sign identities.

| Label | Expression G(a,d) | Real gap domain |
|---|---|---|
| even_lower | -8Q(M) | d>=2 |
| even_upper | 8Q(M+1) | d>=2 |
| odd_lower | -8Q(M-1/2) | d>=1 |
| odd_upper | 8Q(M+1/2) | d>=1 |

In each row substitute a=2d²+20+m and d=d0+t, with m,t>=0 and
d0=2for the even rows, d0=1for the odd rows. The complete positive
identities in the table below express G as sum_i m^i sum_j v_ij t^j.
Each vector gives **ascending powers of t** in the coefficient of m^i.
Every listed coefficient and constant is strictly positive; an omitted
degree is zero. This proves all four signs on their entire real domains.

| Label | i | Ascending t coefficient vector |
|---|---|---|
| even_lower | 0 | [2540926584,6605052084,8253733722,6622457331,3802505228,1645768113,551127074,144082780,29293976,4538368,513792,38656,1536] |
| even_lower | 1 | [442333800,1009155552,1083087594,733577494,348338038,121299512,31509240,6051744,832768,75008,3584] |
| even_lower | 2 | [30753528,60353640,53758926,29356604,10847912,2784656,493312,55552,3328] |
| even_lower | 3 | [1067424,1753376,1224936,495584,126144,19136,1536] |
| even_lower | 4 | [18496,24448,11984,2896,352] |
| even_lower | 5 | [128,128,32] |
| even_upper | 0 | [31525038720,54275046096,51447222400,32786855337,15500128850,5644270719,1621205030,368652292,66178600,9165312,944896,65792,2560] |
| even_upper | 1 | [6745927104,9698993304,7823043894,4178338134,1635789882,480448344,107981896,18222176,2259712,186112,8704] |
| even_upper | 2 | [600936256,692654664,460336030,196260660,60156488,13070704,2044928,205568,12032] |
| even_upper | 3 | [28524768,24710176,12897400,4006176,865856,111424,8704] |
| even_upper | 4 | [760928,440352,166736,29744,3488] |
| even_upper | 5 | [10816,3136,736] |
| even_upper | 6 | [64] |
| odd_lower | 0 | [3761110144,4901536544,4878864528,3194798344,1732219058,723570833,256537234,72224332,17237624,3168768,480000,47872,3584] |
| odd_lower | 1 | [1021253568,1110035248,983913680,543799620,254349942,86822672,25319736,5389728,966656,108288,9728] |
| odd_lower | 2 | [115465984,100484752,78093064,34531796,13480400,3429648,767872,98048,11008] |
| odd_lower | 3 | [6958144,4545040,3034872,968928,299904,44480,6656] |
| odd_lower | 4 | [235712,102720,57328,10128,2272] |
| odd_lower | 5 | [4256,928,416] |
| odd_lower | 6 | [32] |
| odd_upper | 0 | [3456425280,3933037168,3557868656,2045502576,988314476,357181199,110550294,26234644,5335368,791552,100096,7424,512] |
| odd_upper | 1 | [950746336,902595016,733023076,355799368,149872554,44342528,11487752,2070112,328704,29952,2560] |
| odd_upper | 2 | [108946816,82843752,59601332,23128796,8255264,1819632,372608,40192,4352] |
| odd_upper | 3 | [6657088,3801328,2381672,665632,192896,24640,3584] |
| odd_upper | 4 | [228768,87200,46512,7152,1568] |
| odd_upper | 5 | [4192,800,352] |
| odd_upper | 6 | [32] |

There are respectively48,49,49,49nonzero terms. The constant terms are
2540926584,31525038720,3761110144,3456425280. Thus Q(L)<0<Q(U).

The bracket lies above b. Indeed a>=2d²+20 implies a>d²+3d, since
d²-3d+20>0. Both choices of L satisfy

```text
L-b>=2a²-2a-d²-5d/2+1/2>2a²-3a+1/2>0.
```

The intermediate value theorem therefore gives a real exponent root in
(L,U) above b. The [endpoint-one geometry theorem](endpoint-one-geometry.md)
at a>=8,b>=a makes this the unique real root above b. Its simplicity is
as a root of the exponent cubic, not a spectral-multiplicity assertion.
No integer lies in the bracket, proving integer exclusion for every c>b.

## The first two gaps down to minimum eight

For d=1, put L1=2a²-a-2. Exact endpoint identities are

```text
-Q(L1)=4a(a+1)(a⁴-4a²-2a+6),
 Q(L1+1)=4a(a-1)(a+1)(a³-a²+1).
```

For d=2, put L2=2a²+a-6. The corresponding identities are

```text
-Q(L2)=16a⁵+72a⁴-76a³-433a²+69a+595,
 Q(L2+1)=4(a+2)(2a⁵-2a⁴-17a³+25a²+28a-42).
```

The following complete vectors give **descending powers of m** at a=8+m.
Unlike the preceding two-variable table, each small-gap polynomial is
unscaled: the lower row is -Q(Ld) and the upper row is Q(Ld+1).

| Label | Table index | Descending m coefficient vector |
|---|---|---|
| gap_1_lower | 0 | [4,196,3984,42984,259536,831256,1103040] |
| gap_1_upper | 0 | [4,188,3676,38280,223936,697852,905184] |
| gap_2_lower | 0 | [16,712,12468,107311,453685,753723] |
| gap_2_upper | 0 | [8,392,7916,84316,499672,1562808,2016880] |

All coefficients are positive. Also L1-(a+1)=2a²-2a-3>0 and
L2-(a+2)=2a²-8>0 at a>=8. The same sign/uniqueness argument therefore
proves the unit brackets throughout a>=8 for both gaps, without a finite
base. For d=1and2 the ceiling formula in the theorem agrees with L1,L2.

## Spectral consequences and their dependencies

The [uniform low-root theorem](mixed-inertia.md) gives a positive quotient
root in(0,3) for minimum at least four. If all quotient roots were integers,
one or two would have to be a root. When d>=5,a>=2d²+20, endpoint one is
excluded above, while the preserved
[endpoint-two growing-gap theorem](endpoint-two-growing-gap.md)
places its unique real exponent root strictly
in(2a+d-11,2a+d-10). Neither endpoint can occur at integer c. This proves
the stated spectral family entirely by written arguments, for every parity.

For d=1or2,a>=8, the earlier
[small-middle-gap theorem](endpoint-two-small-middle-gaps.md)
excludes endpoint two, retaining its
finite certificates. The original proof of the broader d>=1,a>=2d²+20 consequence used the
[global endpoint-two nonintegrality theorem](endpoint-two-completion.md)
excludes an integer spectrum even if endpoint two occurs. That theorem
retains its8658triple finite base and prior minimum<=7certificate. The
original broader route retained finite dependencies. The later
[structural review](structural-closure-review.md) removes that dependency
for the full quadratic-threshold region by using written tails only.
The gaps1/2 conclusion at all a>=8 still retains its finite certificates.
Repeated and small-minimum triples retain their existing proofs/certificates.

The genuinely repeated endpoint-one zero(9,9,136) remains a control outside
d>=1. No emptiness claim is made for the remaining endpoint-one surface.
The bracket's quadratic minimum threshold is sufficient; optimality is not
claimed. This result advances an unbounded gap region without new two-adic
shifts. Manuscript integration remains pending coauthor review.

## Reproduction and verification scope

With SymPy1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_one_growing_gap.py
```

Compare with [the certificate](../results/endpoint-one-growing-gap.json).
The checker reconstructs the generic6x6quotient and manually stated cubic,
verifies all four complete positive identities, the four small-gap signs
and all31note vectors. Eight selected exponent cubics have exact Sturm
counts on the unit bracket and full c>b interval; integer Horner values
agree with independent6x6Bareiss determinants at both bracket endpoints.
The d>=5fixtures also retain the written endpoint-two brackets. The repeated
control is preserved. JSON reproduces byte-for-byte.

These fixed fixtures supplement the written proofs; they are not a finite
base or parameter scan. No floating spectra or Lean verification is claimed.
All older notes, scripts, certificates and manuscript files remain unchanged.

[Return to the project entrance](../README.md).
