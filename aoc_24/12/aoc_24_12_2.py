from pathlib import Path

# =============== SOLUTION PART =============== #

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def is_in_bounds(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def need_check(grid, x, y, visited):
    return is_in_bounds(grid, x, y) and (x, y) not in visited

def need_visit(grid, cx, cy, nx, ny, visited):
    return need_check(grid, nx, ny, visited) and grid[ny][nx] == grid[cy][cx]

def is_free_corner(grid, x, y, k, l, fence_sides):
    # switch cuz corner
    x, y = x + l, y + k
    return not is_in_bounds(grid, x, y) or (x, y) not in fence_sides

def is_corner(grid, x, y, k, l, fence_sides):
    return is_free_corner(grid, x, y, k, l, fence_sides) and\
           is_free_corner(grid, x, y, -k, -l, fence_sides)

def check_side(grid, x, y, nx, ny, l, k, fence_sides):
    return (
        not is_in_bounds(grid, nx + l, ny + k) or
        grid[ny + k][nx + l] == grid[y][x] or
        (x + l, y + k) not in fence_sides
    )

def is_side(grid, x, y, nx, ny, k, l, cur, fence_sides):
    return (
        (nx, ny) not in cur and
        check_side(grid, x, y, nx, ny, l, k, fence_sides) and
        check_side(grid, x, y, nx, ny, -l, -k, fence_sides)
    )

def check_inner_side(grid, x, y, nx, ny, k, l, cur, fence_sides):
    return (
        is_in_bounds(grid, x + l, y + k) and
        (x + l, y + k) in fence_sides and
        (nx + l, ny + k) not in cur
    )

def is_inner_side(grid, x, y, nx, ny, k, l, cur, fence_sides):
    return (
        (nx, ny) not in cur and
        check_inner_side(grid, x, y, nx, ny, k, l, cur, fence_sides) and
        check_inner_side(grid, x, y, nx, ny, -k, -l, cur, fence_sides)
    )

def sides(grid, x, y, fence_sides, cur):
    sides = 0
    for k, l in DIRECTIONS:
        nx, ny = x + k, y + l

        if not is_in_bounds(grid, nx, ny):
            if is_corner(grid, x, y, k, l, fence_sides):
                sides += 1
        else:
            if is_side(grid, x, y, nx, ny, k, l, cur, fence_sides):
                sides += 1

        if is_inner_side(grid, x, y, nx, ny, k, l, cur, fence_sides):
            sides -= 1

    fence_sides.add((x, y))
    return sides

def solver(input):
    grid = [list(line) for line in input.split('\n')]
    used = set()
    res = 0

    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if (i, j) in used:
                continue
            used.add((i, j))
            nextp, cur = {(i, j)}, set()
            area, perimeter = 0, 0

            while nextp:
                x, y = nextp.pop()
                cur.add((x, y))
                area += 1

                for k, l in DIRECTIONS:
                    nx, ny = x + k, y + l
                    if need_visit(grid, x, y, nx, ny, used):
                        used.add((nx, ny))
                        nextp.add((nx, ny))
            fence_sides = set()

            for x, y in cur:
                perimeter += sides(grid, x, y, fence_sides, cur)
            res += area * perimeter

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
