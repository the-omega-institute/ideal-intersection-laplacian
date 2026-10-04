import hashlib
import json
from pathlib import Path

import sympy

from check_six_support_quotient import support_quotient


step, excess = sympy.symbols('d e', integer=True, nonnegative=True)
families = [
    ((9 + step, 9 + 2 * step, 136 + 4 * step), 1,
     (-9 * step ** 2 - 415 * step - 1384,
      4 * step ** 2 + 66 * step + 170,
      3 * step ** 2 - 56 * step - 939)),
    ((10 + step, 10 + 2 * step, 12 + 4 * step), 2,
     (-9 * step ** 2 - 42 * step,
      4 * step ** 2 + 74 * step + 368,
      3 * step ** 2 + 78 * step + 544)),
]
rows = []
for triple, endpoint, expected in families:
    minimum, middle, maximum = triple
    expressions = (
        (minimum - 2) * (sum(triple) - 2) - 2 * middle * maximum,
        4 * minimum ** 2 - 2 * minimum - maximum,
        (minimum + 2) * (7 * minimum - 16 - maximum) + 40,
    )
    assert all(sympy.expand(actual - target) == 0
               for actual, target in zip(expressions, expected))
    shifted_slack = sympy.Poly(expected[2].subs(step, 32 + excess), excess)
    assert all(coefficient > 0 for coefficient in shifted_slack.all_coeffs())
    base = tuple(int(exponent.subs(step, 0)) for exponent in triple)
    quotient = support_quotient(base, complement=True)
    characteristic_value = (endpoint * sympy.eye(6) - quotient).det()
    assert characteristic_value == 0
    gcd_bound = sympy.gcd(middle - 2 * minimum, maximum - 4 * minimum)
    assert gcd_bound == endpoint
    rows.append({
        'family': [str(exponent) for exponent in triple],
        'endpoint': endpoint,
        'seed': base,
        'seed_integer_characteristic_determinant': int(characteristic_value),
        'inertia_difference': str(expected[0]),
        'quadratic_tail_slack': str(expected[1]),
        'linear_bound_slack_times_minimum_plus_two': str(expected[2]),
        'linear_slack_at_d_equals_32_plus_e': str(shifted_slack.as_expr()),
        'gcd_bound_from_integer_linear_combinations': int(gcd_bound),
        'exponent_residues_modulo_eight': [int(exponent.subs(step, 0) % 8)
                                          for exponent in triple],
    })
sources = [Path(__file__), Path(__file__).with_name('check_six_support_quotient.py')]
print(json.dumps({
    'step_hypothesis': 'd>=32 and divisible by lcm(8, selected moduli)',
    'families': rows,
    'scope': 'Written finite-endpoint-congruence limitation with selected geometric, gcd and valuation filters. Six exact polynomial identities, two positive boundary shifts and two integer6x6determinants. No assertion of actual endpoint zeros, complete arithmetic survival or integral spectra. No exponent scan, floating-point spectrum or Lean.',
    'sympy': sympy.__version__,
    'source_sha256': {source.name: hashlib.sha256(source.read_bytes()).hexdigest()
                      for source in sources},
}, indent=2))
