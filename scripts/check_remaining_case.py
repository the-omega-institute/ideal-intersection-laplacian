import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

import sympy


exponents = (2, 2, 3)
vertices = [coordinates for coordinates in itertools.product(*(range(bound + 1) for bound in exponents))
            if coordinates not in ((0, 0, 0), exponents)]
supports = [sum(1 << index for index, (value, bound) in enumerate(zip(coordinates, exponents))
                if value < bound) for coordinates in vertices]
classes = sorted(set(supports))
neighbors = [[second for second, other in enumerate(vertices)
              if first != second and any(max(left, right) < bound
                                         for left, right, bound in zip(coordinates, other, exponents))]
             for first, coordinates in enumerate(vertices)]
laplacian = sympy.zeros(len(vertices))
for first, adjacent in enumerate(neighbors):
    laplacian[first, first] = len(adjacent)
    for second in adjacent:
        laplacian[first, second] = -1
quotient = sympy.zeros(len(classes))
for row, mask in enumerate(classes):
    representatives = [index for index, support in enumerate(supports) if support == mask]
    expected = None
    for representative in representatives:
        values = [sum(laplacian[representative, column] for column, support in enumerate(supports)
                      if support == target) for target in classes]
        if expected is not None and values != expected:
            raise AssertionError("Partition is not equitable")
        expected = values
    quotient[row, :] = sympy.Matrix([expected])
variable = sympy.Symbol("x")
quotient_polynomial = quotient.charpoly(variable).as_expr()
full_polynomial = laplacian.charpoly(variable).as_expr()
internal = sympy.Integer(1)
for mask, multiplicity in Counter(supports).items():
    representative = supports.index(mask)
    eigenvalue = len(neighbors[representative]) + 1
    internal *= (variable - eigenvalue) ** (multiplicity - 1)
if sympy.expand(full_polynomial - internal * quotient_polynomial) != 0:
    raise AssertionError("Direct full spectrum and quotient decomposition disagree")
antisymmetric_embedding = sympy.Matrix([
    [int(mask == 1) - int(mask == 2), int(mask == 5) - int(mask == 6)]
    for mask in classes
])
antisymmetric_block = sympy.Matrix([[21, -6], [-2, 32]])
if quotient * antisymmetric_embedding != antisymmetric_embedding * antisymmetric_block:
    raise AssertionError("The repeated-exponent block does not match the quotient action")
cubic = variable ** 3 - 80 * variable ** 2 + 2099 * variable - 18052
modulo_five_values = [int(cubic.subs(variable, residue)) % 5 for residue in range(5)]
if any(value == 0 for value in modulo_five_values) or sympy.rem(quotient_polynomial, cubic, variable) != 0:
    raise AssertionError("Irreducible cubic witness fails")
print(json.dumps({
    "exponents": list(exponents), "vertices": len(vertices),
    "quotient": [[int(value) for value in row] for row in quotient.tolist()],
    "quotient_characteristic_polynomial": str(sympy.factor(quotient_polynomial)),
    "full_characteristic_polynomial": str(sympy.factor(full_polynomial)),
    "equal_pair_antisymmetric_block": [[21, -6], [-2, 32]],
    "equal_pair_antisymmetric_eigenvalues": [20, 33],
    "irreducible_cubic_modulo_5_values": modulo_five_values,
    "direct_full_vs_quotient": "passed", "sympy": sympy.__version__,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Exact finite characteristic-polynomial check for exponent vector (2,2,3); not a general-exponent theorem or Lean verification."
}, indent=2))
