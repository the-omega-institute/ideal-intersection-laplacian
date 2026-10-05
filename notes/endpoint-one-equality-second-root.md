# The three remaining equality roots exceed the pair sum

**Unconditional equality theorem.** For real4<=a<=b and c=b(b+2)-a,
the six-support complement quotient has

```text
0=lambda_1<lambda_2<lambda_3=b<a+b<lambda_4<=lambda_5<=lambda_6.
```

The earlier [equality theorem](endpoint-one-equality-root.md) proves
lambda_3=b simple, without an endpoint-one hypothesis. The new strict
bound lambda_4>a+b also needs no endpoint-one hypothesis. If h_C(1)=0,
then lambda_2=1 and F(x)=(x-b)P_3(x), where all three roots of the monic
cubic P_3 exceed a+b. This strengthens the earlier bound that they exceed b.
Integer equality feasibility and integral cubic splitting remain open.

## Two positive identities and interlacing

Write s=a+b. The equality exponent satisfies
c-s=b(b+1)-2a>=b(b-1)>0. Use the earlier symmetric similarity and delete
singleton support2. Its five-support block B is the scalar b on support13
plus the four-support block T on 1,3,12,23. Recall

```text
det(xI-T)=(x-b)K(x),
K(x)=x^3-b(b^2+4b+5)x^2
     +[ac(b^2+1)+b^2(b+2)(b^2+3b+3)]x-abc(b+3).
```

The pair block diag(c,a) gives the largest T eigenvalue at least c>s.
Exact substitution gives K(s)=bU with

```text
U=a^2 b(b^2-a-2)+2a^2
  +ab[b(2b^2-3)+4b^2-5]+b^2(b+1)^2(b+2)>0.
```

Indeed b^2-a-2>=b^2-b-2>0 and all the other displayed factors are
positive for b>=a>=4. T is positive definite, so K has three positive
real roots with multiplicity. Since K(s)>0, an odd number lie below s;
its largest root exceeds s, ruling out three. Exactly one K root is below
s and two above. Because b<s, B has exactly three eigenvalues below s
and two above. Thus beta_4>s. Five-support interlacing yields
lambda_5>=beta_4>s, and therefore lambda_6>s.

The full quotient's nonzero characteristic polynomial has the exact value

```text
h_C(s)=-abc(s+1)V<0,
V=a^2 b(b^2-a-2)+a^2 b^2+2a^2
  +ab[b(b^2-2)+3b^2-5]+b^2(b+1)(b+2)>0.
```

The same domain inequalities prove positivity term by term. Thus no full
eigenvalue equals s, and det(sI-S)=s h_C(s)<0. A six-dimensional determinant
is negative when the number of eigenvalues below s is odd. The earlier
equality theorem already places lambda_1,lambda_2,lambda_3 below s;
the principal bound places lambda_5,lambda_6 above it. If lambda_4 were
below s, that count would be four and the determinant positive. Hence
lambda_4>s. This sign argument is unconditional on h_C(1)=0.

## Exact diagnostics and scope

| (a,b,c) | s=a+b | Other nonzero roots below s | Above s | Endpoint one? |
|---|---:|---:|---:|---|
| (4,4,20) | 8 | 1 | 3 | no |
| (9,12,159) | 21 | 1 | 3 | no |
| (9,30,951) | 39 | 1 | 3 | no |

The counts refer to h_C(x)/(x-b): the removed root b is also below s.
All three are the same selected E=0 fixtures used previously and are off
endpoint one. Exact Sturm counts and determinant signs supplement the
written proof; they are not a finite base or integer endpoint solutions.

The [checker](../scripts/check_endpoint_one_equality_second_root.py) reconstructs
the quotient and T, verifies the two positive identities and c>s, then
checks the three fixed controls. The
[certificate](../results/endpoint-one-equality-second-root.json) records both
decompositions, counts, source and prior-certificate hashes. The earlier
b-index proof supplies the necessary lambda_3 position; neither the
genus-ten argument nor its finite automorphism certificate is used here.
No exponent/modulus search, higher two-adic lift, floating spectrum or Lean
was used. The theorem excludes no new integer equality triple by itself;
the integer cubic roots must now all be searched strictly above a+b.
