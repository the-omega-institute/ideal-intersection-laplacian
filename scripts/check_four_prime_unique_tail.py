import hashlib
import json
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator
from check_four_prime_single_pair_midpoint import integer_determinant


def symbolic_checks():
    first, tail, maximum, variable, offset, growth, left, right = sympy.symbols('a b c x t w u v')
    polynomial = sympy.Matrix(operator(first, tail, maximum)).charpoly(variable).as_expr()
    quadratic = sympy.Poly(polynomial.subs(variable, first + 1 + offset), maximum)
    leading = ((first + 1) ** 2 * (tail + 1) * offset ** 2
               + (first + 1) * (tail + 1) * (first ** 2 - (2 * first + 1) * tail) * offset
               - first ** 2 * tail ** 2 * (2 * first + 1))
    assert sympy.expand(quadratic.nth(2) - leading) == 0
    linear_per_offset = sympy.cancel(quadratic.nth(1) / offset)
    expansion = sympy.Poly(linear_per_offset.subs(offset, tail + left + 1)
                           .subs(tail, left + right + 2).subs(first, growth + 1).expand(), growth, left, right)
    assert len(expansion.terms()) == 34 and expansion.TC() == 13
    assert all(coefficient > 0 for coefficient in expansion.coeffs())
    derivative = (first + 1) * (tail + 1) * (first ** 2 + tail)
    assert sympy.expand(sympy.diff(leading, offset).subs(offset, tail) - derivative) == 0
    lower = -first * tail * (first + tail + 1) * (first * (tail - 1) + tail)
    assert sympy.expand(leading.subs(offset, tail) - lower) == 0
    upper = tail * (2 * first ** 3 + first ** 2 * tail + 2 * first ** 2
                    + 2 * first * tail ** 2 + 2 * first * tail + 2 * tail ** 2 + 2 * tail)
    assert sympy.expand(leading.subs(offset, 2 * tail) - upper) == 0
    width = (first + 1) * tail
    constant = offset * (width - offset) * (offset * (width - offset) + first * offset + first ** 2 * tail)
    assert sympy.expand(quadratic.nth(0) - constant) == 0
    return {'leading_coefficient': str(leading), 'linear_coefficient_divided_by_t': str(linear_per_offset),
            'positive_linear_expansion': {'substitution': 'a=1+w,b=2+u+v,t=b+1+u',
                'terms_w_power_u_power_v_power_coefficient': [list(monomial) + [int(coefficient)] for monomial, coefficient in expansion.terms()],
                'positive_terms': 34, 'constant': 13},
            'leading_derivative_at_t_equals_b': str(derivative),
            'leading_at_t_equals_b': str(lower), 'leading_at_t_equals_2b': str(upper),
            'positive_constant': str(constant),
            'criterion': 'A_t>=0:no positive tail roots; A_t<0:exactly one positive real tail root.',
            'candidate_count': 'at most b-1 positive integer tails for each fixed(a,b),ordered b<c',
            'remaining_offset_domain': 'b<t<tau(a,b)<2b,where tau is the unique positive zero of A_t'}


def fixed_control(first, tail, offset):
    assert tail + 1 <= offset <= 2 * tail - 1
    maximum, variable = sympy.symbols('c x')
    polynomial = sympy.Matrix(operator(first, tail, maximum)).charpoly(variable).as_expr()
    quadratic = sympy.Poly(polynomial.subs(variable, first + 1 + offset), maximum)
    coefficients = [int(quadratic.nth(degree)) for degree in (2, 1, 0)]
    values = []
    for tail_value in (0, 1, 2, 3):
        matrix = operator(first, tail, tail_value)
        anchor = first + 1 + offset
        values.append(integer_determinant([[anchor * (row == column) - matrix[row][column]
                                            for column in range(4)] for row in range(4)]))
    difference = values[2] - 2 * values[1] + values[0]
    assert difference % 2 == 0
    direct_leading = difference // 2
    assert coefficients == [direct_leading, values[1] - values[0] - direct_leading, values[0]]
    assert quadratic.eval(3) == values[3]
    leading, linear, constant = coefficients
    assert linear > 0 and constant > 0
    positive_roots = int(quadratic.count_roots(0, sympy.oo))
    negative_roots = int(quadratic.count_roots(-sympy.oo, 0))
    assert positive_roots == (1 if leading < 0 else 0)
    if leading < 0:
        assert negative_roots == 1
    return {'a': first, 'b': tail, 't': offset,
            'quadratic_coefficients_descending': coefficients,
            'four_direct_integer_determinants_at_c_0_1_2_3': values,
            'exact_positive_real_tail_roots': positive_roots, 'exact_negative_real_tail_roots': negative_roots}


def main():
    directory = Path(__file__).parent
    helpers = ['check_four_prime_pair_three.py', 'check_four_prime_single_pair_midpoint.py']
    report = {'written_theorem': 'For positive(a,a,b,c),ordered b<c,any integral graph has t in[b+1,2b-1],A_t<0. Every remaining quadratic has positive linear and constant coefficients and exactly one positive real tail root. At most b-1 possible integral tails per fixed(a,b),with a contiguous smaller offset domain determined by A_t<0.',
              'symbolic': symbolic_checks(),
              'fixed_controls': [fixed_control(1, 2, 3), fixed_control(5, 5, 6), fixed_control(5, 5, 8),
                                 fixed_control(5, 5, 9), fixed_control(5, 11, 12), fixed_control(30, 5, 6)],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256': {name: hashlib.sha256((directory / name).read_bytes()).hexdigest() for name in helpers},
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded positivity and unique-positive-tail-root proof. Six fixed quadratic controls,24independent integer determinants and12exact Sturm counts. c=0solely algebraic interpolation. Prior graph embedding/root-window proofs retained; no exponent/tail scan,expanded graph,historical finite-base rerun or Lean. General classification remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
