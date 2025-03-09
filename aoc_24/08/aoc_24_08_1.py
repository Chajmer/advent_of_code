from pathlib import Path
from itertools import combinations

# =============== SOLUTION PART =============== #

def is_in_bounds(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def solver(input):
    grid = [list(line) for line in input.split('\n')]
    poss = {}

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '.':
                poss.setdefault(cell, []).append((i, j))

    antinodes = set()

    for positions in poss.values():
        for (x1, y1), (x2, y2) in combinations(positions, 2):
            nx1, ny1 = 2 * x2 - x1, 2 * y2 - y1
            nx2, ny2 = 2 * x1 - x2, 2 * y1 - y2

            if is_in_bounds(nx1, ny1, grid):
                antinodes.add((nx1, ny1))

            if is_in_bounds(nx2, ny2, grid):
                antinodes.add((nx2, ny2))

    return len(antinodes)


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
    print(solver(read_input(input_file)))

print("Test done")
