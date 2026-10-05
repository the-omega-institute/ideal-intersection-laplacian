# A local discriminant obstruction on the equality curve

Let the positive integer exponents be ordered as a<=b<=c, with
c=b(b+2)-a and q=ac. Retain the [explicit cubic](endpoint-one-equality-cubic.md)
P3 and equality equation G=0. On this curve
h_C(x)=(x-1)(x-b)P3(x). Write Delta for the integer discriminant of P3.

**Theorem.** Let p be an odd prime dividing b. If a²=1 modulo p and
13 is a quadratic nonresidue modulo p, the ideal intersection graph is
Laplacian nonintegral. This is a written uniform obstruction, with no
minimum, gap or finite exponent base.

In particular, an integral equality spectrum requires **7 and 11 not
to divide b**. At modulo five, it excludes the previously compatible
rows (a,b)=(1,0),(4,0), leaving precisely the necessary conditions

```text
(a,b)mod5 in {(2,0),(3,0),(0,2),(3,2)}.
```

These four conditions do not assert integer equality points or integral
spectra. The new obstruction requires G=0; it is not a global assertion
about all exponent triples in these residue classes.

## The normalized discriminant is 13

The algebraic reduction is prompted by the double root in the compatible
negative branch. Modulo an odd prime dividing b, G=1-q². For q=-1,
P3=x(x+1)², so Delta=0 modulo p and the ordinary discriminant-square
congruence sees no obstruction. We resolve this degeneracy without a
modulus table: put

```text
v=-1+2b+3b².
```

Exact integer polynomial identities give

```text
G(v,b)=b³(-b⁴-8b³+8b²+20b-7),
Delta(v,b)=13b²+b³R(b),
G(q,b)-G(v,b)=(q-v)[(3b-1)(q+v)+b(b²+4b-1)].
```

The full R(b), in descending order, is

```text
13b¹³+56b¹²-328b¹¹-1774b¹⁰+376b⁹+10222b⁸+5913b⁷
-17770b⁶-14202b⁵+5840b⁴+3263b³-324b²-302b-4.
```

Suppose G(q,b)=0, p|b and q=-1 modulo p. Set e=v_p(b)>=1.
The bracket in the last identity is 2 modulo p and is a p-adic unit.
The first identity then forces q-v to be divisible by p^(3e).
The discriminant is an integer polynomial in q,b, so replacing q by v
changes it by a multiple of q-v. Consequently

```text
Delta(q,b)=13b² mod p^(3e).
```

If 13 is a nonresidue modulo p, p!=13. Thus v_p(Delta)=2e and
the p-adic unit after dividing by p^(2e) is congruent to
13(b/p^e)² modulo p. This unit is a nonresidue. Delta therefore cannot
be a rational square, including zero. An integer-root splitting of P3
would have discriminant equal to the square of the product of its three
pairwise root differences. This contradiction proves nonintegrality.

Since q=ac=-a² modulo p, a²=1 is exactly the branch q=-1 used here.
Every actual integer root d in this branch must have d=0 or -1 modulo p,
but that root congruence alone permits the row. The normalized
discriminant excludes the complete system G=0, P3(d)=0, Delta=u² even
when an actual integer root is supplied.

## The specified prime consequences

For p=7 or11, -1 is a nonresidue. G=0 and p|b imply q²=1 and a⁴=1
modulo p. The alternative a²=-1 is impossible, so a²=1 holds
automatically. The nonzero square sets are {1,2,4} modulo seven and
{1,3,4,5,9} modulo eleven; 13 reduces to6 and2, respectively. The
theorem therefore excludes an integral equality spectrum whenever either
prime divides b, regardless of its positive valuation.

For p=5, 13 reduces to the nonresidue3. Among the four b=0 rows in
the earlier [finite-field table](endpoint-one-equality-mod-five.md),
a=1 or4 gives a²=1 and is excluded. The rows a=2 or3 give q=1;
their reduction P3=x(x²+1) splits modulo five and the present argument
does not exclude them. Together with the earlier b=2 rows, this yields
the four necessary pairs above. No new prime search or higher two-adic
shift is involved.

## Exact verification

Run with Python3.10+ and SymPy1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_endpoint_one_equality_local_discriminant.py
```

The [certificate](../results/endpoint-one-equality-local-discriminant.json)
records both anchor identities, every coefficient of R, the curve
difference factor and its unit2, and generic discriminant divisibility
by q-v. The existing generic direct quotient identity and independent
5x5 Sylvester discriminant check are rerun. Exactly the three specified
prime examples are checked. There is no exponent scan, enumerated integer
equality point, finite exponent base or Lean verification. The general
endpoint-one classification and full Q3 remain open.

[Return to the project entrance](../README.md).
