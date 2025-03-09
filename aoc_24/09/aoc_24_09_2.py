from pathlib import Path
from math import ceil

# =============== SOLUTION PART =============== #

def solver(input):
    disks = []
    counts = {}

    # Parse input and populate disks and counts
    for i in range(ceil(len(input) / 2)):
        count = int(input[i * 2])
        counts[i] = count
        disks.extend([i] * count)
        if i * 2 + 1 < len(input):
            disks.extend(['.'] * int(input[i * 2 + 1]))

    right = len(disks) - 1

    # Rearrange disks
    for disk_type in range(max(counts.keys()), 1, -1):
        left = 0
        while left < right:
            if disks[left] != '.':
                left += 1
                continue
            if disks[right] != disk_type:
                right -= 1
                continue

            next_non_dot = left
            while disks[next_non_dot] == '.':
                next_non_dot += 1

            if counts[disk_type] > next_non_dot - left:
                left = next_non_dot + 1
                continue

            for _ in range(counts[disk_type]):
                disks[left], disks[right] = disks[right], disks[left]
                right -= 1
                left += 1
            break

    # Calculate result
    result = sum(disk * index for index, disk in enumerate(disks) if disk != '.')
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
