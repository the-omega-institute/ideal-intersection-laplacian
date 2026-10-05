# Window signs and coefficient tests for integer roots

Let C be the six-support complement quotient, h_C(x)=det(xI-C)/x,
and assume integer 4<=a<=b<=c on endpoint one h_C(1)=0. Put
s=a+b+c, p=ab+ac+bc, r=abc, N=rs(p+s), so h_C(x)=(x-1)F(x).
The smallest quartic root lies in (a,min(c,a+b)).

## Negativity is not uniform on the full divisor window

The established endpoint-one control (20,20,741) gives

```text
N=7134703976400=21*339747808400,
20<21<min(741,40)=40,
F(21)=1207587225600>0.
```

Thus even among divisors of N in the window, F(d) need not be negative.
The earlier negative evaluation at d=3a/2 was for a particular candidate
on a particular repeated boundary family. It was not a sign theorem for
every divisor. At the same control, F(30)=-1257386661900<0, so both signs
occur among candidates in one window.

In fact the boundary family b=a,c=(a-1)(2a-1) has

```text
F(a)=a^4(a-1)(2a-1)^2(a^2-4a+1)>0 for a>=4.
```

This positivity at the lower endpoint is consistent with the earlier
minimum-root theorem. It does not determine the sign at the next integer.
These controls have repeated exponents. They disprove full-surface uniform
negativity, but do not decide the proposed statement restricted to the
remaining fully distinct integer endpoint-one triples. That narrower
question and full Q3 remain open.

## A coefficient congruence

Write the existing symmetric quartic as

```text
F(x)=x^4-Ax^3+Bx^2-Dx+N,
A=p+3s-1,
B=sr+2sp+3s^2-3s+1,
D=r^2+(s^2-s+1)r+s^2p+p^2+s^3-3s^2+3s-1.
```

Every positive integer root d satisfies both

```text
d divides N,
N/d = D modulo d,
```

or equivalently d^2 divides N-Dd. Indeed F(d)=0 gives

```text
N-Dd=-d^2(d^2-Ad+B).
```

Once d divides N, the second congruence can reject d using just N and D,
without evaluating the full quartic at d. This is a uniform necessary
condition, not a sufficient root condition. It involves the candidate's
own modulus; it is not a new higher two-adic lift of the endpoint test.

## Congruences from the three exponent evaluations

For each e in {a,b,c}, the generic determinant identity is

```text
h_C(e)=-r^2(e^2+3e-s).
```

On endpoint one, therefore,

```text
K_e=F(e)=-r^2(e^2+3e-s)/(e-1).
```

The quotient is an integer because F has integer coefficients and e is
an integer. If d is an integer root and d!=e, the integer polynomial
difference F(d)-F(e) is divisible by d-e. Consequently

```text
d-e divides K_e,
```

equivalently (d-e)(e-1) divides r^2(e^2+3e-s). If d=e, the required
condition is K_e=0, not division by zero. These three tests use only
a,b,c and d; they do not evaluate F(d). When d=b is allowed by the
window, its equality case must be checked explicitly.

Both sets of congruences hold for every integer root, not only the
smallest. They can be combined with the spectral window and 12|N.
Neither their derivation nor their application here gives a uniform
exclusion of all fully distinct surviving triples.

## Exact diagnostics on the existing candidates

The same three established controls and the same 23 divisors from the
earlier pair-sum-window certificate are used. No range is expanded.

| (a,b,c) | Window divisors | Pass N/d=D modulo d | Pass all exponent tests | Pass both |
|---|---:|---|---|---|
| (8,8,105) | 5 | 10,15 | 15 | 15 |
| (9,9,136) | 5 | 14 | 11 | none |
| (20,20,741) | 13 | 30 | 21 | none |

Together these congruences reduce 23 candidates to one. That last divisor,
d=15 at (8,8,105), has F(15)=-798518700 and is not a root. It demonstrates
that passing both congruence sets is insufficient. The positive candidate
d=21 at (20,20,741) passes every exponent test but fails the coefficient
test. All three graphs were already nonintegral by the repeated-exponent
theorem; this is a diagnostic improvement, not a new nonintegrality family.

The [checker](../scripts/check_endpoint_one_root_congruences.py) reconstructs
the generic six-support determinant and quartic coefficients, proves the
three exponent identities, and independently evaluates every candidate by
integer Horner and direct polynomial evaluation. It checks both congruence
remainders against the exact values. The
[certificate](../results/endpoint-one-root-congruences.json) retains every
candidate, remainder, value and source hash. The congruences have written
unbounded proofs; the three controls are finite diagnostics. No exponent
scan, higher endpoint two-adic lifting, floating spectrum or Lean is used.
Prior manuscript, proofs and finite dependencies are retained.
