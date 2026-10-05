# Unit intervals for repeated pairs with tail gap one or two

**Theorem.** For four distinct primes and any positive integers a,b,
each exponent vector (a,a,b,b+r), r in {1,2}, gives a nonintegral
ideal intersection graph. Its repeated-pair restriction has an
eigenvalue kappa in (a+b+1,a+b+2), and the graph has an eigenvalue in
(V-a-b-1,V-a-b), where V=(a+1)^2(b+1)(b+r+1)-2.

No ordering or relative-size condition on a and b is needed. In
particular the two unbounded families (a,a,2a,2a+r), a>=5, lie
outside the earlier balanced and product-tail regions, and every
coordinate fails the small-exponent criterion. This is additional
coverage among the recorded results, not a literature-priority claim.

The proof uses a different root from the smallest-root witness when
a>=5 and b>=a. It therefore establishes these families even where
the smallest root's possible integer endpoints two and three have
not been excluded. General single-pair and fully unequal four-prime
classification remains open.

## Restriction and graph transfer

Use the established graph convention: nonzero proper ideals of Z_n
are adjacent exactly when their intersection is nonzero. The
[general repeated-pair construction](four-prime-pair-three.md)
gives a genuine four-dimensional complement restriction K-I,
in the tail-support order empty,{4},{3},{3,4}:

```text
K = [(a+1)(b+1)(c+1)+a, ac,          ab,          abc]
    [a,                   (a+1)(b+1), ab,          0  ]
    [a,                   ac,          (a+1)(c+1), 0  ]
    [a,                   0,           0,          a+1].
```

The symmetrizer is D=diag(1,c,b,bc). Thus K is similar to a real
symmetric matrix. The paired support functions have weighted sum
zero. Complement reflection and restoration of the a^2bc-1 universal
vertices lift each K eigenvalue kappa to V+1-kappa, with
V=(a+1)^2(b+1)(c+1)-2. These remain genuine invariant-subspace
eigenvalues, not a Rayleigh compression. No second-swap cubic is used
when b!=c.

Put p(x)=det(xI-K). We use two generic endpoint factorizations and,
for tail gap two, one positive intermediate value.

## A root window for every unequal tail

Direct expansion gives the exact identities

```text
p(a+b+1)=ab(b-c)(a+b+1)(abc+ab-ac+bc),
p(a+c+1)=-ac(b-c)(a+c+1)(abc-ab+ac+bc).
```

For positive integer a,b,c with b<c, both final factors are positive:

```text
abc+ab-ac+bc = ac(b-1)+ab+bc > 0,
abc-ab+ac+bc = ab(c-1)+ac+bc > 0.
```

It follows that p(a+b+1)<0<p(a+c+1). The intermediate value theorem
supplies a restricted eigenvalue in (a+b+1,a+c+1). For wider tail
gaps this interval can contain integers, so this general root window
alone does not imply nonintegrality.

If c=b+1, the window already has unit length. Its root is noninteger,
and the graph transfer proves the theorem for r=1.

## The gap-two intermediate value

If c=b+2, the generic lower value is still strictly negative, and
the midpoint has the complete positive identity

```text
p(a+b+2)=(2a+1)[a^2b^2+4a^2b+2a^2
                       +ab^3+5ab^2+7ab+3a
                       +b^3+4b^2+4b+1] > 0.
```

Every term in the bracket is positive for a,b>=1. Thus a root already
lies in (a+b+1,a+b+2), establishing r=2 as well. The desired graph
interval is (V-a-b-1,V-a-b) in both cases. No classification of the
other three restricted eigenvalues is required.

## Unbounded coverage outside the previous sufficient regions

Choose b=2a, c=2a+r and a>=5. These have a repeated minimum, unequal
tails, and c>2a-6, so the balanced theorem does not apply. The only
repeated value is a; the product-tail sufficient condition fails
precisely when the following margin is positive:

```text
C_r=(a^2-1)(b+c)+(a-1)(2a-1)-bc
   =4a^3+(r-2)a^2-(2r+7)a+1-r.
```

Writing a=5+u gives the complete positive identities

```text
C_1=4u^3+59u^2+281u+430,
C_2=4u^3+60u^2+289u+444.
```

Hence neither product-tail test covers these families. The
[previous comparison](four-prime-single-pair-balanced.md)
proves the small-exponent criterion fails at every coordinate of
every repeated-minimum vector a>=2,b,c>=a. It therefore fails here
as well. All coordinates are at least five, excluding the unit and
fixed pair-two/three/four results. The tails are unequal, so these
vectors are outside the completed double-pair family too.

Examples are (5,5,10,11), (20,20,40,42) and (30,30,60,62).
The proof covers arbitrary positive a,b; these examples only
illustrate the added coverage.

## Verification and remaining scope

The [checker](../scripts/check_four_prime_single_pair_small_gap.py)
verifies the generic symmetrizer, both endpoint factorizations, the
positive rewritings of their final factors, the gap-two midpoint
identity and both product-tail failure expansions. All 15 nonzero
coefficients of the expanded midpoint polynomial are positive.

Six specified controls (a,b,r)=(1,1,1),(5,1,2),(5,10,1),
(20,40,2),(7,50,1),(30,60,2) cover both gaps, smallest parameters,
a>b, repeated minima and large unequal tails. They reconstruct all
336 support-column actions, weighted zero sums, symmetry and
complement/universal lifts. Thirty-six standard-library integer
determinants independently interpolate and cross-check the six
quartics; twelve additional direct determinants check their proposed
unit-interval endpoints. Six exact Sturm counts confirm one root
in each control interval. The written proof only needs existence
from the sign change, not a general uniqueness assertion.

The [certificate](../results/four-prime-single-pair-small-gap.json)
reproduces byte-for-byte with SymPy 1.14.0 using
`python3 scripts/check_four_prime_single_pair_small_gap.py`.
It records the script and reused support-helper hashes. The unbounded
conclusion follows from the displayed identities and invariant-space
argument, not an exponent scan or finite exponent base. No expanded
vertex graph, numerical eigensolver, historical finite-base rerun
or Lean was used.

Keep the completed three-prime main manuscript focused. A next bounded
question is a repeated minimum a>=5 with tail gap at least three,
outside the balanced/product-tail regions. The new wider root window
and the established smallest-root interval (1,4) give two structural
routes, without yet excluding every integer possibility. General
single-pair, fully unequal four-prime and higher-prime nonsquarefree
Q3 remain open, as does old orthogonality n=7.
