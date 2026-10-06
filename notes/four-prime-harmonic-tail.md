# A harmonic window for the second root

**Theorem.** For positive integer exponents (a,a,b,c) on four distinct
primes with b<c, the second eigenvalue of the genuine repeated-pair
restriction K lies in

```text
a+b+1 < kappa_2 < a+1+2bc/(b+c) < a+2b+1.
```

There is no ordering requirement between a and b. The tails can be
permuted to impose b<c; equal tails are already covered by the
double-pair theorem. If the graph is Laplacian integral, then
t=kappa_2-a-1 is an integer in [b+1,2b-1]. Thus the
[quadratic tail reduction](four-prime-tail-reduction.md) now requires
only b-1 nonzero quadratics, with at most 2(b-1) possibly integral
tails per fixed (a,b), independent of the repeated exponent a.

The window can contain integers. Root location alone therefore does
not establish nonintegrality in every case. This is a structural
candidate reduction, not a complete classification or a proof that
an integer second root forces equal tails.

## Exact endpoint identities and root index

Use the graph convention and genuine 4x4 support restriction K-I
from the preceding tail-reduction note. Let p(x)=det(xI-K),
h=a+1+2bc/(b+c), and L=a+b+1. The generic identity is

```text
p(h)=bc(b-c)^2 B(a,b,c)/(b+c)^4>0,
```

where the complete positive bracket is

```text
B=2a^3b^3+6a^3b^2c+6a^3bc^2+2a^3c^3
  +a^2b^3c+2a^2b^3+2a^2b^2c^2+6a^2b^2c
  +a^2bc^3+6a^2bc^2+2a^2c^3
  +2ab^3c^2+2ab^3c+2ab^2c^3+4ab^2c^2
  +2ab^2c+2abc^3+2abc^2
  +2b^3c^2+2b^3c+2b^2c^3+2bc^3.
```

All 22 terms have positive coefficients. The established inertia
argument gives kappa_1<a+1<h. Meanwhile the largest eigenvalue
is at least the first diagonal entry (a+1)(b+1)(c+1)+a, which
exceeds a+1+2b and hence h. Explicitly, its difference from
a+1+2b is (c-1)(a+1)(b+1)+2ab+2a+1>0.

All roots of p are real because the positive diagonal
diag(1,c,b,bc) symmetrizes K. Since p(h)>0, an even number of
roots lie below h. At least one does, and the largest lies above;
therefore exactly two lie below h, proving kappa_2<h<kappa_3.

The lower endpoint satisfies

```text
p(L)=ab(b-c)(a+b+1)(abc+ab-ac+bc)<0.
```

The last factor equals ac(b-1)+ab+bc>0. Also a+1<L<h<kappa_3,
so an odd number of roots below L can only be one. Thus L<kappa_2.
The final bound h<a+2b+1 follows from bc/(b+c)<b. This identifies
the second actual restricted root, rather than merely some root
or a Rayleigh compression.

## Candidate count and a smaller constant-term cutoff

The support embedding transfers kappa to V+1-kappa, with
V=(a+1)^2(b+1)(c+1)-2. Thus integrality forces an integer second
root. The previous necessary quadratic equation and divisibility
remain valid, but its offset now satisfies b+1<=t<=2b-1. The
constant term is

```text
H_t=t(d-t)[t(d-t)+at+a^2b], d=(a+1)b.
```

It is positive on this domain, so each of the b-1 quadratics is
nonzero and has at most two positive integer tail roots. For b=1
the domain is empty and the window itself excludes integers.

For a>=3 put T=2b-1. Since T<d/2, t(d-t) and the remaining
positive factor both increase on the whole allowed interval.
Consequently H_t<=H_T. Every integral graph in this region obeys

```text
c<=J[J+aT+a^2b], J=T(d-T), T=2b-1.
```

This is the exact maximum of the positive constant term on the
allowed integer interval when b>=2; it is not claimed to be the
optimal integrality cutoff. At a=b=5 it is 67851, compared with
111375 in the preceding reduction and 186913752 in the original
majorant. More importantly, unequal ordered tails then need only
four candidate offsets t=6,7,8,9, rather than 29. The already proved
triple-five completion retains its full earlier arithmetic records.

## Verification and remaining scope

The [checker](../scripts/check_four_prime_harmonic_tail.py) derives
the complete 22-term identity, lower endpoint, largest-diagonal
comparison and refined bound. The
[certificate](../results/four-prime-harmonic-tail.json) records six
specified support controls, 336 support-column actions, 36 independent
integer determinants reconstructing the quartics, and 18 exact Sturm
counts confirming one root below, one inside and two above each
window. Some control windows contain integers, documenting the
limit of the conclusion. No tail/exponent scan, expanded graph,
historical finite-base rerun or Lean validation is used.

The next question is to analyze the remaining b-1 quadratic integer-root
conditions uniformly as a,b vary, or combine them with another
restricted eigenvalue. General single-pair and fully unequal four-prime
classification stays open. Previous proofs and finite inputs, the
focused three-prime main and the joint manuscript-scope decision
are retained.
