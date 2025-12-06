from pathlib import Path

# =============== SOLUTION PART =============== #

def solve(input):
    lines = [x.split() for x in input.split('\n')]

    result = 0
    
    for i in range(len(lines[0])):
        to_add = 1 if (lines[-1][i] == '*') else 0

        for j in range(len(lines) - 1):
            if lines[-1][i] == '*':
                to_add *= int(lines[j][i])
            else:
                to_add += int(lines[j][i])

        result += to_add

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
