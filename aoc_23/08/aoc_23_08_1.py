from pathlib import Path

# =============== SOLUTION PART =============== #

def solve(input):
    # make map
    literal, map_info = input.split('\n\n')
    map_nodes = {}
    for line in map_info.split('\n'):
        key, val_info = line.split(' = ')
        left, right = val_info.split(', ')
        map_nodes[key] = (left[1::], right[:-1:])
    # while not found iterate through instructions
    steps = 0
    current = 'AAA'
    while current != 'ZZZ':
        for c in literal:
            steps += 1
            current = map_nodes[current][0] if c == 'L'\
                else map_nodes[current][1]
    return steps


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
    if (input_file.stem[6:] == '4'):
        continue
    print(f"Input {input_file.stem[6:]}:")
    print(solve(read_input(input_file)))

print("Test done")
