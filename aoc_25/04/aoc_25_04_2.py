from pathlib import Path

# =============== SOLUTION PART =============== #

def is_in_bounds(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def count_neighbours(grid, x, y):
    result = 0

    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if is_in_bounds(grid, x + dx, y + dy) and grid[y + dy][x + dx] == grid[y][x]:
                result += 1

    return result - 1 # minus middle


def solve(input):
    grid = [list(x) for x in input.split('\n')]

    result, new_removed = 0, 1

    while new_removed != 0:
        new_removed = 0
        to_remove = set()

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '@' and count_neighbours(grid, x, y) < 4:
                    new_removed += 1
                    to_remove.add((x, y))
        
        for x, y in to_remove:
            grid[y][x] = '.'

        result += new_removed

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
    print(solve(read_input(input_file)))

print("Test done")
