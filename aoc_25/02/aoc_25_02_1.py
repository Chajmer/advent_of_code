from pathlib import Path

# =============== SOLUTION PART =============== #

def is_valid(num):
    num = str(num)
    l = len(num)
    return num[:int(l/2)] != num[int(l/2):] if l % 2 == 0 else True


def solve(input):
    result = 0

    for seq in input.split(','):
        start, end = [int(x) for x in seq.split('-')]

        for n in range(start, end + 1):
            if not is_valid(n):
                result += n

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
