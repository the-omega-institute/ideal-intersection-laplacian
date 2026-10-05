# A uniform product tail for repeated exponents

**Theorem.** Let n have t>=4 distinct prime factors and positive integer
exponents (a,a,k_3,...,k_t). Put

```text
A = product_(i=3)^t k_i,
B = product_(i=3)^t (k_i+1),
V = (a+1)^2 B - 2.
```

If

```text
a^2 A >= (a^2-1)B + (a-1)(a-2),
```

the ideal intersection graph has a noninteger Laplacian eigenvalue in
(V-1,V). Equality is included. This is an unbounded sufficient criterion
for arbitrary repeated exponent a, not a complete higher-prime classification.

In particular, for four prime factors, every (a,a,b,c) satisfying

```text
bc >= (a^2-1)(b+c) + (a-1)(2a-1)
```

is nonintegral. For every a>=2, the entire tail b,c>=2a^2-1 satisfies
this condition. The result continues the general tensor restriction in
the [pair-three proof](four-prime-pair-three.md), rather than extending
the fixed-exponent endpoint tables to further values of a.

## The invariant space and the graph transfer

Use the established graph convention: vertices are nonzero proper ideals
of Z_n and adjacency means nonzero intersection. Remove the a^2 A-1
universal vertices. The complement F of the remaining graph H has one
independent class for each nonempty proper support S subset of [t], with
weight w(S)=product_(i in S) k_i. Its edges join exactly disjoint supports.

Write R={3,...,t}. For each function h on subsets of R, define f to have
values h(T) on {1} union T, -h(T) on {2} union T, and zero on every
other support. The two paired classes have the same weight a*w(T),
so f has weighted sum zero. Supports containing neither 1 nor 2 see
equal opposite contributions; supports containing both see none.

On {1} union T, the complement degree is
(a+1)*product_(i in R\T)(k_i+1)-1. Its nonzero-valued neighbors are
{2} union U with U disjoint from T and weight a*w(U). Consequently
the 2^(t-2)-dimensional space is invariant and F acts by K_a-I, where

```text
K_a = (a+1) tensor_(i in R) E_(k_i) + a tensor_(i in R) F_(k_i),
E_k = diag(k+1,1),
F_k = [[1,k],[1,0]].
```

In the subset basis, D=diag(w(T)) symmetrizes K_a: D*K_a is symmetric.
Thus K_a is similar to a real symmetric matrix. If kappa is an eigenvalue
of K_a, then kappa-1 is an actual F eigenvalue on a zero-sum vector.
Let N be the number of vertices of H. The identity L(H)+L(F)=N*I-J
reflects it to N+1-kappa on H. Extending the vector by zero on the
universal vertices adds a^2 A-1 to the eigenvalue, giving V+1-kappa.
This uses an invariant operator embedding, not a Rayleigh compression
or a claim that a principal submatrix eigenvalue is a graph eigenvalue.

## The lower endpoint for every repeated exponent

In the symmetric basis, F_k becomes S_k=[[1,sqrt(k)],[sqrt(k),0]].
The normalized factor T_k=E_k^(-1/2)*S_k*E_k^(-1/2) has eigenvalues
1 and -k/(k+1). Each eigenvalue of tensor_i T_(k_i) is a product of
these numbers. A negative product has absolute value strictly less than
one, so every tensor eigenvalue is strictly greater than -1.

With E=tensor_i E_(k_i), the symmetric similar matrix of K_a is

```text
E^(1/2) * [(a+1)I + a tensor_i T_(k_i)] * E^(1/2).
```

The bracket is strictly greater than I as a quadratic form. Since E>=I,
the entire matrix is strictly greater than I. Therefore kappa_min>1
for every positive a and every positive remaining exponent. This extends
the existing four-prime positivity argument to arbitrary prime count.

## The upper endpoint, including equality

Consider the empty and full subsets of R in the symmetric matrix K_a-2I.
Their principal block is

```text
P = [[(a+1)B+a-2, a*sqrt(A)],
     [a*sqrt(A),   a-1       ]].
det(P) = (a^2-1)B + (a-1)(a-2) - a^2 A.
```

If the determinant is negative, this block has a negative direction.
Extending that direction by zero and applying the variational principle
gives kappa_min<2.

If the determinant is zero, a cannot equal one, since then det(P)=-A<0.
Thus a>=2 and P is positive semidefinite and singular. In the original
weighted basis take h(empty)=a-1, h(R)=-a, and h(T)=0 elsewhere.
Both endpoint coordinates of (K_a-2I)h vanish, and its weighted Rayleigh
quotient for K_a is exactly two. But for any nonempty proper T subset R,

```text
((K_a-2I)h)(T) = a(a-1) != 0.
```

Such a T exists because t>=4. Therefore h is not a full eigenvector
at two. If kappa_min were two, every trial vector attaining that minimum
would be an eigenvector, a contradiction. Hence kappa_min<2 also here.

There is an explicit rational negative direction at equality as well.
For a chosen intermediate T, set
d_T=(a+1)*product_(i in R\T)(k_i+1)-2>0 and replace h(T)=0 by
-a(a-1)/d_T. The weighted quadratic form for K_a-2I becomes
-w(T)*a^2*(a-1)^2/d_T<0. This gives an exact trial certificate without
extracting any roots. Combining both endpoints proves 1<kappa_min<2;
its graph lift is in (V-1,V), proving the theorem.

The t>=4 hypothesis matters at equality. For t=3 the endpoint block
is the entire restriction. The known family k_3=(a-1)(2a-1), a>=2,
has kappa_min=2 and an entirely integral tensor block, as explained in
the [three-prime consolidation](three-prime-tensor-consolidation.md).
The three-prime graph is still nonintegral by other established arguments.
We do not extend this equality proof to that block.

## Four-prime consequences and comparison

Substitute A=bc and B=(b+1)(c+1) in the determinant. It becomes

```text
-bc + (a^2-1)(b+c) + (a-1)(2a-1).
```

For L=2a^2-1, b=L+u, c=L+v with u,v>=0, the negative of this is

```text
uv + a^2(u+v) + 3a-2 > 0.
```

This proves the announced uniform tail. Its diagonal subfamily (a,a,L,L)
is not covered by the earlier [small-exponent criterion](small-exponent-rayleigh.md).
For that criterion, write A_m=product_(i!=m) k_i and
B_m=product_(i!=m)(k_i+1)-1-A_m. Its failure margin is
(m^2-1)B_m-(m-1)-A_m. The only possible distinguished values are a and L;
their respective margins are

```text
4a^6-4a^4-a^3-a^2-a+2,
16a^7+12a^6-16a^5-18a^4+3a^2+2.
```

After a=z+2 their coefficient lists, in descending powers, are
[4,48,236,607,857,623,180] and
[16,236,1472,5022,10096,11923,7628,2030]. Every coefficient is positive.
Thus all four coordinate choices fail that previous sufficient criterion
for every a>=2. For a>=5 this family also contains no exponent one,
two, three or four, so the earlier unit and fixed pair-two/three/four
theorems do not supply its witness. This establishes additional coverage
within the recorded higher-prime results; it is not a literature-priority claim.

An infinite boundary family illustrating strictness is

```text
b=a^2, c=a^4+a^2-3a+1, a>=2.
```

Indeed the equality condition is
(b-(a^2-1))(c-(a^2-1))=a^4-3a+2. Even though this principal determinant
vanishes, the full restriction has kappa_min strictly below two.

## Verification and next question

The [checker](../scripts/check_repeated_pair_product_tail.py) verifies the
generic product determinant, the four-prime specialization, tail identity,
boundary family, both positive comparison polynomials, and normalized
two-dimensional characteristic identity. Seven specified controls rebuild
the invariant embedding from all proper supports: five four-prime controls
and two five-prime controls, including equality at both prime counts.
Exact leading minors verify the lower endpoint; Sturm counts verify an
interior root when the sufficient condition holds. Boundary controls also
check the rational negative direction. A three-prime equality control
checks the integral-block limitation. No expanded vertex graphs, floating
eigenvalues, exponent-range scan or Lean run are used.

The [certificate](../results/repeated-pair-product-tail.json) is reproducible
with SymPy 1.14.0 using `python3 scripts/check_repeated_pair_product_tail.py`.
The unbounded assertion rests on the written argument; the fixed controls
validate its algebra and implementation. The focused three-prime manuscript
is not enlarged by this supporting note.

The [four-prime diagonal theorem](four-prime-diagonal.md) subsequently
settles the condition-failing family (a,a,a,a). The next spectral question
is the other repeated-pair region where this product condition fails,
especially unequal double pairs with all entries at least five.
Failure of the condition does not imply an integral tensor block or graph.
Four-prime fully unequal vectors, general higher-prime nonsquarefree Q3,
and old orthogonality n=7 remain open.
