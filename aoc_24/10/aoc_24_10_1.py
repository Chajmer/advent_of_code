from pathlib import Path

# =============== SOLUTION PART =============== #

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_in_bounds(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def find_trail_score(grid, found, x, y):
    if grid[y][x] == 9:
        found.add((x, y))

    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        if is_in_bounds(grid, new_x, new_y) and grid[y][x] + 1 == grid[new_y][new_x]:
            find_trail_score(grid, found, new_x, new_y)

    return len(found)

def solver(input):
    grid = [[int(x) for x in list(line)] for line in input.split('\n')]
    result = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                result += find_trail_score(grid, set(), x, y)

    return result


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
