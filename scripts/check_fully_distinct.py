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
        symbols, Matrix, Poly, factor_list, nroots, GF, Integer
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
            B[i][j] = d[i] if i == j else -N[i][j]

    return Matrix(B)


def analyze(k1, k2, k3):
    B = quotient_matrix(k1, k2, k3)
    char = B.charpoly(x).as_expr()
    # Factor out x
    g = char / x
    g_poly = Poly(g, x, domain='ZZ')
    factors, _ = factor_list(g_poly, x)
    degrees = []
    has_irr = False
    for f, mult in factors:
        try:
            deg = int(f.degree())
        except Exception:
            deg = 1
        degrees.append(deg)
        if deg >= 2:
            has_irr = True
    # Numerical roots
    roots = nroots(g, n=20)
    real_nonint = []
    for r in roots:
        rc = complex(r)
        if abs(rc.imag) < 1e-12:
            val = rc.real
            if abs(val - round(val)) > 1e-10:
                real_nonint.append(val)
    return {
        'k': (k1, k2, k3),
        'g': g_poly,
        'factor_degrees': degrees,
        'has_irreducible_factor': has_irr,
        'noninteger_roots': real_nonint,
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
          f"{'noninteger?':>12} | {'smallest nonint':>18}")
    print("-" * 90)

    results = []
    for (k1, k2, k3) in triples:
        r = analyze(k1, k2, k3)
        deg_str = ",".join(str(d) for d in r['factor_degrees'])
        nonint = "yes" if r['noninteger_roots'] else "no"
        smallest = f"{r['noninteger_roots'][0]:.6f}" if r['noninteger_roots'] else "-"
        print(f"{k1:>3} {k2:>3} {k3:>3} | {deg_str:>20} | "
              f"{nonint:>12} | {smallest:>18}")
        results.append(r)

    # Summary
    print()
    print("=" * 90)
    print("Summary")
    print("=" * 90)
    n_total = len(results)
    n_nonint = sum(1 for r in results if r['noninteger_roots'])
    print(f"Total triples: {n_total}")
    print(f"With noninteger root: {n_nonint}")
    print()
    print("If all triples have a noninteger root, this suggests the")
    print("fully-distinct case can be attacked uniformly. If some have")
    print("only integer roots, the problem is genuinely case-by-case.")

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
