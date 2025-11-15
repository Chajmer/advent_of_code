from pathlib import Path

# =============== SOLUTION PART =============== #

def is_char_in_all(c, arr):
    return all(c in s for s in arr)


def find_same(arr):
    # big alphabet
    for c in (chr(i) for i in range(ord('A'), ord('Z')+1)):
        if is_char_in_all(c, arr):
            return c

    # small alphabet
    for c in (chr(i) for i in range(ord('a'), ord('z')+1)):
        if is_char_in_all(c, arr):
            return c


def map_badge(badge):
    if badge.islower():
        return ord(badge) - ord('a') + 1      # a=1 … z=26
    else:
        return ord(badge) - ord('A') + 27     # A=27 … Z=52


def solve(input):
    lines = input.split('\n')
    result = 0
    
    for line in lines:
        half = len(line) // 2
        result += map_badge(find_same([line[:half], line[half:]]))

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
