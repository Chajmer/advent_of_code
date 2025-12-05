from pathlib import Path

# =============== SOLUTION PART =============== #

def parse_ranges(ranges):
    return [range(int(start), int(end) + 1) for start, end in (x.split('-') for x in ranges.split())]


def parse_input(input):
    return parse_ranges(input.split('\n\n')[0])


def solve(input):
    fresh_ranges = parse_input(input)
    fresh_ranges.sort(key=lambda x: x.start)

    result = 0
    curr = fresh_ranges[0].start

    for r in fresh_ranges:
        if r.stop > curr:
            result += r.stop - max(r.start, curr)
            curr = r.stop

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
