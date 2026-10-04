import hashlib
import json
from math import isqrt
from pathlib import Path

import sympy

from check_aa_b import cubic_coeffs, cubic_poly


first_exponent, third_exponent, variable = sympy.symbols("a b x")
quotient = sympy.Matrix([
    [first_exponent ** 2 + first_exponent * third_exponent, 0, -first_exponent ** 2, -first_exponent * third_exponent],
    [0, 2 * first_exponent * third_exponent, 0, -2 * first_exponent * third_exponent],
    [-2 * first_exponent, 0, 2 * first_exponent + 2 * first_exponent * third_exponent, -2 * first_exponent * third_exponent],
    [-first_exponent, -third_exponent, -first_exponent ** 2, first_exponent ** 2 + first_exponent + third_exponent],
])
coefficients = cubic_coeffs(first_exponent, third_exponent)
cubic = variable ** 3 - coefficients[0] * variable ** 2 + coefficients[1] * variable - coefficients[2]
discriminant = ((first_exponent + 1) ** 2 * third_exponent ** 2
                + 2 * first_exponent * (3 * first_exponent + 1) * third_exponent + first_exponent ** 2)
center = (first_exponent + 1) ** 2 * third_exponent + first_exponent * (3 * first_exponent + 1)


def equal(first, second):
    if sympy.expand(first - second) != 0:
        raise AssertionError("Polynomial identity failed")


equal(quotient.charpoly(variable).as_expr(), variable * cubic)
equal(center ** 2 - (first_exponent + 1) ** 2 * discriminant, 4 * first_exponent ** 3 * (2 * first_exponent + 1))
equal(first_exponent ** 3 * (2 * first_exponent + 1) + 1 - first_exponent * (3 * first_exponent + 1),
      (first_exponent + 1) ** 2 * (first_exponent - 1) * (2 * first_exponent - 1))
equal(cubic.subs(third_exponent, first_exponent),
      (variable - 2 * first_exponent * (first_exponent + 1))
      * (variable ** 2 - (5 * first_exponent ** 2 + 2 * first_exponent) * variable
         + 6 * first_exponent ** 4 + 3 * first_exponent ** 3))
equal(cubic.subs(third_exponent, first_exponent * (first_exponent + 1)),
      (variable - 2 * first_exponent * (first_exponent + 1) ** 2)
      * (variable ** 2 - (3 * first_exponent ** 3 + 4 * first_exponent ** 2 + 2 * first_exponent) * variable
         + 2 * first_exponent ** 6 + 6 * first_exponent ** 5 + 7 * first_exponent ** 4 + 3 * first_exponent ** 3))
expected = {2: [3], 3: [10], 4: [2, 21]}
records = []
for repeated_exponent, exceptional_exponents in expected.items():
    constant = 4 * repeated_exponent ** 3 * (2 * repeated_exponent + 1)
    factors = []
    admissible = []
    for lower in range(1, isqrt(constant) + 1):
        if constant % lower:
            continue
        upper = constant // lower
        valid = False
        value = None
        square_root = None
        if (lower + upper) % 2 == 0:
            numerator = (lower + upper) // 2 - repeated_exponent * (3 * repeated_exponent + 1)
            denominator = (repeated_exponent + 1) ** 2
            if numerator % denominator == 0 and (upper - lower) % (2 * (repeated_exponent + 1)) == 0:
                value = numerator // denominator
                square_root = (upper - lower) // (2 * (repeated_exponent + 1))
                valid = value >= 1
        factors.append({"lower": lower, "upper": upper, "admissible": valid,
                        "third_exponent_if_integral": value, "square_root_if_integral": square_root})
        if valid:
            admissible.append(value)
            equal(discriminant.subs({first_exponent: repeated_exponent, third_exponent: value}), square_root ** 2)
    if sorted(admissible) != exceptional_exponents:
        raise AssertionError("Complete factor-pair enumeration does not match the stated exception list")
    witnesses = []
    for third_value in exceptional_exponents:
        prime = 13 if (repeated_exponent, third_value) == (3, 10) else 5
        polynomial = cubic_poly(repeated_exponent, third_value)
        residues = [int(polynomial.eval(residue)) % prime for residue in range(prime)]
        if any(value == 0 for value in residues):
            raise AssertionError("Exceptional cubic has a root modulo its witness prime")
        witnesses.append({"third_exponent": third_value, "polynomial": str(polynomial.as_expr()),
                          "prime": prime, "values_modulo_prime": residues})
    records.append({"repeated_exponent": repeated_exponent, "constant": constant,
                    "all_factor_pairs": factors, "exceptional_third_exponents": exceptional_exponents,
                    "exceptional_cubic_witnesses": witnesses})
print(json.dumps({"symbolic_identities": "passed", "fixed_exponents": records,
                  "sympy": sympy.__version__,
                  "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "diagnostic_sha256": hashlib.sha256(Path(__file__).with_name('check_aa_b.py').read_bytes()).hexdigest(),
                  "scope": "Complete fixed-a=2,3,4 certificates for all b>=1; exact identity supporting written all-a upper-bound corollary b>(a-1)(2a-1). Below-bound exceptional pairs at arbitrary a and fullQ3 remain open; no Lean."}, indent=2))
