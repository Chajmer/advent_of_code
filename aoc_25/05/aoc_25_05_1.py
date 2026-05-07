from pathlib import Path

# =============== SOLUTION PART =============== #

def parse_ranges(ranges):
    return [range(int(start), int(end) + 1) for start, end in (x.split('-') for x in ranges.split())]


def parse_input(input):
    blocks = input.split('\n\n')
    return (parse_ranges(blocks[0]), [int(x) for x in blocks[1].split('\n')])


def is_fresh(id, fresh_ranges):
    for fresh_range in fresh_ranges:
        if id in fresh_range:
            return True
    return False


def solve(input):
    fresh_ranges, ingredients = parse_input(input)

    result = 0
    for id in ingredients:
        if is_fresh(id, fresh_ranges):
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
