# Constant divisibility and infinitely many divisor candidates

Let C be the six-support complement quotient and h_C(x)=det(xI-C)/x.
For positive integer exponents put s=a+b+c, p=ab+ac+bc, r=abc and
N=rs(p+s). On endpoint one, h_C(1)=0, the residual quartic has F(0)=N>0.

**Uniform divisibility.** Every integer endpoint-one triple satisfies

```text
12 divides N.
```

**Sharpness on the full surface.** Over all ordered integer triples
4<=a<=b<=c on endpoint one, the greatest common divisor of their constants
N is exactly 12. No fixed prime at least five divides all those constants;
neither an additional factor two nor an additional factor three is universal.
This sharpness concerns the full endpoint-one surface, including the already
settled repeated-exponent family. It does not determine the greatest common
divisor on the narrower, still-open fully distinct region.

**Infinitely many window candidates.** For every a=6k, k>=1, the known
endpoint-one boundary triple

```text
(a,a,c), c=(a-1)(2a-1),
```

has the integer d=3a/2 as a divisor of N inside its smallest-root window
(a,min(c,2a))=(a,2a). Nevertheless F(d)<0, so d is not a root. Thus
constant-term divisibility and the window alone cannot make all candidate
lists empty beyond a threshold. The equation F(d)=0 remains essential.
These are written unbounded statements, with no parameter scan or finite base.

## The factor four

The generic endpoint polynomial is symmetric in the exponents. Modulo two,
h_C(1) is one on both all-even and all-odd residue triples, and zero on
the six mixed patterns. Therefore an integer endpoint-one triple has mixed
parity. If two exponents are even, r is divisible by four. If exactly one
is even, both r and s are even. In either case 4 divides N.

This uses the basic parity evaluation of the existing determinant, not a
new sequence of higher two-adic lifts.

## The factor three

If an exponent vanishes modulo three, r is divisible by three. Otherwise
the following complete unordered nonzero-residue table suffices, by symmetry:

| Residues | s modulo 3 | p+s modulo 3 | N modulo 3 | h_C(1) modulo 3 |
|---|---:|---:|---:|---:|
| (1,1,1) | 0 | 0 | 0 | 2 |
| (1,1,2) | 1 | 0 | 0 | 0 |
| (1,2,2) | 2 | 1 | 2 | 1 |
| (2,2,2) | 0 | 0 | 0 | 1 |

The only pattern with N nonzero modulo three has h_C(1)=1 modulo three,
so is excluded on endpoint one. Thus 3 divides N. Combining the coprime
factors gives 12 divides N.

## Why the common divisor is exactly twelve

On the known repeated boundary, the constant specializes to

```text
N(a)=a²(a-1)(2a-1)(2a²-a+1)(4a³-3a²+a+1).
```

For a=36k+26, k>=0, the two-adic valuation is exactly two: a is two
modulo four and every other displayed factor is odd. The three-adic
valuation is exactly one: only 2a-1 is divisible by three, and
2a-1=3(24k+17) is not divisible by nine. All the other factors are nonzero
modulo three. This excludes universal factors eight and nine.

There is no universal factor five, since N(a)=2 modulo five when a=4
modulo five. There is no universal factor seven, since N(a)=1 modulo seven
when a=5 modulo seven. These residue classes give arbitrarily large positive
boundary triples. For any prime ell>=11, N(a) is a nonzero polynomial of
degree nine over F_ell, with leading coefficient 16. It has at most nine
roots and therefore cannot vanish on every residue class. Choose a nonroot
class and an integer a>=4 in it to obtain an endpoint-one triple whose
constant is not divisible by ell. These arguments exclude every fixed
prime beyond two and three, proving the claimed greatest common divisor.

## A divisor in the window is not a spectral root

Let a=6k>=6 and c=(a-1)(2a-1). Then c>2a, and
d=3a/2 satisfies a<d<2a. It divides a² because a²/d=2a/3=4k is an
integer, hence divides N(a). Exact specialization of the residual gives

```text
F(3a/2)=-a²(4a²-2a-1)T(a)/16,
T(a)=8a⁵+48a⁴-132a³+95a²-32a+4.
```

For a=4+m with m>=0,

```text
T(4+m)=8m⁵+208m⁴+1916m³+8239m²+16920m+13428>0.
```

Also 4a²-2a-1>0, so F(3a/2)<0 throughout this unbounded family.
The repeated-exponent theorem already proves these graphs nonintegral.
The new point is the persistence of divisor candidates: a common factor
of N, or a size comparison alone, cannot replace testing F(d).

The [checker](../scripts/check_endpoint_one_constant_divisibility.py)
reconstructs the generic determinant, its complete eight-pattern parity
table and 27 residue triples modulo three, the boundary factorization,
valuation specializations and the two positive identities used above.
Only the three established controls (8,8,105),(9,9,136),(20,20,741) are
used as finite fixtures. The [certificate](../results/endpoint-one-constant-divisibility.json)
records the exact residue values and source hashes. The infinite conclusions
have written proofs; the tables and controls are exact diagnostics.
Full Q3 and the fully distinct splitting problem remain open. No higher
two-adic shift, exponent range scan, floating spectrum or Lean is used.
