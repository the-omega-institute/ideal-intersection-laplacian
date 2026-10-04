"""
Diagnostic for the inertia approach on the open region
8 <= a < b < c < 4a^2 - 2a.

Uses the Schur-complement criteria from the collaborators'
Proposition 11.1 to check, for each (a,b,c), whether there is
some integer m with 2 <= m < a satisfying:

  (1) (c-m)(s-m) < m a b           [K(m) negative definite]
  (2) (a-m+1)(s-m+1) > (m-1) b c   [both eigenvalues in (m-1,m)]

where s = a+b+c. If such m exists, the complement quotient has
two eigenvalues in (m-1, m) and the graph is not Laplacian integral.

DIAGNOSTIC ONLY. Uses only the Python standard library.
"""

import math
from collections import Counter


def is_square(n):
    """Return True iff n is a perfect square (n >= 0)."""
    if n < 0:
        return False
    return math.isqrt(n) ** 2 == n


def find_witness_m(a, b, c):
    """
    Return the smallest m in [2, a-1] satisfying both Schur
    criteria, or None if no such m exists.
    """
    s = a + b + c
    for m in range(2, a):
        cond1 = (c - m) * (s - m) < m * a * b
        cond2 = (a - m + 1) * (s - m + 1) > (m - 1) * b * c
        if cond1 and cond2:
            return m
    return None


def main():
    a_max = 20  # increase carefully; cost grows like a^3 log(a)

    print("=" * 78)
    print("Inertia-approach diagnostic for 8 <= a < b < c < 4a^2 - 2a")
    print("=" * 78)
    print()

    for a in range(8, a_max + 1):
        c_max = 4 * a * a - 2 * a
        counter = Counter()
        example_for_m = {}
        example_for_none = None
        total = 0

        for b in range(a + 1, c_max - 1):
            for c in range(b + 1, c_max):
                total += 1
                m = find_witness_m(a, b, c)
                counter[m] += 1
                if m is not None and m not in example_for_m:
                    example_for_m[m] = (a, b, c)
                if m is None and example_for_none is None:
                    example_for_none = (a, b, c)

        # Summary line
        witness_m = sorted(k for k in counter if k is not None)
        n_witness = sum(counter[m] for m in witness_m)
        n_none = counter.get(None, 0)

        print(f"a = {a}, c_max = {c_max}, total pairs = {total}")
        print(f"  with witness m: {n_witness}")
        for m in witness_m:
            print(f"    m = {m:>3}: {counter[m]:>6} pairs   "
                  f"example = {example_for_m[m]}")
        if n_none:
            print(f"  WITHOUT witness m: {n_none} pairs   "
                  f"example = {example_for_none}")

        # Compact: smallest and largest witness m
        if witness_m:
            print(f"  witness range: m_min = {min(witness_m)}, "
                  f"m_max = {max(witness_m)}")
        print()


if __name__ == "__main__":
    main()
