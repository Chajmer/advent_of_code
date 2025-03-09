from pathlib import Path

# =============== SOLUTION PART =============== #

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def is_in_bounds(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def fences(grid, x, y):
    faces = 4
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if is_in_bounds(grid, nx, ny) and grid[ny][nx] == grid[y][x]:
            faces -= 1
    return faces

def need_check(grid, x, y, visited):
    return is_in_bounds(grid, x, y) and (x, y) not in visited

def need_visit(grid, cx, cy, nx, ny, visited):
    return need_check(grid, nx, ny, visited) and grid[ny][nx] == grid[cy][cx]

def solver(input):
    grid = [list(line) for line in input.split('\n')]
    visited = set()
    total_price = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in visited:
                continue
            visited.add((x, y))
            to_visit = {(x, y)}
            area, perimeter = 0, 0

            while to_visit:
                cur_x, cur_y = to_visit.pop()
                area += 1
                perimeter += fences(grid, cur_x, cur_y)

                for dx, dy in DIRECTIONS:
                    nx, ny = cur_x + dx, cur_y + dy
                    if need_visit(grid, cur_x, cur_y, nx, ny, visited):
                        visited.add((nx, ny))
                        to_visit.add((nx, ny))

            total_price += area * perimeter

    return total_price


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
