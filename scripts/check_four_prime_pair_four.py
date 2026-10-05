import hashlib
import json
from math import isqrt
from pathlib import Path

import sympy

from check_four_prime_pair_three import operator, support_embedding


def symbolic_check():
    middle, maximum, variable = sympy.symbols('b c x')
    matrix = sympy.Matrix(operator(4, middle, maximum))
    diagonal = lambda entry: sympy.diag(entry + 1, 1)
    disjoint = lambda entry: sympy.Matrix([[1, entry], [1, 0]])
    tensor = (5 * sympy.kronecker_product(diagonal(middle), diagonal(maximum))
              + 4 * sympy.kronecker_product(disjoint(middle), disjoint(maximum)))
    assert all(sympy.expand(entry) == 0 for entry in matrix - tensor)
    second = (-9 * middle ** 2 * maximum ** 2 + 120 * middle ** 2 * maximum - 15 * middle ** 2
              + 120 * middle * maximum ** 2 + 1014 * middle * maximum + 306 * middle
              - 15 * maximum ** 2 + 306 * maximum + 189)
    third = (-54 * middle ** 2 * maximum ** 2 + 30 * middle ** 2 * maximum - 60 * middle ** 2
             + 30 * middle * maximum ** 2 + 540 * middle * maximum + 96 * middle
             - 60 * maximum ** 2 + 96 * maximum + 48)
    assert sympy.expand((matrix - 2 * sympy.eye(4)).det() - second) == 0
    assert sympy.expand((matrix - 3 * sympy.eye(4)).det() - third) == 0
    upper_minor = (matrix - 4 * sympy.eye(4)).extract([0, 3], [0, 3]).det()
    assert sympy.expand(upper_minor - (-11 * middle * maximum + 5 * middle + 5 * maximum + 5)) == 0
    assert sympy.expand(upper_minor.subs({middle: middle + 2, maximum: maximum + 2})
                        + 11 * middle * maximum + 17 * middle + 17 * maximum + 19) == 0
    boundary = matrix.subs({middle: 2, maximum: 2}) - 3 * sympy.eye(4)
    minors = [int(boundary[:size, :size].det()) for size in range(1, 5)]
    assert minors == [46, 520, 3424, 1728]
    expected_tails = {32: [9, 456, 5391, 456, 20490, 189390, 5391, 189390, 545475],
                      4: [54, 402, 804, 402, 2436, 3696, 804, 3696, 2448]}
    tails = {}
    for polynomial, shift in [(second, 32), (third, 4)]:
        shifted = sympy.Poly(sympy.expand(-polynomial.subs({middle: middle + shift, maximum: maximum + shift})), middle, maximum)
        assert shifted.coeffs() == expected_tails[shift]
        assert all(coefficient > 0 for coefficient in shifted.coeffs())
        tails[str(shift)] = [list(monomial) + [int(coefficient)] for monomial, coefficient in shifted.terms()]
    leading = -9 * middle ** 2 + 120 * middle - 15
    linear = 120 * middle ** 2 + 1014 * middle + 306
    constant = -15 * middle ** 2 + 306 * middle + 189
    assert sympy.expand(second - (leading * maximum ** 2 + linear * maximum + constant)) == 0
    assert [int(expression.subs(middle, value)) for expression in (leading, constant)
            for value in (2, 13)] == [189, 24, 741, 1632]
    assert sympy.diff(leading, middle, 2) < 0
    assert sympy.diff(constant, middle, 2) < 0
    discriminants = {14: (1446279552, 38029), 15: (1808958096, 42531), 16: (2234549520, 47271),
                     17: (2729779200, 52247), 18: (3301705152, 57460), 19: (3957718032, 62910),
                     20: (4705541136, 68596), 22: (6509174400, 80679), 23: (7582094352, 87075),
                     24: (8781044112, 93707), 25: (10115410176, 100575), 26: (11594911680, 107679),
                     28: (15029860752, 122596), 29: (17006409792, 130408),
                     30: (19170297216, 138456), 31: (21532905360, 146740)}
    rows = []
    for value in range(2, 32):
        coefficients = [int(expression.subs(middle, value)) for expression in (leading, linear, constant)]
        polynomial = sympy.Poly(second.subs(middle, value), maximum)
        assert polynomial.all_coeffs() == coefficients
        row = {'b': value, 'coefficients': coefficients}
        if value <= 13:
            assert all(coefficient > 0 for coefficient in coefficients)
            row['obstruction'] = 'positive coefficients, also certified by concavity'
        elif value in (21, 27):
            factorization = (-24 * maximum * (61 * maximum - 3105) if value == 21
                             else -12 * (2 * maximum - 69) * (139 * maximum - 3))
            assert sympy.expand(polynomial.as_expr() - factorization) == 0
            roots = ([sympy.Rational(3105, 61)] if value == 21
                     else [sympy.Rational(69, 2), sympy.Rational(3, 139)])
            assert all(root.q != 1 and polynomial.eval(root) == 0 for root in roots)
            row.update(obstruction='rational noninteger positive roots', positive_roots=list(map(str, roots)))
        else:
            discriminant = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
            anchor = isqrt(discriminant)
            assert (discriminant, anchor) == discriminants[value]
            assert anchor ** 2 < discriminant < (anchor + 1) ** 2
            assert int(sympy.discriminant(polynomial.as_expr(), maximum)) == discriminant
            row.update(obstruction='nonsquare discriminant', discriminant=discriminant, square_anchor=anchor)
        rows.append(row)
    assert sum(row['obstruction'] == 'nonsquare discriminant' for row in rows) == 16
    third_rows = {2: -216 * maximum * (maximum - 6),
                  3: -6 * (4 * maximum - 17) * (19 * maximum - 2)}
    for value, factorization in third_rows.items():
        assert sympy.expand(third.subs(middle, value) - factorization) == 0
    assert sympy.Poly(third_rows[2], maximum).eval(6) == 0
    for root in [sympy.Rational(17, 4), sympy.Rational(2, 19)]:
        assert root.q != 1 and sympy.Poly(third_rows[3], maximum).eval(root) == 0
    cubic = variable ** 3 - 161 * variable ** 2 + 5775 * variable - 35343
    exceptional = matrix.subs({middle: 2, maximum: 6})
    assert sympy.expand((variable * sympy.eye(4) - exceptional).det() - (variable - 3) * cubic) == 0
    signs = [int(cubic.subs(variable, endpoint)) for endpoint in (7, 8)]
    assert signs == [-2464, 1065]
    return {'tensor_identity': 'passed', 'generic_second_endpoint': str(second), 'generic_third_endpoint': str(third),
            'upper_bound_principal_minor': str(sympy.expand(upper_minor)),
            'b_c_two_third_endpoint_leading_minors': minors, 'complete_positive_tails': tails,
            'all_thirty_second_endpoint_rows': rows, 'third_endpoint_rows': {str(value): str(polynomial) for value, polynomial in third_rows.items()},
            'second_endpoint_integer_pairs': [], 'sole_unordered_third_endpoint_pair': [2, 6],
            'exceptional_cubic': str(cubic), 'exceptional_cubic_at_seven_eight': signs}


def main():
    controls = [(2, 2), (2, 6), (3, 5), (13, 32), (14, 100), (21, 51), (27, 35), (32, 32), (19, 100)]
    report = {'written_theorem': 'Every positive four-prime exponent vector with at least two entries equal to four is Laplacian nonintegral.',
              'symbolic': symbolic_check(),
              'specified_support_controls': [support_embedding(4, *control) for control in controls],
              'independent_expanded_graph_controls': [support_embedding(4, *control, expand=True) for control in [(2, 2), (2, 3)]],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'embedding_dependency_sha256': hashlib.sha256(Path(__file__).with_name('check_four_prime_pair_three.py').read_bytes()).hexdigest(),
              'sympy_version': sympy.__version__,
              'scope': 'Written unbounded invariant-space proof, thirty symbolic endpoint-two rows and two endpoint-three rows, sixteen nonsquare discriminants, four rational factorizations and two cubic signs. Nine specified support controls and two expanded graphs validate implementation. No exponent rectangle scan, modular search, floating eigenvalues, Lean or historical three-prime certificate rerun. Main manuscript scope unchanged; higher-prime nonsquarefree Q3 remains open.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
