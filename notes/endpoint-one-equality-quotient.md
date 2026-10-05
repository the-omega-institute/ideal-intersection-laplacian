# The known genus-three quotient has no further rational involution

The [equality curve](endpoint-one-equality-curve.md) has genus ten. Its
involution a -> b(b+2)-a exchanges a and c, giving the genus-three
hyperelliptic quotient H: y^2=D(b). This is already the descent supplied
by the a/c symmetry; exchanging c introduces no second independent symmetry.

The other support permutations do not preserve the equality subfamily in
general. For instance, after interchanging a and b, the required equality
would be b+c=a(a+2). On the original equality subfamily its difference is

```text
b+c-a(a+2)=(b-a)(b+a+3),
```

which is nonzero for positive fully distinct a<b. Thus the symmetry of
the original quotient must not be confused with automorphisms of this curve.

## A complete branch-stabilizer certificate at five

Reduction of the degree-eight branch form D at five has ascending coefficients

```text
[4,1,1,3,1,2,3,2,2].
```

It retains degree eight and gcd(D,D')=1 over F5. The projective double
cover therefore has good smooth reduction at five, including its two
unramified points at infinity. For a matrix M in PGL2(F5), write

```text
D_hom(M(X,Z))=k D_hom(X,Z), k!=0.
```

This coefficient identity is exactly the condition that M preserve the
whole eight-point branch divisor over the algebraic closure; it does not
test only the F5-rational roots. Normalize the first nonzero matrix entry
to one and require nonzero determinant. The checker exhausts all
5(5^2-1)=120 elements and finds the identity as the sole stabilizer.

Suppose H had a rational involution other than its hyperelliptic involution.
Its action on the intrinsic hyperelliptic base P1 would be a nontrivial
rational involution. At good reduction it extends to the smooth proper
model over Z5, and therefore to its hyperelliptic quotient P1 over Z5.
Its reduction would stabilize the branch divisor, hence be the identity
by the certificate. But the kernel of
PGL2(Z5) -> PGL2(F5) is a pro-five group and has no nontrivial order-two
element. This contradicts its being an involution. Thus H has no extra
rational involution and no degree-two quotient over Q of genus one or two.
The hyperelliptic quotient has genus zero and retains the square condition.

The extension used here is the standard uniqueness of the smooth proper
model of a good-reduction curve of genus at least two; the quotient is
intrinsic and two is invertible at five. The characteristic-five computation
and this characteristic-zero specialization argument are distinct steps.

This rules out the simplest further double-cover descent on H. It does
not classify maps of higher degree, involutions of the original genus-ten
curve, or maps defined over number fields. No genus-one or genus-two
subcover supporting an effective integer-point computation is established.

## Rank and presentation

No Mordell-Weil rank or certified bound has been computed for either
Jacobian. The classical Chabauty-Coleman condition is rank J(Q)<genus:
rank at most nine would suffice for the genus-ten curve, and rank at most
two for H. Neither inequality follows from the genus calculation or this
finite branch-stabilizer check. Pullback from H gives an isogeny factor in
the larger Jacobian and hence rank J(C)(Q)>=rank J(H)(Q); this is not an
upper bound. A sieve would also need additional certified arithmetic data.

For the combinatorial manuscript, the genus-ten finiteness consequence is
suited to a compact remark rather than a separate main section. The detailed
normalization/ramification argument and this descent diagnostic remain in
supporting notes. Effective admissible integer-point classification and the
remaining cubic's integral splitting stay open.

The [checker](../scripts/check_endpoint_one_equality_quotient.py) and
[certificate](../results/endpoint-one-equality-quotient.json) retain the exact
branch coefficients, good-reduction gcd and exhaustive 120-element result.
This finite group computation addresses this specific descent question;
it is not an enlarged parameter search, a rank computation or Lean verification.
