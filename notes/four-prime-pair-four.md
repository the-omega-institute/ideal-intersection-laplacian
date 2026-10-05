# Four prime factors with two exponents equal to four

**Theorem.** Every positive four-prime exponent vector with at least
two entries equal to four gives a Laplacian nonintegral ideal intersection
graph. In particular this holds for (4,4,b,c), b,c>=2.

Except at the unordered pair {b,c}={2,6}, the four-dimensional
antisymmetric restriction supplies a noninteger graph eigenvalue in
(V-3,V), different from V-1 and V-2, where V=25(b+1)(c+1)-2.
At {2,6}, the same restriction supplies a noninteger graph eigenvalue
in (V-7,V-6). If b or c is one, the existing unit-exponent theorem applies.

This is a written unbounded argument. Its endpoint reduction uses
sixteen fixed nonsquare discriminants and four explicit low-b
factorizations, followed by two cubic sign values at the exceptional
pair. It uses no finite two-parameter exponent base or modular search.
The remaining higher-prime classification stays open.

## The invariant operator and its interval

Use the paired-support functions in the
[general repeated-pair construction](four-prime-pair-three.md): values
h(T) on {1} union T, -h(T) on {2} union T, and zero elsewhere,
for T subset of {3,4}. Their weighted sum is zero. The complement
restriction is K-I, where in the order empty,{4},{3},{3,4},

```text
K = 5 E_b tensor E_c + 4 F_b tensor F_c
  = [ 5(b+1)(c+1)+4   4c          4b          4bc ]
    [ 4               5(b+1)      4b          0   ]
    [ 4               4c          5(c+1)      0   ]
    [ 4               0           0           5   ].
```

Here E_k=diag(k+1,1), F_k=[[1,k],[1,0]], and diag(1,c,b,bc)
symmetrizes K. The established tensor normalization proves
kappa_min(K)>1. A K-eigenvalue kappa lifts to the original graph
eigenvalue V+1-kappa by complement reflection and the universal shift.

The first/fourth principal submatrix of the symmetric similar matrix
K-4I has determinant

```text
5(b+1)(c+1)-16bc = -11bc+5b+5c+5.
```

At b=2+u,c=2+v, this is -11uv-17u-17v-19<0. Therefore it has a
negative Rayleigh direction, giving kappa_min(K)<4. Consequently

```text
1 < kappa_min(K) < 4,
```

and only the integers two and three need to be examined. The interval
cannot be uniformly shortened to (1,3): at b=c=2, the leading principal
minors of K-3I are 46, 520, 3424, 1728, all positive. Thus
3<kappa_min(K)<4 there.

## The endpoint two never occurs

Put P_2(b,c)=det(K-2I). Direct expansion gives

```text
P_2 = -9b^2c^2+120b^2c-15b^2+120bc^2
      +1014bc+306b-15c^2+306c+189.
```

Order b<=c. For b=32+u,c=32+v, u,v>=0, its negative is

```text
-P_2 = 9u^2v^2+456u^2v+5391u^2+456uv^2+20490uv
       +189390u+5391v^2+189390v+545475 > 0.
```

The remaining thirty symbolic b rows are 2<=b<=31. Write

```text
P_2 = A_b c^2+B_b c+C_b,
A_b=-9b^2+120b-15,
B_b=120b^2+1014b+306,
C_b=-15b^2+306b+189.
```

For 2<=b<=13, A_b and C_b are concave quadratics with positive
endpoint values A_2=189,A_13=24 and C_2=741,C_13=1632.
Thus A_b,C_b>0 throughout that real interval, and B_b>0.
These twelve rows have no positive zero. Two further rows factor as

```text
P_2(21,c)=-24c(61c-3105),
P_2(27,c)=-12(2c-69)(139c-3).
```

Their positive roots 3105/61,69/2,3/139 are not integers. For each
remaining row the discriminant D_b=B_b^2-4A_bC_b lies strictly between
h_b^2 and (h_b+1)^2:

| b | D_b | h_b |
| --- | --- | --- |
| 14 | 1446279552 | 38029 |
| 15 | 1808958096 | 42531 |
| 16 | 2234549520 | 47271 |
| 17 | 2729779200 | 52247 |
| 18 | 3301705152 | 57460 |
| 19 | 3957718032 | 62910 |
| 20 | 4705541136 | 68596 |
| 22 | 6509174400 | 80679 |
| 23 | 7582094352 | 87075 |
| 24 | 8781044112 | 93707 |
| 25 | 10115410176 | 100575 |
| 26 | 11594911680 | 107679 |
| 28 | 15029860752 | 122596 |
| 29 | 17006409792 | 130408 |
| 30 | 19170297216 | 138456 |
| 31 | 21532905360 | 146740 |

None of these quadratics has a rational root. This exhausts the
unbounded reduction, so det(K-2I) never vanishes for integer b,c>=2.

## Endpoint three has one exceptional pair

Direct expansion gives

```text
P_3(b,c)=det(K-3I)
 = -54b^2c^2+30b^2c-60b^2+30bc^2
   +540bc+96b-60c^2+96c+48.
```

For b=4+u,c=4+v, its negative is

```text
-P_3 = 54u^2v^2+402u^2v+804u^2+402uv^2+2436uv
       +3696u+804v^2+3696v+2448 > 0.
```

The only remaining ordered rows are b=2 and b=3:

```text
P_3(2,c)=-216c(c-6),
P_3(3,c)=-6(4c-17)(19c-2).
```

The second row has only the noninteger positive roots 17/4 and 2/19.
Thus {b,c}={2,6} is the sole integer endpoint pair. Outside that pair,
the smallest K-eigenvalue is noninteger in (1,4) and yields the stated
graph eigenvalue in (V-3,V), different from V-1 and V-2.

At (b,c)=(2,6), the exact characteristic polynomial is

```text
det(xI-K)=(x-3)f(x),
f(x)=x^3-161x^2+5775x-35343.
```

The values f(7)=-2464 and f(8)=1065 have opposite signs, so f has
a real root strictly between seven and eight. It is a noninteger
K-eigenvalue, and its graph lift lies in (V-7,V-6). This settles the
exception without a modular subcertificate and completes the theorem.

## Exact verification and presentation scope

The [checker](../scripts/check_four_prime_pair_four.py) verifies the
tensor matrix, both endpoint polynomials, all eighteen coefficients
of the two complete positive tails, all thirty endpoint-two rows,
the two endpoint-three rows, the sixteen strict nonsquare bounds,
the four factorizations, the principal-minor upper bound and the
exceptional characteristic polynomial and cubic signs. Nine specified
support controls check every embedding column, weighted zero sums,
symmetry and complement/universal lifts. Two small expanded graphs
independently check the embedding. The
[report](../results/four-prime-pair-four.json) reproduces byte-for-byte.
These controls validate the implementation; the unbounded conclusion
follows from the written argument and fixed arithmetic.

The theorem is kept as a supporting research note while the authors
consider the classification core and companion-result organization.
It does not change the current 61/67-page manuscript's theorem list.
There is no exponent rectangle scan, numerical eigensolver or Lean
claim, and the historical three-prime certificates were not rerun.
Remaining four-prime candidates have at most one exponent equal to
each of two, three and four, and fail the prior support-weight criterion.
Other repeated exponents a>=5 and higher-prime nonsquarefree Q3
outside the established families remain open.
