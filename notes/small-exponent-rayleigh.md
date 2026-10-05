# A small exponent with arbitrary prime-factor count

**Theorem.** Let n have t>=3 distinct prime factors and positive integer
exponents (k_1,...,k_(t-1),m). Define

```text
A = product_i k_i,
B = product_i (k_i+1) - 1 - A > 0.
```

If A >= (m^2-1)B-(m-1), the ideal intersection graph has a Laplacian
eigenvalue in (V-1,V), where V=product_i(k_i+1)(m+1)-2.
Consequently it is Laplacian nonintegral. The condition includes equality.
The exponent m need not be the smallest, and the criterion can be applied
after any permutation of the coordinates.

This extends the [unit-exponent theorem](unit-exponent-any-prime-count.md)
to unbounded families with all exponents at least two. It is a sufficient
criterion, not a classification of the remaining higher-prime cases.

## Three collections and a compression

Remove the mA-1 universal vertices and let F be the complement of the
remaining graph H. Its independent support classes have weights equal
to products of the corresponding exponents, with edges exactly between
disjoint supports. The singleton classes connect every proper support
to the same connected component, so F is connected.

Partition its vertices into three collections:

- L: support [t-1], with A vertices;
- Z: support {t}, with m vertices;
- R: all remaining proper supports, with (m+1)B vertices.

The L-Z edges form K_(A,m). There are no L-R edges. Each vertex in Z
has B neighbors in R: the nonempty proper supports not containing t.
The R vertices containing t have total weight mB and no neighbors in Z.
The remaining R vertices have total weight B and each has m neighbors
in Z. Internal R edges are irrelevant to functions constant on R.
The complement vertex count is N=A+m+(m+1)B, and V=N+mA-1.

For values (x,y,z) on (L,Z,R), the exact energy and norm are

```text
E = mA(x-y)^2 + mB(y-z)^2,
D = Ax^2 + my^2 + (m+1)Bz^2.
```

The compressed Laplacian for this quadratic form is

```text
Q = [ m      -m              0           ]
    [ -A      A+B           -B           ]
    [ 0      -m/(m+1)        m/(m+1)      ].
```

Multiplication on the left by diag(A,m,(m+1)B) makes Q symmetric.
Its quadratic form is positive semidefinite with kernel exactly the
constants. This is a Rayleigh compression, **not an equitable quotient**
of F: the two kinds of R vertices have different Z degrees. We use
its eigenvectors only as trial functions for the full Laplacian.

Direct expansion gives det(uI-Q)=u p(u), with

```text
p(u) = u^2 - (A+B+m+m/(m+1))u
             + m(A+(m+1)B+m)/(m+1),
p(1) = ((m^2-1)B-A-(m-1))/(m+1).
```

The two nonzero compression eigenvalues are positive. The larger
exceeds one: their sum is A+B+m+m/(m+1)>4 since A>=1 and B>=2.
Thus p(1)<=0 implies that the smaller compression eigenvalue rho
satisfies 0<rho<=1. Its eigenvector is orthogonal to the weighted
constant vector. The associated trial function on F gives
0<lambda_2(F)<=rho by the variational principle.

There is also an entirely rational trial certificate for the same sign
condition. Choose

```text
x=m, y=m-1, z=-m(A+m-1)/((m+1)B).
```

The weighted sum is zero and direct expansion factors the energy minus
the squared norm as

```text
E-D = m*((m^2-1)B-A-(m-1))
        *(mA+(m^2-1)B+m(m-1))/(B(m+1)^2).
```

The second factor is positive for every m>=1. Consequently this explicit
nonzero trial function has Rayleigh quotient at most one under exactly
the stated condition, and strictly less than one off the boundary.
This gives the bound without computing either compression eigenvalue.

## Strictness at the boundary

If p(1)<0, then rho<1 and the desired strict bound already holds.
Suppose p(1)=0. This cannot occur for m=1 since A>0. For m>=2,
A=(m^2-1)B-(m-1), and the explicit values

```text
(x,y,z) = (m, m-1, -m(m-1))
```

have weighted sum zero and satisfy Q(x,y,z)^T=(x,y,z)^T.
Their trial Rayleigh quotient is therefore exactly one. They are
not a full F-eigenvector at one: at every R vertex whose support
contains t, all neighbors with different trial values are absent,
so L(F)f=0 there, whereas f=-m(m-1) is nonzero. Such vertices exist
because mB>0. Equality in the Rayleigh minimum would force f to
be a lambda_2(F)-eigenvector. Hence lambda_2(F)<1 even at this boundary.

Connectedness gives 0<lambda_2(F)<1 in both cases. On its zero-sum
eigenvector, L(H)+L(F)=NI-J reflects the eigenvalue to N-lambda_2(F).
The universal-vertex join shifts it by mA-1. The resulting graph
eigenvalue V-lambda_2(F) is strictly between V-1 and V.

## An explicit unbounded all-exponents-at-least-two family

For m>=2 it suffices that sum_i 1/k_i <= 1/m^2. Indeed, put
u_i=1/k_i and s=sum u_i<1. The product inequality
product_i(1-u_i)>=1-s follows by induction. Since 1+u_i<1/(1-u_i),

```text
product_i (1+1/k_i) < 1/(1-s) <= m^2/(m^2-1),
B/A = product_i (1+1/k_i)-1-1/A < 1/(m^2-1).
```

Thus A>(m^2-1)B, which is stronger than the theorem's hypothesis.
In particular, **every k_i>=m^2(t-1)** suffices. This gives a written
nonintegrality family for every fixed m>=2 and every t>=4, with no
upper bound on the other exponents and no finite base.

For example, (10,10,10,2) has A=1000,B=330 and p(1)=-11/3.
The boundary example (4,19,74,2) has A=5624,B=1875 and p(1)=0;
the strictness argument above is essential. The vector (2,2,2,2)
has p(1)=15>0, so this compression criterion gives no conclusion
for it. Failure of the criterion is not evidence of integrality.

## Verification and scope

The [checker](../scripts/check_small_exponent_rayleigh.py) verifies the
generic compressed characteristic polynomial and boundary vector
symbolically. For nine specified three-, four- and five-prime controls,
it independently builds disjoint-support adjacency, the aggregated
energy matrix, connectivity, complement reflection and universal join
on exact rational trial functions. It checks boundary non-eigenvector
residuals and includes negative controls outside the criterion.
Two small expanded graphs independently verify the energy identities.
The report also checks the reciprocal sufficient condition on selected
controls. These controls test the implementation; the all-input result
is the written proof above. There is no exponent scan, floating-point
eigensolver or Lean verification.

The full higher-prime nonsquarefree Q3 remains open outside this
criterion. The completed three-prime theorem and its historical finite
dependencies are unaffected; the old orthogonality n=7 problem is separate.
