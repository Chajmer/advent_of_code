from pathlib import Path

# =============== SOLUTION PART =============== #

DIRECTIONS = [(0, 1),(0, -1),(1, 0),(-1, 0),
              (1, 1),(1, -1),(-1, 1),(-1, -1)]
LETTERS = "XMAS"

def in_bounds(grid, i_line, check_x, check_y):
    return 0 <= check_x < len(grid) and 0 <= check_y < len(grid[i_line])

def solver(input):
    res = 0
    grid = input.split('\n')

    for i_line in range(len(grid)):
        for i_col in range(len(grid[i_line])):

            if grid[i_line][i_col] == 'X':

                # check 8 directions
                for x, y in DIRECTIONS:
                    rl_state = 0 # regular language automaton state

                    for j in range(1, len(LETTERS)):

                        grid_x, grid_y = i_line + x * j, i_col + y * j
    
                        if in_bounds(grid, i_line, grid_x, grid_y) and grid[grid_x][grid_y] == LETTERS[j]:
                            rl_state += 1

                    if rl_state == 3:
                        res += 1

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
