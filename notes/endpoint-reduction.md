# A linear bound for the integer endpoint two

For ordered exponents **`4<=a<=b<=c`**, an integer complement root at two
forces the strict bound

```text
c < R(a) = (7a^2-2a+8)/(a+2) = 7a-16+40/(a+2).
```

Consequently, **every all-even triple with minimum at least four and
`c>=R(a)` is nonintegral**. At minimum at least eight, `c>=7a-12`
suffices. This linear tail lies inside the earlier quadratic cutoff.
Examples newly reached by this criterion are `(8,10,44)`, `(10,14,58)`
and `(40,42,266)`; their common divisor is two.

Read [the manuscript proof](../paper/sections/endpoint-reduction.tex),
[the PDF](../paper/paper.pdf), and [exact checks](../results/endpoint-reduction.json).

## Positivity of the endpoint polynomial

Fix the smallest and largest exponents, a and c. The symmetric complement
quintic evaluated at two is a cubic in the middle exponent:

```text
h_C(2) = A(a,c)b^3+B(a,c)b^2+D(a,c)b+E(a,c),
A = ac(a+c-1)+2a(a-1)+2c(c-1)-4,
B = c^2[(a+2)c-(7a^2-2a+8)]
    +(a^3+2a^2-6a-4)c+2(a-2)(a^2-2a-6),
D = (a-2)(c-2)[a^2c+a^2+ac^2+6ac+4a+c^2+4c-12],
E = 2(a-2)(c-2)(a+c-2)(ac+a+c-2).
```

For a,c at least four, A,D,E are strictly positive. The two trailing
terms of B are also strictly positive: `a^3+2a^2-6a-4` is positive at
four and increasing thereafter, and `a^2-2a-6` is likewise positive.
Thus `c>=R(a)` makes B positive, and hence **`h_C(2)>0`** for every
positive b. Conversely, `h_C(2)=0` forces B negative, and therefore
`c<R(a)`. Equality in the rational cutoff is excluded as well.

For three even exponents every entry of C is even. The rational-root
theorem for the integer matrix C/2 says that any integer eigenvalue of C
is even, excluding one. The uniform root in `(0,3)` and `h_C(2)>0`
therefore supply a noninteger root. Alternatively,
`h_C(0)=-abc(a+b+c)(a+b+c+ab+ac+bc)<0` and `h_C(2)>0` directly put a
root in `(0,2)`; it cannot be one. Its graph lift is noninteger.
For a at least eight, `40/(a+2)<=4`, giving `R(a)<=7a-12`.

The surface is not empty: the already settled repeated triple
`(10,10,12)` has `h_C(2)=0` and satisfies the strict linear bound.
This checks the direction of the necessary inequality; it is not a new
family or an integral example.

## Exact divisibility on the two remaining surfaces

For any fixed a,b at least four, the endpoints are integer cubics in c
with nonzero constant terms. Reducing an endpoint equation modulo c gives

```text
h_C(1)=0 => c divides (a-1)(b-1)(a+b-1)(ab+a+b-1),
h_C(2)=0 => c divides 2(a-2)(b-2)(a+b-2)(ab+a+b-2).
```

These give exact finite candidate sets for a fixed pair, followed by
substitution into the cubic; divisibility alone does not imply a root.
No enumeration of those sets or of new exponent ranges is needed here.

The remaining all-even triples are confined to gcd two and
`8<=a<b<c<R(a)`, outside the previously proved regions. Mixed-parity
triples may still have an endpoint at one when `c>=R(a)`; full Q3 stays open.

## Verification

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_reduction.py
```

The checker reconstructs both endpoint cubics from the general quotient,
verifies the coefficient, rational-cutoff and divisor identities, and
checks five positive shifted-coefficient expressions. Three direct integer
quotient fixtures cross-check endpoints with independent integer Horner
evaluation, confirm even entries, and use exact Sturm counts in `(0,2)`.
The existing endpoint-zero fixtures `(9,9,136)` and `(10,10,12)` check the
respective divisibility conditions; the latter checks the strict bound.
Both retain nonlinear rational factors. This is a written infinite-family
proof with symbolic and selected finite exact checks, without an exponent
scan or Lean.

[Return to the project entrance](../README.md).
