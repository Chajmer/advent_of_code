from pathlib import Path

# =============== SOLUTION PART =============== #

TURNS = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}

def find_agent(grid):
    for i, row in enumerate(grid):
        if '^' in row:
            x, y = row.index('^'), i
            grid[y][x] = 'X'
            return x, y

def turn(facing):
    return (facing + 1) % 4

def move(x, y, facing):
    return x + TURNS[facing][0], y + TURNS[facing][1]

def is_in_bounds(x, y, facing_step, grid):
    x, y = move(x, y, facing_step)
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def is_obstacle(x, y, facing_step, grid):
    x, y = move(x, y, facing_step)
    return grid[y][x] == '#'

def solver(input):
    grid = [list(line) for line in input.split()]
    x, y = find_agent(grid)
    facing = 0

    turnable = True

    while turnable:

        # try forward then right
        if is_in_bounds(x, y, facing, grid):

            if not is_obstacle(x, y, facing, grid):
                x, y = move(x, y, facing)
                grid[y][x] = 'X'

            else:
                facing = turn(facing)

        else:
            turnable = False

    return sum(line.count('X') for line in grid)


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
