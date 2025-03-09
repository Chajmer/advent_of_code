from pathlib import Path

# =============== SOLUTION PART =============== #

DIRECTIONS = [(1, 1),(1, -1),(-1, -1),(-1, 1)]
LETTERS_COMBINATIONS = ["MSSM", "SSMM", "SMMS", "MMSS"]

def in_bounds(grid, i_line, check_x, check_y):
    return 0 <= check_x < len(grid) and 0 <= check_y < len(grid[i_line])

def solver(input):
    res = 0
    grid = input.split('\n')

    for i_line in range(len(grid)):
        for i_col in range(len(grid[i_line])):
    
            if grid[i_line][i_col] == 'A':

                # check 4 directions
                word = ""
                for x, y in DIRECTIONS:

                    grid_x, grid_y = i_line + x, i_col + y

                    if in_bounds(grid, i_line, grid_x, grid_y):
                        word += grid[grid_x][grid_y]

                if word in LETTERS_COMBINATIONS:
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
