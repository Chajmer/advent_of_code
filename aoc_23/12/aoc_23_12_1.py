from pathlib import Path
from functools import cache

# =============== SOLUTION PART =============== #

@cache
def rec_counter(count, items, idx, springs, damaged_counts):
    if count == 1:
        # no '#' in operational area permitted
        return 1 if '#' not in springs[idx:] else 0

    # zero '.' on start
    res = rec_counter(count - 1, items, damaged_counts[0], springs, damaged_counts) if count == len(damaged_counts) + 1 and '.' not in springs[:damaged_counts[0]] else 0

    # chosen is taken so count-2 is left -> enough for each gap to have one '.'
    for chosen in range(1, items - count + 3):

        # no '#' in operational area permitted
        if springs[idx] == '#':
            break
        idx += 1

        # no '.' in damaged area permitted
        if '.' not in springs[idx: idx + damaged_counts[len(damaged_counts) - count + 1]]:
            res += rec_counter(count - 1, items - chosen, idx + damaged_counts[len(damaged_counts) - count + 1], springs, damaged_counts)

    return res


def count_arrangements(input):

    springs, counts = input.split(' ')
    counts = tuple(int(x) for x in counts.split(','))

    return rec_counter(len(counts) + 1, len(springs) - sum(counts), 0, springs, counts)


def solve(input):
    return sum(count_arrangements(line) for line in input.split('\n'))


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
