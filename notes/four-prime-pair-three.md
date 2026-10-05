# Four prime factors with two exponents equal to three

**Theorem.** For four distinct primes and integers b,c>=2, the ideal
intersection graph with exponent vector (3,3,b,c) has a noninteger
Laplacian eigenvalue in (V-2,V), where V=16(b+1)(c+1)-2. More precisely,
the eigenvalue differs from V-1. Together with the unit-exponent theorem,
this proves nonintegrality for every positive four-prime exponent vector
with at least two entries equal to three.

The proof uses an invariant subspace, a general tensor positivity bound,
and a complete symbolic endpoint reduction. The remaining fixed arithmetic
is eight nonsquare discriminants and two explicit rational factorizations.
There is no finite two-parameter exponent base, modular search or Lean claim.

## A general repeated-pair restriction

For exponents (a,a,b,c), a>=1, use functions equal to h(T) on support
{1} union T, -h(T) on {2} union T, and zero elsewhere, for T subset
of {3,4}. The paired support classes have equal weights, so these
functions have weighted sum zero. Other supports see canceling contributions.
In the disjoint-support complement after removing a^2bc-1 universals,
the degree on {1} union T is
(a+1)*product_(i in {3,4}\T)(k_i+1)-1. Its nonzero-valued neighbors
are the {2} union T' classes with T' disjoint from T, of weight
a*product_(i in T')k_i. Thus the four-dimensional space is invariant
and, in the order T=empty,{4},{3},{3,4}, the complement acts by K_a-I,
where

```text
K_a = (a+1) E_b tensor E_c + a F_b tensor F_c,
E_k = diag(k+1,1), F_k = [[1,k],[1,0]].
```

Multiplication by diag(1,c,b,bc) symmetrizes K_a. If kappa is an
eigenvalue of K_a, the zero-sum complement reflection and direct
universal-vertex lift give the graph eigenvalue V+1-kappa, where
V=(a+1)^2(b+1)(c+1)-2. This is an actual operator embedding, not a
principal-submatrix or non-equitable compression argument.

## A uniform lower bound for the general restriction

In the weighted symmetric basis, F_k becomes
S_k=[[1,sqrt(k)],[sqrt(k),0]]. Put
T_k=E_k^(-1/2) S_k E_k^(-1/2). Its eigenvalues are

```text
1, -k/(k+1).
```

For example, this follows from the characteristic polynomial
(x-1)(x+k/(k+1)). All eigenvalues of T_b tensor T_c are strictly
greater than -1. Write E=E_b tensor E_c. The symmetric similar
matrix of K_a is

```text
E^(1/2) [ (a+1)I + a(T_b tensor T_c) ] E^(1/2).
```

The bracket is strictly greater than I as a quadratic form. Therefore
the symmetric restriction is strictly greater than E, which is at
least I. In particular, **kappa_min(K_a)>1 for every a,b,c>=1**.
This general positivity statement does not by itself prove
nonintegrality for arbitrary repeated exponent a.

## The upper bound when a=3

For a=3 the restriction is

```text
K = [ 4(b+1)(c+1)+3   3c          3b          3bc ]
    [ 3               4(b+1)      3b          0   ]
    [ 3               3c          4(c+1)      0   ]
    [ 3               0           0           4   ].
```

Direct expansion gives

```text
det(K-3I) = -35b^2c^2+8b^2c-20b^2+8bc^2+109bc+11b-20c^2+11c+4.
```

With b=2+u,c=2+v, its negative is

```text
35u^2v^2+132u^2v+144u^2+132uv^2+387uv
  +315u+144v^2+315v+108 > 0.
```

The symmetric similar matrix K-3I has negative determinant and
therefore a negative eigenvalue. Combining this with the lower bound,

```text
1 < kappa_min(K) < 3.
```

It remains to exclude the only integer in this interval, namely two.

## The endpoint equation has no integer solution

Put P(b,c)=det(K-2I). Direct expansion gives

```text
P(b,c) = -7b^2c^2+48b^2c-8b^2+48bc^2+302bc+76b-8c^2+76c+40.
```

Order b<=c by exchanging the remaining coordinates. For b=17+u,c=17+v,

```text
-P(17+u,17+v) = 7u^2v^2+190u^2v+1215u^2+190uv^2+4526uv
                   +22228u+1215v^2+22228v+27721 > 0.
```

This handles every b>=17 without an upper bound on c. For the remaining
2<=b<=16, write

```text
P(b,c) = A_b c^2+B_b c+C_b,
A_b = -7b^2+48b-8,
B_b = 48b^2+302b+76,
C_b = -8b^2+76b+40.
```

For b=2,...,6, the A_b values are (60,73,72,57,28), and the C_b
values are (160,196,216,220,208). Since B_b>0, these rows have no
positive real zero. For b=10 and b=14 the exact factorizations are

```text
P(10,c) = -12c(19c-658),
P(14,c) = -4(3c-58)(59c-2).
```

Their positive roots 658/19,58/3,2/59 are not integers. For the
other eight b values, the discriminant D_b=B_b^2-4A_bC_b and its
integer square-root anchor h_b are as follows:

| b | D_b | h_b |
| --- | --- | --- |
| 7 | 20640564 | 4543 |
| 8 | 30997264 | 5567 |
| 9 | 44692596 | 6685 |
| 11 | 84630100 | 9199 |
| 12 | 112262544 | 10595 |
| 13 | 146014164 | 12083 |
| 15 | 235204596 | 15336 |
| 16 | 292433040 | 17100 |

Each row satisfies h_b^2<D_b<(h_b+1)^2, so none of these quadratics
has a rational root. This exhausts the symbolic reduction. Hence
P(b,c) is nonzero for every pair of integers b,c>=2; no exponent
rectangle was enumerated and no exceptional integer pair remains.

The smallest K-eigenvalue is therefore noninteger in (1,3).
Its graph lift V+1-kappa_min lies in (V-2,V), differs from V-1,
and proves the theorem. For b=1 or c=1 the existing arbitrary-prime-count
unit theorem supplies nonintegrality separately.

## Verification and remaining scope

The [checker](../scripts/check_four_prime_pair_three.py) verifies the
generic repeated-pair tensor identity, the normalized two-dimensional
characteristic identity, both endpoint polynomials and complete positive
expansions. It reconstructs all fifteen low-b coefficient rows from the
same generic endpoint polynomial, checking five positive rows, the two
factorizations and eight strict nonsquare bounds. Ten specified support
controls reconstruct all four embedding columns directly, including
eight a=3 controls and two controls for other a. Two small expanded
graphs independently verify the embedding. The certificate reproduces
byte-for-byte. These controls validate implementation; the infinite
argument is the written proof with its explicit constant arithmetic.
No floating eigenvalues, parameter-range scan or Lean verification is used.

This extends the [pair-two theorem](four-prime-pair-two.md) to a
different repeated-pair family. The general four-prime classification,
higher-prime nonsquarefree Q3 and old orthogonality n=7 remain open.
In the remaining four-prime domain there can be at most one exponent
equal to two and at most one equal to three; other repeated exponents
are not settled by this note.
