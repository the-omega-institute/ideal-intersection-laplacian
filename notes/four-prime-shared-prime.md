# Integer-root valuations with shared tail primes

**Theorem.** Let a,b,c be positive integers and let s>=2 be an
integer root of the genuine repeated-pair restriction K(a,b,c).
Put h=a+1-s. For any prime ell dividing h and not dividing
s(s-1)(2s-1), set

```text
e=v_ell(h),
r=min(v_ell(b),v_ell(c)),
t=max(v_ell(b),v_ell(c)).
```

Then h is nonzero and the following necessary conditions hold:

| Tail valuations | Necessary root valuation |
|---|---|
| r<t | e=r or e=2t |
| r=t | r>=1 and r<=e<=2r |

There is no coprimality assumption on the tails. For the branch
e=r<t, let u be the tail with smaller valuation. Then additionally

```text
h/ell^r = (s-1)(u/ell^r) or -s(u/ell^r) modulo ell.
```

The two residues are distinct. More generally, whenever e=r>=1,
the cubic resonance condition below is necessary, including equal
tail valuations. These are necessary conditions only; satisfying
them does not assert an integer root.

**First-valuation corollary.** At any such good prime, e=1 forces

```text
v_ell(gcd(b,c))=1.
```

Both tails must be divisible by ell, and at least one must not be
divisible by ell^2. Thus a root is impossible if neither tail, just
one tail, or both tails to order at least two share that prime.

**Nonintegrality region.** For four distinct primes with positive
exponents (a,a,b,c), all vectors satisfying

```text
a=156+2450n, n>=0, b,c>=a,
v_5(gcd(b,c)) != 1 and v_7(gcd(b,c)) != 1
```

have noninteger Laplacian spectrum. The common divisor can be one,
can have arbitrary prime factors other than 5 and 7, or can include
5 and 7 each to order at least two. No finite exponent base is needed.

## The leading polynomial when the unit argument fails

Use p(x)=det(xI-K) and the
[genuine restriction and graph transfer](four-prime-single-pair-balanced.md).
The [preceding valuation lemma](four-prime-root-valuation.md) treated
coprime tails by making its polynomial quotient a unit. When a prime
divides both tails, that quotient is not generally a unit. Its exact
leading terms give the replacement argument.

Substitute a=s-1+h and define

```text
F1=(s-1)b-sc-h,
F2=sb-(s-1)c+h,
C_s=(s-1)^2(2s-1).
```

Direct integer-polynomial expansion gives

```text
p(s)=-h(s-1)F1 F2 - C_s b^2c^2 + R_s(h,b,c).
```

Every monomial h^i b^j c^k in R_s has an integer polynomial
coefficient in s and satisfies

```text
i>=1, i+j+k>=4, j<=2, k<=2.
```

The checker retains the complete remainder coefficient list, so these
bounds concern every term. In particular the homogeneous cubic is
exactly -h(s-1)F1 F2, and the only term independent of h is
-C_s b^2c^2. At b=c=0 the polynomial is h^3(s-1+2h), consistent
with the leading cubic. Zero tails here are algebraic specializations,
not graph exponent choices.

The anchor p(a+1)=-a^2b^2c^2(2a+1) shows h!=0. The good-prime
assumption makes s,s-1,2s-1 and C_s units. If r=t=0, reduction
modulo ell gives p(s)=-C_s b^2c^2!=0, so this case is impossible.

## Valuation proof

First suppose e<r. Both F1 and F2 have valuation e, from their
respective h terms. The cubic consequently has valuation 3e.
The anchor has valuation 2r+2t>3e, and every remainder term has
valuation at least 4e>3e. There is a unique lowest-valuation summand,
which cannot cancel. Thus every root has e>=r.

Next suppose r<t and e>r. By tail symmetry assume v_ell(b)=r.
The b terms make each of F1,F2 have valuation r, so the cubic
has valuation e+2r. The anchor has valuation 2r+2t. Every
remainder term has strictly larger valuation than e+2r: for i=1
its degree and tail-power bounds force valuation at least e+2r+t;
for i=2,3 or i>=4, lower bounds are respectively 2e+2r,3e+r
and 4e. All are strictly larger because e>r and t>r. Unless
the cubic and anchor valuations agree, one is uniquely smallest.
A root therefore forces e=2t. Together with the case e=r this
proves the unequal-tail row of the theorem, including r=0.

Now suppose r=t>=1 and e>r. The cubic has valuation at least
e+2r, the anchor has valuation 4r, and every remainder term has
valuation strictly greater than e+2r, by the same monomial bounds.
If e>2r, the anchor is uniquely smallest. Thus e<=2r. The case
e=r is already allowed, giving the equal-tail row.

For e=r>=1, put H=h/ell^r, B=b/ell^r and C=c/ell^r. Dividing
p(s) by ell^(3r) and reducing modulo ell removes the anchor and
the remainder. At a root this gives the cubic resonance condition

```text
-H(s-1)[(s-1)B-sC-H][sB-(s-1)C+H]=0 modulo ell.
```

When r<t, the larger tail vanishes in this reduction. The two
possible H residues are (s-1)U and -sU, with U=u/ell^r a unit.
They are distinct because their difference (2s-1)U is a unit.
This proves the additional congruence.

If e=1, unequal valuations give r=1: the alternative e=2t is
even. Equal valuations require r<=1<=2r and r>=1, also forcing
r=1. This proves the first-valuation corollary. At a prime dividing
exactly one tail, r=0<t and e=2t=2v_ell(bc), recovering the
preceding coprime-tail lemma locally.

## An unbounded region with noncoprime tails

For a=156+2450n,

```text
a-1=5(31+490n), a-2=7(22+350n),
v_5(a-1)=v_7(a-2)=1.
```

The [low-root bound](four-prime-low-root-divisibility.md) is
1<kappa_min(K)<4 for a>=5,b,c>=a. Its only possible integer
values are 2 and 3. At s=2 the prime 5 is good and h=a-1;
root 2 would force v_5(gcd(b,c))=1. At s=3 the prime 7 is
good and h=a-2; root 3 would force v_7(gcd(b,c))=1. The stated
conditions exclude both. Since the actual graph lift is
V+1-kappa_min with V=(a+1)^2(b+1)(c+1)-2, this proves
nonintegrality.

For explicit unbounded noncoprime subfamilies one can take
b=d(a+1),c=d(a+2). Their gcd is d. Any d>=2 coprime to 35
works, as does any positive multiple d of 1225. This extends the
preceding all-coprime-tail progression to arbitrarily large common
divisors, including primes shared by both tails to higher order.

For a checked example take

```text
(a,a,b,c)=(156,156,73005,48048), gcd(b,c)=3,
b=3*155*157, c=3*154*104.
```

Both earlier coarse endpoint divisibilities hold, but the prior
gcd(b,c)=1 lemma does not apply. The only prime dividing a+1 is
157. The two factor quadratics reduce to x(x-1) and (x-3)(x+2),
so all the [previous modular splitting tests](repeated-pair-modular.md)
pass as well. The new theorem excludes low roots 2 and 3. Exact
independent determinant values are

```text
p(2)=-618942518275209847040,
p(3)=-606895825753733049902060.
```

The earlier minor at three also excludes root 3 for this example;
the new good-prime argument supplies the root-2 exclusion despite
its passing coarse divisibility. This is a comparison with these
specific prior arithmetic tests, not a general priority claim.

## Verification and remaining problem

The [checker](../scripts/check_four_prime_shared_prime.py) verifies
the generic cubic/anchor decomposition against an independent symbolic
permutation determinant and the monomial bounds for every term of R_s.
Six specified positive controls all have
noncoprime tails. They verify 336 support-column actions, weighted
zero sums and symmetry, the actual complement-to-graph lift,
30 independent integer determinants reconstructing six quartics,
and six exact Sturm counts in (1,4). At every good prime in these
controls, a forbidden valuation branch predicts the exact nonzero
determinant valuation. Whenever e=r>=1, direct determinants also
check the cubic resonance residue.

The controls include unequal-tail e=r and e=2t branches, equal-tail
e>2r exclusion, and the newly admitted progression with common
divisor 1225. The (26,26,27,30) control passes every available
valuation-range test without asserting integrality. The
(156,156,71610,298375) control has permitted valuation ranges but
does not meet the progression's sufficient condition, and its
cubic resonance supplies further local information. These distinguish
necessary local conditions from sufficient nonintegrality regions.

The [certificate](../results/four-prime-shared-prime.json) is
reproducible with SymPy 1.14.0 using
`python3 scripts/check_four_prime_shared_prime.py`.
The unbounded conclusion rests on the written valuation proof,
not on the six fixed controls. No parameter scan, expanded graph,
historical finite-base rerun, floating eigenvalues or Lean validation
is used. Previous proofs and the complete eleven-row coprime
completion retain their scopes.

The valuation rows leave genuine resonant branches, and primes
dividing s(s-1)(2s-1) are outside this unit argument. Next combine
the resonances with the actual p(2)=0 or p(3)=0 equations and
the second-root offset conditions h=-t. General single-pair,
fully unequal four-prime and higher-prime classification remain open;
the three-prime main and joint manuscript-scope decisions are retained.
