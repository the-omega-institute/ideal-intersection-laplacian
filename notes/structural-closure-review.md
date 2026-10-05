# A structural region and the remaining closure problem

For positive integer exponents in size order a<b<c, let d=b-a and
h_C(x)=det(xI-C)/x for the established six-support complement quotient.
There is a structural exclusion with an unbounded gap, independent of
every congruence and parity choice.

**Theorem.** Every integer triple (a,a+d,c) with d>=1,
a>=2d²+20 and c>a+d is Laplacian nonintegral. The whole region has a
written proof with no finite exponent base.

The [growing-gap note](endpoint-one-growing-gap.md) already recorded this
region as a broader consequence using the global endpoint-two theorem.
The present argument removes that consequence's unnecessary finite-base
dependency. Its purely written statement previously covered d>=5; the
same proof structure now covers every d>=1. This strengthens the evidence
scope for an existing spectral family, rather than enlarging its region.

## Proof from the endpoint-one bracket and written endpoint-two tails

The uniform low-root theorem gives a positive quotient root in(0,3).
If the spectrum were integral, either1 or2 would be a root.
The endpoint-one growing-gap theorem places the unique real exponent
solution of h_C(1)=0 above b in the open unit interval

```text
L<c<L+1,
L=2a²+(2d-3)a-d²-ceil(3d/2)+1.
```

Thus h_C(1) cannot vanish for integer c. This bracket has a written
proof for every d>=1,a>=2d²+20: its four boundary signs are complete
positive polynomial identities, and endpoint-one root uniqueness identifies
the exponent root in the bracket. No finite base is used.

If a>=40, the **real tail** of the endpoint-two theorem suffices.
At h_C(2)=0 its rectangle bounds and the112/44-term positive identities
give h_C(4)>0>h_C(5). A quotient root then lies in(4,5), contradicting
an integer spectrum. This real tail is written and does not use the
8,658-triple integer base of the stronger all-minimum theorem.

If a<40, the inequality a>=2d²+20 forces d<=3. The existing written
endpoint-two tails cover each remaining gap:

| d | Minimum forced here | Existing written tail starts | Endpoint-two exponent bracket |
|---|---:|---:|---|
| 1 | 22 | 20 | (2a-9,2a-8) |
| 2 | 28 | 20 | (2a-8,2a-7) |
| 3 | 38 | 16 | (2a-7,2a-6) |

These are open intervals between consecutive integers, above b.
Each has opposite endpoint signs throughout its stated tail, by complete
positive polynomial identities, and the established endpoint-two exponent
root uniqueness makes it the only solution above b. Hence h_C(2) also
cannot vanish at integer c in these cases.

Both possible integer values of the uniform low root are therefore
excluded, or an additional root in(4,5) contradicts integrality.
The complement and universal-class lifts give the graph conclusion.
Every step holds on its whole domain; no exceptional finite base is left.

This closes a region allowing arbitrarily large c and unbounded d.
It does not require emptiness of either endpoint surface outside the
stated hypotheses, and does not settle the remaining endpoint-one region.
The separate minimum-eight and gaps1/2-at-all-minima results retain their
actual finite dependencies.

## Assessment of the three structural routes

**Spectral route.** The endpoint-two alternative is already complete.
The theorem above supplies a structural endpoint-one exclusion across
all residue patterns. The next spectral target is therefore the fully
distinct endpoint-one region with d>=3 and a<2d²+20, together with its
existing root windows and sum bound. The residual quartic must be tested
there above a; the earlier interlacing windows alone do not force a
noninteger root. No theorem presently closes this whole remaining region.

**Descent route.** The known a/c quotient of the genus-ten equality curve
has genus three. Its good-reduction branch-stabilizer certificate excludes
an extra rational involution. Riemann-Hurwitz then also excludes every
map from that quotient over Q to a genus-two curve: such a map would have
degree at most2, and degree2 would supply the excluded involution.
This does not exclude other low-genus maps from the original genus-ten
curve, or elliptic Jacobian factors. No certified rank bound or effective
integer-point computation is available. A lower-genus descent cannot
currently be assumed as a closure step.

**Finite covering route.** The CRT construction explains why a finite
set of congruence exclusions alone does not cover the remaining region.
It does not rule out a covering that also uses spectral inequalities,
the regime split and actual root/divisor equations. Such a covering
would need explicit domains and a proof that every surviving triple
falls into one of them. No such completeness argument is established.

These findings support pausing residue-by-residue additions. They supply
an existing large-region result for a future compact manuscript synthesis,
while keeping the unresolved global question precise. The current49-page
manuscript is unchanged by this review; publication scope and submission
remain joint decisions.

## Exact validation

The [checker](../scripts/check_structural_growing_region.py) reruns the
growing-gap proof identities, all31 note vectors and its eight specified
Sturm/Horner/6x6Bareiss fixtures. It reconstructs the six-support quintic
and verifies the six small-gap endpoint-two boundary polynomials, the
112/44 positive tail identities and their saved vectors. It also rechecks
the existing120-element branch stabilizer at the fixed good prime5 for
the descent assessment. These support written arguments with distinct
scopes; they are not a parameter scan or a finite exponent base.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_structural_growing_region.py
```

Compare with [the certificate](../results/structural-growing-region.json).
The historical8,658/27,562-triple and108-pair finite certificates are
retained without rerunning them. No Jacobian rank, point enumeration,
new prime-power refinement or Lean verification is claimed. Full Q3,
higher-prime nonsquarefree cases and the old orthogonality n=7 remain open.
