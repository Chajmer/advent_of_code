from pathlib import Path

# =============== SOLUTION PART =============== #

TURNS = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}

def find_agent(grid):
    for i, row in enumerate(grid):
        if '^' in row:
            return row.index('^'), i

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

def perform_moves(grid, x, y, facing, max_moves, loop_check):
    moves = 0
    turnable = True

    while turnable and (loop_check or moves < max_moves):

        # try forward then right
        if is_in_bounds(x, y, facing, grid):

            if not is_obstacle(x, y, facing, grid):
                x, y = move(x, y, facing)
                moves += 1
                if loop_check is not None:
                    loop_check.add((x, y))

            else:
                facing = turn(facing)
                
        else:
            turnable = False

    return moves

def solver(input):
    grid = [list(line) for line in input.split()]
    x, y = find_agent(grid)
    facing = 0

    # positions which will be checked for looping
    loop_check = {(x, y)}

    perform_moves(grid, x, y, facing, float('inf'), loop_check)

    # check each suspision position for looping
    max_moves = 6000 # finded constant - should be cycle check
    res = 0

    for i, j in loop_check:

        grid[j][i] = '#'

        if (perform_moves(grid, x, y, facing, max_moves, None) == max_moves):
            res += 1

        grid[j][i] = '.'

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
