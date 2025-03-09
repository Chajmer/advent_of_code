from pathlib import Path
from math import floor

# =============== SOLUTION PART =============== #

def split_line(line, sep):
    return map(int, [x.split(sep)[1] for x in line.split(': ')[1].split(', ')])

def solver(input):
    result = 0
    for block in input.split('\n\n'):
        lines = block.split('\n')
        a1, b1 = split_line(lines[0], '+')
        a2, b2 = split_line(lines[1], '+')
        x, y = split_line(lines[2], '=')

        det = a1 * b2 - a2 * b1
        if det == 0:
            continue

        t = (b2 * x - a2 * y) / det
        s = (a1 * y - b1 * x) / det

        if 0 <= t <= 100 and 0 <= s <= 100 and t.is_integer() and s.is_integer():
            result += 3 * t + s

    return floor(result)


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
