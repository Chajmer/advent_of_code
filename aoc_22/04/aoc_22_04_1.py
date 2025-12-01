from pathlib import Path

# =============== SOLUTION PART =============== #

def is_in_interval(i1, i2):
    return i1[0] >= i2[0] and i1[1] <= i2[1]

def solve(input):

    result = 0

    for line in input.split('\n'):
        
        i1, i2 = ([int(s) for s in (x.split('-'))] for x in line.split(','))
        
        if is_in_interval(i1, i2) or is_in_interval(i2, i1):
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
