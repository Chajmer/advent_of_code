from pathlib import Path

# =============== SOLUTION PART =============== #

def solver(input):
    left = []
    right = []
    for line in input.split('\n'):
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    right_counter = {}
    for num in right:
        right_counter[num] = right_counter.get(num, 0) + 1

    res = 0
    for num in left:
        res += num * right_counter.get(num, 0)
    return res


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
