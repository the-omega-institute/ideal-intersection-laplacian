# Endpoint-two nonintegrality and completion of three parity classes

Let C be the six-support complement quotient and `h_C(x)=det(xI-C)/x`.
Exponents a,b,c are in **size order**, independently of residue roles.

**Written tail theorem.** For ordered real exponents with **a>=40**, if
`h_C(2)=0`, then

```text
h_C(4)>0>h_C(5).
```

Thus a further quotient root lies strictly in `(4,5)`, proving
nonintegrality on the whole endpoint-two surface at these minima.
The theorem has no parity hypothesis and needs no finite base.

**Global integer consequence.** Every positive integer three-exponent
vector with h_C(2)=0 has a nonintegral quotient spectrum. A complete
8,658-triple finite base excludes fully distinct endpoint-two zeros for
8<=a<=39. The existing repeated-exponent theorem and minimum-through-seven
result cover the other cases. This global conclusion depends on finite
computations, including the previously recorded minimum-through-seven
certificate; it is not claimed as a purely written all-triples theorem.

**Parity-class completion.** Every all-even exponent triple, and every
permutation of `(1,3,2)` or `(3,3,0)` modulo four, has a nonintegral
ideal intersection graph. There is no bound on sizes, gaps or ratios.
These classes reduce to endpoint two under an integer-spectrum assumption;
the global endpoint-two obstruction now closes that alternative.
Other endpoint-one classes and full Q3 remain open.

## Two difference identities

Write `D_4=h_C(4)-3h_C(2)` and `D_5=4h_C(2)-h_C(5)`.
They cancel the common leading symmetric terms responsible for the
endpoint-two surface. Put `s=a+b+c`, `p=ab+ac+bc`, `r=abc`. The exact
generic quotient identities are

```text
D_4=2r^2-2s^2r-2sp^2-2pr-6s^2p-4s^3
    +120s^2+72sp+36sr-624s-4p^2-168p-4r+928,
D_5=9s^3+12s^2p+6s^2r+3sp^2+9p^2+3pr
    -279s^2-168sp-87sr+1683s+468p+9r-2997.
```

The proof below gives complete positive-coefficient identities for both
differences, rather than relying on their leading terms or numerical roots.

## The upper sign at five

For arbitrary a,b,c>=8, set `a=8+m,b=8+t,c=8+u`, with m,t,u>=0.
The polynomial D_5 has **44 nonzero terms, all with positive coefficients**,
including constant4629843. The complete vectors are listed below, with
each vector giving ascending powers of m in the coefficient of t^i u^j.
A zero vector denotes an absent component.

| i | j=0 | j=1 | j=2 | j=3 |
|---|---|---|---|---|
| 0 | [4629843,996483,67377,1353] | [996483,186366,10395,156] | [67377,10395,417,3] | [1353,156,3] |
| 1 | [996483,186366,10395,156] | [186366,29079,1239,12] | [10395,1239,30] | [156,12] |
| 2 | [67377,10395,417,3] | [10395,1239,30] | [417,30] | [3] |
| 3 | [1353,156,3] | [156,12] | [3] | [0] |

Consequently D_5>0 for all exponents at least eight. On h_C(2)=0 this
gives h_C(5)<0. No upper ratio bound or ordering is needed for this sign.

## The lower sign at four on the endpoint-two surface

The preserved [middle bound](endpoint-two-middle-tail.md) and
[maximum bound](endpoint-two-sharp-maximum.md) imply that an ordered
endpoint-two zero at a>=40 must satisfy

```text
a<=b<2a-2<2a,  a<=c<9a/4-8<9a/4.
```

Parameterize a larger rectangle containing this whole surface by

```text
a=40+m,
b=a(1+2t)/(1+t),  t=(b-a)/(2a-b),
c=a(4+9u)/(4(1+u)),  u=4(c-a)/(9a-4c),
m,t,u>=0.
```

Both inverse formulas and positive denominators are exact. Clearing them
gives `G=64(1+t)^3(1+u)^3 D_4`. The full polynomial G has **112 nonzero
terms, all with positive coefficients**, including constant611305472.
The complete vectors, again ascending in m for each t^i u^j, are:

| i | j=0 | j=1 | j=2 | j=3 |
|---|---|---|---|---|
| 0 | [611305472,13438528512,1669177344,83080704,2067840,25728,128] | [225809391616,101554217216,10552548352,490948992,11793920,143584,704] | [575935266816,199453648896,19487672672,881946672,20857320,251384,1224] | [218865180672,94951560192,9789841664,453837884,10879740,132278,648] |
| 1 | [181014296576,89306490880,9443545088,442607616,10675840,130304,640] | [2226833891328,644107380480,59528518784,2622449728,61045920,728192,3520] | [5054388092928,1267215288320,110831526304,4741723008,108398120,1277272,6120] | [2483032498176,647063198720,57495972608,2481039396,57022790,674384,3240] |
| 2 | [440930932736,161760308224,16049227264,731519232,17370880,209920,1024] | [4630697975808,1163490925312,101856239872,4360110016,99710080,1175200,5632] | [10376062353408,2312188925952,191477361952,7938026736,177794520,2065240,9792] | [5505239310336,1225715108864,101452569344,4204474452,94149320,1093460,5184] |
| 3 | [193009477632,77502509056,7857856000,361629184,8634112,104704,512] | [2343969284096,585405371648,51112650880,2184643072,49911296,587872,2816] | [5508276535296,1195972016128,97721281760,4018207392,89506456,1035632,4896] | [3069924728832,652290753536,52684826880,2150833004,47677022,549714,2592] |

Thus G>0 and D_4>0 throughout this rectangle. On h_C(2)=0 this yields
h_C(4)>0. Together with h_C(5)<0, the intermediate value theorem proves
a quotient root strictly between four and five. Such a root is noninteger.
This argument covers all real endpoint-two solutions above minimum forty;
their exponent c need not be an integer.

## Complete necessary finite base

For the remaining fully distinct integer triples, the geometric bounds
reduce the base to precisely

```text
8<=a<=39,  a<b<2a-2,  b<c<9a/4-8.
```

For each minimum a the largest permitted integer c is
`floor((9a-33)/4)`. There are exactly **8,658 triples** in this domain.
The base uses neither the small-gap nor growing-gap exclusions, so its
coverage does not depend on their additional finite certificates.

Every endpoint value is evaluated in two independent ways: integer Horner
evaluation of the generic cubic in c, and an integer fraction-free Bareiss
determinant of the explicit six-by-six matrix2I-C. They agree through
`det(2I-C)=2h_C(2)` in all8,658cases, and none vanishes. The complete
[CSV](../results/endpoint-two-completion-base.csv) saves both values for
every triple; the [JSON certificate](../results/endpoint-two-completion.json)
records per-minimum counts and its SHA256 hash. The smallest absolute
endpoint value in the whole base is8208.

This finite computation is the entire base required by the written tail
and geometric bounds. It does not impose an arbitrary cutoff on c or
extend an unrelated search. Minima<=7 retain their existing nonintegrality
proofs/certificates; repeated exponents retain the existing complete
[repeated-exponent theorem](repeated-exponent-completion.md).
The genuine repeated endpoint zero `(10,10,12)` is preserved. It is outside
this fully distinct base and below the written-tail threshold; its h_C(4)
is negative, so no `(4,5)` bracket is claimed for all smaller minima.

## Closing the parity classes

Suppose a graph in one of the three stated classes had an integer spectrum.
Repeated triples and minima<=7 are already excluded. In all other cases
the uniform low-root theorem supplies a quotient root in `(0,3)`.
For all-even exponents, an integer spectrum of C cannot contain one:
C/2 is an integer matrix and the rational-root argument forces integer
eigenvalues of C to be even. For the two mixed patterns, the established
root-distribution argument forces hypothetical odd integer roots to be
three modulo four, also excluding one. Thus the low root must be two.

At minima8through39 the complete finite base excludes endpoint two;
at minima>=40 the written tail supplies another noninteger root in `(4,5)`.
Either case contradicts an integer quotient spectrum. Complement and
universal-class lifts transfer the contradiction to the original graph.
The exclusion of one in mixed classes is conditional on an integer
spectrum, not an assertion that h_C(1) is always nonzero.

This settles all-even triples, including the previously remaining gcd-two,
unequal-two-adic-valuation region, and both stated mixed residue classes.
It does **not** prove that the unbounded endpoint-two surface has no fully
distinct integer points. Any such point would already have a nonintegral
spectrum, which is sufficient for Q3. The remaining endpoint-one classes,
full three-prime classification and higher-prime nonsquarefree vectors
remain open. No statement about the old binary-subspace n=7 problem changes.

## Reproduction and scope

With SymPy 1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_completion.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_completion.py --csv
```

The checker reconstructs the generic quotient, both complete positive
identities and their inverse substitutions. All32note vectors are checked
against the certificate. Every necessary finite-base triple has independent
integer-Horner/Bareiss agreement. Seven selected direct quotient/Horner/Sturm
fixtures and the repeated endpoint-zero control provide additional checks.
Both saved outputs reproduce byte-for-byte.

The written tail, new finite base and earlier finite dependencies are
separately recorded. No floating spectra or Lean verification are claimed.
Previous proofs, checkers, certificates and manuscript files remain unchanged;
the standalone completion on PR9 awaits review and manuscript integration.

[Return to the project entrance](../README.md).
