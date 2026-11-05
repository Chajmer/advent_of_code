from pathlib import Path

# =============== SOLUTION PART =============== #

def horizontal_score(pattern):

    for i in range(1, len(pattern)):
        mirror = True

        for j in range(min(i, len(pattern) - i)):
            if pattern[i - 1 - j] != pattern[i + j]:
                mirror = False
                break

        if mirror:
            return i

    return 0


def vertical_score(pattern):

    for i in range(1, len(pattern[0])):
        mirror = True

        for j in range(min(i, len(pattern[0]) - i)):

            for k in range(len(pattern)):
                if pattern[k][i - 1 - j] != pattern[k][i + j]:
                    mirror = False
                    break

            if not mirror:
                break

        if mirror:
            return i

    return 0


def solve(input):

    res = 0

    for pattern in input.split('\n\n'):
        pattern = pattern.split('\n')
        res += 100 * horizontal_score(pattern) + vertical_score(pattern)

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
    print(solve(read_input(input_file)))

print("Test done")
