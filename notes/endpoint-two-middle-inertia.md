# A middle-diagonal restriction on the endpoint-two problem

For ordered, fully distinct exponents `4<=a<b<c`, write `s=a+b+c` and
`k_t=s-2-2abc/[t(t-2)]`. If **`k_b<=0`**, the complement quotient has
a positive eigenvalue strictly between zero and two.

Consequently, each of the following has a nonintegral ideal intersection
graph whenever **`(b-2)(s-2)<=2ac`**:

- All-even exponent triples.
- Permutations of `(1,3,2)` modulo four.
- Permutations of `(3,3,0)` modulo four.

For the mixed patterns, exclusion of the integer root one is conditional
on an integer spectrum, as in the existing [mixed-endpoint proof](mixed-endpoint-roots.md).
We do not assert that their endpoint value at one is always nonzero.
This result uses the established Schur complement; it requires no new
congruence lift, exponent scan or endpoint-zero enumeration.

## Proof of the interval statement

The existing symmetric quotient has Schur complement at two

```text
K(2)=diag(k_a,k_b,k_c)-vv^T,
v=(sqrt(a),sqrt(b),sqrt(c)).
```

Its lower eliminated block `diag(a,b,c)-2I` is positive definite.
The function `k_t` strictly increases for `t>2`, so `k_a<k_b<=0`.
The principal two-by-two block on a,b has negative trace and determinant

```text
k_a k_b - a k_b - b k_a > 0.
```

Indeed the first two summands are nonnegative and the last is strictly
positive. This block is negative definite, including the boundary `k_b=0`.
Thus K(2) has at least two negative eigenvalues. Sylvester's law of inertia
gives at least two quotient eigenvalues strictly below two. Exactly one is
zero because the complement support graph is connected; the others are
positive. At least one therefore lies in `(0,2)`.

If all exponents are even, C/2 is an integer matrix, so a hypothetical
integer spectrum of C has only even roots by the rational-root theorem.
For the two mixed patterns, the previously established shifted-quintic
identity forces every hypothetical odd root to be three modulo four.
In either case an integer spectrum cannot contain one. The positive
root in `(0,2)` therefore contradicts integrality. The complement and
universal-class lifts transfer this obstruction to the original graph.

## A strict sandwich for a possible integer spectrum

For any of these three classes, an integer spectrum would require

```text
(a-2)(s-2) < 2bc,
(b-2)(s-2) > 2ac,
h_C(2)=0.
```

The middle inequality is the new interval consequence. The earlier
balanced-region theorem excludes `k_a>0`. At `k_a=0`, strict ordering
gives `k_b,k_c>0` and the rank-one determinant formula gives

```text
det K(2) = -a k_b k_c != 0.
```

Thus two is not an eigenvalue on that boundary either. The uniform
positive root in `(0,3)`, together with the conditional exclusion of one,
rules it out. Hence `k_a<0<k_b<k_c` is necessary.

On a compatible endpoint-two zero, the diagonal is nonsingular and
`F(2)=1-a/k_a-b/k_b-c/k_c=0`. The existing mixed-inertia formula gives
one negative eigenvalue and a one-dimensional kernel for K(2).
Therefore **two must be the smallest positive quotient eigenvalue and
must be simple** under the integer-spectrum assumption. This does not
settle whether the other four positive eigenvalues can all be integers.

## An explicit middle-dependent tail

When `b<2a+2`, the new exclusion is equivalently

```text
c >= U(a,b) = (b-2)(a+b-2)/(2a-b+2).
```

When `b>=2a+2`, its left-hand expression is always positive for positive c,
so this particular criterion excludes no triples. For the stated three
classes a possible integer spectrum must satisfy both `c<U(a,b)`, when
applicable, and the earlier `c<R(a)=7a-16+40/(a+2)`.

The all-even examples `(20,22,40)` and `(20,22,46)` illustrate respectively
the equality boundary and strict exclusion. Here U=40 while R=1384/11.
The mixed example `(19,23,52)` has residues `(3,3,0)` and U=840/17,
below R=2497/21. These examples have middle exponent above15 and minimum
above7, gcd1or2, unequal2-adic valuations, and lie outside the old sufficient
balanced exclusion and beyond the bounded-gap families. They illustrate
the new inequality; we do not claim that every earlier arithmetic criterion
fails for these individual examples.

## Strengthening the principal-block test

The same block can remain negative definite when `k_b>0`. Put

```text
Delta_ab = k_a k_b - a k_b - b k_a.
```

If `k_a<0` and `Delta_ab>0`, its first diagonal entry `k_a-a` is
negative and its determinant positive, so it is negative definite.
The interval and nonintegrality conclusions above still apply. Thus in
the surviving sign region `k_a<0<k_b`, an integer spectrum in the stated
classes also requires **`Delta_ab<=0`**.

For `(a,b)=(20,22)`, exact expansion gives

```text
(a-2)(b-2) Delta_ab = 40(13c^2-414c-720).
```

The quadratic is 232 at c=34 and increases thereafter. Also `k_a<0`
for c>=34. Hence every integer c>=34 is excluded in the stated classes;
in this fixed pair they are all-even triples, so a remaining largest
exponent must be even and at most32. This improves the preceding c<40
bound without enumerating c. The old outside-criterion example `(20,22,38)`
is covered by this stronger test, although its middle diagonal is positive.

## The b boundary and the arithmetic overlap

The interval theorem itself has no hypothesis `b<2a+2`. That condition
arises solely when solving `k_b<=0` for a positive upper tail in c:

```text
(b-2)k_b = (b-2)(a+b-2)+(b-2-2a)c.
```

For b>=2a+2 the right side is positive, so this sufficient condition
cannot hold. Moreover

```text
k_b-b = a-2+c(1-2a/(b-2)) > 0.
```

On the remaining branch `k_a<0`, this gives
`Delta_ab=k_a(k_b-b)-a k_b<0`. Thus the stronger principal a,b block test
also does not exclude that branch for b>=2a+2. The ordering always gives
`k_a<k_b`; its difference does not change sign at this boundary. A further
reduction of the full secular equation, rather than repeated application
of this particular principal block, is needed there. These sign conditions
alone have not been proved contradictory.

The subsequent [full determinant argument](endpoint-two-middle-tail.md)
now excludes this entire branch, and more: `b>=2a-2` implies `h_C(2)>0`.
This is a separate positivity argument for the full endpoint polynomial;
the limitation of the principal a,b test described above remains valid.
The [maximum-tail refinement](endpoint-two-maximum-tail.md) further requires
`c<3a-4` on the remaining endpoint-two zero surface.

The geometric and arithmetic excluded sets overlap. For example,
`(17,19,50)` is in the excluded modulo-eight row `(1,3,2)` and has
`k_b(2)=-16`, so both methods apply. The geometric criterion is not
contained in those six modulo-eight rows: it covers all-even examples
and `(19,23,52)`, whose residues are `(3,7,4)` modulo eight and `(3,3,0)`
modulo four. Their congruence and geometric restrictions should therefore
be used together, without treating them as disjoint or claiming that an
example escapes every earlier arithmetic theorem.

The finite endpoint-congruence limitation concerns selected endpoint-value
tests and the explicitly listed filters. It does not prove that every
possible two-adic root-distribution method fails. Closing endpoint two
would still leave the general mixed-parity endpoint-one problem unless
that surface is separately excluded.

## Exact verification and remaining scope

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_two_middle_inertia.py`
with SymPy1.14.0 and compare the output with
[the certificate](../results/endpoint-two-middle-inertia.json).

The checker reconstructs the generic complement quotient and its rational
Schur congruence, verifies the middle-bound and zero-diagonal determinant
identities, and checks selected strict, equality, strengthened-principal-block,
overlap and outside-criterion
fixtures by exact rational principal minors and integer characteristic
polynomials with Sturm counts. The outside fixture `(20,22,38)` is
deliberate: failure of the first sufficient inequality does not imply integrality
or absence of a root in `(0,2)`. It is now covered by the stronger principal
block test. The `(20,22,33)` control is outside both tests but still has a positive
root in `(0,2)`, so neither test is necessary for that interval. The existing repeated endpoint-two control
`(10,10,12)` is outside the distinct-exponent hypothesis.

The proof is an unbounded interval argument. The fixtures are finite exact
checks, not the proof or an enlarged scan. No Lean verification is claimed.
The surviving endpoint surfaces, full Q3 and higher-prime nonsquarefree
vectors remain open. This standalone note leaves manuscript files unchanged
pending coauthor review and integration.
Reza has since deferred manuscript closure while structural work is informative;
standalone deductions remain separate for review before integration.
