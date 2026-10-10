"""
Modular endpoint surface analysis for the fully-distinct region.

For each prime p and each endpoint x_val in {1, 2}, compute for
every (a mod p, b mod p) the set of residues c mod p such that
h_C(x_val) ≡ 0 mod p. From the two endpoint sets, form S_p, the
set of residue triples (a, b, c) mod p where AT LEAST ONE endpoint
vanishes. This union is the necessary low-root candidate condition.

If S_p is empty for some prime p, then no integer triple has either
h_C(1) = 0 or h_C(2) = 0. Combined with the uniform root in
(0,3), the fully-distinct region is settled at that prime.

Uses the corrected reflection N = |V(H)| = a + b + c + ab + ac + bc.

Requires sympy.
"""

import argparse
import json
import sys

try:
    import sympy as sp
except ImportError:
    print("ERROR: sympy is required. pip install sympy")
    sys.exit(1)


a, b, c, x = sp.symbols('a b c x')


def build_B_and_N():
    """Build the 6x6 Laplacian quotient of H and its size N."""
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

    N = sum(sizes)  # = a + b + c + ab + ac + bc
    return B, N


def build_h_C_endpoint(x_val, B, N):
    """h_C(x_val) as a polynomial in a, b, c."""
    char = B.charpoly(x).as_expr()
    g_B = sp.cancel(char / x)
    return sp.expand(-g_B.subs(x, N - x_val))


def root_set(h_expr, p):
    """For each (a_r, b_r), the set of c_r in F_p with h_expr = 0 mod p."""
    result = {}
    for a_r in range(p):
        for b_r in range(p):
            roots = []
            for c_r in range(p):
                val = h_expr.subs({a: a_r, b: b_r, c: c_r})
                if sp.Integer(val) % p == 0:
                    roots.append(c_r)
            result[(a_r, b_r)] = roots
    return result


def modular_analysis(h1, h2, p):
    roots_1 = root_set(h1, p)
    roots_2 = root_set(h2, p)
    surviving = []
    pairs = []
    both_zero = 0
    for a_r in range(p):
        for b_r in range(p):
            first_roots = set(roots_1[(a_r, b_r)])
            second_roots = set(roots_2[(a_r, b_r)])
            either_roots = sorted(first_roots | second_roots)
            both_zero += len(first_roots & second_roots)
            surviving.extend((a_r, b_r, c_r) for c_r in either_roots)
            pairs.append({'a': a_r, 'b': b_r, 'c_roots_endpoint_one': sorted(first_roots),
                          'c_roots_endpoint_two': sorted(second_roots), 'c_roots_either_endpoint': either_roots})
    return {'prime': p, 'surviving_union_count': len(surviving),
            'excluded_both_nonzero_count': p ** 3 - len(surviving),
            'both_zero_intersection_count': both_zero, 'sample_union': surviving[:8], 'pairs': pairs}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', action='store_true')
    arguments = parser.parse_args()
    B, N = build_B_and_N()
    h1 = build_h_C_endpoint(1, B, N)
    h2 = build_h_C_endpoint(2, B, N)
    primes = [2, 3, 5, 7, 11, 13]
    rows = [modular_analysis(h1, h2, prime) for prime in primes]
    if arguments.json:
        print(json.dumps({'necessary_condition': 'h_C(1)=0 OR h_C(2)=0; union, not intersection',
                          'primes': primes, 'prime_tables': rows,
                          'scope': 'Complete residue-root sets at the six fixed primes proposed by the contributor. Modular survivors are necessary candidates, not asserted integer zeros or integral spectra. Zero/equal coordinate residues are retained. FullQ3 remains open.'}, indent=2))
        return
    print("=" * 78)
    print("Modular endpoint surface analysis (fully-distinct region)")
    print("=" * 78)
    print()

    print("Building B, N, h_C(1), h_C(2) symbolically ...")
    print(f"  N = {N}")
    print("  done.")
    print()

    for row in rows:
        p = row['prime']
        print(f"--- p = {p} ---")
        if not row['surviving_union_count']:
            print(f"  S_p = EMPTY")
            print(f"  -> no integer triple has either endpoint zero")
            print(f"  -> region settled at prime {p}")
        else:
            print(f"  |S_p| = {row['surviving_union_count']} residue triples survive (union)")
            print(f"  excluded with both endpoints nonzero: {row['excluded_both_nonzero_count']}")
            print(f"  both endpoints zero: {row['both_zero_intersection_count']} (separate diagnostic)")
            print(f"  sample: {row['sample_union']}{' ...' if row['surviving_union_count'] > 8 else ''}")
        print()

    print("=" * 78)
    print("Limitation")
    print("=" * 78)
    print("""
Any finite set of moduli admits survivor classes congruent to the
known zeros (9,9,136) on endpoint 1 and (10,10,12) on endpoint 2.
Those survivors are not claimed to be actual integer zeros. A
combination with interval restrictions or another-root obstruction
is still required for full closure.
""")


if __name__ == "__main__":
    main()
