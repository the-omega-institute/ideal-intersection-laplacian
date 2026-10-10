"""
Diophantine reduction for the open fully-distinct region.

For a fixed pair (a, b), we compute h_C(1) and h_C(2) as
polynomials in c, and find their integer roots c > b.

The bound B_max is inclusive in b. All integer c > b are found
exactly from the rational linear factors of each endpoint cubic;
there is no imposed bound on c. An empty list settles this finite
pair range, not the unbounded three-prime problem. Endpoint zeros
outside the remaining region may also be reported.

Uses only sympy. The quotient matrix is built symbolically in c
with a, b fixed integers.
"""

import sys

try:
    import sympy as sp
except ImportError:
    print("ERROR: sympy is required. pip install sympy")
    sys.exit(1)


c, x = sp.symbols('c x')


def quotient_matrix_H(a_val, b_val):
    """6x6 Laplacian quotient of H, symbolic in c."""
    cells = [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
    k = {1: sp.Integer(a_val), 2: sp.Integer(b_val), 3: c}

    sizes = []
    for S in cells:
        s = sp.Integer(1)
        for i in S:
            s *= k[i]
        sizes.append(s)

    n = len(cells)
    B = sp.zeros(n, n)
    for i, S in enumerate(cells):
        external = sp.Integer(0)
        for j, T in enumerate(cells):
            if j != i and set(S) & set(T):
                external += sizes[j]
                B[i, j] = -sizes[j]
        B[i, i] = external
    return B


def h_C_at_x(a_val, b_val, x_val):
    """
    Return h_C(x_val) as a polynomial in c for fixed a, b.

    We use the identity h_C(x) = -g_B(N - x), where
    g_B(y) = det(yI - B)/y and N = a+b+c+ab+ac+bc is |V(H)|.
    """
    B = quotient_matrix_H(a_val, b_val)
    char_expr = sp.expand(B.charpoly(x).as_expr())
    g_B = sp.cancel(char_expr / x)
    N = a_val + b_val + c + a_val * b_val + a_val * c + b_val * c
    val = -g_B.subs(x, N - x_val)
    return sp.expand(val)


def integer_roots_in_c(poly_in_c, c_min):
    """Return integer roots of poly_in_c that are >= c_min."""
    p = sp.Poly(poly_in_c, c, domain='ZZ')
    if p.degree() < 1:
        return []
    roots = p.ground_roots()
    result = []
    for root in roots:
        if root.is_Integer and int(root) >= c_min:
            result.append(int(root))
    return sorted(result)


def factor_check(a_val, b_val, c_val):
    """
    For a triple (a, b, c), factor h_C(x) over Z and report
    whether all roots are integers.
    """
    B = quotient_matrix_H(a_val, b_val).subs(c, c_val)
    char_expr = sp.expand(B.charpoly(x).as_expr())
    g_B = sp.cancel(char_expr / x)
    N = a_val + b_val + c_val + a_val * b_val + a_val * c_val + b_val * c_val
    # h_C(x) = -g_B(N - x)
    h_C_expr = sp.expand(-g_B.subs(x, N - x))
    h_C_poly = sp.Poly(h_C_expr, x, domain='ZZ')
    assert h_C_poly.degree() == 5 and h_C_poly.LC() == 1

    # Factor over Z
    factors = sp.factor_list(h_C_poly, x)
    all_linear = all(f.degree() <= 1 for f, m in factors[1])
    return h_C_poly, factors, all_linear


def main():
    B_max = 15

    print("=" * 70)
    print(f"Diophantine enumeration for h_C(1)=0 and h_C(2)=0")
    print(f"Range: 4 <= a < b <= {B_max}, c > b")
    print("=" * 70)

    candidates = []

    for x_val in [1, 2]:
        print(f"\n=== Surface h_C({x_val}) = 0 ===")
        total = 0
        for a_val in range(4, B_max):
            for b_val in range(a_val + 1, B_max + 1):
                poly = h_C_at_x(a_val, b_val, x_val)
                roots = integer_roots_in_c(poly, c_min=b_val + 1)
                for c_val in roots:
                    print(f"  (a, b, c) = ({a_val}, {b_val}, {c_val})")
                    candidates.append((a_val, b_val, c_val, x_val))
                    total += 1
        print(f"  Subtotal: {total} triples")

    print()
    print("=" * 70)
    print(f"Total candidate triples: {len(candidates)}")
    print("=" * 70)

    # For each candidate, factor h_C completely
    print()
    print("Full factorizations:")
    for (a_val, b_val, c_val, x_val) in candidates:
        h_C_poly, factors, all_linear = factor_check(a_val, b_val, c_val)
        print(f"\n(a,b,c) = ({a_val},{b_val},{c_val})  [endpoint {x_val}]")
        print(f"  h_C(x) = {h_C_poly.as_expr()}")
        print(f"  factors: {factors}")
        print(f"  all roots integer: {all_linear}")


if __name__ == "__main__":
    main()
