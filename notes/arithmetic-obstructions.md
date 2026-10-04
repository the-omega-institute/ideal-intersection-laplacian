# Common exponent divisors and congruence classes

The [uniform complement root below three](mixed-inertia.md) and the
integer characteristic polynomial give further complete infinite families:

- Every positive three-prime exponent triple with **`gcd(a,b,c)>=3`**
  is nonintegral. Thus every integer `m^d`, `d>=3`, whose base has exactly
  three distinct prime factors has a nonintegral ideal intersection graph.
- Every triple whose **three exponents are all odd** is nonintegral.
- For any odd prime `ell`, if all three exponents have the same nonzero
  residue `r`, and **`r^2+8r+4` is a quadratic nonresidue modulo ell**,
  the graph is nonintegral. In particular this covers common residues
  **1, 3 or 4 modulo 5**, and **1, 2, 4 or 5 modulo 7**.

The exponents may be unequal with arbitrarily large ratios or differences.
These are written arithmetic proofs; they require no exponent scan.
Read [the manuscript source](../paper/sections/arithmetic-obstructions.tex),
[the PDF](../paper/paper.pdf), and
[the exact checks](../results/arithmetic-obstructions.json).

## A common divisor rules out both low integers

Let `d=gcd(a,b,c)>=3`. The six-support complement quotient C has entries
formed from the exponents and their pairwise products, so **C/d is an
integer matrix**. If its eigenvalue `mu/d` is rational, the rational-root
theorem for its monic integer characteristic polynomial forces `mu/d`
to be an integer.

If the minimum exponent equals three, the prior minimum-three theorem
already settles the triple. Otherwise the uniform comparison provides a
positive quotient eigenvalue `0<mu<3`. If mu were an integer, mu/d
would be rational and hence an integer, contradicting `0<mu/d<1`.
Thus mu is noninteger and lifts to a noninteger graph eigenvalue.

Equivalently, an integer quotient eigenvalue must be a multiple of d.
This excludes both 1 and 2, precisely the possible low integers in the
remaining three-prime problem.

## Modular splitting detects another noninteger root

Write `h_C(x)=det(xI-C)/x`, a monic integer quintic. If every root were
an integer, its reduction modulo every prime would split completely into
linear factors. An irreducible nonlinear factor modulo even one prime
therefore proves nonintegrality. The quotient is similar to a real
symmetric Laplacian, so its roots are real, and a noninteger complement
root lifts to a noninteger graph eigenvalue. This reasoning does not
require the smallest positive root itself to be noninteger.

For all odd exponents, reduction of the general quotient gives

```text
h_C(x) mod2 = x(x^2+x+1)^2.
```

The quadratic takes the value 1 at both elements of the binary field,
so it is irreducible. Consequently every all-odd triple is nonintegral.
The other parity patterns give `x^5` when all exponents are even, and
`x^2(x+1)^3` when one or two exponents are odd. These reductions supply
no obstruction; they do not prove integrality.

For three exponents with the same residue r modulo a prime, specialize
the general equal-exponent identity from the preceding proof:

```text
h_C(x) = (x-r^2-r)[x^2-(r^2+4r)x+3r^2]^2 modulo ell.
```

The quadratic discriminant is `r^2(r^2+8r+4)`. For an odd prime and
nonzero r, it is nonsquare exactly when `r^2+8r+4` is nonsquare. The
quadratic is then irreducible. Actual equality of the three exponents
is unnecessary: their common residue gives the same reduced polynomial.

Modulo 5, the squares are `{0,1,4}`. At residues 1, 3 and 4, the
discriminant factors are respectively 3, 2 and 2, proving those three
infinite congruence classes. Modulo 7 the nonzero squares are `{1,2,4}`;
residues 1, 2, 4 and 5 give factors 6, 3, 3 and 6. For example,
`(11,16,21)`, `(13,18,23)` and `(14,19,24)` have mixed parity and gcd1,
so the modulo-five argument adds cases outside the other two arithmetic
conditions and outside the earlier balanced-span bound.

## The endpoint-zero condition remains necessary, not sufficient

The prior low-root bound says that a possible integral triple with
minimum exponent at least four must satisfy `h_C(1)h_C(2)=0`.
The new common-divisor theorem excludes gcd at least three altogether;
the modular theorem can rule out integrality through another quotient
root even if one of the low endpoints vanishes.

An existing example is Reza's repeated-exponent boundary family:
`h_(a,a,c)(1)` contains the factor `2a^2-3a-c+1`. At `(9,9,136)`,
`h_C(1)=0`, while the quotient still has a nonlinear irreducible factor
over the rationals. The already proved boundary theorem settles this
example. It is not a new family or an integral example.

The remaining problem has gcd1 or2, at least one even exponent, and lies
outside the proved congruence classes as well as the earlier families,
cutoff and balanced criterion. Its possible integral triples must still
lie on one of the two endpoint-zero surfaces. Full Q3 and nonsquarefree
vectors with more than three prime factors remain open.

## Exact verification

Run with Python 3.10+ and SymPy 1.14.0:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_arithmetic_obstructions.py
```

The checker verifies that the symbolic quotient at `(da,db,dc)`, divided
by d, has integer-polynomial entries, and verifies the general equal-exponent
factorization and discriminant identity. It checks all **eight parity
patterns**, every nonzero common residue for primes **3, 5 and 7**, and
all **70 quadratic residue evaluations** including the binary quadratic,
using independent integer Horner arithmetic. Direct characteristic
polynomials agree with the symbolic reductions and exact factorizations.

Six selected positive exponent triples independently check the quotient
scaling, low-root and modular witnesses. The existing endpoint-zero
boundary example is also reconstructed directly. These fixtures validate
the formulas; the infinite theorems use the written divisibility and
finite-field arguments. The earlier large finite certificates are retained,
not rerun or enlarged. No numerical spectrum or Lean is used.

[Return to the project entrance](../README.md).
