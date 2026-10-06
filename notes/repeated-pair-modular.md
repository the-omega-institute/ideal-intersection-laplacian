# A modular splitting obstruction for arbitrary repeated pairs

**Theorem.** Let the positive exponent vector on t>=3 distinct primes
be (a,a,k_3,...,k_t). For any prime p dividing a+1, integrality of
the ideal intersection graph requires every quadratic

```text
x^2-x-k_i, 3<=i<=t,
```

to split into linear factors over F_p. Equivalently, every remaining
exponent must be even when p=2; for odd p, each 1+4k_i must be a
quadratic residue modulo p, with zero allowed.

In particular, an odd repeated exponent together with any other odd
exponent always gives a nonintegral graph, regardless of the number
or size of the remaining exponents. There is no tail-order hypothesis.
The three-prime classification is already complete; the theorem also
gives unbounded exclusions for four or more prime factors.

## The genuine tensor restriction

Use the invariant space and weighted-zero-sum graph transfer established
in the [product-tail proof](repeated-pair-product-tail.md). Its operator is

```text
K_a=(a+1) tensor_(i=3)^t E_(k_i) + a tensor_(i=3)^t F_(k_i),
E_k=diag(k+1,1), F_k=[[1,k],[1,0]].
```

It is an integer matrix, similar to a real symmetric matrix. Each
eigenvalue kappa gives an actual graph eigenvalue V+1-kappa, where
V=(a+1)^2 product_(i=3)^t(k_i+1)-2. Thus graph integrality forces
all eigenvalues of K_a to be integers. Its monic characteristic
polynomial would then split over the integers, and its reduction
would split over every prime field.

If p divides a+1, the tensor operator reduces to

```text
K_a = -tensor_(i=3)^t F_(k_i) modulo p.
```

We determine exactly when this reduced characteristic polynomial splits.

## Tensor splitting cannot conceal a nonsplit factor

**Lemma.** Over a field, let M_1,...,M_r be two-dimensional matrices
with trace one. The characteristic polynomial of their tensor product
splits over the field if and only if every individual characteristic
polynomial does.

If the individual polynomials split, triangularizing each factor over
the field makes the tensor product triangular, with diagonal entries
equal to products of individual eigenvalues. This proves sufficiency,
including repeated roots and zero eigenvalues.

Conversely, suppose a factor has nonsplit quadratic characteristic
polynomial, with roots alpha,beta in an algebraic closure. Both roots
are nonzero and alpha+beta=1. Each other factor has a nonzero
eigenvalue, because its trace is one. Fix one such eigenvalue per other
factor and let their nonzero product be P. Triangularization over the
algebraic closure shows that P*alpha and P*beta are eigenvalues of
the tensor product, even if some factors have repeated roots.

If the tensor characteristic polynomial split over the base field,
these two nonzero products would belong to that field. Their ratio
rho=alpha/beta would therefore belong to it as well. Since
alpha+beta=(rho+1)beta=1, rho+1 is nonzero and
beta=1/(rho+1) belongs to the field. So does alpha, contradicting
nonsplitting. This proves necessity.

Apply the lemma to F_k, whose trace is one and characteristic polynomial
is x^2-x-k. Multiplication of the tensor product by -1 preserves
splitting. This proves the theorem. For odd p, completing the square
gives the discriminant condition. At p=2, even k gives x(x+1),
whereas odd k gives the irreducible x^2+x+1.

## Small-prime consequences

These conditions apply separately to every remaining exponent.

| p dividing a+1 | Excluded k_i residues modulo p |
|---|---|
| 2 | 1 |
| 3 | 1 |
| 5 | 3,4 |

For four prime factors and odd a, the complete parity table for the
characteristic polynomial of K_a is

| b parity | c parity | Characteristic polynomial modulo two |
|---|---|---|
| even | even | x^3(x+1) |
| even | odd | x^2(x^2+x+1) |
| odd | even | x^2(x^2+x+1) |
| odd | odd | (x+1)^2(x^2+x+1) |

Only the first row passes this modular test. Passing it is a necessary
condition, not a claim of integral graph spectrum.

## Additional coverage beyond the previous sufficient regions

Every vector (a,a,2a,2a^2+1) with odd a>=5 is now excluded by
the binary obstruction. Its unequal tail gap is r=2a^2-2a+1>=41.
It has no exponent one through four, no second equal pair, and its
tails lie outside the balanced region c<=2a-6.

The product-tail criterion fails by the strictly positive margin
2a^4-2a^3+a^2-7a. The odd-gap weighted criterion fails by
8a^5-12a^4+8a^3-8a^2-2a+1; this also excludes the earlier
midpoint condition b>=r^2. To check every coordinate choice in the
small-exponent criterion, use its failure margin
(m^2-1)B_m-(m-1)-A_m, with
A_m=product_(i!=m)k_i and B_m=product_(i!=m)(k_i+1)-1-A_m.
All five comparison polynomials have positive coefficients after a=z+5:

| Comparison | Coefficients in descending powers of z |
|---|---|
| product tail | 2,38,271,853,990 |
| odd-gap weighted | 8,188,1768,8312,19518,18291 |
| small exponent m=a | 6,150,1500,7495,18693,18590 |
| small exponent m=2a | 16,410,4212,21680,55894,57720 |
| small exponent m=2a^2+1 | 20,616,7920,54414,210708,436030,376700 |

The large-tail sufficient cutoff is also above this family's tail:
M=(a+1)(2a+1)>2a^2, so
24(M+a)^3(3M+a)>72M^4>2a^2+1. The earlier candidate-finiteness
results continue to apply but do not themselves exclude this entire
unbounded family. This comparison concerns the recorded sufficient
criteria; no literature-priority claim is made.

## Verification and remaining question

The [checker](../scripts/check_repeated_pair_modular.py) verifies the
generic tensor reduction and quadratic characteristic identity, all
four binary rows, all ten tail-residue rows for p=2,3,5, and the five
positive coverage identities. Six specified four-/five-prime controls
include both split and nonsplit reductions. They reconstruct 704
support-column actions and check weighted symmetry, zero sums and the
actual complement-to-graph lift. Thirty-eight independent integer
determinants verify the characteristic polynomials at enough distinct
arguments to determine each polynomial. Standard-library synthetic
division independently checks full splitting of the reduced control
polynomials and all ten residue rows.

The [certificate](../results/repeated-pair-modular.json) is reproducible
with SymPy 1.14.0 using `python3 scripts/check_repeated_pair_modular.py`.
The written tensor lemma proves the unbounded result; these exact
controls check its algebra and implementation. No exponent/tail scan,
expanded vertex graph, Sturm calculation, historical finite-base rerun
or Lean validation is used.

For four primes, combine these necessary tail residues with the
[unique-tail reduction](four-prime-unique-tail.md) before analyzing
square discriminants and numerator divisibility. Cases passing every
prime divisor of a+1 remain open; passing finite-field splitting does
not imply integer restricted roots. Fully unequal four-prime and
general higher-prime classification also remain open. The focused
three-prime main and joint manuscript-scope decisions are retained.
