from pathlib import Path

# =============== SOLUTION PART =============== #

def parse_structure(structure):

    res = [0] * len(structure)

    for i in range(len(structure[0])):
        for j in range(len(structure)):
            res[i] += 1 if structure[j][i] == '#' else 0

    return res

def parse_input(input):

    keys, locks = [], []

    for structure in input.split('\n\n'):
        (keys if structure[0][0] == '.' else locks).append(parse_structure(structure.split('\n')[1:-1]))

    return keys, locks


def is_insertable(key, lock):

    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False

    return True


def solver(input):

    keys, locks = parse_input(input)

    return sum(is_insertable(key, lock) for key in keys for lock in locks)


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
