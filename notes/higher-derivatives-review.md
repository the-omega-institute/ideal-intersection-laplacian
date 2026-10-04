# Higher derivatives, conditional thresholds and a further infinite family

Reza's PR8 script was run unchanged at its requested384canonical mixed-parity
representatives in0..7. The reflected complement quintic and all three
derivatives are correct. The [original output](../results/higher-derivatives-original.txt)
is retained. Two interpretation changes are needed: zero has valuation
infinity, rather than99, and the exact valuation of a representative need
not be the valuation of every exponent triple in its residue class.
The [revised output](../results/higher-derivatives-corrected.txt) makes these
points explicit; the original symbolic construction and requested domain
are unchanged.

## What the requested output says

| Value at one | Exact valuation distribution at the384representatives |
| --- | --- |
| h | 3:96, 4:84, 5:63, 6:45, 7:18, 8:12, 9:12, 10:6, infinity:48 |
| h' | 2:240, 3:60, 4:42, 5:21, 6:6, 7:3, 9:6, infinity:6 |
| h'' | 2:192, 3:96, 4:42, 5:24, 6:6, 7:6, 8:9, infinity:9 |
| h''' | 1:384 |

There are243representatives with v2(h(1))<6. This is a diagnostic list,
not243uniform exclusions. The [certificate](../results/higher-derivatives-verification.json)
saves every exact value, all joint patterns and the corrected zero convention.
For example, (0,0,1) has h(1)=h'(1)=h''(1)=0, whereas the positive lift
(8,16,9), in the same residue class modulo eight, has all three nonzero.
Also h(3)=-2592 at(1,3,6), but h(3)=0 at(9,3,6). The first value is32mod64
and the second0mod64. Therefore a divisor64test does not in general descend
to an exponent class modulo eight, even though the divisor32test does.

## The conditional thresholds

Suppose the mixed-parity quintic has five integer roots. Its binary
factorization gives two even roots and three odd roots. If k of the odd
roots are one modulo four, then at x=1 their factors supply k factors
of four and3-kfactors of two. The product rule gives these divisibilities:

| k | Required power of two dividing h(1) | h'(1) | h''(1) | h'''(1) |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 8 | 4 | 4 | 2 |
| 1 | 16 | 4 | 4 | 2 |
| 2 | 32 | 8 | 4 | 2 |
| 3 | 64 | 16 | 8 | 2 |

At x=3, replace k by3-k. For derivative order j, each term is j! times
a product retaining5-jroot factors. Removing the odd-root factors with
the strongest guaranteed divisibility gives the displayed minima; the
factor two from2! is included. The argument also covers repeated roots
and zero values.

The coefficientwise binary factorization of h(2y+1)/8 determines k for
all twelve unordered mixed exponent patterns modulo four. The exact
checker saves this full table. For all mixed exponent parities,
**h'''(1)=2mod4**, so the third-derivative requirement is always met.
The second-derivative requirements are also always met at one and three
with this root information. The first derivative excludes36ordered
classes modulo eight, all already excluded by the earlier results.
Derivative values at one and three have coordinate period eight modulo
16,8,4for orders1,2,3respectively;36symbolic identities verify that fact.
Thus these specific second/third-derivative thresholds alone give no
new exclusions. Stronger information about the root residues can still
give stronger conditions.

## A stronger value constraint gives a new infinite family

For a=4u+1, b=4v+3, c=4w+2, coefficientwise expansion gives

```text
h(2y+1)/8 = (y+1)^3 modulo 2,
h(3)/16 belongs to Z[u,v,w],
h(3)/16 = (2v+1)(u+w+1) modulo 4.
```

If all roots were integers, the first identity would force all three
odd roots to be three modulo four. The k=0row at one, equivalently
the k=3row at three, then forces64|h(3). Since2v+1is invertible modulo
four, the last identity requires4|u+w+1. Equivalently,

```text
a+c = 15 modulo 16.
```

Consequently **every positive triple with a=1,b=3,c=2mod4 and
a+c!=15mod16 is nonintegral**, including all permutations. There is
no minimum, size or ratio bound. The condition distinguishes the
exponent one modulo four from the even exponent; it does not assume
that the variables are in increasing order.

Of the64role-ordered residue triples modulo sixteen,48are excluded
and16survive this necessary condition. The earlier divisor32test
excluded32of these64; the new condition adds16role-ordered classes,
or96ordered classes after all permutations. It does not settle the
surviving sum class. Examples(14,25,27) and(10,29,31) have h(3)=32mod64
while passing the previous divisor32test; both have gcd one, unequal
2-adic valuations and middle exponent above fifteen.

## Independent verification and scope

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_higher_derivatives.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_higher_derivatives.py
```

The [verifier](../scripts/verify_higher_derivatives.py) checks the generic
reflected quintic and its derivatives against a separately written direct
complement matrix, including permutation symmetry. For each of the384
requested representatives, it independently reconstructs derivatives
of det(xI-C) through order three by principal integer minors:
D^(j)(t)=j! times the sum of all principal(6-j)-minors of tI-C.
From D=xh it then obtains
h^(j)(t)=(D^(j)(t)-j h^(j-1)(t))/t.
The checks at t=1use42determinants per representative, with exact integer
Bareiss arithmetic. The two new fixtures at three and four lift controls
at one add252minor determinants, for16380in total. All values agree.

The infinite result follows from the written root-distribution and
divisibility proof. Symbolic identities verify the algebra for arbitrary
shifts; the64derived residue representatives display that identity's
classes. No exponent range or unconstrained modulus scan was added.
There is no Lean formalization or numerical spectrum. Full Q3 and
nonsquarefree higher-prime vectors remain open.
