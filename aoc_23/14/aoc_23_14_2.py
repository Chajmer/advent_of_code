from pathlib import Path

# =============== SOLUTION PART =============== #

def tilt_up(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 'O':
                continue

            grid[i][j] = '.'
            up = i

            while up > 0 and grid[up - 1][j] == '.':
                up -= 1

            grid[up][j] = 'O'


def spin_cycle(grid):

    grid = [list(x) for x in grid]

    for _ in range(4):
        tilt_up(grid)
        grid = [list(x) for x in zip(*reversed(grid))]

    return tuple(''.join(x) for x in grid)


def get_load(grid):
    res = 0

    for i in range(len(grid)):
        for c in grid[i]:
            if c == 'O':
                res += len(grid) - i

    return res


def solve(input):

    grid = tuple(input.split('\n'))

    cycles = 1000000000
    i = 0
    seen = {}

    while i < cycles:
        if grid in seen:
            i = cycles - (cycles - i) % (i - seen[grid])
            seen.clear()
            continue

        seen[grid] = i
        grid = spin_cycle(grid)
        i += 1

    return get_load(grid)


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
