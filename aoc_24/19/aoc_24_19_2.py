from pathlib import Path

# =============== SOLUTION PART =============== #

def is_madeable(design, idx, patterns, precounted):
    # on the end
    if idx == len(design):
        return 1

    # was already solved in backtracking
    if (design, idx) in precounted.keys():
        return precounted[(design, idx)]
    
    count = 0
    for pattern in patterns:
        if len(pattern) <= len(design) - idx and pattern == design[idx:idx+len(pattern)]:
            count += is_madeable(design, idx + len(pattern), patterns, precounted)

    precounted[(design, idx)] = count
    return count

def solver(input):
    header, designs = input.split("\n\n")
    patterns = header.split(", ")

    result = 0
    precounted = dict()
    for design in designs.split():
        result += is_madeable(design, 0, patterns, precounted)
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
