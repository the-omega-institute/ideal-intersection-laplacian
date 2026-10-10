import json

import sympy

from verify_minimum_three import complement_quotient


minimum, middle, maximum, exponent_sum, exponent_product, offset = sympy.symbols("a b c q z u")
matrix = sympy.Matrix(complement_quotient((minimum, middle, maximum)))
direct_endpoint = sympy.expand((sympy.eye(6) - matrix).det(method="domain-ge"))
cutoff = 2 * minimum ** 2 - 2 * minimum + 1
leading_cutoff = 4 * minimum ** 2 - 2 * minimum + 1
constant = ((minimum ** 2 - 1) * exponent_sum ** 3
            + (minimum ** 3 - minimum ** 2 - 3 * minimum + 3) * exponent_sum ** 2
            - 3 * (minimum - 1) ** 2 * exponent_sum - (minimum - 1) ** 3)
endpoint = ((exponent_sum - leading_cutoff) * exponent_product ** 2
            - minimum * (minimum - 1) * (exponent_sum + 2 * minimum - 1) * exponent_product
            + constant)
assert sympy.expand(direct_endpoint - endpoint.subs({exponent_sum: middle + maximum,
                                                    exponent_product: middle * maximum})) == 0
lower_product = minimum * (exponent_sum - minimum)
difference = ((exponent_product - lower_product)
              * ((exponent_sum - leading_cutoff) * (exponent_product + lower_product)
                 - minimum * (minimum - 1) * (exponent_sum + 2 * minimum - 1)))
assert sympy.expand(endpoint - endpoint.subs(exponent_product, lower_product) - difference) == 0
assert sympy.expand(middle * maximum - minimum * (middle + maximum - minimum)
                    - (middle - minimum) * (maximum - minimum)) == 0
assert sympy.expand(cutoff - leading_cutoff + 2 * minimum ** 2) == 0
boundary_polynomial = (minimum ** 3 - 2 * minimum ** 2 * maximum ** 2
                       + minimum ** 2 * maximum + minimum ** 2 + 3 * minimum * maximum
                       - 3 * minimum + maximum ** 2 - 2 * maximum + 1)
boundary_factor = ((minimum - 1) * (2 * minimum - 1) - maximum) * boundary_polynomial
assert sympy.expand(endpoint.subs({exponent_sum: minimum + maximum,
                                  exponent_product: minimum * maximum}) - boundary_factor) == 0
positive_coefficients = [
    2 * minimum ** 2 - 1,
    (minimum - 2) * (4 * minimum ** 2 + 7 * minimum + 9) + 20,
    (minimum - 2) * (2 * minimum ** 3 + 2 * minimum ** 2 - minimum + 3) + 5,
]
positive_polynomial = sum(coefficient * offset ** degree
                          for degree, coefficient in zip((2, 1, 0), positive_coefficients))
assert sympy.expand(-boundary_polynomial.subs(maximum, minimum + offset) - positive_polynomial) == 0
assert sympy.expand(direct_endpoint.subs({middle: minimum,
                                        maximum: (minimum - 1) * (2 * minimum - 1)})) == 0
assert sympy.expand((minimum - 1) * (2 * minimum - 1) - minimum
                    - (2 * (minimum - 1) ** 2 - 1)) == 0
assert direct_endpoint.subs({minimum: 2, middle: 2, maximum: 3}) == 0
assert direct_endpoint.subs({minimum: 3, middle: 3, maximum: 10}) == 0

print(json.dumps({
    "statement": "For real2<=a<=b<=c, h_C(1)=0 implies b+c>=2a^2-2a+1; equality iff b=a,c=(a-1)(2a-1)",
    "generic_determinant_identity": "passed, direct6x6 set-disjointness quotient",
    "product_lower_bound_identity": "passed",
    "quadratic_monotonicity_difference": "passed",
    "boundary_factorization": "passed",
    "negative_boundary_polynomial_at_t_a_plus_u": [str(value) for value in positive_coefficients],
    "coefficient_positivity": "Written proof: a>=2 makes a-2>=0,2a^2-1>0; all other displayed factors strictly positive",
    "equality_identity": "passed generically; admissibility c>=a follows from2(a-1)^2-1>0",
    "lower_minimum_equality_controls": [[2, 2, 3], [3, 3, 10]],
    "residual_spectrum_scope": "Unchanged a>=4 hypothesis; not extended to a>=2",
    "sympy": sympy.__version__,
    "finite_exponent_scan": False,
    "lean_run": False,
    "scope": "Exact generic identities supporting a written real-domain strengthening; shared independent set-quotient constructor, no original characteristic-polynomial helper",
    "status": "passed",
}, indent=2))
