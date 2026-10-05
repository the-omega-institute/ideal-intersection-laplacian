# Four prime factors with two exponents equal to two

**Theorem.** For four distinct primes and positive integers b,c>=2,
the ideal intersection graph with exponent vector (2,2,b,c) is
Laplacian nonintegral. The same holds after any permutation.
Together with the established unit-exponent theorem, this covers
every positive four-prime vector with at least two entries equal to two.

This is a written invariant-subspace argument with one explicit
17-residue irreducibility certificate. It requires no finite exponent
base or parameter scan. It covers balanced vectors such as (2,2,2,2),
outside the [small-exponent Rayleigh criterion](small-exponent-rayleigh.md).

## A four-dimensional invariant subspace

Use the disjoint-support complement F after removing the 4bc-1
full-support universal vertices. For each T subset of {3,4}, put a
support-constant function equal to h(T) on {1} union T, -h(T) on
{2} union T, and zero elsewhere. The two paired support classes
have the same size, so the weighted sum is zero. Supports containing
neither or both of coordinates 1,2 see equal opposite contributions.
Thus this four-dimensional subspace is invariant. The functions vanish
on the full support and no class in this subspace is removed.

In the order T=empty,{4},{3},{3,4}, define

```text
K = [ 3(b+1)(c+1)+2   2c          2b          2bc ]
    [ 2               3(b+1)      2b          0   ]
    [ 2               2c          3(c+1)      0   ]
    [ 2               0           0           3   ].
```

For support {1} union T, its complement degree is
3*product_(i in {3,4}\T)(k_i+1)-1. Its nonzero-valued neighbors
are precisely the {2} union T' classes with T' disjoint from T,
with size 2*product_(i in T')k_i and value -h(T'). This gives
the restricted complement operator K-I. The swapped classes give
the negatives and all other classes give zero, proving the claimed
invariance by direct counts, rather than by a principal-submatrix claim.

Equivalently, K=3 E_b tensor E_c+2 F_b tensor F_c, where
E_k=diag(k+1,1) and F_k=[[1,k],[1,0]]. Multiplying K on the left by
diag(1,c,b,bc) makes it symmetric. Therefore K has real eigenvalues.
If kappa is a K-eigenvalue, the associated zero-sum function is a
complement eigenvector at kappa-1. Complement reflection and the
universal-vertex shift give the graph eigenvalue V+1-kappa, with
V=9(b+1)(c+1)-2. Thus any noninteger kappa is an obstruction.

## The smallest restricted eigenvalue lies between one and three

The leading principal minors of K-I are

```text
D1 = 3bc+3b+3c+4,
D2 = 9b^2c+9b^2+15bc+18b+2c+8,
D3 = 15b^2c^2+33b^2c+6b^2+33bc^2+84bc+28b+6c^2+28c+16,
D4 = 2(5b^2c^2+21b^2c+6b^2+21bc^2+76bc+28b+6c^2+28c+16).
```

All coefficients are positive. The symmetric matrix similar to K-I
has leading minors equal to these same determinants, so Sylvester's
criterion gives K-I positive definite. Hence kappa_min>1.
The principal submatrix of K-3I on its first and fourth coordinates
has determinant -4bc. In the symmetric similar matrix it is likewise
indefinite, giving a negative Rayleigh quotient. Hence kappa_min<3.

Consequently, unless det(K-2I)=0, this smallest eigenvalue is
noninteger. Its graph eigenvalue lies in (V-2,V) and differs from V-1.

## The only positive integer endpoint pair

Direct expansion gives

```text
P(b,c) = det(K-2I)
       = -5b^2c^2+12b^2c-3b^2+12bc^2+48bc+8b-3c^2+8c+3.
```

Order b<=c by exchanging the two remaining coordinates. If b>=7,
put b=7+u,c=7+v. Then

```text
-P(7+u,7+v) = 5u^2v^2+58u^2v+164u^2+58uv^2+596uv
                +1364u+164v^2+1364v+1600 > 0.
```

This excludes the whole unbounded tail. For the five remaining
values of b the polynomial in c is

| b | P(b,c) |
| --- | --- |
| 2 | c^2+152c+7 |
| 3 | 4c(65-3c) |
| 4 | -35c^2+392c-13 |
| 5 | -4(c-8)(17c-1) |
| 6 | -111c^2+728c-57 |

The first two have no positive integer zero. For b=4 the
discriminant 151844 lies strictly between 389^2 and 390^2;
for b=6 the discriminant 504676 lies strictly between 710^2 and 711^2.
Those two quadratics have no rational zero. The remaining row b=5
has the sole positive integer zero c=8. Thus det(K-2I)=0 exactly
at the unordered pair {b,c}={5,8}, throughout the integer domain b,c>=2.
This is a symbolic reduction to five fixed polynomials, not a finite
range search.

## The exceptional pair is nonintegral as well

At (b,c)=(5,8), direct determinant expansion gives

```text
det(xI-K) = (x-2)(x^3-210x^2+7701x-53240).
```

Modulo 17 the cubic is x^3+11x^2+4. Its values at x=0,...,16 are

```text
4,16,5,11,6,13,4,2,13,9,13,14,1,14,8,6,14.
```

None is zero, so the cubic is irreducible over F_17 and hence over Q.
All its roots are real, because they are eigenvalues of the symmetric
similar operator. None is rational; in particular they cannot all be
integers. Their reflected graph eigenvalues prove nonintegrality also
for this exceptional pair. This completes the theorem.

## Verification and remaining scope

The [checker](../scripts/check_four_prime_pair_two.py) verifies all four
generic principal-minor identities, the endpoint polynomial, the complete
nine-term tail expansion and the five symbolic low-b rows. It verifies
the two nonsquare discriminants and the exceptional determinant/root-free
cubic. Eight specified support controls reconstruct the invariant
subspace action directly from disjoint supports, its zero sum and the
complement/join lift; two small expanded graphs independently check the
same operator embedding. The report reproduces byte-for-byte.
The infinite families follow from the written proof, with the stated
17-residue subcertificate, not from the controls. No floating-point
eigensolver, exponent scan or Lean verification is used.

The higher-prime nonsquarefree classification remains open beyond the
established families. No assertion about all four-prime vectors, source
literature priority or manuscript submission follows from this theorem.
