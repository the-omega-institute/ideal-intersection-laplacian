import json
from pathlib import Path

import sympy

from verify_minimum_three import complement_quotient


ROOT = Path(__file__).resolve().parents[1]


def main():
    minimum = sympy.Symbol('a', positive=True)
    span, offset = sympy.symbols('r d', nonnegative=True)
    variable = sympy.Symbol('x')
    middle, maximum = minimum + offset, minimum + span
    criterion = (minimum - 2) * (minimum + middle + maximum - 2) - 2 * middle * maximum
    worst = minimum ** 2 - 2 * minimum * span - 8 * minimum - 2 * span ** 2 - 4 * span + 4
    threshold = span + 4 + sympy.sqrt(3) * (span + 2)
    other_zero = span + 4 - sympy.sqrt(3) * (span + 2)
    assert sympy.expand(criterion - worst - (span - offset) * (minimum + 2 * span + 2)) == 0
    assert sympy.expand(worst - (minimum - threshold) * (minimum - other_zero)) == 0
    assert sympy.simplify(worst.subs(minimum, threshold)) == 0
    assert sympy.simplify(3 * span + 8 - threshold - (2 - sympy.sqrt(3)) * (span + 2)) == 0
    assert sympy.simplify(2 - other_zero - (sympy.sqrt(3) - 1) * span - 2 * (sympy.sqrt(3) - 1)) == 0
    controls = []
    for exponents in ((35, 45, 45), (281, 381, 381)):
        first, second, third = exponents
        span_value = third - first
        lower = (first - 2) * (sum(exponents) - 2) - 2 * second * third
        assert lower > 0 and first < 3 * span_value + 8
        matrix = sympy.Matrix(complement_quotient(exponents))
        determinant = sympy.expand((variable * sympy.eye(6) - matrix).det())
        quotient, remainder = sympy.div(determinant, variable, variable)
        assert remainder == 0
        polynomial = sympy.Poly(quotient, variable)
        assert all(polynomial.eval(endpoint) != 0 for endpoint in (0, 2, 3))
        counts = [sum(multiplicity * factor.count_roots(left, right)
                      for factor, multiplicity in polynomial.sqf_list()[1])
                  for left, right in ((0, 2), (2, 3))]
        assert counts[0] == 0 and counts[1] >= 1
        controls.append({'exponents': list(exponents), 'span': span_value,
                         'criterion_value': lower, 'former_minimum_bound': 3 * span_value + 8,
                         'positive_roots_below_two': int(counts[0]),
                         'positive_roots_between_two_and_three': int(counts[1]),
                         'quintic': str(sympy.factor(quotient))})
    assert sympy.expand(criterion.subs({minimum: 34, offset: 10, span: 10})) == -32
    source = (ROOT / 'paper/sections/mixed-inertia.tex').read_text()
    assert r'a>\rho+4+\sqrt3(\rho+2)' in source
    print(json.dumps({'statement': 'a>r+4+sqrt(3)(r+2),r=c-a, guarantees a complement quotient root in(2,3) and integer-exponent graph nonintegrality',
        'generic_worst_middle_identity': 'passed', 'generic_factorization': 'passed',
        'exact_boundary': 'Delta=0 at a=r+4+sqrt(3)(r+2),b=c=a+r',
        'strict_criterion_span_threshold': 'exact for a>=4; not claimed necessary for a root in(2,3)',
        'old_bound_comparison': '(3r+8)-[r+4+sqrt(3)(r+2)]=(2-sqrt(3))(r+2)>0',
        'fixed_direct_quotient_controls': controls,
        'below_threshold_criterion_control': {'exponents': [34, 44, 44], 'criterion_value': -32,
            'scope': 'criterion sign only; no spectral failure or integrality claim'},
        'supporting_manuscript_statement': 'passed', 'sympy': sympy.__version__,
        'scope': 'Written exact worst-middle/factorization proof strengthens supporting span corollary. Shared set-disjointness support constructor/SymPy, no original characteristic helper. Two fixed direct quotient controls count exact roots with multiplicities; endpoints2/3 absent. No parameter scan,new finite base,historical finite-base rerun,floats or Lean. Selected main classification manuscript and historical integer classification inputs retained.',
        'status': 'passed'}, indent=2))


if __name__ == '__main__':
    main()
