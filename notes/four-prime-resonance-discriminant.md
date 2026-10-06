# A discriminant obstruction in the resonant branch

**Theorem.** Let a,b,c be positive integers, let s>=2 be an
integer root of the genuine repeated-pair restriction K(a,b,c),
and put h=a+1-s. Fix a prime ell dividing h and not dividing
s(s-1)(2s-1). If

```text
v_ell(b+h)>=2v_ell(h),
```

then the rational number z=(b+h)/h^2 is integral at ell, and

```text
D_s(z)=(2s-1)^2z^2+2s^2(2s-1)^2z+s^4
```

must be a square or zero modulo ell. There is no tail coprimality
or ordering hypothesis. By symmetry the same test applies with c
in place of b. This addresses the double resonance admitted by
the [previous valuation theorem](four-prime-shared-prime.md),
without asserting that passing the new test produces a root.

**Unbounded nonintegrality family.** For four distinct primes,
every positive exponent vector (a,a,b,c) with

```text
a=6+25n, b=20+100n+125m, n,m>=0, c>=2a-2
```

has noninteger Laplacian spectrum. The tails need not be coprime
or ordered. This written conclusion requires no finite exponent base.

## Exact discriminant at the double resonance

Use p(x)=det(xI-K) and the
[genuine restriction and graph transfer](four-prime-single-pair-balanced.md).
For fixed a,b,s the expression p(s) is a quadratic in c. Denote
its discriminant by Delta_c(s;a,b). At an integer tail root it is
a square: if p(s)=Ac^2+Bc+C=0, then

```text
Delta_c=B^2-4AC=(2Ac+B)^2.
```

This identity remains valid if the leading coefficient vanishes.
The nonzero anchor p(a+1)=-a^2b^2c^2(2a+1) gives h!=0.

Set a=s-1+h and b=-h+h^2z. Direct integer-polynomial division
gives the generic identity

```text
Delta_c(s;s-1+h,-h+h^2z)
    =h^6(s-1)^2 D_s(z)+h^7 E_s(h,z),
E_s in Z[s,h,z].
```

The checker records the full integer polynomial E_s and independently
reconstructs p(s) by a symbolic permutation determinant. The identity
is polynomial in all three variables; no numerical root approximation
or parameter search enters the argument.

The hypothesis on b+h makes z integral at ell. Concretely, if
e=v_ell(h), H=h/ell^e and U=(b+h)/ell^(2e), then H is a unit
and z reduces to U/H^2 modulo ell. Substitute this rational z in
the identity and divide by h^6(s-1)^2. The error is a multiple
of ell, since h is divisible by ell and s-1 is a unit. Thus

```text
Delta_c/[h^6(s-1)^2]=D_s(z) modulo ell.
```

If Delta_c were a square, this normalized rational number would
also be a square. It is integral at ell by the displayed identity,
so its residue must be a square or zero. A nonzero quadratic
nonresidue D_s(z) therefore excludes the integer root s.

The condition implies v_ell(b)=e and b/h=-1 modulo ell. At
e=min tail valuation, the prior cubic resonance then forces the
other scaled tail to the same double-resonance point. The new
discriminant tests the next algebraic constraint at that point.
For v_ell(b+h)>2e, z=0 modulo ell and D_s(0)=s^4 is a square;
the new obstruction can act at the equality v_ell(b+h)=2e.

## Two complete low-root residue tables

For s=2, D_2(z)=9z^2+72z+16. At ell=5:

| z modulo 5 | D_2(z) modulo 5 | Quadratic character |
|---|---|---|
| 0 | 1 | square |
| 1 | 2 | nonsquare |
| 2 | 1 | square |
| 3 | 3 | nonsquare |
| 4 | 3 | nonsquare |

Thus z=1,3,4 excludes root 2. For s=3,
D_3(z)=25z^2+450z+81. At ell=7:

| z modulo 7 | D_3(z) modulo 7 | Quadratic character |
|---|---|---|
| 0 | 4 | square |
| 1 | 3 | nonsquare |
| 2 | 3 | nonsquare |
| 3 | 4 | square |
| 4 | 6 | nonsquare |
| 5 | 2 | square |
| 6 | 6 | nonsquare |

The excluded residues are 1,2,4,6. These are complete local
tables for the stated polynomial at two fixed primes, not an
exponent rectangle or an expanded binary-modulus diagnostic.

## Proof of the three-parameter family

For a=6+25n and b=20+100n+125m,

```text
h=a-1=5(1+5n),
b+h=25(1+5n+5m),
b-(2a-2)=10+50n+125m>0.
```

Hence v_5(h)=1, v_5(b+h)=2, and
z=(b+h)/h^2 reduces to 1 modulo 5. The new discriminant
obstruction excludes root 2, for every integer tail c.

Both tails are at least 2a-2. The
[previous cutoff minor](four-prime-coprime-completion.md) gives
1<kappa_min(K)<3 in this region. Indeed, writing
b=2a-2+u and c=2a-2+v with u,v>=0, the empty/full principal
minor of the symmetric matrix similar to K-3I is

```text
-(a+2)uv-(a^2+3a-2)(u+v)-2(a-1)(3a+2)<0.
```

The only integer in this open low-root interval is 2, already
excluded. Its actual graph lift is V+1-kappa_min, where
V=(a+1)^2(b+1)(c+1)-2, proving nonintegrality. The equality
c=2a-2 is included because the minor remains strictly negative.

## A passing old resonance that is excluded

Take (a,a,b,c)=(6,6,145,20). Both old coarse endpoint
divisibilities hold. At the only good prime 5 for root 2,
e=r=t=1, so the previous valuation range passes. The scaled
values are H=1,B=29,C=4; both cubic factors vanish modulo 5:

```text
B-2C-H=20,
2B-C+H=55.
```

The old modular splitting condition also passes. The only prime
dividing a+1 is 7; the two factors are (x-4)^2 and (x-3)(x+2).
There is no good prime in h=a-2=4 for root 3, so the prior
good-prime valuation test supplies no exclusion there either.

However, b+h=150=25*6 and z=1 modulo 5. The new test
excludes root 2 for every integer c at this fixed a,b. The actual
tail quadratic is

```text
p(2)=-212460c^2+9600900c-459000.
```

It has potential positive real roots, but its discriminant divided
by 5^6 is 2 modulo 5 and cannot be a square. At c=20 the exact
characteristic values are p(2)=106575000 and p(3)=-801589680.
The prior cutoff minor excludes root 3. This comparison concerns
the named arithmetic tests, not every earlier sufficient region or
a claim of priority.

## Verification and limits

The [checker](../scripts/check_four_prime_resonance_discriminant.py)
checks the generic discriminant identity and integer quotient,
the unbounded family identities and strict cutoff minor. Both
complete local residue tables are checked by quadratic characters
and independently by enumerating the squares in the finite fields.
Six specified positive controls verify 336 support-column actions,
weighted zero sums and symmetry, and the actual graph transfer.
Twenty-four independent integer determinants at algebraic c=0,1,2,3
reconstruct and cross-check the six tail quadratics and discriminants.
Zero here is a polynomial interpolation point, not a graph exponent.
Thirty more integer determinants reconstruct six genuine quartics,
and six exact Sturm counts verify one root in (1,3).

Controls include two c=2a-2 boundaries, the root-3 test at prime
7, and a root-2 test with z=2 that passes the necessary discriminant
condition. Passing does not assert an integer root or integrality.
The [certificate](../results/four-prime-resonance-discriminant.json)
is reproducible with SymPy 1.14.0 using
`python3 scripts/check_four_prime_resonance_discriminant.py`.
The unbounded proof does not depend on the six fixed controls.
No parameter scan, expanded graph, historical finite-base rerun,
floating eigenvalues or Lean validation is used.

Other resonances and primes dividing s(s-1)(2s-1) remain unresolved.
The generic test can also constrain second-root offsets through
h=-t. General single-pair, fully unequal four-prime and higher-prime
classification remain open; all prior results and complete finite
inputs retain their scopes. The three-prime main and joint manuscript
decisions are unchanged.
