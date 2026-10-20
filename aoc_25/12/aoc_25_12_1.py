from pathlib import Path

# =============== SOLUTION PART =============== #

def solve(input):
    input = input.split('\n\n')
    patterns = input[:-1]
    puzzles = [
        ([int(x) for x in grid.split('x')], [int(x) for x in counts.split(' ')])
        for line in input[-1].split('\n')
        for grid, counts in [line.split(': ')]
    ]
    result = 0

    for grid, counts in puzzles:
        if (grid[0] // 3) * (grid[1] // 3) + 2 >= sum(counts):
            result += 1

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
