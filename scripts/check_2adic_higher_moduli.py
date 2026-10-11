"""
2-adic divisibility at higher moduli for mixed-parity triples.

For mixed-parity (a, b, c) — at least one even, at least one odd —
h_C(x) ≡ x^2 (x+1)^3 mod 2, so if all five roots are integers,
exactly three are odd. Theorem 13.6 of the collaborators shows
that 32 | h_C(1) or 32 | h_C(3) under that hypothesis.

This script enumerates (a, b, c) modulo M for M in {8, 16, 32},
keeps only the mixed-parity classes, and computes h_C(1) and
h_C(3) modulo 32 for each. A class is "excluded" if both
h_C(1) mod 32 and h_C(3) mod 32 are nonzero, because the
necessary divisibility fails in that class.

Uses N = |V(H)| = a + b + c + ab + ac + bc, NOT the full vertex
count (a+1)(b+1)(c+1) - 2 (which would include the universal
class incorrectly).

Requires sympy.
"""

import sympy as sp

a, b, c, x = sp.symbols('a b c x')


def build_B_and_N():
    """
    Return (B, N):
      B = 6x6 Laplacian quotient of H (the graph obtained by
          removing the universal class C_{1,2,3} from the ideal
          intersection graph);
      N = |V(H)| = a + b + c + ab + ac + bc.
    """
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


def h_C_at(x_val):
    """
    Return h_C(x_val) as a polynomial in a, b, c.

    Uses the reflection h_C(x) = -g_B(N - x), where
    g_B(y) = det(y I - B) / y.
    """
    B, N = build_B_and_N()
    charpoly = sp.expand(B.charpoly(x).as_expr())
    g_B = sp.expand(charpoly / x)   # charpoly has no constant term
    return sp.expand(-g_B.subs(x, N - x_val))


def is_mixed_parity(a_r, b_r, c_r):
    """True iff not all of a_r, b_r, c_r are even or all are odd."""
    p = (a_r % 2, b_r % 2, c_r % 2)
    return not (p == (0, 0, 0) or p == (1, 1, 1))


def evaluate_mod(expr, subs_dict, modulus):
    """Evaluate expr at integer subs and reduce mod modulus."""
    val = expr.subs(subs_dict)
    return int(sp.Integer(val)) % modulus


def main():
    print("=" * 78)
    print("2-adic divisibility at higher moduli (mixed-parity triples)")
    print("=" * 78)
    print()

    print("Building h_C(1) and h_C(3) symbolically ...")
    h1 = h_C_at(1)
    h3 = h_C_at(3)
    print("  done.")
    print()

    # Sanity check: h_C(1) at (9,9,136) should be 0 (known zero on
    # endpoint one), and h_C(2) at (10,10,12) should be 0.
    # We only test h_C(1) here as a quick consistency check.
    h1_at_9_9_136 = int(sp.Integer(h1.subs({a: 9, b: 9, c: 136})))
    print(f"  Sanity: h_C(1) at (9, 9, 136) = {h1_at_9_9_136}")
    if h1_at_9_9_136 != 0:
        print("    WARNING: expected 0. The reflection or N may be wrong.")
        return
    print("    (matches the known endpoint-one zero)")
    print()

    target = 32

    for M in [8, 16, 32]:
        n_mixed = 0
        n_excluded = 0
        n_survivor = 0
        survivor_sample = []
        for a_r in range(M):
            for b_r in range(M):
                for c_r in range(M):
                    if not is_mixed_parity(a_r, b_r, c_r):
                        continue
                    n_mixed += 1
                    v1 = evaluate_mod(h1, {a: a_r, b: b_r, c: c_r}, target)
                    v3 = evaluate_mod(h3, {a: a_r, b: b_r, c: c_r}, target)
                    if v1 == 0 or v3 == 0:
                        n_survivor += 1
                        if len(survivor_sample) < 5:
                            survivor_sample.append((a_r, b_r, c_r, v1, v3))
                    else:
                        n_excluded += 1
        print(f"M = {M}: mixed = {n_mixed}, "
              f"excluded = {n_excluded}, survivors = {n_survivor}")
        if survivor_sample:
            print(f"  sample survivors: {survivor_sample}")
        print()

    # Detailed table at M = 8 for (a odd, b odd, c even), to compare
    # with Theorem 13.6.
    print("=" * 78)
    print("Detail at M = 8 for (a odd, b odd, c even)")
    print("=" * 78)
    M = 8
    for a_r in range(1, M, 2):
        for b_r in range(1, M, 2):
            for c_r in range(0, M, 2):
                v1 = evaluate_mod(h1, {a: a_r, b: b_r, c: c_r}, target)
                v3 = evaluate_mod(h3, {a: a_r, b: b_r, c: c_r}, target)
                status = "SURV" if (v1 == 0 or v3 == 0) else "EXCL"
                print(f"  ({a_r},{b_r},{c_r}): "
                      f"h1 mod 32 = {v1:>2}, h3 mod 32 = {v3:>2}  [{status}]")


if __name__ == "__main__":
    main()
