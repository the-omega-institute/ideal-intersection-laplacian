"""
Diagnostic for the still-open region 4 <= a < b < c < 4a^2 - 2a.

For n = p1^a p2^b p3^c with a < b < c, we build the Laplacian
quotient matrix B of the graph H obtained by removing universal
vertices from the ideal intersection graph. The cells are indexed
by the nonempty proper subsets of {1,2,3}, and B is 6x6 with
row sums zero. Its characteristic polynomial is x*h(x) with h of
degree 5.

For each (a, b, c) in the region, we check whether h has a
noninteger root. Since h is monic with integer coefficients,
every rational root is an integer; hence h has no noninteger
root iff h factors into five linear factors over Z.

This script is a DIAGNOSTIC, not a proof. It requires sympy.
"""

import sys
from math import isqrt

try:
    from sympy import symbols, Matrix, Poly, Integer, divisors
except ImportError:
    print("ERROR: sympy is required. pip install sympy")
    sys.exit(1)


x = symbols('x')


def quotient_matrix(a, b, c):
    """
    Return the 6x6 Laplacian quotient matrix B for H.

    Cells are (1,), (2,), (3,), (1,2), (1,3), (2,3) in this order,
    with sizes a, b, c, ab, ac, bc respectively. Two cells are
    adjacent in the quotient iff their supports intersect. For a
    cell-constant vector, internal neighbors cancel in the Laplacian
    action, so the diagonal of B is exactly the number of external
    neighbors of any vertex in the cell.
    """
    k = {1: a, 2: b, 3: c}
    cells = [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
    n = len(cells)

    # Cell sizes
    sizes = []
    for S in cells:
        s = 1
        for i in S:
            s *= k[i]
        sizes.append(s)

    # Build B
    B = [[0] * n for _ in range(n)]
    for i, S in enumerate(cells):
        external = 0
        for j, T in enumerate(cells):
            if j != i and set(S) & set(T):
                external += sizes[j]
        B[i][i] = external
        for j, T in enumerate(cells):
            if j != i and set(S) & set(T):
                B[i][j] = -sizes[j]

    return Matrix(B)


def quintic(B):
    """Return h(x) = charpoly(B) / x as a Poly over Z."""
    char_expr = B.charpoly(x).as_expr()
    return Poly(char_expr / x, x, domain='ZZ')


def has_noninteger_root(h):
    """
    Return True iff h has a noninteger root.

    h is monic with integer coefficients, so every rational root is
    an integer. Thus h has a noninteger root iff h does NOT factor
    into five linear factors over Z.

    Fast pre-filter: if the discriminant is a nonzero non-square,
    the answer is immediately True.
    """
    disc = h.discriminant()
    if disc != 0:
        disc_sq = Integer(disc).is_square
        if disc_sq is False:
            return True

    remaining = Poly(h, x, domain='ZZ')
    while remaining.degree() > 0:
        const = int(remaining.all_coeffs()[-1])
        if const == 0:
            remaining = Poly(remaining.as_expr() / x, x, domain='ZZ')
            continue
        found = False
        for d in divisors(abs(const)):
            for sign in (1, -1):
                r = sign * int(d)
                if remaining.eval(r) == 0:
                    remaining = Poly(remaining.as_expr() / (x - r),
                                     x, domain='ZZ')
                    found = True
                    break
            if found:
                break
        if not found:
            return True
    return False


def sign_char(v):
    if v > 0: return '+'
    if v < 0: return '-'
    return '0'


def main():
    a_max = 7  # increase carefully: cost grows roughly like a^4

    print("=" * 80)
    print("Open region 4 <= a < b < c < 4a^2 - 2a")
    print("=" * 80)

    for a in range(4, a_max + 1):
        c_max = 4 * a * a - 2 * a
        n_pairs = 0
        n_nonint = 0
        patterns = {}
        for b in range(a + 1, c_max - 1):
            for c in range(b + 1, c_max):
                B = quotient_matrix(a, b, c)
                h = quintic(B)
                n_pairs += 1
                if has_noninteger_root(h):
                    n_nonint += 1
                key = (sign_char(h.eval(1)),
                       sign_char(h.eval(2)),
                       sign_char(h.eval(3)))
                patterns[key] = patterns.get(key, 0) + 1

        print(f"\na = {a}, c_max = {c_max}, pairs = {n_pairs}, "
              f"with noninteger root = {n_nonint}")

        # Print sign patterns of (h(1), h(2), h(3))
        for key, count in sorted(patterns.items(),
                                 key=lambda kv: -kv[1]):
            print(f"  (h(1), h(2), h(3)) = {key}: {count}")


if __name__ == "__main__":
    main()
