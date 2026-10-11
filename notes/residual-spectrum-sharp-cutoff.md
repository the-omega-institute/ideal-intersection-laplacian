# Sharp real cutoff for the endpoint-one residual spectrum

On the real ordered endpoint-one surface
\(2\le a\le b\le c\), \(h_C(1)=0\), the root-one and residual
separation statement holds whenever

\[
a>2+\sqrt3.
\]

Root one is simple and the smallest positive quotient root. The four
remaining positive roots satisfy

\[
a<\mu_1<\min\{c,a+b\},\qquad a+b+c<\mu_2\le\mu_3\le\mu_4.
\]

This strengthens the former real hypothesis \(a\ge4\) and gives its
sharp uniform lower cutoff for the strict residual bound. The integer
divisor corollary still starts at \(a=4\), and the global three-prime
classification retains its existing integer proof and finite inputs.

The established sharp sum bound gives

\[
b+c-(a^2+2a)\ge a^2-4a+1
=(a-2-\sqrt3)(a-2+\sqrt3)>0.
\]

The direct determinant identity is therefore

\[
h_C(a)=a^2b^2c^2[b+c-a^2-2a]>0.
\]

The symmetric quotient's pair-support principal block is
\(\operatorname{diag}(c,b,a)\), so at most three eigenvalues lie
below \(a\). At least two do, namely zero and the endpoint root one.
No eigenvalue equals \(a\). The positive determinant
\(\det(aI-S)=a h_C(a)\) forces an even number below it, hence exactly
two. Root one is consequently simple and smallest positive, and all
four other roots exceed \(a\).

Interlacing with the pair-support block gives \(\lambda_3\le c\),
while

\[
h_C(c)=-a^2b^2c^2(c^2+2c-a-b)<0
\]

excludes equality. The established global gap gives
\(\lambda_3<a+b\) and \(\lambda_4>a+b+c\); its sole equality
case \((2,2,2)\) is outside the new cutoff. These facts give the
claimed residual windows.

The cutoff is sharp on the ordered repeated endpoint-one family

\[
b=a,\qquad c=(a-1)(2a-1),\qquad a\ge2.
\]

It is admissible because \(c-a=2(a-1)^2-1>0\). The generic
determinant on this family obeys

\[
h_C(1)=0,\qquad
h_C(a)=a^4(a-1)^2(2a-1)^2(a^2-4a+1).
\]

At \(a=2+\sqrt3\), a residual root equals \(a\), so the strict
lower window fails. The global gap and the three distinct roots zero,
one and \(a\) show that both low positive roots are simple there;
the other three exceed the total sum. For every \(2\le a<2+\sqrt3\),
the determinant at \(a\) is negative. At least two and at most three
eigenvalues lie below it, so determinant parity forces exactly three.
After removing zero and one, a residual root lies below \(a\).
Thus a uniform extension of this entire strict residual statement to
all real minima two or three would be false.

With Python 3.10 or later and SymPy 1.14.0, run:

```sh
python3 scripts/verify_residual_spectrum_cutoff.py
```

The saved result is `results/residual-spectrum-sharp-cutoff.json`.
The checker verifies generic direct determinant and anchor identities,
the sum-bound factorization, the full repeated equality family and its
ordering, and the exact boundary root over \(\mathbb Q(\sqrt3)\).
Two fixed controls below the cutoff, \((2,2,3)\) and \((3,3,10)\),
each have one residual root below the minimum and three above the total
sum. The newly admitted rational control
\((15/4,15/4,143/8)\) has one residual root in the stated lower window
and three above the total sum. The controls supplement the written
proof; there is no parameter scan or finite exponent base. The support
constructor and SymPy backend are shared, and the original
characteristic-polynomial helper is not imported. No Lean verification
or historical finite-base rerun is claimed.
