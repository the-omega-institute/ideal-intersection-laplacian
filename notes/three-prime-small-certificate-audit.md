# Verification of the smaller finite inputs

The [structural dependency review](three-prime-referee-checks.md) identifies
finite inputs beyond the two large bases. This bounded audit reruns three
earlier checkers and independently verifies their selected finite inputs.
It does not extend any parameter domain or add a nonintegrality theorem.

## Reproduction of the original checkers

At source revision 81a7dd3cdfd2d1c3008cf0aa4fc6147189d03731, a new detached
checkout ran the following commands with new interpreter processes:

```sh
PYTHONDONTWRITEBYTECODE=1 python scripts/check_distinct_tail.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_repeated_exponent_completion.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_minimum_two.py
```

The isolated virtual environment created for the preceding large-base
rerun was reused unchanged: Python 3.14.4, SymPy 1.14.0, mpmath 1.3.0,
without system site packages. All three outputs are byte-identical to
their saved historical JSON files. The
[rerun receipt](../results/three-prime-small-base-rerun.json) records
source and output hashes. This is separate from the previous large-base
rerun and does not claim that a second virtual environment was created.

## Independent verification from matrices

The new [standard-library verifier](../scripts/verify_three_prime_small_certificates.py)
imports neither SymPy nor any original checker. It constructs the
six-support complement Laplacian directly from disjoint-support adjacency,
then uses integer Leibniz determinants and exact rational arithmetic.
At x=0, the coefficient of x in det(xI-C), namely h_C(0), is computed as
the sum of the six principal cofactors of -C. At a nonzero rational
argument p/q, it computes det(pI-qC)/q^6 and divides by p/q.

For minimum three, the independently constructed domain is exactly
a=3, 4<=b<c<30, with 325 distinct pairs. The verifier recomputes h_C(1),
h_C(2), both endpoints of every saved strict sign-changing interval, and
the reflected graph-eigenvalue interval using V=(a+1)(b+1)(c+1)-2.
All values agree. There are 257 positive and 68 negative values at one,
and no zero. The exceptional triple (3,4,5) has

```text
h_C(1)=-3792, h_C(3/2)=48825/32>0.
```

Its root in (1,3/2) is sufficient for nonintegrality; no uniqueness claim
is needed for this finite sign certificate.

For repeated exponents, the written factor-index reduction gives
d | (j+1)^3(j+2). The verifier independently enumerates all divisors of
24,108,320 for j=1,2,3 and checks the admissibility conditions. Exactly
eight positive exponent pairs survive. For each, it builds the four-class
quotient directly, recovers its monic cubic coefficients from determinant
values at 1,2,3, and recomputes every residue modulo the certificate's
prime. All eight cubics have no root modulo that prime, with every saved
residue agreeing. These monic cubics are therefore irreducible over Q
and their nonzero real roots supply the required noninteger eigenvalues.
The infinite factor-index reduction and j>=4 argument remain written
dependencies; this finite check does not replace them.

For the minimum-two exception (2,3,4), the independently reconstructed
support matrix gives

```text
h_C(1)=-48, h_C(3/2)=13437/32>0.
```

This checks its exact rational sign certificate. The minimum-two
unbounded positive expansions are also rerun by their original checker.

The complete [independent report](../results/three-prime-small-certificate-audit.json)
reproduces byte-identically with

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_three_prime_small_certificates.py
```

This supplements the existing two-large-base and polynomial-identity
audits. It is not a fresh verification of every dependency: the
unit-exponent theorem, repeated boundary family, all written reductions
and other symbolic arguments remain explicit dependencies. The result
remains computer-assisted and has no Lean verification. Higher-prime
nonsquarefree Q3 and the separate orthogonality problem at n=7 remain open.
