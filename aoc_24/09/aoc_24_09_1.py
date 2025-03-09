from pathlib import Path
from math import ceil

# =============== SOLUTION PART =============== #

def solver(input):
    disks = []
    # Parse the input to create the disks list
    for i in range(ceil(len(input) / 2)):
        count = int(input[i * 2])
        disks.extend([i] * count)
        if i * 2 + 1 < len(input):
            empty_count = int(input[i * 2 + 1])
            disks.extend(['.'] * empty_count)

    # Move all '.' to the end of the list
    left, right = 0, len(disks) - 1
    while left < right:
        if disks[left] != '.':
            left += 1
        elif disks[right] == '.':
            right -= 1
        else:
            disks[left], disks[right] = disks[right], disks[left]
            left += 1
            right -= 1

    # Calculate the result
    result = 0
    for i, disk in enumerate(disks):
        if disk == '.':
            break
        result += disk * i

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
    print(solver(read_input(input_file)))

print("Test done")
