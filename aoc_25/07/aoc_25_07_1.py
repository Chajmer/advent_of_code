from pathlib import Path

# =============== SOLUTION PART =============== #

def solve(input):
    grid = [list(x) for x in input.split('\n')]
    width, height = len(grid[0]), len(grid)

    # change start to beam already
    for i in range(width):
        if grid[0][i] == 'S':
            grid[0][i] = '|'
            break

    result = 0

    for i in range(1, height):
        for j in range(width):
            
            if grid[i][j] == '^' and grid[i - 1][j] == '|':
                grid[i][j - 1], grid[i][j + 1] = '|', '|'
                result += 1

            elif grid[i - 1][j] == '|':
                grid[i][j] = '|'

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
