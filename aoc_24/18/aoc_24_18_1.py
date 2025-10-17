from pathlib import Path

# =============== SOLUTION PART =============== #

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def is_in_bounds(position, grid):
    x, y = position
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def is_free_cell(grid, position):
    return is_in_bounds(position, grid) and grid[position[1]][position[0]] == '.'

# returns length of shortest maze path
def solve_maze(grid):
    if len(grid) == 1:
        return 0
    
    # bfs solution of maze
    start = (0, 0)
    end = (len(grid[0]) - 1, len(grid) - 1)
    bfs_iter = [start]
    visited = set()
    steps = 1

    while bfs_iter:
        bfs_next_iter = []

        for x, y in bfs_iter:
            for dx, dy in DIRECTIONS:
                next = (x + dx, y + dy)

                if next == end:
                    return steps
                
                if next not in  visited and is_free_cell(grid, next):
                    visited.add(next)
                    bfs_next_iter.append(next)

        bfs_iter = bfs_next_iter
        steps += 1

    return -1

def solver(input):
    lines = input.split('\n')
    space, falls = [int(x) for x in lines[0].split(':')]
    grid = [['.' for _ in range(space + 1)] for _ in range(space + 1)]

    for i in range(1, falls + 1):
        x, y = [int(x) for x in lines[i].split(',')]
        grid[y][x] = '#'

    return solve_maze(grid)


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
