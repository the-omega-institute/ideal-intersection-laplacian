# Laplacian integrality of ideal intersection graphs

The [resonant discriminant obstruction](notes/four-prime-resonance-discriminant.md)
adds D_s(z)=(2s-1)^2z^2+2s^2(2s-1)^2z+s^4 as a necessary
quadratic residue at good primes ell|h=a+1-s when
v_ell(b+h)>=2v_ell(h),z=(b+h)/h^2. It excludes a double
resonance passing the previous valuation and modular tests.
In particular all a=6+25n,b=20+100n+125m,n,m>=0,c>=2a-2
give nonintegrality, without tail coprimality or ordering. The proof
uses a generic discriminant identity and the strict low-root cutoff;
no finite exponent base is required. General classification stays open.

The [shared-prime valuation theorem](notes/four-prime-shared-prime.md)
removes the tail coprimality hypothesis. For a good prime ell|a+1-s,
let e=v_ell(a+1-s),r=min tail valuation,t=max tail valuation.
If r<t, an integer root requires e=r or e=2t; if r=t, it requires
r>=1 and r<=e<=2r. In particular e=1 forces the tail gcd to
have valuation exactly one. Thus every a=156+2450n,n>=0,b,c>=a
with neither v_5(gcd(b,c)) nor v_7(gcd(b,c)) equal to one is
nonintegral. Arbitrarily large common tail divisors are allowed.
The written theorem also gives a cubic resonance condition;
general classification remains open.

The [root-valuation lemma](notes/four-prime-root-valuation.md)
proves v_ell(a+1-s)=2v_ell(bc) for any integer restricted root
s>=2, coprime tails, and ell|a+1-s not dividing s(s-1)(2s-1).
Odd good-prime multiplicities in both a-1 and a-2 exclude the low
roots 2 and 3. In particular every a=156+2450r,r>=0, with
b,c>=a,gcd(b,c)=1 gives nonintegrality. A specified example passes
both older coarse divisibilities and every p|a+1 splitting test.
This written unbounded result also constrains second-root offsets;
no finite exponent base is required. General classification stays open.

The [coprime completion](notes/four-prime-coprime-completion.md)
proves every (a,a,b,c),a>=5,b,c>=a,gcd((a-1)(a-2),bc)=1,
nonintegral, removing all four exceptions from the preceding corollary.
An explicit tail cutoff reduces a=6,12,22 to exactly eleven quadratics,
all with nonsquare discriminants; a=7 is excluded by the existing
modular theorem. The larger tail stays unbounded. Next examine
noncoprime repeated minima and combine their low-root equations with
the remaining unique-tail conditions. General classification stays open.

The [low-root divisibility theorem](notes/four-prime-low-root-divisibility.md)
proves nonintegrality for a>=5,b,c>=a whenever neither
(a-1)|3b^2c^2 nor (a-2)|20b^2c^2 holds. The smallest genuine
restricted root lies in (1,4); these residues exclude both integer
endpoints 2 and 3. Coprime tails settle every a except 6,7,12,22.
In particular every (a,a,a+1,(a+1)^2),a=6s,s>=3,is now settled,
despite passing every preceding p|a+1 modular splitting test and
lying outside the earlier sufficient spectral regions. Next combine
these low-root divisibilities with the remaining unique-tail conditions.
General classification remains open.

The [modular repeated-pair theorem](notes/repeated-pair-modular.md)
gives necessary tail residues for arbitrary prime count: for every
prime p dividing a+1, all x^2-x-k_i must split over F_p.
Thus an odd repeated exponent with any other odd exponent always
gives nonintegrality. For odd p, each 1+4k_i must be a quadratic
residue, including zero. The written tensor-splitting lemma supplies
the unbounded proof. In particular, every (a,a,2a,2a^2+1), odd a>=5,
is excluded outside the prior sufficient spectral regions. Next combine
these modular restrictions with the remaining tail-candidate conditions.
General classification remains open.

The [unique positive tail-root theorem](notes/four-prime-unique-tail.md)
reduces positive (a,a,b,c), b<c, to at most b-1 possibly integral
tails per fixed (a,b), halving the preceding bound. A complete positive
identity proves the linear coefficient of each candidate quadratic
strictly positive. Its leading coefficient must be negative, leaving
exactly one positive real tail root per retained offset. The retained
offsets form a contiguous initial segment; at a=b=5 only t=6,7,8
remain. Next analyze square discriminants and numerator divisibility
uniformly, or impose a second restricted root. General classification
remains open.

The [harmonic second-root window](notes/four-prime-harmonic-tail.md)
places kappa_2 between a+b+1 and a+1+2bc/(b+c),for b<c.
Only b-1 integer offsets remain,leaving at most2(b-1)quadratic
tail candidates per fixed(a,b),independent of repeated a. For
a>=3,the positive constant-term cutoff sharpens to H_(2b-1).
The wider window can contain integers; general classification
remains open. Next analyze these reduced integer-root conditions
uniformly,without tail scans. Previous results retain their scopes.

The [quadratic tail reduction](notes/four-prime-tail-reduction.md)
limits possibly integral positive(a,a,b,c)tails to at most2((a+1)b-1)
quadratic integer-root candidates for each fixed(a,b),with no ordering
between a,b. A positive constant-term divisor identity also gives
c<=U[U+a(d-1)+a^2b],d=(a+1)b,U=floor(d^2/4),improving the
previous cutoff by a factor greater than128. Complete29candidate-row
arithmetic and one explicit cubic interval settle every(5,5,5,c),c>=1.
The uniform reduction is a written proof; the fixed-pair corollary
retains its exact finite arithmetic. General classification stays open.

The [effective large-tail theorem](notes/four-prime-large-tail.md)
proves every positive(a,a,b,c)nonintegral when
c>24(M+a)^3(3M+a),M=(a+1)(b+1),without ordering a,b.
Two distinct bounded restricted roots and a leading tail quadratic
that cannot have two integer roots give the written proof. Consequently
each fixed(a,b)has only finitely many possibly integral tails.
The explicit bound is conservative; the remaining unbounded
classification stays open, with no parameter scan needed for this result.

The [even-gap midpoint theorem](notes/four-prime-even-midpoint.md)
proves every positive(a,a,b,b+r),even r>=2,8ab>=(2a+1)r^2,
nonintegral, including equality and without ordering a,b. A restricted
root lies between consecutive integers a+b+r/2 and a+b+r/2+1.
The sufficient threshold halves the previous weighted bound for even
gaps. Four small-tail polynomial identities also complete every
positive tail-gap-four vector; all positive gaps one through four
are now settled. General single-pair classification remains open.

The [weighted midpoint theorem](notes/four-prime-weighted-midpoint.md)
proves every positive(a,a,b,b+r),r>=3,4ab>=(2a+1)r^2,nonintegral,
including equality and with no ordering between a,b. A complete128-term
positive identity improves the previous square bound to
b>=(1/2+1/(4a))r^2. Four written small-tail cubics also complete every
positive tail-gap-three vector. Thus gaps one through three are settled;
general single-pair classification remains open.

The [single-pair midpoint theorem](notes/four-prime-single-pair-midpoint.md)
proves every positive(a,a,b,b+r),r>=2,b>=r^2,nonintegral, with a
restricted root in(a+b+(r+1)/2,a+b+(r+2)/2). Consecutive half-integer
grid endpoints exclude integer roots. The repeated exponent a is
arbitrary and the tail gap r is unbounded. A generic positive midpoint
identity and complete91-coefficient negative lower-endpoint identity
prove the region, including b=r^2. The families(a,a,2a,2a+r),r>=3,
a>=r^2,add coverage outside the previous sufficient regions.

The [single-pair small-gap theorem](notes/four-prime-single-pair-small-gap.md)
proves every positive (a,a,b,b+r), r=1 or 2, nonintegral, with no
ordering or size condition on a,b. A restricted root lies in
(a+b+1,a+b+2), giving a graph eigenvalue in(V-a-b-1,V-a-b).
Two generic endpoint factorizations and one positive midpoint identity
supply the written proof. The families(a,a,2a,2a+r),a>=5,add coverage
outside the balanced, product-tail and small-exponent criteria.

The [single-pair balanced theorem](notes/four-prime-single-pair-balanced.md)
proves every four-prime vector (a,a,b,c), a<=b<=c<=2a-6, nonintegral,
including unequal tails. Four positive leading-minor identities for the
genuine 4x4 restriction give 3<kappa_min<4. Independently, every
repeated-minimum vector a>=5,b,c>=a has kappa_min<4. The unequal-tail
balanced region is outside the product-tail and small-exponent criteria.
General single-pair and fully unequal four-prime classification stays open.

The [double-pair completion](notes/four-prime-double-pair-completion.md)
proves every positive four-prime vector (a,a,b,b) nonintegral. Its
smallest repeated-pair witness lies in one of (1,2),(2,3),(3,4), with
complete exponent thresholds. Two unique-positive-root cubics have
unbounded consecutive-integer brackets, supplemented by eight fixed
bracket rows. This settles the entire double-pair transition without
an exponent rectangle base; general single-pair and fully unequal
four-prime vectors remain open.

The [unequal-double-pair theorem](notes/four-prime-double-pair-balanced.md)
proves every (a,a,b,b) with a<=b<=2a-6 nonintegral. A genuine second-swap
cubic restriction has its smallest eigenvalue in (3,4); complete positive
identities cover the entire two-parameter region, including its boundaries.
Both repeated-pair orientations fail the earlier product-tail condition,
and all coordinates fail the small-exponent criterion. The offset-six
interval cannot be replaced uniformly by five. The subsequent completion
settles all double pairs; the wider four-prime classification remains open.

The [four-prime diagonal theorem](notes/four-prime-diagonal.md) proves
every (a,a,a,a), a>=5, nonintegral, with smallest repeated-pair eigenvalue
in (3,4) and a graph eigenvalue in (V-3,V-2). A second coordinate-swap
reduces the restriction to a cubic; complete positive expansions give
the unbounded interval. Earlier unit/pair-two/three/four results cover
the other positive a. This diagonal family is outside the product-tail
and small-exponent criteria and is now completely settled.

The [repeated-pair product tail](notes/repeated-pair-product-tail.md) gives
a uniform sufficient condition for every repeated exponent a and every
prime count t>=4, including its equality boundary. For four primes,
bc>=(a^2-1)(b+c)+(a-1)(2a-1) supplies a graph eigenvalue in (V-1,V).
In particular every (a,a,b,c) with a>=2 and b,c>=2a^2-1 is nonintegral.
The diagonal tail is outside the earlier small-exponent criterion;
for a>=5 it also avoids all previous fixed pair-two/three/four cases.
This is a supporting written theorem, not a full higher-prime classification.

The [pair-four theorem](notes/four-prime-pair-four.md) proves every
four-prime vector (4,4,b,c), b,c>=2, nonintegral. Its restricted
eigenvalue lies in (1,4); endpoint two never occurs, and endpoint
three has only the pair {b,c}={2,6}, handled by an explicit cubic
root in (7,8). This supporting result uses a complete unbounded
endpoint reduction with fixed arithmetic and does not enlarge the
current manuscript while its core organization is under discussion.

The [three-prime consolidation diagnostic](notes/three-prime-tensor-consolidation.md)
derives the two-dimensional tensor restriction and explains its limitation:
Professor Nikandish's existing boundary family has an entirely integral
restricted spectrum for arbitrarily large repeated exponents. A separate
dependency guide gives the established minimum-seven hybrid classification
core and identifies auxiliary arithmetic that it does not invoke.

Public workspace for the follow-on collaboration between **Haobo Ma,
Reza Nikandish and Wenlin Zhang**, studying ideal intersection graphs of
`Z_n` and their Laplacian spectra.

Our first question is the **Laplacian integrality characterization**:
which graphs in this family have only integer Laplacian eigenvalues?
Every positive three-prime exponent vector is now nonintegral; the
nonsquarefree higher-prime classification remains open.

For any number of prime factors t>=3, a
[unit exponent](notes/unit-exponent-any-prime-count.md) gives a noninteger
graph eigenvalue in (V-1,V). A connected complement with a pendant class
has an explicit Rayleigh quotient (4B+A)/(4B+2A)<1. This written proof
requires no finite base and leaves higher-prime vectors with every
exponent at least two as the remaining nonsquarefree domain.

For an arbitrary distinguished exponent m, the
[three-collection Rayleigh compression](notes/small-exponent-rayleigh.md)
extends this obstruction whenever A>=(m^2-1)B-(m-1), including equality,
where A is the product of the other exponents and B is their proper-support
weight. For m>=2, every other exponent at least m^2(t-1) suffices. This
settles unbounded all-exponents-at-least-two families for every prime
count t>=4, while Q3 outside this sufficient criterion remains open.

For four prime factors, every vector
[(2,2,b,c), b,c>=2](notes/four-prime-pair-two.md) is nonintegral.
An antisymmetric four-dimensional invariant subspace has its smallest
restricted eigenvalue between one and three. The only possible integer
endpoint pair is {b,c}={5,8}; its remaining cubic is irreducible modulo17.
This written proof covers (2,2,2,2) and needs no finite exponent base.

The [pair-three theorem](notes/four-prime-pair-three.md) proves every
(3,3,b,c), b,c>=2 nonintegral as well, with a graph eigenvalue in
(V-2,V) different from V-1. Tensor normalization gives a general lower
bound for the repeated-pair operator, and the exponent-three endpoint
equation has no integer solution. Two complete positive expansions,
eight fixed nonsquare discriminants and two rational factorizations
settle the unbounded domain without an exponent rectangle scan.

The [largest-root unit interval](notes/largest-root-unit-interval.md)
proves bc+a+b+c<lambda_max<bc+a+b+c+1 for real3<=a<=b<=c,
b-a>=3,c>=a²-a. On endpoint one, the established sum bound supplies
this maximum condition. Written gap1/2 brackets cover the other
fully distinct endpoint-one cases at minimum>=8. Together with the
repeated, small-minimum and endpoint-two results, this completes the
three-prime nonintegrality classification. The combined theorem retains
the27562/8658historical finite bases; the new interval has a written
unbounded proof and complete positive coefficient identities.

An [independent audit](notes/three-prime-independent-audit.md) reconstructs
eight generic determinant identities directly from disjoint supports using
standard-library integer polynomial arithmetic, checks all 40 manuscript
coefficient rows, and verifies coverage and integrity of the two historical
finite bases. It does not rerun their discriminant or determinant calculations.

The subsequent [five structural checks](notes/three-prime-referee-checks.md)
include a dependency diagram and a fresh complete rerun of both historical
large bases, with byte-identical CSVs, independent five-term coefficient
extracts, explicit small-gap uniqueness, and the integer-anchor domain.

The [smaller finite-input audit](notes/three-prime-small-certificate-audit.md)
reruns the earlier minimum-three, repeated-exponent and minimum-two
checkers. Independent integer determinants also verify all 325 minimum-three
pairs, eight root-free cubic certificates and the minimum-two rational endpoints.

The [total-sum gap](notes/total-sum-spectral-gap.md) strengthens the
three larger-root bound to lambda_4>a+b+c for real2<=a<=b<=c,
with the sharp exception lambda_4=6 at(2,2,2). On endpoint one at
minimum>=4, the total-sum gap and exact quartic coefficients also
give N/D<mu_1<N/(D-NR), with R=2/s+1/(A-U-2s), U=min(c,a+b).
The three established controls reduce23divisor candidates to4;
all four exact values are nonzero. These are written spectral and
coefficient bounds, not a full integer-splitting classification.

The [global pair-sum gap](notes/global-pair-sum-separation.md) proves
lambda_3<a+b<=b+c<lambda_4 for every real 2<=a<=b<=c, counting
multiplicity. On endpoint one at minimum>=4 this places the three
larger quartic roots strictly above b+c, alongside the smallest-root
window (a,min(c,a+b)). Principal interlacing and a negative determinant
give a written proof; five fixed exact controls supplement it. The
remaining quartic integrality problem and full Q3 stay open.

The [structural review](notes/structural-closure-review.md) gives a written
proof for the entire region d=b-a>=1,a>=2d²+20,c>b, across all residues
and parities, with no finite exponent base. This region was already
recorded as a broader consequence; written endpoint-two tails remove its
unnecessary dependence on the global finite base. The review assesses
the spectral, descent and covering routes without extending the49-page
manuscript. Further residue additions are paused while a global structural
route and manuscript scope are considered.

The [exceptional-prime proof](notes/endpoint-one-equality-thirteen.md)
now requires b=104mod169 for an integral equality spectrum on the
q=-1mod13 branch with13 dividing b. The refined congruence
Delta=13b²-18b³ mod13^(4v_13(b)) gives an odd valuation in every other
class. In particular13² cannot divide b on this negative branch.
The positive branch at13 retains its three simple local roots; the
remaining b=104mod169 class needs a further discriminant analysis.
This is a written unbounded obstruction with exact symbolic checks.

The [local splitting theorem](notes/endpoint-one-equality-local-splitting.md)
now completes the cubic test at odd primes p|b, except the negative branch
at p=13. The q=1modp branch always splits over Z_p by three simple Hensel
lifts. The q=-1modp branch splits exactly when13 is a residue modulo p;
its two colliding roots differ by valuationv_p(b). In particular, the two
surviving b=0mod5 rows pass splitting modulo every power of five. Higher
five-power tables alone cannot exclude them. This is a written local result.
For every fixed b in5Z_5, both rows also have unique local curve points
with split cubics, so simultaneous curve-and-splitting tests cannot exclude
them at any finite five-power modulus. These are local points,
not a global integer splitting theorem or an integer-point construction.

The [local discriminant proof](notes/endpoint-one-equality-local-discriminant.md)
excludes an integral equality spectrum whenever an odd prime p divides b,
a²=1modp and 13 is a nonresidue modulo p. In particular neither7nor11
may divide b. The negative branch has Delta=13b² modp^(3v_p(b)), so
its normalized discriminant detects an obstruction despite Delta=0modp.
It removes two earlier modulo-five compatibility rows, leaving
{(2,0),(3,0),(0,2),(3,2)}. This uniform written proof needs no finite base;
the equality curve and full Q3 remain open.

The [modulo-five splitting proof](notes/endpoint-one-equality-mod-five.md)
now excludes every permutation of `(1,1,2)` or `(1,4,4)` modulo five,
without size, gap or endpoint hypotheses. On the equality curve G=0,
integral splitting requires b!=1mod5; its six initial compatibility pairs
are refined to four by the local discriminant theorem above.
One excluded cubic has square discriminant modulo five but is irreducible;
the root equation adds information beyond the discriminant-square test.
The complete fixed-prime tables and independent determinant checks are saved.
The working manuscript on [PR3](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/3)
has already integrated the endpoint-two completion; this branch retains
the separate research notes and their exact evidence.

The [explicit equality cubic](notes/endpoint-one-equality-cubic.md) now
gives its three coefficients and discriminant in a,b. Generic determinant
and Sylvester identities are checked exactly. At each known integer equality
point, divisors above a+b and a quadratic square test decide integral
splitting. Square cubic discriminant alone is necessary, not sufficient;
Siegel finiteness and computable Riemann-Roch spaces supply no exhaustive
integer-point list here. That global arithmetic step remains open.

The [endpoint-two completion](notes/endpoint-two-completion.md) now settles
**every all-even exponent triple**, and every permutation of `(1,3,2)` or
`(3,3,0)` modulo four, with no size/gap/ratio bound. On an endpoint-two zero
at minimum>=40, a written proof puts another quotient root in `(4,5)`.
A complete8,658triple necessary base excludes fully distinct endpoint-two
zeros at minima8through39, independently checked by integer Horner and6x6
Bareiss determinants. Earlier repeated/minimum<=7results handle the other
cases. The global completion uses finite computation; remaining endpoint-one
classes and full Q3 stay open. Standalone manuscript integration awaits review.

The remaining [endpoint-one geometry](notes/endpoint-one-geometry.md) now
has an exact fixed-pair real existence test and a unique simple exponent
root c>b. Its middle threshold lies in(2a^2-a-2,2a^2-a-1) at a>=8.
Every ordered endpoint-one zero also requires **b+c<4a^2-2a**; beyond
this sum cutoff a root in(0,1)proves nonintegrality without a parity
hypothesis. These are written unbounded results, with no finite base.
General integer endpoint-one feasibility and full Q3 remain open.

The [endpoint-one growing-gap theorem](notes/endpoint-one-growing-gap.md)
now excludes every integer endpoint-one solution for d=b-a>=1,
**a>=2d^2+20**, by an exact unit-width bracket for its unique real
exponent c>b. Gaps1and2 are excluded already at every a>=8. Combining
the written endpoint-one/two brackets proves nonintegrality for every
parity pattern at **d>=5,a>=2d^2+20**, with no finite base. The structural
review above extends the written evidence scope to all d>=1 in this
quadratic-threshold region. The additional gaps1/2 consequence at all
minima>=8 retains its earlier finite dependencies.
Any fully distinct integer spectrum at minimum>=8 would now require
**d>=3,a<2d^2+20**, in addition to the existing endpoint-one bounds.
Full Q3 and the remaining endpoint-one region stay open.

The [minimum-eight completion](notes/minimum-eight.md) now certifies
nonintegrality for **every triple with minimum exactly eight**. Written
reductions leave precisely108middle exponents11through118on endpoint one.
The complete fixed-pair certificate brackets each unique real exponent
between consecutive integers, with216independent6x6Bareiss boundary
checks and216exact Sturm counts, covering every integer c>b. Endpoint
two is excluded here by the written maximum cutoff, without its global
finite base. The theorem requires the108pair finite certificate; the
cumulative minimum<=8result also retains the earlier27562triple base.
Full Q3 remains open, with remaining minimum at least nine.

The [endpoint-one spectral gap](notes/endpoint-one-spectral-gap.md) now
proves that, for real exponents at least eight on h_C(1)=0, **one is a
simple smallest positive quotient root and all four other roots exceed
four**. A complete350termpositive identity proves residual-quartic
positivity on the closed interval[0,4], without a finite base. This is
actual spectral simplicity, distinct from exponent-root uniqueness.
The gap does not itself exclude integer spectra; the remaining quartic
must be studied above four. Full Q3 stays open.

The [endpoint-one divisor window](notes/endpoint-one-divisor-window.md)
answers the constant-term and upper-bound questions: F(0)=rs(p+s)>0,
and weighted principal interlacing gives the second smallest nonzero
quotient root strictly below c for every ordered positive real triple.
On endpoint one at minimum>=8, the smallest quartic root lies in (4,c).
An integer spectrum therefore requires a divisor of rs(p+s) in [5,c-1]
to vanish in F. Exact checks on the three established controls find none.
This is a finite test per fixed triple, not a global surface decision.

The [minimum-dependent endpoint-one theorem](notes/endpoint-one-minimum-root.md)
strengthens the window to **a<mu_1<c**, and proves root one simple with
all four other roots above a, for every real 4<=a<=b<=c on endpoint one.
A written comparison proves b+c>=2a²-2a+1, with equality exactly at the
repeated boundary; determinant sign and interlacing then count exactly
two quotient eigenvalues below a, zero and one. This uses no finite base
or minimum-eight positivity certificate. Integer candidates now lie in
[a+1,c-1]; three established controls leave252nonzero evaluations.
The unbounded surface and full Q3 remain open.

The [pair-sum upper bound](notes/endpoint-one-pair-sum-window.md) now gives
lambda_3<a+b for every ordered positive real triple, by interlacing with
a four-support principal block. On endpoint one at real minimum>=4,
the smallest quartic root therefore lies in **(a,min(c,a+b))**.
Hypothetical integer spectra require a divisor of rs(p+s) in that window.
The three established controls leave only23candidates, all nonzero under
exact evaluation. No finite base or new nonintegrality family is claimed;
the unbounded surface and full Q3 remain open.

The [constant-divisibility analysis](notes/endpoint-one-constant-divisibility.md)
proves **12 divides F(0)** on every integer endpoint-one triple, and the
greatest common divisor of the constants over the full surface at
minimum>=4 is exactly 12. The known repeated boundary also gives infinitely
many divisors inside the smallest-root window that are not spectral roots.
Thus the splitting problem must use F(d)=0 alongside divisibility and size.
These are written unbounded results; the fully distinct region remains open.

The [root-congruence analysis](notes/endpoint-one-root-congruences.md)
shows that window candidates can give either sign: F(21)>0 at (20,20,741).
Integer roots must additionally satisfy N/d=D modulo d and three congruences
from exact evaluations at a,b,c. Together these necessary conditions leave
one of the existing 23 candidates, which still fails exact F evaluation.
The fully distinct sign question and global splitting problem remain open.

The [middle-exponent location theorem](notes/endpoint-one-middle-root.md)
refines the smallest-root window on real endpoint one at minimum>=4.
If c+a>b(b+2), the smallest residual root exceeds b; if c+a<b(b+2),
exactly one residual root lies below b. Integer candidates therefore lie
in (b,min(c,a+b)) or (a,b), respectively. At equality the
[equality theorem](notes/endpoint-one-equality-root.md) identifies b as
the simple smallest residual root; integer feasibility and splitting
of the remaining cubic stay open. The [equality pair-sum gap](notes/endpoint-one-equality-second-root.md)
now puts all three remaining roots strictly above a+b, even proving
lambda_4>a+b off endpoint one. The [equality curve analysis](notes/endpoint-one-equality-curve.md)
gives geometric genus ten and integer-point finiteness, without a point list.
The [quotient descent check](notes/endpoint-one-equality-quotient.md) rules out
extra rational involutions on its known genus-three quotient; other low-genus
maps and Jacobian ranks remain unclassified.
The proof
uses determinant sign and principal interlacing, with no finite base.

The [higher-coefficient analysis](notes/endpoint-one-root-hierarchy.md)
adds necessary tests modulo d^3 and d^4; the quadratic and exponent tests
reject all23existing candidates. The earlier infinite boundary candidate
d=3a/2 fails the linear test uniformly. Both E sign regimes and E=0 points
occur at arbitrarily large real minima, with no integer-feasibility claim.
The equality subfamily has an explicit Diophantine equation G(a,b)=0.
These results do not establish sufficiency or close full Q3.

A standalone [middle-diagonal inertia restriction](notes/endpoint-two-middle-inertia.md)
narrows the endpoint-two problem without further congruence lifting. For
`4<=a<b<c`, `(b-2)(a+b+c-2)<=2ac` supplies a positive quotient root in `(0,2)`.
This proves nonintegrality for all-even triples and the mixed patterns
`(1,3,2)/(3,3,0)` modulo four. The consolidated manuscript is unchanged.

The [full endpoint-two determinant](notes/endpoint-two-middle-tail.md) now
excludes every `b>=2a-2` for ordered `4<=a<=b<=c`: its endpoint polynomial
is strictly positive and gives a root in `(0,2)`. Every endpoint-two zero
therefore requires `b<2a-2`. Nonintegrality follows in the same three parity
classes; the other endpoint-one cases remain open.

The [sharper maximum tail](notes/endpoint-two-maximum-tail.md) now proves
`c>=3a-4 => h_C(2)>0` for ordered minimum at least four. Every endpoint-two
zero therefore requires both `b<2a-2` and `c<3a-4`, replacing the earlier
maximum bound `c<7a-16+40/(a+2)`. Full Q3 remains open.

The [endpoint-two root geometry](notes/endpoint-two-surface-geometry.md)
now gives an exact existence test and a unique real c>b solution for
each fixed a>=8,b>=a that passes it. The middle threshold is a unique
cubic root beta(a)<2a-2. Minimum eight has no fully distinct endpoint-two
solutions; at (a,b)=(20,22) the sole real c lies between32and33, excluding
every integer endpoint-two solution for that pair.

The [gap-two integer-feasibility result](notes/endpoint-two-gap-two.md)
extends this to every ordered `(a,a+2,c)` with integer a>=8,c>a+2:
endpoint two never occurs. A uniform unit-width real-root bracket proves
the infinite tail a>=20; a complete twelve-pair exact computation covers
8<=a<=19. Nonintegrality follows in the all-even and stated mixed classes;
other endpoint-one cases and arbitrary middle gaps remain open.

The [growing-gap integer exclusion](notes/endpoint-two-growing-gap.md) now
allows an unbounded middle difference d: for real `d>=5,a>=2d^2+20,b=a+d`,
the unique endpoint-two solution c>b lies in `(2a+d-11,2a+d-10)`.
For integer exponents this excludes endpoint two throughout the stated
family. The complete domain has a written coefficient-positivity proof,
with no finite base required. Nonintegrality follows in the all-even and
stated mixed classes; general endpoint-two feasibility remains open.

The [small-middle-gap theorem](notes/endpoint-two-small-middle-gaps.md) now
excludes endpoint two for every integer `(a,a+d,c)` with a>=8,1<=d<=4,c>a+d.
Gaps1,3,4 use written infinite tails and a complete76pair finite base;
gap2 uses its preserved theorem. With the growing-gap result, every fully
distinct integer endpoint-two zero at minimum>=8 must have **d=b-a>=5 and
a<2d^2+20**. General feasibility in this remaining region stays open.

The [nine-fourths maximum bound](notes/endpoint-two-sharp-maximum.md)
now improves the whole endpoint-two region at minimum>=8 to **c<9a/4-8**,
strictly below the preceding3a-4bound. Two nonnegative square expressions
and a complete84term positive residual prove h_C(2)>0 beyond this cutoff
throughout the unbounded real domain, with no finite base or exponent scan.
The remaining fully distinct integer region requires d>=5,a<2d^2+20,
b<beta(a),b<c<9a/4-8. General integer feasibility stays open.

## First results

We prove nonintegrality for every squarefree integer with at least three
distinct prime factors and for every exponent vector that is a permutation
of `(1,1,k)`, `k >= 1`. This completes the squarefree composite classification:
the integral case is exactly two prime factors, including the edgeless graph.
Read [the proofs and exact verification scope](notes/integrality-obstructions.md).
Reza's [further infinite family](notes/repeated-exponent-family.md) covers
`(a,a,(a-1)(2a-1))`, `a >= 2`, including `(2,2,3)`. Its antisymmetric block
has integer eigenvalues; a symmetric cubic proves nonintegrality.
We now prove nonintegrality for **every `(a,a,b)`, a,b >= 1**:
read [the complete repeated-exponent proof](notes/repeated-exponent-completion.md).
We also prove nonintegrality for **every `(1,b,c)`, b,c >= 1** using the
general six-support complement quotient:
[read the proof and exact diagnostic](notes/one-unit-exponent.md).
The same quotient now settles **every `(2,b,c)`, b,c >= 1**:
[read the minimum-two proof](notes/minimum-two.md). Thus every triple
with minimum exponent at most2 is nonintegral.
We now also settle **every `(3,b,c)`, b,c >= 1**, and prove the uniform
cutoff **`c >= 4a^2 - 2a`** for ordered `2 <= a <= b <= c`:
[read the cutoff and minimum-three proof](notes/distinct-tail.md).
Thus every triple with minimum exponent at most3 is nonintegral.
The subsequently [requested finite-region run](notes/open-region-diagnostic.md)
exhausts all27,562remaining triples at minimum4,5,6,7. Every discriminant
is independently verified nonsquare by integer Sylvester determinants.
Together with the written cutoff, **every triple with minimum exponent
at most7 is now certified nonintegral**; this extension uses the complete
finite computation.
An inertia argument now also settles **every triple whose maximum minus
minimum is at most3**, and **every `(a,a+3,a+4)`, a>=1**:
[read the low-eigenvalue proof](notes/low-spectrum.md).
It counts two complement eigenvalues below3 and excludes the integers
1 and2 with positive polynomial factors and four complete modular certificates.
For **every `4<=a<=b<=c`**, a uniform comparison now places a positive
complement quotient eigenvalue in `(0,3)`. If
**`(a-2)(a+b+c-2)>2bc`**, a root lies in `(2,3)`, proving nonintegrality.
In particular, **minimum exponent `a>=3r+8`, with span `r=c-a`, suffices**:
[read the uniform comparison and balanced-region proof](notes/mixed-inertia.md).
This written argument allows unbounded spans and does not enlarge any scan.
Arithmetic arguments now also settle **every triple with gcd at least3**,
**every all-odd triple**, and explicit common-residue classes, including
**common residues1,3,4 modulo5**:
[read the divisibility and congruence proofs](notes/arithmetic-obstructions.md).
These results allow arbitrarily large exponent ratios and differences.
Scaling now also settles **every triple whose exponents are all congruent
to two modulo four**, and hence **every triple with equal 2-adic valuations**:
[read the parity and divisibility contradiction](notes/even-exponent-congruence.md).
This includes gcd-two triples inside the remaining even region.
Reza's requested endpoint diagnostic now has a complete independent
certificate for **all66pairs `4<=a<b<=15`, with every integer `c>b`**.
Neither endpoint vanishes. With the low-root theorem and earlier cases,
**every triple whose second-smallest exponent is at most15 is nonintegral**:
[read the corrected diagnostic and exact scope](notes/endpoint-surfaces-diagnostic.md).
An integer complement root at two now forces the linear bound
**`c<7a-16+40/(a+2)`** for ordered `4<=a<=b<=c`. Every all-even triple
beyond this bound is nonintegral; **`c>=7a-12` suffices at minimum>=8**:
[read the endpoint reduction and divisor constraints](notes/endpoint-reduction.md).
The remaining triples lie within `8 <= a < b < c < 4a^2 - 2a`, outside
these families and the general inertia criterion;
the complete endpoint certificate additionally requires `b>=16`.
The full characterization remains open.
The root distributions and low-root theorem now also settle **every
permutation of (3,0,0) modulo four**, an entire one-odd-exponent class.
For mixed residue patterns **(1,3,2)** and **(3,3,0) modulo four**, integer
spectra require the same linear maximum bound as the all-even region:
**`M<7m-16+40/(m+2)`**, where m and M are the minimum and maximum.
[Read the proof and independent exact checks](notes/mixed-endpoint-roots.md).
Endpoint congruences also settle **all residue triples (2,2,2) and
permutations of (1,2,2) modulo three**:
[read the proof, full parity table and covering limitation](notes/endpoint-residues.md).
A stronger divisibility argument also settles **six mixed-parity exponent
classes modulo eight**, without bounds on sizes or ratios:
[read the three-odd-root proof](notes/mixed-parity-congruence.md).
The shifted quintic and its derivative now settle **every permutation
of (3,3,2) modulo four**, including odd exponents equal modulo eight:
[read the uniform root-distribution proof](notes/odd-root-distribution.md).
For exponent residue roles **(1,3,2) modulo four**, one main theorem now
collects the necessary conditions: **`a+c=b(b+2)mod128`**,
**`b=11or15mod16`**, and the stated binary-cubic parity condition.
For minimum m>=4, it also requires **`h_C(2)=0`** and
**`M<7m-16+40/(m+2)`**, where M is the maximum exponent.
The earlier sum congruences follow from these arithmetic conditions.
[Read the consolidated statement and proof guide](notes/manuscript-consolidation.md).
Theorem 13.5 combines all the mixed-parity exclusions and restrictions,
with one worked example in the main text. Theorem 14.1 combines the endpoint
reductions. The complete case calculations are grouped in Appendix B,
and the endpoint proofs in Appendix C. Appendix A gives grouped verification
scopes; the full per-checker catalogue remains in the optional detailed build.
Earlier notes and exact certificates remain available in the navigation below.

## Start here

| What you want | Where to go |
| --- | --- |
| Understand the first task and current status | [Research plan](RESEARCH-PLAN.md) |
| Read the consolidated working manuscript | [PDF](paper/paper.pdf) · [LaTeX source](paper/paper.tex) · [Build and section guide](paper/README.md) |
| Read the complete repeated-exponent theorem | [All (a,a,b) proof](notes/repeated-exponent-completion.md) · [Exact certificate](results/repeated-exponent-completion.json) |
| Read the unit-exponent theorem and unequal-triple diagnostic | [All (1,b,c) proof](notes/one-unit-exponent.md) · [Requested 35-case output](results/fully-distinct-diagnostic.txt) |
| Read the minimum-two theorem | [All (2,b,c) proof](notes/minimum-two.md) · [Exact certificate](results/minimum-two.json) |
| Read the uniform cutoff and minimum-three theorem | [Proof](notes/distinct-tail.md) · [Complete 325-case certificate](results/distinct-tail.json) |
| Read the inertia criterion and bounded-gap families | [Proof](notes/low-spectrum.md) · [Exact modular certificate](results/low-spectrum.json) |
| Read the uniform low-root bound and growing balanced region | [Proof](notes/mixed-inertia.md) · [Exact checks](results/mixed-inertia.json) |
| Read the common-divisor, all-odd and congruence-class theorems | [Proof](notes/arithmetic-obstructions.md) · [Exact checks](results/arithmetic-obstructions.json) |
| Read the all-two-modulo-four and common-valuation theorems | [Proof](notes/even-exponent-congruence.md) · [Exact checks](results/even-exponent-congruence.json) |
| Read the six mixed-parity modulo-eight classes | [Proof](notes/mixed-parity-congruence.md) · [Exact checks](results/mixed-parity-congruence.json) |
| Read the uniform (3,3,2) modulo-four family | [Proof](notes/odd-root-distribution.md) · [Exact checks](results/odd-root-distribution.json) |
| Read the linear endpoint-two bound and all-even tail | [Proof](notes/endpoint-reduction.md) · [Exact checks](results/endpoint-reduction.json) |
| Read the modulo-three endpoint classes and complete parity table | [Proof and covering limitation](notes/endpoint-residues.md) · [Exact residue tables](results/endpoint-residues.json) |
| Understand finite endpoint tests inside the geometric restrictions | [Scope and explicit constructions](notes/endpoint-congruence-scope.md) · [Exact identities](results/endpoint-congruence-scope.json) |
| Read Reza's requested finite-region run and minimum-through-seven result | [Report and proof](notes/open-region-diagnostic.md) · [Complete CSV](results/open-region-discriminants.csv) · [Independent verification](results/open-region-certificate-check.json) |
| Read the source preprint and original Q3 | [Zenodo DOI10.5281/zenodo.23134979](https://doi.org/10.5281/zenodo.23134979) |
| Read the requested (a,a,b) diagnostic and fixed-a theorem | [Exact diagnostic and proof](notes/aa-b-diagnostic.md) |
| Read the sharper cutoff and complete a=5,6 families | [Second linear cutoff](notes/second-linear-cutoff.md) |
| Read the fixed-index divisor criterion and current cutoff | [Factor-index reduction](notes/factor-index-reduction.md) |
| Read the first checked contributions | [Nonintegrality proofs](notes/integrality-obstructions.md) |
| Read Reza's extension of the (2,2,3) case | [Repeated-exponent family](notes/repeated-exponent-family.md) |
| Read the requested endpoint diagnostic and exact scope | [Report](notes/endpoint-surfaces-diagnostic.md) · [Corrected output](results/endpoint-surfaces-corrected.txt) · [Complete certificate](results/endpoint-surfaces-verification.json) |
| Read the modular endpoint script review and corrected candidate logic | [Review](notes/modular-endpoints-review.md) · [Full root sets](results/modular-endpoints.json) · [Independent verification](results/modular-endpoints-verification.json) |
| Read the higher-modulus diagnostic and its period-eight limit | [Review](notes/higher-2adic-moduli-review.md) · [Original output](results/higher-2adic-moduli-original.txt) · [Independent verification](results/higher-2adic-moduli-verification.json) |
| Read the conditional derivative thresholds and new sum-congruence family | [Proof and review](notes/higher-derivatives-review.md) · [Requested output](results/higher-derivatives-original.txt) · [Independent verification](results/higher-derivatives-verification.json) |
| Read the stronger weighted-sum condition for the remaining sum class | [Proof](notes/odd-root-lift.md) · [Exact certificate](results/odd-root-lift.json) |
| Read the clustered-root value, derivative and third-shift conditions | [Proof](notes/clustered-odd-roots.md) · [Exact certificate](results/clustered-odd-roots.json) |
| Discuss a conjecture or share a checked argument | [Project issues](https://github.com/the-omega-institute/ideal-intersection-laplacian/issues) |
| Review proposed additions | [Pull requests](https://github.com/the-omega-institute/ideal-intersection-laplacian/pulls) |
| Read the previous joint paper | [Binary subspace orthogonality project](https://github.com/the-omega-institute/binary-subspace-orthogonality) |

## Current status

We have agreed to start with Q3, the integrality question proposed by Reza.
The graph convention has been reviewed. The working manuscript consolidates
the squarefree classification, the `(1,1,k)` family, Reza's boundary family,
the successive linear cutoffs, and the complete fixed-exponent families.
Reza's diagnostic request now has exact output for all 90 requested pairs.
The repeated-exponent family is now completely settled: every `(a,a,b)`
with positive exponents is nonintegral. For square antisymmetric
discriminant, the boundary and factor indices 1,2,3 have complete proofs
and finite modular certificates. Every later index forces
`b <= (a-5)(2a-5)/(4a+5)`, strictly below a uniform cubic sign threshold;
a root lies between the consecutive integers `2ab-1` and `2ab`.
The earlier cutoffs and fixed-a checks remain as intermediate results.
The complement quotient now also settles every triple with a unit exponent.
Reza has hand-checked the repeated-exponent completion identities and gap.
Two positive-coefficient expansions and a single rational interval now
settle every triple with an exponent of two, as well.
The uniform endpoint cutoff reduces the remaining pairs for any fixed minimum
exponent to a finite set. For minimum3, the derived 325 pairs have complete
integer sign certificates; positive endpoint expansions and one rational
exception close the whole family. No arbitrary parameter cutoff is used.
The Schur-complement inertia criterion now counts two low eigenvalues
without relying on a sign change. Four complete bounded-gap families use
38 root-free modular residues to exclude integer endpoints; no minimum-exponent
scan is needed. In particular every triple with exponent span at most3 is settled.
Reza's requested finite range at minima4through7 is now completely certified:
all27,562discriminants pass independent integer determinant reconstruction
and strict square brackets. The original and complement quotient signs
are kept separate. With the cutoff this certifies every minimum-entry<=7 triple.
The mixed-sign Schur complement now has a uniform positive root below3
for every minimum exponent at least4. The lower endpoint inequality
`(a-2)(a+b+c-2)>2bc` places a root in `(2,3)` and settles a growing
balanced region, including every minimum `a>=3(c-a)+8`.
In the remaining region `8 <= a < b < c < 4a^2 - 2a`, any integral graph
must satisfy `h_C(1)h_C(2)=0`. These two endpoint-zero surfaces are the
next mathematical question; the necessary condition does not classify them.
The new arithmetic theorems restrict the remaining triples to gcd1or2,
at least one even exponent, and residues outside the proved congruence classes.
The endpoint-two surface now has the strict linear bound
`c<7a-16+40/(a+2)`. Every remaining all-even triple has gcd2 and obeys
this bound. The two endpoint equations also give exact divisor candidates
for a fixed pair `(a,b)`; the candidate still has to satisfy the equation.
Every possible integral triple also has unequal 2-adic valuations. In
the remaining all-even region, at least one exponent is divisible by four
and at least one is congruent to two modulo four.
The requested endpoint certificate excludes every middle exponent through15;
remaining triples have `b>=16`. The absence of roots in the66pair domain
does not establish a global absence of integer points on either surface.
nonsquarefree vectors with more than three prime factors also remain open.

The source preprint is public on
[Zenodo](https://doi.org/10.5281/zenodo.23134979). Its general spectral
reduction and equal-exponent results motivate this follow-on work.
We link the source PDF; private correspondence remains outside this repository.

## How we work

We use short cycles of conjecture, proof or counterexample, and independent
verification. Each contribution states its assumptions and separates written
proofs, exact finite computations and Lean verification.

The initial work is to fix the graph convention and spectral reduction,
then develop the integrality argument. Vertex connectivity may become a
companion result if it fits naturally; other invariants and unequal-exponent
matrix questions remain later directions.

Use one focused pull request for each checked contribution, with a readable
explanation and reproducible evidence where relevant. Existing collaborator
edits are preserved. See [rights and provenance](RIGHTS.md).
