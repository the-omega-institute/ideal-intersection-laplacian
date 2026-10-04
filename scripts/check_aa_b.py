"""
Diagnostic script for the (a,a,b) family of ideal intersection graphs.

For n = p^a q^a r^b with distinct primes p, q, r, the reduced cubic is

    f_{a,b}(x) = x^3 - E1 x^2 + E2 x - E3

with

    E1 = 2a^2 + 5ab + 3a + b
    E2 = a^4 + 7a^3 b + 3a^3 + 8a^2 b^2 + 11a^2 b + 2a^2
         + 3a b^2 + 2ab 
    E3 = 2a^2 b (a+b+1)(a^2 + 2ab + 2a + b)

The graph is non-Laplacian-integral iff this cubic has a
non-integer root, which is equivalent to: the cubic has an
irreducible factor of degree >= 2 over Q.

This script is a DIAGNOSTIC, not a proof. It reports, for each (a,b):

  - integer roots of f_{a,b}
  - whether f_{a,b} has an irreducible factor of degree >= 2 over Q
  - the numerical location of any real root strictly between two
    consecutive integers
  - the smallest prime p such that f_{a,b} mod p is irreducible

Requires: sympy (pip install sympy).
"""

import sys

try:
    from sympy import symbols, Poly, factor_list, nroots, divisors, Integer, GF
except ImportError:
    print("ERROR: sympy is required. Install with: pip install sympy")
    sys.exit(1)


x = symbols('x')


# ----------------------------------------------------------------------
# Cubic and its coefficients
# ----------------------------------------------------------------------

def cubic_coeffs(a, b):
    """Return (E1, E2, E3) for f(x) = x^3 - E1 x^2 + E2 x - E3."""
    E1 = 2*a**2 + 5*a*b + 3*a + b
    E2 = (a**4 + 7*a**3*b + 3*a**3 + 8*a**2*b**2
          + 11*a**2*b + 2*a**2 + 3*a*b**2 + 2*a*b)
    E3 = 2*a**2*b*(a + b + 1)*(a**2 + 2*a*b + 2*a + b)
    return E1, E2, E3


def cubic_poly(a, b):
    """Return the cubic as a Poly over ZZ."""
    E1, E2, E3 = cubic_coeffs(a, b)
    return Poly(x**3 - E1*x**2 + E2*x - E3, x, domain='ZZ')


# ----------------------------------------------------------------------
# Integer roots (rational root theorem)
# ----------------------------------------------------------------------

def integer_roots(poly):
    coeffs = poly.all_coeffs()
    const = int(coeffs[-1])
    if const == 0:
        return [Integer(0)]
    roots = []
    for d in divisors(abs(const)):
        for sign in (1, -1):
            c = sign * Integer(d)
            if poly.eval(c) == 0:
                roots.append(c)
    return roots


# ----------------------------------------------------------------------
# Factorization over ZZ
# ----------------------------------------------------------------------

def factorization_info(poly):
    factors, _ = factor_list(poly, x)
    out = []
    has_irr = False
    for f, m in factors:
        try:
            deg = int(f.degree()) if hasattr(f, 'degree') else 1
        except Exception:
            deg = 1
        out.append((f, m, deg))
        if deg >= 2:
            has_irr = True
    return out, has_irr


# ----------------------------------------------------------------------
# Trapped real root
# ----------------------------------------------------------------------

def trapped_root_info(poly):
    roots = nroots(poly.as_expr(), n=30)
    best = None
    for r in roots:
        rc = complex(r)
        if abs(rc.imag) < 1e-12:
            val = rc.real
            nearest = round(val)
            if abs(val - nearest) > 1e-15:
                if best is None or abs(val - nearest) < abs(best - round(best)):
                    best = val
    return (best is not None, best)


# ----------------------------------------------------------------------
# Irreducibility mod p
# ----------------------------------------------------------------------

def irreducible_mod_p(poly, p):
    try:
        poly_mod = Poly(poly.as_expr(), x, domain=GF(p))
        return bool(poly_mod.is_irreducible)
    except Exception:
        return None


def smallest_irreducible_prime(poly,
                               primes=(2, 3, 5, 7, 11, 13,
                                       17, 19, 23, 29, 31)):
    for p in primes:
        res = irreducible_mod_p(poly, p)
        if res is True:
            return p
    return None


# ----------------------------------------------------------------------
# Analyze a single (a, b)
# ----------------------------------------------------------------------

def analyze(a, b):
    poly = cubic_poly(a, b)
    roots = integer_roots(poly)
    factors, has_irr = factorization_info(poly)
    has_trap, trap_val = trapped_root_info(poly)
    p_irr = smallest_irreducible_prime(poly)
    return {
        'a': a,
        'b': b,
        'poly': poly,
        'int_roots': roots,
        'has_irrational': has_irr,
        'factor_degrees': [d for _, _, d in factors],
        'has_trapped': has_trap,
        'trap_val': trap_val,
        'p_irr': p_irr,
    }


# ----------------------------------------------------------------------
# Printing helpers
# ----------------------------------------------------------------------

def fmt_trap(val):
    if val is None:
        return "-"
    return f"{val:.6f}"


def print_header(title):
    print()
    print("=" * 90)
    print(title)
    print("=" * 90)


def print_table(rows):
    header = (f"{'a':>3} | {'b':>4} | {'int roots':>15} | "
              f"{'irrational?':>11} | {'factor deg':>12} | "
              f"{'trapped?':>9} | {'trap value':>13} | {'p_irr':>6}")
    print(header)
    print("-" * 90)
    for r in rows:
        int_str = ",".join(str(v) for v in r['int_roots']) if r['int_roots'] else "-"
        deg_str = ",".join(str(d) for d in r['factor_degrees'])
        p_str = str(r['p_irr']) if r['p_irr'] is not None else "-"
        print(f"{r['a']:>3} | {r['b']:>4} | {int_str:>15} | "
              f"{str(r['has_irrational']):>11} | {deg_str:>12} | "
              f"{str(r['has_trapped']):>9} | "
              f"{fmt_trap(r['trap_val']):>13} | {p_str:>6}")


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    print_header("Family (a,a,b): diagnostic for Laplacian non-integrality")
    print("Cubic: f(x) = x^3 - E1 x^2 + E2 x - E3, with")
    print("  E1 = 2a^2 + 5ab + 3a + b")
    print("  E2 = a^4 + 7a^3 b + 3a^3 + 8a^2 b^2 + 11a^2 b + 2a^2")
    print("       + 3a b^2 + 2ab")
    print("  E3 = 2a^2 b (a+b+1)(a^2 + 2ab + 2a + b)")
    print()
    print("Columns:")
    print("  int roots    : integer roots of f_{a,b}")
    print("  irrational?  : True iff f_{a,b} has an irreducible factor")
    print("                 of degree >= 2 over Q")
    print("  factor deg   : degrees of the irreducible factors")
    print("  trapped?     : True iff some real root lies strictly")
    print("                 between two consecutive integers")
    print("  trap value   : numerical value of a trapped root")
    print("  p_irr        : smallest prime p with f_{a,b} mod p irreducible")

    print_header("Part 1: a = 2, b = 1..30")
    print_table([analyze(2, b) for b in range(1, 31)])

    print_header("Part 2: a = 3, b = 1..25")
    print_table([analyze(3, b) for b in range(1, 26)])

    print_header("Part 3: a = 4, b = 1..20")
    print_table([analyze(4, b) for b in range(1, 21)])

    print_header("Part 4: special parametric sub-families")

    print("\n--- Family b = a + 1, a = 2..15 ---")
    print_table([analyze(a, a + 1) for a in range(2, 16)])

    print("\n--- Family b = (a-1)(2a-1), a = 2..12 ---")
    print_table([analyze(a, (a - 1) * (2 * a - 1)) for a in range(2, 13)])

    print("\n--- Family b = 2a - 1, a = 2..15 ---")
    print_table([analyze(a, 2 * a - 1) for a in range(2, 16)])

    print_header("Summary")

    a2 = [analyze(2, b) for b in range(1, 31)]
    n_irr_2 = sum(1 for r in a2 if r['has_irrational'])
    n_trap_2 = sum(1 for r in a2 if r['has_trapped'])
    print(f"a = 2, b = 1..30: irrational in {n_irr_2}/30, "
          f"trapped in {n_trap_2}/30")

    a3 = [analyze(3, b) for b in range(1, 26)]
    n_irr_3 = sum(1 for r in a3 if r['has_irrational'])
    n_trap_3 = sum(1 for r in a3 if r['has_trapped'])
    print(f"a = 3, b = 1..25: irrational in {n_irr_3}/25, "
          f"trapped in {n_trap_3}/25")

    a4 = [analyze(4, b) for b in range(1, 21)]
    n_irr_4 = sum(1 for r in a4 if r['has_irrational'])
    n_trap_4 = sum(1 for r in a4 if r['has_trapped'])
    print(f"a = 4, b = 1..20: irrational in {n_irr_4}/20, "
          f"trapped in {n_trap_4}/20")

    print()
    print("Interpretation:")
    print("  - If 'irrational?' is True for all (a,b), the cubic always")
    print("    has a non-integer root, so the graph is not integral.")
    print("  - If 'trapped?' is True for all (a,b), the non-integer root")
    print("    is always located between two consecutive integers.")
    print("  - If 'p_irr' is a small prime for all (a,b), a modular")
    print("    irreducibility argument may close the family.")
 

if __name__ == "__main__":
    main()
