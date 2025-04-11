from pathlib import Path
from math import sqrt, ceil, floor

# =============== SOLUTION PART =============== #

def solve(input: str) -> int:
    info = [x.split(':')[1].split() for x in input.split('\n')]
    time, distance = [int("".join(x)) for x in info]
    D = sqrt(time**2 - 4 * distance)
    # +-0.0001 to avoid floating point errors
    return floor((time + D) / 2 - 0.0001)\
            - ceil((time - D) / 2 + 0.0001) + 1 # +1 to count start itself


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
