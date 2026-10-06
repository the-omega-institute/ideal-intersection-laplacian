# Prime multiplicities of integer restricted roots

**Root-valuation lemma.** Let a,b,c be positive integers with
gcd(b,c)=1, and let s>=2 be an integer root of the genuine
repeated-pair restriction K(a,b,c). Put h=a+1-s. Then h is
nonzero, and for every prime ell dividing h with

```text
ell does not divide s(s-1)(2s-1),
```

one has

```text
v_ell(h)=2v_ell(bc).
```

Here v_ell(h) means the valuation of |h| when h<0. In particular,
each such prime has even multiplicity in h and divides exactly one
tail. The conclusion concerns any integer restricted root, with no
ordering hypothesis on a,b,c.

**Nonintegrality corollary.** For four distinct primes with positive
exponents (a,a,b,c), assume a>=5, b,c>=a and gcd(b,c)=1. If a-1
has a prime ell>=5 of odd multiplicity and a-2 has a prime q>=7
of odd multiplicity, the ideal-intersection graph is nonintegral.
Consequently, every such vector with

```text
a=156+2450r, r>=0,
```

is nonintegral, for every coprime pair of tails b,c>=a. This is an
unbounded written result and requires no finite exponent base.

## Polynomial identity and proof

Use the [genuine restriction and graph transfer](four-prime-single-pair-balanced.md):

```text
K = [ (a+1)(b+1)(c+1)+a   ac          ab          abc ]
    [ a                   (a+1)(b+1) ab          0   ]
    [ a                   ac          (a+1)(c+1) 0   ]
    [ a                   0           0          a+1 ].
```

Set p(x)=det(xI-K) and C_s=(s-1)^2(2s-1). The anchor identity

```text
p(a+1)=-a^2b^2c^2(2a+1)
```

shows that h cannot vanish at a root. Substituting a=s-1 in p(s)
gives -C_s b^2c^2. Polynomial division in the integer polynomial
ring therefore gives

```text
p(s)=-C_s b^2c^2+(a+1-s)Q_s(a,b,c),
Q_s(s-1,0,c)=-s(s-1)^2c^2,
Q_s(s-1,b,0)=-s(s-1)^2b^2.
```

The last two identities are obtained by the same division and
specialization; the checker records the full integer polynomial Q_s.
The specializations with a tail zero are algebraic identities, not
graph exponent choices.

Fix a prime ell satisfying the lemma. The factor C_s is a unit
modulo ell. If ell did not divide bc, the identity modulo ell would
give p(s) nonzero, contradicting the root hypothesis. Thus ell divides
bc. Since gcd(b,c)=1, it divides exactly one tail. If ell divides b,
reduce Q_s at a=s-1,b=0 modulo ell. Its value
-s(s-1)^2c^2 is a unit because ell divides neither s(s-1) nor c.
The argument for ell dividing c uses the other specialization.
Hence Q_s is an ell-adic unit. At a root the exact equation is

```text
h Q_s = C_s b^2c^2.
```

Taking valuations proves v_ell(h)=2v_ell(bc).

## Low-root exclusion and the progression

The [low-root bound](four-prime-low-root-divisibility.md) gives
1<kappa_min(K)<4 for a>=5,b,c>=a. If the graph were integral,
this genuine restricted root would be an integer, hence 2 or 3;
its graph lift is V+1-kappa_min, where
V=(a+1)^2(b+1)(c+1)-2.

For s=2, the excluded primes in s(s-1)(2s-1) are exactly 2,3,
and h=a-1. An odd multiplicity at any prime ell>=5 contradicts
the lemma. For s=3, the excluded primes are 2,3,5, and h=a-2.
An odd multiplicity at any prime q>=7 excludes this root too.
The two exclusions prove the corollary.

For a=156+2450r,

```text
a-1=5(31+490r),
a-2=7(22+350r).
```

The parenthesized factors are nonzero modulo 5 and 7 respectively,
so v_5(a-1)=v_7(a-2)=1 for every integer r>=0.

## Additional coverage beyond the previous arithmetic tests

The coprimality hypothesis here is gcd(b,c)=1. The
[previous completed region](four-prime-coprime-completion.md) instead
assumes gcd((a-1)(a-2),bc)=1. Neither of these two coprimality
hypotheses implies the other. The new result explicitly allows the
tails to share factors with a-1 or a-2, provided the tails themselves
are coprime and the odd-multiplicity conditions hold.

For a concrete comparison take

```text
a=156, b=24335=155*157, c=16016=154*104.
```

These are positive with b,c>=a and gcd(b,c)=1. Both preceding
coarse divisibilities hold:

```text
(a-1) divides 3b^2c^2,
(a-2) divides 20b^2c^2.
```

Also a+1=157 is prime, and b,c reduce to 0,2 modulo 157.
The corresponding factor quadratics are x(x-1) and (x-2)(x+1),
so the [modular repeated-pair test](repeated-pair-modular.md) passes
at every prime dividing a+1. Nevertheless the multiplicities
v_5(a-1)=v_7(a-2)=1 exclude both integer low roots. Independently,

```text
p(2)=72785938852601822540,
p(3)=-7452438203099991664332.
```

This compares the stated arithmetic tests only. In this example
both tails also exceed 2a-2, so the previous minor at three already
excludes the low root 3; the new valuation rule additionally excludes
root 2, which passes its coarse divisibility test.

## The remaining second-root equations

If an integer second restricted root is s=a+1+t, then h=-t.
Thus, for coprime tails, every prime ell dividing t with

```text
ell does not divide (a+t+1)(a+t)(2a+2t+1)
```

must satisfy v_ell(t)=2v_ell(bc). This applies to the
[unique positive tail-root reduction](four-prime-unique-tail.md)
as an additional necessary condition on its retained offsets.
It does not assert that an offset passing the condition gives a root.

## Verification and limitations

The [checker](../scripts/check_four_prime_root_valuation.py) verifies
the generic polynomial division in Z[a,b,c,s], both unit
specializations, the nonzero anchor, good-prime lists, progression
identities and second-root substitution. Six specified positive
controls verify 336 support-column actions, weighted zero sums,
symmetry and the actual complement-to-graph lift. Thirty independent
integer determinants reconstruct six quartics; six exact Sturm counts
verify one root in (1,4). Prime valuations of the nonzero endpoint
determinants independently check the unequal-summand valuation rule
for every odd good-prime witness in those controls. The comparison
example checks both older divisibilities and all required modular
factorizations.

The a=26,b=27,c=28 control lies outside the sufficient criterion:
a-1=25 has even 5-multiplicity and a-2=24 has no prime at least
seven. It illustrates a limitation, without asserting integrality.
The [certificate](../results/four-prime-root-valuation.json) is
reproducible with SymPy 1.14.0 using
`python3 scripts/check_four_prime_root_valuation.py`.
The unbounded proof does not depend on these fixed controls. No
parameter scan, expanded graph, historical finite-base rerun,
floating eigenvalues or Lean validation is used.

At primes dividing both tails, or dividing s(s-1)(2s-1), the unit
argument need not apply. These cases, along with the general
single-pair, fully unequal four-prime and higher-prime classification,
remain open. The previous eleven-row coprime completion and all
other established results retain their exact scopes. The three-prime
main and final joint manuscript decisions are unchanged.
