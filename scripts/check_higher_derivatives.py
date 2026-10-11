"""
Higher-derivative 2-adic diagnostic for mixed-parity triples.

For each canonical mixed-parity representative (a, b, c) in 0..7,
this script computes exact values and the first few derivatives of h_C
at x = 1 and reports their 2-adic valuations. These full valuations
are not generally constant on a residue class. Zero has valuation infinity.

The idea is to extend the argument of Theorem 13.6 / 13.8: if
h_C has all integer roots in a mixed-parity triple, then the
values h_C(1), h_C'(1), h_C''(1), h_C'''(1) must satisfy certain
2-adic divisibility conditions derived from the distribution of
the three odd roots. If, on some surviving class, one of these
conditions fails, that class is excluded.

Uses the reflection h_C(x) = -g_B(N - x), where
g_B(y) = det(y I - B) / y and N = |V(H)| = a + b + c + ab + ac + bc.

Requires sympy.
"""

import sys
from collections import Counter

try:
    import sympy as sp
except ImportError:
    print("ERROR: sympy is required. pip install sympy")
    sys.exit(1)


a, b, c, x, y = sp.symbols('a b c x y')


def build_B_and_N():
    """Return (B, N): quotient matrix and |V(H)|."""
    cells = [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]
    k = {1: a, 2: b, 3: c}

    sizes = []
    for S in cells:
        s = sp.Integer(1)
        for i in S:
            s = s * k[i]
        sizes.append(s)

    n = len(cells)
    B = sp.zeros(n, n)
    for i, S in enumerate(cells):
        external = sp.Integer(0)
        for j, T in enumerate(cells):
            if j != i and set(S) & set(T):
                external = external + sizes[j]
                B[i, j] = -sizes[j]
        B[i, i] = external

    N = sum(sizes)
    return B, N


def build_h_C_derivatives(order=3):
    """
    Return a list [h_C^(0), h_C^(1), ..., h_C^(order)] as
    expressions in (a, b, c, x).
    """
    B, N = build_B_and_N()
    char_y = sp.expand(B.charpoly(y).as_expr())
    g_B = sp.expand(char_y / y)   # degree 5 in y
    h_C = sp.expand(-g_B.subs(y, N - x))
    derivs = [h_C]
    for _ in range(order):
        derivs.append(sp.expand(sp.diff(derivs[-1], x)))
    return derivs


def is_mixed_parity(a_r, b_r, c_r):
    p = (a_r % 2, b_r % 2, c_r % 2)
    return not (p == (0, 0, 0) or p == (1, 1, 1))


def v2(n):
    """2-adic valuation, with infinity for zero."""
    if n == 0:
        return float('inf')
    n = abs(n)
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def main():
    print("=" * 78)
    print("Higher-derivative 2-adic diagnostic for mixed-parity triples")
    print("=" * 78)
    print()

    print("Building h_C and derivatives symbolically ...")
    derivs = build_h_C_derivatives(order=3)
    h_C, h_C_1, h_C_2, h_C_3 = derivs
    print("  done.")
    print()

    # Sanity check: h_C(1) at (9,9,136) should be 0
    val = int(sp.Integer(h_C.subs({a: 9, b: 9, c: 136, x: 1})))
    print(f"  Sanity: h_C(1) at (9,9,136) = {val}")
    if val != 0:
        print("    WARNING: expected 0. Reflection or N is wrong.")
        return
    print("    (matches endpoint-one zero)")
    print()

    M = 8
    print(f"Evaluating canonical mixed-parity representatives mod {M} ...")
    rows = []
    for a_r in range(M):
        for b_r in range(M):
            for c_r in range(M):
                if not is_mixed_parity(a_r, b_r, c_r):
                    continue
                subs = {a: a_r, b: b_r, c: c_r, x: 1}
                v0 = int(sp.Integer(h_C.subs(subs)))
                v1 = int(sp.Integer(h_C_1.subs(subs)))
                v2v = int(sp.Integer(h_C_2.subs(subs)))
                v3v = int(sp.Integer(h_C_3.subs(subs)))
                rows.append(((a_r, b_r, c_r), v0, v1, v2v, v3v))

    print(f"  total mixed-parity representatives: {len(rows)}")
    print()

    # Distribution of 2-adic valuations
    cnt0 = Counter()
    cnt1 = Counter()
    cnt2 = Counter()
    cnt3 = Counter()
    for (_, v0, v1, v2v, v3v) in rows:
        cnt0[v2(v0)] += 1
        cnt1[v2(v1)] += 1
        cnt2[v2(v2v)] += 1
        cnt3[v2(v3v)] += 1

    print("2-adic valuation of h_C(1):",
          dict(sorted(cnt0.items())))
    print("2-adic valuation of h_C'(1):",
          dict(sorted(cnt1.items())))
    print("2-adic valuation of h_C''(1):",
          dict(sorted(cnt2.items())))
    print("2-adic valuation of h_C'''(1):",
          dict(sorted(cnt3.items())))
    print()

    # Joint pattern distribution
    patterns = Counter()
    for (_, v0, v1, v2v, v3v) in rows:
        patterns[(v2(v0), v2(v1), v2(v2v), v2(v3v))] += 1

    print("Distinct joint v2-patterns "
          "(h_C(1), h_C'(1), h_C''(1), h_C'''(1)):")
    for p, cnt in sorted(patterns.items(), key=lambda kv: -kv[1]):
        print(f"  {p}: {cnt} representatives")
    print()

    # Consistency: for a triple with all integer roots, the
    # expected pattern for the (3,3,2) mod 4 case is
    # v2(h_C(1)) >= 6 and v2(h_C'(1)) >= 4.
    # We list classes with v2(h_C(1)) < 6.
    print("=" * 78)
    print("Representatives with v2(h_C(1)) < 6:")
    print("This is not a list of uniform residue-class exclusions.")
    print("=" * 78)
    low = [(pat, v0, v1, v2v, v3v) for (pat, v0, v1, v2v, v3v) in rows
           if v2(v0) < 6]
    print(f"  count: {len(low)}")
    sample = low[:24]
    for (pat, v0, v1, v2v, v3v) in sample:
        print(f"  {pat}: "
              f"v2(h_C(1))={v2(v0)}, v2(h_C'(1))={v2(v1)}, "
              f"v2(h_C''(1))={v2(v2v)}, v2(h_C'''(1))={v2(v3v)}")
    if len(low) > 24:
        print(f"  ... and {len(low) - 24} more")


if __name__ == "__main__":
    main()
