from pathlib import Path

# =============== SOLUTION PART =============== #

def tilt_north(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 'O':
                continue

            grid[i][j] = '.'
            north = i

            while north > 0 and grid[north - 1][j] == '.':
                north -= 1

            grid[north][j] = 'O'


def get_load(grid):
    res = 0

    for i in range(len(grid)):
        for c in grid[i]:
            if c == 'O':
                res += len(grid) - i

    return res


def solve(input):

    grid = [list(x) for x in input.split('\n')]

    tilt_north(grid)

    return get_load(grid)


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
