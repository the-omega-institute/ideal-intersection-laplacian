# Every four-prime double-pair vector is nonintegral

**Theorem.** For four distinct primes and any positive integer exponents
a,b, the ideal intersection graph with exponent vector (a,a,b,b) is
Laplacian nonintegral. Permuting the prime coordinates does not change
the conclusion. Put V=(a+1)^2(b+1)^2-2.

Order a<=b. If a=1, the smallest repeated-pair eigenvalue kappa is in
(1,2), yielding a graph eigenvalue in (V-1,V). If a>=2, then

```text
1 < kappa < 4, kappa != 2,3,
```

so its graph lift V+1-kappa is noninteger in (V-3,V), different from
V-2 and V-1. The proof also locates this witness in one of three open
unit intervals, as described below.

This completes the double-pair family, including the transition left by
the [balanced-region proof](four-prime-double-pair-balanced.md). It uses
written unbounded endpoint brackets and eight fixed cubic brackets, not
an exponent rectangle search or a finite graph-classification base.
The general four-prime classification remains open.

## The invariant cubic and the graph lift

We retain the established graph convention: nonzero proper ideals of Z_n
are vertices, and adjacency means nonzero intersection. The antisymmetric
space for the first repeated pair gives the actual complement operator K-I.
The second swap decomposes K into scalar a+b+1 and the restriction

```text
Q = [[(a+1)(b+1)^2+a, 2ab,          ab^2],
     [a,               (2a+1)b+a+1, 0   ],
     [a,               0,           a+1]].
```

D=diag(1,2b,b^2) symmetrizes Q. These are invariant spaces, not
principal-submatrix eigenvalue transfers. The weighted zero-sum
complement reflection and universal-vertex extension send every K
eigenvalue kappa to V+1-kappa in the graph. The construction and tensor
normalization in the [general repeated-pair proof](four-prime-pair-three.md)
give kappa_min(K)>1 for all positive a,b.

Write p(x)=det(xI-Q). Thus det(xI-K)=(x-(a+b+1))*p(x).
For a=1, the empty/full principal minor of the symmetric K-2I is -b^2<0,
giving kappa_min<2. Assume a>=2 henceforth.

## A uniform upper endpoint four

Put u=a-2 and d=b-a, both nonnegative. Direct expansion gives

```text
p(4) = 4d^3u^2+24d^3u+35d^3
       +8d^2u^3+80d^2u^2+246d^2u+233d^2
       +4du^4+68du^3+367du^2+759du+503d
       +12u^4+130u^3+489u^2+717u+353 > 0.
```

Hence det(Q-4I)=-p(4)<0. A negative eigenvalue of the symmetric
similar matrix Q-4I gives kappa_min(K)<4. The remaining scalar a+b+1
is at least five, so the smallest K eigenvalue belongs to Q.

It remains to exclude two and three as eigenvalues of Q.

## Endpoint two: a bracket for every a>=2

Direct expansion gives the following polynomial in the exponent b:

```text
P_2(a,b)=p(2)
  = (2a+1)b^3
    -(a-1)(4a^2+6a+1)b^2
    -(a-1)(4a^2-3)b
    -(a-1)^2(2a-1).
```

For a>=2 its coefficient signs are +,-,-,-. Descartes' rule gives
exactly one positive root, counting multiplicity; existence follows
also from the negative constant and positive leading coefficient.
The root is simple, and the polynomial is negative before it and
positive after it.

With u=a-2>=0, the exact endpoint identities are

```text
-P_2(a,2a^2-2)=4u^5+36u^4+124u^3+201u^2+154u+45 > 0,
 P_2(a,2a^2-1)=4u^5+48u^4+220u^3+483u^2+504u+200 > 0.
```

Thus its unique positive exponent root beta_2(a) satisfies
2a^2-2<beta_2(a)<2a^2-1. It is never an integer. In particular
p(2)!=0 for every positive integer b, without any bound on b.

## Endpoint three: an unbounded bracket and complete fixed rows

The second endpoint polynomial is

```text
P_3(a,b)=p(3)
  = (a+2)(2a+1)b^3
    -a(a-2)(4a+5)b^2
    -2(a-2)(2a^2-2a-3)b
    -2(a-2)^2(a-1).
```

For a=2 this is 20b^3, which never vanishes at positive b. For a>=3,
its signs are again +,-,-,- and there is exactly one simple positive
root beta_3(a). When a=3 or 4, P_3(a,a) is respectively 428 or 408,
so beta_3(a)<a and there is no zero at any b>=a.

For a>=13, write u=a-13>=0. The complete identities are

```text
-P_3(a,2a-6)=4u^4+250u^3+5388u^2+48806u+159264 > 0,
 P_3(a,2a-5)=4u^4+146u^3+1839u^2+8839u+10452 > 0.
```

Consequently 2a-6<beta_3(a)<2a-5 for every a>=13, excluding integer
b there. The remaining eight a values have the following complete
constant arithmetic:

| a | h | P_3(a,h) | P_3(a,h+1) |
| --- | --- | --- | --- |
| 5 | 5 | -932 | 1728 |
| 6 | 7 | -1784 | 4896 |
| 7 | 9 | -2730 | 11100 |
| 8 | 11 | -3518 | 21816 |
| 9 | 13 | -3800 | 38808 |
| 10 | 15 | -3132 | 64128 |
| 11 | 17 | -974 | 100116 |
| 12 | 18 | -115600 | 3310 |

For each row, uniqueness gives h<beta_3(a)<h+1, excluding every
positive integer b, including arbitrarily large b. This exhausts all
a>=2. No integer double-pair vector can have p(3)=0.

The smallest K eigenvalue is strictly between one and four and avoids
both possible integers. Its graph lift proves the theorem.

## The complete three-interval witness

For a>=5 define H(a) by the h column above for 5<=a<=12, and
H(a)=2a-6 for a>=13. The smallest K eigenvalue is located as follows:

| Integer exponent range | kappa_min(K) | Graph witness V+1-kappa_min |
| --- | --- | --- |
| a<=b<=H(a) | (3,4) | (V-3,V-2) |
| H(a)+1<=b<=2a^2-2 | (2,3) | (V-2,V-1) |
| b>=2a^2-1 | (1,2) | (V-1,V) |

For a=2,3,4 the first row is absent: a<=b<=2a^2-2 gives (2,3),
and the final tail gives (1,2). For a=1 the witness is always in (1,2).

Here is the additional positivity needed to identify the smallest root,
rather than just the endpoint signs. For lambda=2 and a>=2, the first
two leading minors of Q-lambda*I are positive: their diagonal factors
are at least (a+1)(b+1)^2 and (2a+1)b, and their off-diagonal product
is 2a^2b. Thus the second minor is at least
b*((a+1)(b+1)^2(2a+1)-2a^2)>0. For lambda=3 the same argument
works when a>=3. Diagonal similarity preserves these leading minors.

Before beta_lambda(a), p(lambda)<0 and the third minor
det(Q-lambda*I)=-p(lambda)>0, making Q-lambda*I positive definite
in its symmetric basis. After the exponent root, its determinant is
negative and the smallest eigenvalue is below lambda. Applying this
at two and three gives the table, with the lower bound one and upper
bound four already established. The three intervals remain distinct;
an endpoint in the exponent b is not an endpoint in the spectral variable.

## Verification and remaining scope

The [checker](../scripts/check_four_prime_double_pair_completion.py)
verifies the generic invariant embedding, scalar eigenvector, weighted
symmetry and characteristic factorization directly. Both endpoint cubics
are verified coefficientwise. All 39 coefficients in five complete
positive expansions check: 17 for the four-endpoint bound and 22 for the
four exponent-root brackets. The two small positive values and all eight
fixed bracket rows are evaluated by integer Horner and independently
reconstructed by 18 direct 3x3 Bareiss determinants.

Nine specified support controls cover a=1, the first endpoint-two bracket,
the last small endpoint-three bracket, the start of the unbounded
endpoint-three bracket and its endpoint-two tail. They independently
check all four support embedding columns, weighted zero sums, symmetry
and complement/universal lifts. Forty-five direct cubic determinant
values reconstruct/cross-check the characteristic polynomials; 27 leading
minors and nine exact Sturm counts check the indicated unit intervals.
No expanded vertex graphs are used.

The [certificate](../results/four-prime-double-pair-completion.json)
reproduces byte-for-byte with SymPy 1.14.0 using
`python3 scripts/check_four_prime_double_pair_completion.py`; the reused
support-checker dependency hash is recorded. The theorem has a written
unbounded reduction with ten fixed rows of constant arithmetic (two small
positive evaluations and eight brackets), not a finite two-parameter
exponent base. No numerical eigenvalues, exponent scan, historical
finite-base rerun or Lean verification is claimed.

The completed three-prime manuscript remains unchanged. The next spectral
question is the general single repeated pair (a,a,b,c) with b!=c and all
entries at least five, outside the existing product criterion. Its genuine
four-dimensional block remains available, but the second-swap cubic
decomposition used here does not. General four-prime and higher-prime
nonsquarefree Q3, including (2,3,4,5), and old orthogonality n=7 remain open.
