from pathlib import Path
from sympy import symbols, solve as sympy_solve

# =============== SOLUTION PART =============== #

def solve(input):
    # parse
    hail_stones = ([([([int(x2) for x2 in x1.split(', ')],
                       [int(x2) for x2 in y1.split(', ')])
                    for x1, y1 in [x.split('@')]])[0] for x in input.split('\n')])
    # solve
    x, y, z, vx, vy, vz, a, b, c = symbols('x y z vx vy vz a b c')
    coords = [x, y, z]
    velocity = [vx, vy, vz]
    coeffs = [a, b, c]
    equations = []
    for i, hs in enumerate(hail_stones[:3]):
        for j in range(3):
            equations.append(coords[j]-hs[0][j]
                             + coeffs[i]*(velocity[j]-hs[1][j]))
    solution = sympy_solve(equations)
    # return
    return solution[0][x] + solution[0][y] + solution[0][z]


# =============== TEMPLATE PART =============== #

# README INPUTS:
# Inputs are separete files in this path-name template:
# {this_file_dir}/inputs/input_*.txt

def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read().rstrip()
    
input_dir = Path(__file__).parent / 'inputs'

# Iterate over all files matching the pattern 'input_*.txt'
for input_file in sorted(input_dir.glob(f'input_*.txt')):
    print(f"Input {input_file.stem[6:]}:")
    print(solve(read_input(input_file)))

print("Test done")
