# Endpoint-one roots above the minimum exponent

Let C be the six-support complement quotient, h_C(x)=det(xI-C)/x,
and sort the positive real exponents as 4<=a<=b<=c.

**Theorem.** On h_C(1)=0,

```text
b+c>=2a²-2a+1,
```

with equality precisely when b=a and c=(a-1)(2a-1). Root one is simple
and is the smallest positive quotient root. All four remaining roots
are strictly greater than a. In particular the smallest root mu_1 of
F(x)=h_C(x)/(x-1) satisfies

```text
a<mu_1<c.
```

These are written results for the entire stated real domain, with no
finite base. The proof does not use the earlier minimum-eight positive
coefficient certificate. That earlier result additionally gives generic
residual positivity off endpoint one and is preserved.

## A lower bound on the exponent sum

Put q=b+c, z=bc and K=4a²-2a+1. Rewriting the generic endpoint determinant
in these symmetric variables gives

```text
H_a(q,z)=h_C(1)
 =(q-K)z²-a(a-1)(q+2a-1)z+P_a(q),
P_a(q)=(a²-1)q³+(a³-a²-3a+3)q²
        +(-3a²+6a-3)q-a³+3a²-3a+1.
```

Since (b-a)(c-a)>=0, z>=z_0=a(q-a). Let Q=2a²-2a+1.
If q<=Q, then q-K<=-2a²<0, and

```text
H_a(q,z)-H_a(q,z_0)
 =(z-z_0)[(q-K)(z+z_0)-a(a-1)(q+2a-1)]<=0.
```

The bracket is strictly negative, so equality here requires z=z_0.
The value at z_0 is the repeated-minimum specialization, with t=q-a>=a:

```text
H_a(q,z_0)=[(a-1)(2a-1)-t]B(a,t),
B(a,t)=a³-2a²t²+a²t+a²+3at-3a+t²-2t+1.
```

To see B<0 throughout a>=4,t>=a, set a=4+m and t=a+u, m,u>=0.
The exact identity is

```text
-B(4+m,4+m+u)
 =2m⁴+4m³u+30m³+2m²u²+47m²u+163m²
  +16mu²+179mu+381m+31u²+222u+323>0.
```

For q<Q the first factor is positive, so H_a(q,z)<0, which excludes
endpoint one. For q=Q, H_a(q,z_0)=0 and the strictly negative difference
excludes z>z_0. Equality therefore requires (b-a)(c-a)=0; size ordering
gives b=a, c=(a-1)(2a-1). Conversely that triple has h_C(1)=0 by the
displayed factorization. Every fully distinct endpoint-one triple has q>Q.

## Counting the roots below a

The established weighted symmetric similarity
S=W^(1/2)CW^(-1/2), W=diag(a,b,c,ab,ac,bc), is positive semidefinite
with one-dimensional zero kernel. Its pair-support principal block is
diag(c,b,a). Write its eigenvalues as
0=lambda_1<lambda_2<=...<=lambda_6. Principal interlacing gives
a<=lambda_4, so at most three eigenvalues can be strictly below a.

The sum bound gives

```text
q-(a²+2a)>=a²-4a+1=(a-4)²+4(a-4)+1>0.
h_C(a)=-a²b²c²(a²+2a-b-c)>0.
```

Thus a is not an eigenvalue and det(aI-S)=a h_C(a)>0. In dimension
six, the sign of this determinant is (-1)^N, where N is the number of
eigenvalues strictly below a, counted with multiplicity. Hence N is even.
The zero root and the endpoint root one are both below a, so N>=2;
interlacing gives N<=3. Therefore N=2, exactly the roots zero and one.
In particular one is simple and lambda_3,...,lambda_6 are all above a.

The [strict upper bound](endpoint-one-divisor-window.md) gives lambda_3<c,
so mu_1=lambda_3 lies in (a,c). This is an endpoint-one statement;
the residual outside h_C(1)=0 is not identified with quotient roots.

## Sharpened integer-root diagnostic

With integer exponents, F is monic with positive integer constant
rs(p+s), where s=a+b+c,p=ab+ac+bc,r=abc. An integer spectrum requires
its smallest root to be a positive divisor d of that constant with

```text
a+1<=d<=c-1.
```

The previous [5,c-1] window at minimum>=8 is thus sharpened to [a+1,c-1].
For the three established controls the counts drop from38,39,197to
34,35,183 respectively. All252remaining candidates have nonzero exact
Horner values. Independent rational factorization agrees, and exact Sturm
counts give no residual roots on [0,a] and one in (a,c) in each control.
These controls were already nonintegral by the repeated-exponent theorem;
the checks do not establish a new nonintegrality family or decide the
unbounded endpoint-one surface. Full Q3 stays open.

The [checker](../scripts/check_endpoint_one_minimum_root.py) reconstructs
the generic quotient and all identities above, including the complete
12-term positive identity. The [certificate](../results/endpoint-one-minimum-root.json)
records every control candidate/evaluation and source hash. The infinite
statements have written proofs; the three controls are finite exact
diagnostics. No Lean verification is claimed.
