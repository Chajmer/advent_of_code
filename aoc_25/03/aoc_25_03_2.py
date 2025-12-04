from pathlib import Path

# =============== SOLUTION PART =============== #

def biggest_num_inside(arr, start, length):
    if length == 1:
        return max(arr[start:])

    first = max(arr[start:-length + 1])

    i = start
    while arr[i] != first:
        i += 1
    
    return first * 10**(length - 1) + biggest_num_inside(arr, i + 1, length - 1)


def solve(input):
    result = 0

    for line in input.split():
        result += biggest_num_inside([int(x) for x in list(line)], 0, 12)

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
