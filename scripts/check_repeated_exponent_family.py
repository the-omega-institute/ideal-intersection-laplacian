import hashlib
import itertools
import json
from pathlib import Path

import sympy


exponent, third_exponent, variable = sympy.symbols("a c x")
positive_offset = sympy.Symbol("b")
quotient = sympy.Matrix([
    [exponent ** 2 + exponent * third_exponent, 0, -exponent ** 2, -exponent * third_exponent],
    [0, 2 * exponent * third_exponent, 0, -2 * exponent * third_exponent],
    [-2 * exponent, 0, 2 * exponent + 2 * exponent * third_exponent, -2 * exponent * third_exponent],
    [-exponent, -third_exponent, -exponent ** 2, exponent ** 2 + exponent + third_exponent],
])
first_coefficient = 2 * exponent ** 2 + 5 * exponent * third_exponent + 3 * exponent + third_exponent
second_coefficient = (exponent ** 4 + 7 * exponent ** 3 * third_exponent + 3 * exponent ** 3
                      + 8 * exponent ** 2 * third_exponent ** 2 + 11 * exponent ** 2 * third_exponent
                      + 2 * exponent ** 2 + 3 * exponent * third_exponent ** 2 + 2 * exponent * third_exponent)
third_coefficient = (2 * exponent ** 2 * third_exponent * (exponent + third_exponent + 1)
                     * (exponent ** 2 + 2 * exponent * third_exponent + 2 * exponent + third_exponent))
cubic = variable ** 3 - first_coefficient * variable ** 2 + second_coefficient * variable - third_coefficient
antisymmetric = sympy.Matrix([
    [exponent ** 2 + exponent * third_exponent, -exponent * third_exponent],
    [-exponent, exponent ** 2 + exponent + third_exponent + 2 * exponent * third_exponent],
])
family = (exponent - 1) * (2 * exponent - 1)
family_cubic = sympy.expand(cubic.subs(third_exponent, family))
upper_integer = 2 * exponent ** 3 - 2 * exponent ** 2 + 2 * exponent - 1
upper_value = 2 * (5 * exponent ** 4 - 10 * exponent ** 3 + 7 * exponent ** 2 - 1)
lower_factor = 2 * exponent ** 4 - 7 * exponent ** 3 + 7 * exponent ** 2 - exponent - 3
lower_value = -2 * (exponent - 1) * (exponent + 2) * lower_factor


def equal(first, second):
    if sympy.expand(first - second) != 0:
        raise AssertionError("Polynomial identity failed")


equal(quotient.charpoly(variable).as_expr(), variable * cubic)
equal(family_cubic.subs(variable, upper_integer), upper_value)
equal(family_cubic.subs(variable, upper_integer - 1), lower_value)
equal(lower_factor.subs(exponent, positive_offset + 3),
      2 * positive_offset ** 4 + 17 * positive_offset ** 3 + 52 * positive_offset ** 2 + 68 * positive_offset + 30)
equal(upper_value, 2 * (5 * exponent ** 3 * (exponent - 2) + 7 * exponent ** 2 - 1))
antisymmetric_roots = [4 * exponent ** 3 - 3 * exponent ** 2 + exponent, 2 * exponent ** 3 - 2 * exponent ** 2 + 1]
equal(antisymmetric.subs(third_exponent, family).charpoly(variable).as_expr(),
      sympy.prod(variable - root for root in antisymmetric_roots))
base_cubic = family_cubic.subs(exponent, 2)
residues = [int(base_cubic.subs(variable, residue)) % 5 for residue in range(5)]
if any(value == 0 for value in residues):
    raise AssertionError("Base irreducibility witness failed")
equal(base_cubic.subs(variable, variable - 11), variable ** 3 - 80 * variable ** 2 + 2099 * variable - 18052)


def check_graph(first_exponent):
    last_exponent = int(family.subs(exponent, first_exponent))
    bounds = (first_exponent, first_exponent, last_exponent)
    vertices = [coordinates for coordinates in itertools.product(*(range(bound + 1) for bound in bounds))
                if coordinates not in ((0, 0, 0), bounds)]
    supports = [sum(1 << index for index, (value, bound) in enumerate(zip(coordinates, bounds)) if value < bound)
                for coordinates in vertices]
    neighbors = [[] for coordinates in vertices]
    pairs = 0
    for first, coordinates in enumerate(vertices):
        for second in range(first + 1, len(vertices)):
            pairs += 1
            if any(max(left, right) < bound for left, right, bound in zip(coordinates, vertices[second], bounds)):
                neighbors[first].append(second)
                neighbors[second].append(first)
    masks = list(range(1, 8))
    actual_quotient = sympy.zeros(7)
    for mask in masks:
        expected = None
        for representative, support in enumerate(supports):
            if support != mask:
                continue
            row = [len(neighbors[representative]) * int(mask == target)
                   - sum(supports[neighbor] == target for neighbor in neighbors[representative]) for target in masks]
            if expected is not None and row != expected:
                raise AssertionError("Direct ideal graph partition is not equitable")
            expected = row
        actual_quotient[mask - 1, :] = sympy.Matrix([expected])
    universal_size = supports.count(7)
    reduced = actual_quotient[:6, :6] - universal_size * sympy.eye(6)
    symmetric_embedding = sympy.Matrix([[int(mask in cell) for cell in ({1, 2}, {4}, {3}, {5, 6})] for mask in range(1, 7)])
    antisymmetric_embedding = sympy.Matrix([[int(mask == 1) - int(mask == 2), int(mask == 5) - int(mask == 6)]
                                          for mask in range(1, 7)])
    substitutions = {exponent: first_exponent, third_exponent: last_exponent}
    symmetric_block = quotient.subs(substitutions)
    antisymmetric_block = antisymmetric.subs(substitutions)
    if reduced * symmetric_embedding != symmetric_embedding * symmetric_block:
        raise AssertionError("Symmetric block embedding fails")
    if reduced * antisymmetric_embedding != antisymmetric_embedding * antisymmetric_block:
        raise AssertionError("Antisymmetric block embedding fails")
    extension = symmetric_embedding.col_join(sympy.zeros(1, 4))
    nonconstant_embedding = extension * symmetric_block
    if nonconstant_embedding.rank() != 3:
        raise AssertionError("Nonconstant quotient space has incorrect dimension")
    if actual_quotient * nonconstant_embedding != nonconstant_embedding * (symmetric_block + universal_size * sympy.eye(4)):
        raise AssertionError("Universal-vertex lift fails")
    expected_polynomial = (variable * (variable - len(vertices))
                           * antisymmetric_block.charpoly(variable).as_expr().subs(variable, variable - universal_size)
                           * cubic.subs(substitutions).subs(variable, variable - universal_size))
    equal(actual_quotient.charpoly(variable).as_expr(), expected_polynomial)
    return {"exponents": list(bounds), "vertices": len(vertices), "vertex_pairs_checked": pairs,
            "universal_vertices": universal_size, "equitable_partition": "passed",
            "symmetric_and_antisymmetric_embeddings": "passed", "nonconstant_join_lift": "passed",
            "full_support_quotient_characteristic_polynomial": str(sympy.factor(expected_polynomial)),
            "lower_sign_value": int(lower_value.subs(exponent, first_exponent)),
            "upper_sign_value": int(upper_value.subs(exponent, first_exponent))}


cases = [check_graph(first_exponent) for first_exponent in (2, 3, 4)]
print(json.dumps({
    "symbolic_identities": "passed", "base_cubic_modulo_5": residues,
    "lower_factor_at_a_equals_b_plus_3": "2*b**4 + 17*b**3 + 52*b**2 + 68*b + 30",
    "cases": cases, "total_vertex_pairs_checked": sum(case["vertex_pairs_checked"] for case in cases),
    "sympy": sympy.__version__, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Polynomial identities plus direct-graph checks for a=2,3,4. For a=2 the sign interval is not used: irreducibility modulo5 supplies the obstruction. No full548vertex characteristic polynomial, numerical eigensolver or Lean verification."
}, indent=2))
