# The three-prime tensor restriction and a shorter classification core

This note answers the [structural consolidation question](https://github.com/the-omega-institute/ideal-intersection-laplacian/pull/9#issuecomment-6000145701).
It gives an exact obstruction to replacing the classification by the
repeated-pair tensor block, and separates the essential classification
chain from auxiliary arithmetic. The classification and the boundary
family below are existing results; the tensor formulation here is a
diagnostic, not a new nonintegrality classification.

The shared spectral idea has two forms: Theorems 8.2 and 8.3 use
zero-sum Rayleigh trial functions (the three-collection compression
is not equitable), whereas Theorems 8.5 and 8.6 use genuine invariant
subspaces. A Rayleigh bound need not give the spectrum of a small
restricted operator.

## The two-dimensional repeated-pair block

For exponents (a,a,b), assign values h_0,-h_0 on singleton supports
{1},{2}, values h_1,-h_1 on {1,3},{2,3}, and zero on the other supports.
Paired support weights are equal, so the function has weighted sum zero.
In the disjoint-support complement F after removing a^2 b-1 universal
vertices, this is a genuine invariant subspace, with operator K-I:

```text
K = (a+1) E_b + a F_b
  = [[(a+1)(b+1)+a, ab], [a, a+1]],
E_b = diag(b+1,1),  F_b = [[1,b],[1,0]].
```

The symmetrizer is diag(1,b). A K-eigenvalue kappa gives a complement
eigenvalue mu=kappa-1 and an original graph eigenvalue V+1-kappa,
where V=(a+1)^2(b+1)-2. These conventions matter: an interval (2,3)
for mu corresponds to (3,4) for kappa.

Tensor normalization gives kappa_min>1 for every a,b>=1, exactly as
in the four-prime argument. In the weighted symmetric basis F_b
becomes S_b=[[1,sqrt(b)],[sqrt(b),0]]. The normalized matrix
T_b=E_b^(-1/2) S_b E_b^(-1/2) has eigenvalues 1,-b/(b+1).
Thus (a+1)I+aT_b>I, and the symmetric K is greater than E_b>=I.
This lower bound does not exclude integer restricted spectra.

The characteristic polynomial and two endpoint determinants are

```text
det(xI-K) = x^2 - ((a+1)(b+2)+a)x
             + ((2a+1)b+(a+1)(2a+1)),
det(K-2I) = (a-1)(2a-1)-b,
det(K-3I) = 2(a-2)(a-1)-(a+2)b.
```

### An unbounded family with an entirely integral tensor block

Take b=(a-1)(2a-1), a>=2. Then b>=a and

```text
det(xI-K) = (x-2)(x-(2a^3-a^2+a+1)).
```

Both restricted eigenvalues are integers; kappa_min=2 exactly.
Their complement values and original graph lifts are integers too.
This is **Professor Nikandish's existing boundary family**, proved
nonintegral through its symmetric cubic in
[the boundary proof](repeated-exponent-family.md), and integrated as
Theorem 5.1 in the manuscript. The tensor block supplies no
nonintegrality witness on this family, for arbitrarily large a.
It therefore cannot replace the three-prime proof by a strict
noninteger interval for this block, or leave just finitely many
exceptional values of the repeated exponent a.

There is also no universal upper bound kappa_min<3. At b=a,

```text
det(K-3I) = a^2-8a+4,
det(K-4I) = 9-12a.
```

For a=8+u, u>=0, the first is u^2+8u+4>0, and the first leading
minor of K-3I is a^2+3a-2>0. Its symmetric similar matrix is
positive definite. The second determinant is negative. Hence
**3<kappa_min<4 for every a>=8 at b=a**. This is a valid
noninteger interval, but it differs from the proposed (1,2)/(2,3)
intervals for kappa; in complement notation it is 2<mu_min<3.

### Why fully distinct triples need a different restriction

For (a,d,b), with a!=d, the unweighted opposite-value ansatz already
fails weighted zero sum. Even reweighting it does not preserve the
whole two-dimensional space. Put values d h_0,-a h_0 on {1},{2}
and d h_1,-a h_1 on {1,3},{2,3}. Other supports receive canceling
contributions. However, after applying the complement Laplacian,
the normalized paired outputs differ by

```text
b(d-a)(h_0-h_1)    on the singleton pair,
(a-d)(h_0-h_1)     on the pair-support pair.
```

For arbitrary h_0,h_1 these vanish only when a=d. The line h_0=h_1
does not repair invariance: its two output coordinates are
b(a+d+1)+a+d and a+d, which are unequal for b>=1 unless the vector
is zero. Thus this paired-support construction does not provide
the required block for fully distinct triples.

There is a full tensor identity, but it is not the same small block.
On all binary supports, set E=E_a tensor E_d tensor E_b and
F=F_a tensor F_d tensor F_b. The principal restriction of E-F
to the six nonempty proper supports is **C+I**, where C is the
six-support complement Laplacian quotient. In the weighted symmetric
basis, tensor normalization makes the symmetric matrix similar to E-F
congruent to I-T_a tensor T_d tensor T_b, which is positive
semidefinite. The proper-support restriction and the
weighted zero-sum restriction still have to be analyzed; the full
tensor eigenvalues do not survive these restrictions as a list of
quotient eigenvalues. In particular C+I has the exact eigenvalue
one coming from the constant function. Positivity alone supplies
no open integer-free interval for its nonzero complement roots.

## A concrete existing hybrid core

The manuscript already supplies a cutoff **A=7 for the minimum
exponent**, independently of the repeated-pair tensor method.
This cutoff is different from the repeated exponent a in (a,a,b).
At [manuscript revision 7be8459](https://github.com/the-omega-institute/ideal-intersection-laplacian/blob/7be84599097fdff320b196cb4f84a2dfe505bd77/paper/paper.tex),
the core classification can be read as follows:

| Input | Role in the classification |
| --- | --- |
| Graph reduction, Lemma 2.1 and the six-support quotient | Weighted symmetry and complement/universal lift |
| Theorem 7.1 | Every repeated-exponent triple, including the integral tensor-block boundary family |
| Corollary 11.4 | Every triple with minimum at most seven; retains the 27,562-triple certificate and earlier smaller inputs |
| Theorem 12.2 | For minimum at least four, a positive complement root in (0,3) |
| Theorem 14.8 | Excludes integral quotient spectra on endpoint two; retains the 8,658-triple base and complete positive identities |
| The sum-bound part of Theorem 14.2 | On endpoint one, b+c>=2a^2-2a+1 |
| Lemma 16.2 | Excludes endpoint one for middle gaps one and two |
| Theorem 16.1 | For gap at least three and c>=a^2-a, puts the largest quotient root in an open unit interval |

**Core proof.** Sort a<=b<=c. Theorem 7.1 covers repeated entries,
and Corollary 11.4 covers minimum at most seven. Otherwise
8<=a<b<c. If the quotient spectrum were integral, Theorem 12.2
would give a positive root equal to one or two. Theorem 14.8
excludes two, so h_C(1)=0. Lemma 16.2 excludes b-a=1 or 2.
For b-a>=3, the endpoint-one sum bound gives
c>=(b+c)/2>=a^2-a+1/2>a^2-a. Theorem 16.1 then gives a quotient
root strictly between the integers bc+a+b+c and bc+a+b+c+1.
The graph lift contradicts integrality. This exhausts all triples.

The low-root input uses the symmetric Schur-complement construction
in Proposition 11.1. The small-minimum input retains the unit,
minimum-two, minimum-three and repeated-exponent arguments and their
finite certificates. The endpoint-two input retains its rectangle
lemma and coefficient identities. The largest-root and small-gap
inputs retain their full positive identities. A short statement of
this core must not disguise these dependencies as removed proofs
or a certificate-free classification.

The [source review receipt](../results/three-prime-classification-core-review.json)
binds these eight numbered inputs to exact statement/proof hashes at
the cited manuscript revision and records their explicit references.
The mathematical dependency review also retains the subproofs and
identities just listed; reference extraction alone is not a proof of
transitive correctness.

The auxiliary common-divisor/2-adic exclusions in Section 13, the
modulo-five and local equality-cubic splitting results, the earlier
endpoint-divisor/modulo-three refinements, and the residual quartic
divisor-window/equality-curve analysis are not invoked by this
classification route. They can be presented as additional results
in a companion note or supplement. The boundary cubic, small-minimum
certificates, endpoint-two completion and final unit-interval identities
remain part of the proof package. The precise final page saving depends
on that organization; a 15-20-page reduction is not established by
the tensor calculation.

## Verification and next step

The [exact diagnostic checker](../scripts/check_three_prime_tensor_consolidation.py)
reconstructs the six-support quotient from disjoint supports, verifies
the full tensor identity and weighted symmetry, derives the repeated-pair
embedding and the unequal-pair residuals, and checks the generic
characteristic/endpoint polynomials and both unbounded-family identities.
Six specified support controls verify all embedding columns and graph
lifts; they are implementation controls, not an exponent search.
The [saved report](../results/three-prime-tensor-consolidation.json)
records the exact scope. No floating-point eigenvalues or Lean are used.
Existing classification certificates were not rerun for this diagnostic.

The next mathematical question is a new zero-sum restriction or a
uniform eigenvalue interval for the fully distinct six-support operator
that also handles its integer endpoints. The present two-dimensional
block does not furnish it. A shorter presentation of the established
hybrid chain can proceed independently of that open simplification.
