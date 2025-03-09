from pathlib import Path

# =============== SOLUTION PART =============== #

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_in_bounds(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def find_trail_rating(grid, ratings, x, y):
    if grid[y][x] == 9:
        ratings += 1

    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        if is_in_bounds(grid, new_x, new_y) and grid[y][x] + 1 == grid[new_y][new_x]:
            ratings = find_trail_rating(grid, ratings, new_x, new_y)

    return ratings

def solver(a):
    res = 0
    map = [[int(x) for x in list(aa)] for aa in a.split('\n')]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                res += find_trail_rating(map, 0, j, i)
    return res


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
