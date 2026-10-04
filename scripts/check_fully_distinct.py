"""
Diagnostic for the fully-distinct exponent vector (k1, k2, k3).

For n = p1^k1 p2^k2 p3^k3 with k1, k2, k3 pairwise distinct, the
equitable partition has 6 cells indexed by the nonempty proper subsets
of {1, 2, 3}. The quotient matrix B is 6x6, and its characteristic
polynomial is x * g(x) with g of degree 5.

This script:
  1. Builds B for given (k1, k2, k3).
  2. Computes g(x) = det(xI - B) / x.
  3. Factors g over Z.
  4. For a range of triples, reports whether g has a noninteger root.

Diagnostic, not proof. Requires sympy.
"""

import sys
from itertools import combinations

try:
    from sympy import (
        symbols, Matrix, Poly, factor_list, cancel, Rational, floor
    )
except ImportError:
    print("ERROR: sympy is required. pip install sympy")
    sys.exit(1)


x = symbols('x')


def quotient_matrix(k1, k2, k3):
    """Return the 6x6 quotient matrix B for (k1, k2, k3)."""
    k = {1: k1, 2: k2, 3: k3}

    # Cell sizes for supports
    m = {
        (1,): k1, (2,): k2, (3,): k3,
        (1, 2): k1 * k2, (1, 3): k1 * k3, (2, 3): k2 * k3
    }

    # Cells in order
    cells = [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
    idx = {c: i for i, c in enumerate(cells)}

    n = len(cells)
    N = [[0] * n for _ in range(n)]  # neighbor counts

    for i, S in enumerate(cells):
        for j, T in enumerate(cells):
            if i == j:
                N[i][j] = m[S] - 1  # internal
            elif set(S) & set(T):
                N[i][j] = m[T]  # complete join
            # else 0

    # Degrees
    d = [sum(row) for row in N]

    # Quotient matrix B = diag(d) - N
    B = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            B[i][j] = d[i] - N[i][i] if i == j else -N[i][j]

    return Matrix(B)


def analyze(k1, k2, k3):
    B = quotient_matrix(k1, k2, k3)
    char = B.charpoly(x).as_expr()
    # Factor out x
    g = cancel(char / x)
    g_poly = Poly(g, x, domain='ZZ')
    _, factors = factor_list(g_poly)
    degrees = []
    has_irr = False
    for f, mult in factors:
        deg = int(f.degree())
        degrees.append(deg)
        if deg >= 2:
            has_irr = True
    noninteger_intervals = []
    for bounds, multiplicity in g_poly.intervals(eps=Rational(1, 1000)):
        lower, upper = bounds
        if lower == upper:
            continue
        while floor(lower) != floor(upper) or lower <= floor(lower):
            lower, upper = g_poly.refine_root(lower, upper, eps=(upper - lower) / 10)
        noninteger_intervals.append((lower, upper))
    return {
        'k': (k1, k2, k3),
        'g': g_poly,
        'factor_degrees': degrees,
        'has_irreducible_factor': has_irr,
        'noninteger_intervals': noninteger_intervals,
    }


def main():
    print("=" * 90)
    print("Fully-distinct (k1, k2, k3): diagnostic")
    print("=" * 90)
    print()

    # Small triples
    triples = []
    for k1 in range(1, 6):
        for k2 in range(k1 + 1, 7):
            for k3 in range(k2 + 1, 8):
                triples.append((k1, k2, k3))

    print(f"{'k1':>3} {'k2':>3} {'k3':>3} | {'factor degrees':>20} | "
          f"{'noninteger?':>12} | {'first root interval':>20}")
    print("-" * 90)

    results = []
    for (k1, k2, k3) in triples:
        r = analyze(k1, k2, k3)
        deg_str = ",".join(str(d) for d in r['factor_degrees'])
        nonint = "yes" if r['has_irreducible_factor'] else "no"
        if r['noninteger_intervals']:
            lower, upper = r['noninteger_intervals'][0]
            smallest = f"({floor(lower)},{floor(lower) + 1})"
        else:
            smallest = "-"
        print(f"{k1:>3} {k2:>3} {k3:>3} | {deg_str:>20} | "
              f"{nonint:>12} | {smallest:>20}")
        results.append(r)

    # Summary
    print()
    print("=" * 90)
    print("Summary")
    print("=" * 90)
    n_total = len(results)
    n_nonint = sum(1 for r in results if r['has_irreducible_factor'])
    print(f"Total triples: {n_total}")
    print(f"With noninteger root: {n_nonint}")
    print()
    print("All intervals are exact certificates between consecutive integers.")
    print("This finite range is not an all-parameter integrality proof.")
    print("An integer quotient spectrum would require checking the remaining graph modes.")

    # Show the smallest example's polynomial
    if results:
        r = results[0]
        print()
        print("=" * 90)
        print(f"Example: (k1, k2, k3) = {r['k']}")
        print("=" * 90)
        print(f"g(x) = {r['g'].as_expr()}")
        print(f"factor degrees: {r['factor_degrees']}")


if __name__ == "__main__":
    main()
