import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


second, third, variable, first_offset, gap_offset = sympy.symbols('b c x u v')
quotient = support_quotient((2, second, third), complement=True)
quintic = sympy.Poly(sympy.cancel(quotient.charpoly(variable).as_expr() / variable), variable)
total = 2 + 3 * second + 3 * third + second * third
assert sympy.expand(quintic.eval(0) + 2 * second * third * (second + third + 2) * total) == 0
sum_parameter = second + third
product_parameter = second * third
endpoint = ((sum_parameter - 13) * product_parameter ** 2
            - (2 * sum_parameter + 6) * product_parameter
            + 3 * sum_parameter ** 3 + sum_parameter ** 2 - 3 * sum_parameter - 1)
assert sympy.expand(quintic.eval(1) - endpoint) == 0

first_region = 12 * gap_offset ** 3 + 112 * gap_offset ** 2 + 268 * gap_offset + 120
assert sympy.expand(endpoint.subs({second: 3, third: gap_offset + 5}) - first_region) == 0
second_region = ((first_offset ** 2 + 8 * first_offset + 19) * gap_offset ** 3
                 + (4 * first_offset ** 3 + 38 * first_offset ** 2 + 128 * first_offset + 170)
                 * gap_offset ** 2
                 + (5 * first_offset ** 4 + 62 * first_offset ** 3 + 271 * first_offset ** 2
                    + 502 * first_offset + 368) * gap_offset
                 + 2 * first_offset ** 5 + 32 * first_offset ** 4 + 190 * first_offset ** 3
                 + 504 * first_offset ** 2 + 552 * first_offset + 160)
assert sympy.expand(endpoint.subs({second: first_offset + 4, third: first_offset + gap_offset + 5})
                    - second_region) == 0
first_coefficients = [int(value) for value in sympy.Poly(first_region, gap_offset).all_coeffs()]
second_coefficients = [int(value) for value in sympy.Poly(second_region, first_offset, gap_offset).coeffs()]
assert all(value > 0 for value in first_coefficients + second_coefficients)

exception = sympy.Poly(quintic.as_expr().subs({second: 3, third: 4}), variable)
expected_coefficients = [1, -53, 953, -6523, 13134, -7560]
assert [int(value) for value in exception.all_coeffs()] == expected_coefficients
endpoint_records = []
for argument, expected in [(sympy.Integer(1), sympy.Integer(-48)),
                           (sympy.Rational(3, 2), sympy.Rational(13437, 32))]:
    value = sympy.Integer(0)
    for coefficient in expected_coefficients:
        value = value * argument + coefficient
    assert value == expected == exception.eval(argument)
    endpoint_records.append({'argument': str(argument), 'value': str(value), 'independent_horner': 'passed'})
assert exception.count_roots(1, sympy.Rational(3, 2)) == 1

source_paths = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({'symbolic_identities': 'passed',
                  'complement_endpoint_at_0': str(sympy.factor(quintic.eval(0))),
                  'complement_endpoint_at_1': str(sympy.expand(endpoint)),
                  'positive_region_b3_c_at_least5': str(first_region),
                  'positive_region_b_at_least4_c_above_b': str(second_region),
                  'all_nonzero_coefficients_positive': True,
                  'region_one_coefficients': first_coefficients,
                  'region_two_coefficients': second_coefficients,
                  'exception': {'exponents': [2, 3, 4], 'quintic': str(exception.as_expr()),
                                'endpoints': endpoint_records, 'sturm_count_between_endpoints': 1,
                                'graph_vertex_count': 58, 'graph_eigenvalue_interval': ['113/2', '57']},
                  'sympy': sympy.__version__,
                  'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                                    for source in source_paths},
                  'scope': 'General a2 complement endpoint identities and two positive-coefficient infinite-region expansions; one (2,3,4) quintic/rational-endpoint/Horner/Sturm certificate. No parameter scan or Lean. Together with prior repeated/unit proofs, every triple with minimum exponent<=2 is settled. Fullydistinct all>=3 and fullQ3 remain open.'}, indent=2))
