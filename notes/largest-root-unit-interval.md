# A largest-root unit interval and the three-prime classification

Let C be the six-support complement quotient in support order
1,2,3,12,13,23, with h_C(x)=det(xI-C)/x and s=a+b+c.
Exponents are in size order, independently of residue roles.

**Unit-interval theorem.** For real 3<=a<=b<=c with b-a>=3 and
c>=a²-a, put M=bc+s. The largest quotient eigenvalue satisfies

```text
M < lambda_max(C) < M+1.
```

For integer exponents this is a noninteger quotient root and proves
Laplacian nonintegrality after the established complement and
universal-class lifts. The theorem has a written proof on the entire
unbounded real domain, with no finite exponent base.

**Three-prime classification.** Every ideal intersection graph of
Z_(p^a q^b r^c), for distinct primes p,q,r and positive integer a,b,c,
is Laplacian nonintegral. This combines the new unit interval with
established written and computer-assisted results. In particular its
small-minimum and endpoint-two steps retain their historical finite
certificates; this classification is not claimed as entirely computation-free
or Lean-verified. The higher-prime nonsquarefree part of full Q3 stays open.

## The two determinant signs

Direct expansion gives

```text
h_C(M)=-a²bc T(a,b,c),
T=(2b²-ab+b-a)c²-[(a-1)b²+a²]c-ab(a+b).
```

Let P(a,b,c)=h_C(M+1). The coefficient tables below are complete
identities for T and P under

```text
a=3+m, b=a+3+u, c=a²-a+v, m,u,v>=0.
```

Each row (i,j) lists the ascending m coefficient vector of u^i v^j.
Every listed coefficient is strictly positive, and no row is omitted.
There are36nonzero terms for T and170for P, with constant terms1404
and513220. Therefore h_C(M)<0<h_C(M+1) throughout the theorem domain.
The intermediate value theorem already gives a root in (M,M+1).

### T coefficient identity

| i | j | Ascending m coefficient vector |
|---|---|---|
| 0 | 0 | [1404,3042,2517,1036,224,24,1] |
| 0 | 1 | [603,684,261,39,2] |
| 0 | 2 | [57,15,1] |
| 1 | 0 | [603,1188,875,305,50,3] |
| 1 | 1 | [240,240,72,6] |
| 1 | 2 | [22,3] |
| 2 | 0 | [57,103,67,19,2] |
| 2 | 1 | [22,19,4] |
| 2 | 2 | [2] |

### P coefficient identity

| i | j | Ascending m coefficient vector |
|---|---|---|
| 0 | 0 | [513220,2023568,3509410,3571354,2381713,1095075,354193,80470,12554,1277,76,2] |
| 0 | 1 | [461006,1356418,1739823,1279064,593441,179723,35391,4351,302,9] |
| 0 | 2 | [142258,295089,256850,120963,33056,5205,436,15] |
| 0 | 3 | [18594,23290,11201,2530,270,11] |
| 0 | 4 | [882,399,60,3] |
| 1 | 0 | [461006,1812246,3118532,3129572,2042989,911507,283142,61012,8889,828,44,1] |
| 1 | 1 | [398473,1159066,1455815,1037238,460760,131613,23978,2659,161,4] |
| 1 | 2 | [118957,239834,199807,88401,22137,3087,219,6] |
| 1 | 3 | [15059,17725,7741,1509,131,4] |
| 1 | 4 | [693,253,29,1] |
| 2 | 0 | [142258,547789,915785,883535,547176,227591,64328,12165,1466,101,3] |
| 2 | 1 | [118957,336158,404388,271110,110621,27997,4258,352,12] |
| 2 | 2 | [34629,66544,51528,20429,4311,450,18] |
| 2 | 3 | [4285,4597,1712,248,12] |
| 2 | 4 | [193,49,3] |
| 3 | 0 | [18594,69414,111456,101999,58928,22337,5555,872,78,3] |
| 3 | 1 | [15059,40917,46523,28811,10495,2240,257,12] |
| 3 | 2 | [4285,7749,5460,1864,303,18] |
| 3 | 3 | [520,496,147,12] |
| 3 | 4 | [23,3] |
| 4 | 0 | [882,3171,4853,4172,2218,750,158,19,1] |
| 4 | 1 | [693,1797,1911,1075,339,57,4] |
| 4 | 2 | [193,325,204,57,6] |
| 4 | 3 | [23,19,4] |
| 4 | 4 | [1] |

## Why this is the largest root

The symmetric similarity S=W^(1/2)CW^(-1/2), with
W=diag(a,b,c,ab,ac,bc), has pair-support block diag(c,b,a).
For x>c its Schur complement in xI-S is

```text
H(x)=diag(ell_a,ell_b,ell_c)+zz^T,
z=(sqrt(a),sqrt(b),sqrt(c)),
ell_t=x-s-xabc/[t(x-t)].
```

At x=M+1, x-b>bc and x-c>bc, so

```text
ell_b=c(b-a)+1-abc/(x-b)>c(b-a)+1-a>0,
ell_c=b(c-a)+1-abc/(x-c)>b(c-a)+1-a>0.
```

Here c>=a²-a>=a+3 at a>=3. Thus H's b,c principal block
is positive definite. The full determinant is x P(a,b,c)>0,
and the eliminated pair-support block is positive definite. Hence
H has positive determinant. Its remaining scalar Schur complement is
positive, so xI-S is positive definite: every eigenvalue is less than M+1.
The negative determinant at M rules out all eigenvalues being below M.
Consequently the root in the unit interval is exactly the largest root.

For an independent algebraic reconstruction, put
L_t=(x-s)(x-t)-xabc/t. The Schur identity is

```text
det(xI-C)=L_a L_b L_c
 +a(x-a)L_b L_c+b(x-b)L_a L_c+c(x-c)L_a L_b.
```

It agrees coefficientwise with the characteristic polynomial obtained
from the support-derived six-by-six quotient; it also defines P without
requiring a separately copied71-term expanded polynomial.

## Completion of the three-prime case

Sort the integer exponents. Repeated exponents are already settled by the
[all-repeated theorem](repeated-exponent-completion.md), and minima at most
seven by the [existing complete certificate](open-region-diagnostic.md).
For the remaining a>=8,a<b<c, the uniform positive root below three
would be1or2 if the spectrum were integral.

The [endpoint-two completion](endpoint-two-completion.md) already rules
out an integral spectrum when2is a root. Thus an integral spectrum
would require h_C(1)=0.

If b-a=1or2, the written [small-gap endpoint-one brackets](endpoint-one-growing-gap.md)
exclude every integer c>b. Their lower anchors are
2a²-a-2 and2a²+a-6, respectively; opposite signs at the consecutive
endpoints and unique real exponent-root geometry give the exclusion
for every a>=8. The four complete univariate positive vectors are
rechecked in the new certificate, without invoking a new finite base.

If b-a>=3, the established [endpoint-one sum bound](endpoint-one-minimum-root.md)
gives b+c>=2a²-2a+1. Since c>=b, it follows that
c> a²-a. The new largest-root theorem then supplies a quotient
eigenvalue strictly between the integers bc+s and bc+s+1, again
contradicting an integral spectrum. These alternatives exhaust the
positive three-prime exponent vectors.

The last step bypasses the smallest quartic root equation. The earlier
coefficient windows and equality-curve results remain valid structural
results, but no global Diophantine point enumeration or quartic factorization
is needed for this classification. Integer exponent points on endpoint one
and on the equality curve are not claimed to be absent.

## Verification and dependencies

With SymPy1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_largest_root_unit_interval.py
```

The [checker](../scripts/check_largest_root_unit_interval.py) and
[certificate](../results/largest-root-unit-interval.json) reconstruct the
generic quotient and independent Schur determinant, the lower identity,
all34complete coefficient rows (36+170terms), and the four preserved
small-gap sign vectors. Seven stated spectral controls cover the real
boundary, minimum-eight domain, two earlier endpoint-feasibility pairs,
and strongly unequal exponents. Fourteen independent6x6Bareiss determinants
check the two signs; exact squarefree-factor Sturm counts retain
multiplicity, prove one root in each open unit interval and none above.
These controls are supplementary fixtures, not an exponent scan.

The combined classification retains the old27562-triple minimum-through-seven
and8658-triple endpoint-two bases, along with the earlier repeated/small-minimum
proof dependencies. They are source-hashed, not rerun in this cycle. The
separate108-pair minimum-eight certificate is valid but not required by
this proof route. No Lean, floating spectrum, new parameter or modulus
scan, merge, publication, or shared-CI change is involved. Original
orthogonality n=7 and the nonsquarefree higher-prime part of full Q3 remain open.

[Return to the project entrance](../README.md).
