# Value, derivative and third-shift conditions for clustered odd roots

For positive exponent residue roles a=1, b=3, c=2 modulo four, an
integer Laplacian spectrum requires all the following conditions:

1. a+c=b(b+2) modulo128.
2. b=11 or15 modulo16.
3. Put a=4u+1 and t=(a+c-b(b+2))/128. For b=16v+11, t+u+v is odd;
   for b=16v+15, t+v is odd.

Every violation proves nonintegrality, including all permutations and
without a size or ratio bound. These variables identify the residue roles,
not the increasing order of the exponents. The third condition is applied
after the first two, so its integer parameters are well-defined.

## Proof

The preceding shifted-root theorem forces all three hypothetical integer
odd complement roots to be b modulo eight. The two remaining roots are
even. Thus 512 divides h_C(b), and64 divides h_C'(b): every derivative
term retains at least two odd-root factors divisible by eight. These
conditions include repeated roots and zero evaluations.

Exact substitution into the complement quintic gives

```text
h_C(b)=a^2*b^2*c^2*(a+c-b(b+2)).
```

Because a,b are odd and c=2mod4, the prefactor has two-adic valuation
exactly two. Therefore512|h_C(b) forces128|a+c-b(b+2).
This remains true when h_C(b)=0.

Write (a,b,c)=(4u+1,4w+3,b(b+2)+128t-a). Coefficientwise expansion gives

```text
h_C'(b)=16(w^2-w+2) modulo64.
```

As w runs through0,1,2,3 modulo four, the derivative residues are32,32,0,0.
The required divisor64 forces w=2 or3mod4, equivalently b=11 or15mod16.

For either remaining b residue, set K(z)=h_C(8z+b)/512. Coefficientwise
identities give integer polynomials and their binary reductions:

| Exponent b | K(z) modulo two |
| --- | --- |
| 16v+11 | z^3+z^2+(1+v+u^2)z+t |
| 16v+15 | z^3+z^2+(1+v)z+t |

If all roots were integers, write the three odd roots as b+8r_i.
Then K(z) is the product of the three factors z-r_i and the two
even-root factors8z+b-eta_j. The latter reduce to one modulo two.
Hence this binary cubic must split completely into linear factors.
For lambda,t in the binary field, z^3+z^2+lambda*z+t splits precisely
when t=lambda: the two possibilities are z^2(z+1) and(z+1)^3.
Otherwise it is z(z^2+z+1), or the irreducible cubic z^3+z^2+1.
Using u^2=u modulo two gives exactly the third conditions above.
Any failure therefore supplies a noninteger complement root and graph lift.

## Exact checks and remaining scope

The [checker](../scripts/check_clustered_odd_roots.py) matches the direct
complement quintic to Reza's reflected source and verifies all six exponent
permutations, the exact value factorization, the derivative identity and
both integer-scaled third-shift identities. It displays all four derivative
residues and sixteen shift-parity binary polynomials. These are checks of
the written identities, not an exponent or modulus range scan.

Eight selected fixtures independently reconstruct full quintics by integer
determinant interpolation, including the zero-root checks:56six-by-six
determinants. Another48five-by-five principal cofactors check the derivatives
at b using D=xh_C and D'(b)=h_C(b)+b*h_C'(b).
The fixtures include one new value failure, one derivative failure, both
third-shift failures and four compatible controls.

In particular, the residue-role triples(29,27,754) and(45,47,2258) have
h_C(b)=0 and64|h_C'(b), yet their third-shift cubics fail to split.
This gives explicit obstructions when the clustered-root value and first
derivative tests are both satisfied. The compatible controls retain
nonlinear rational factors; compatibility does not imply integrality.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_clustered_odd_roots.py`
and compare with [the certificate](../results/clustered-odd-roots.json).
There is no Lean formalization or numerical eigenvalue evidence here.
Full Q3 and nonsquarefree higher-prime exponent vectors remain open.
The focused residual question is whether the remaining root distributions,
combined with the endpoint-zero and interval restrictions, force another
noninteger root; one-odd-exponent patterns remain a separate focused case.
