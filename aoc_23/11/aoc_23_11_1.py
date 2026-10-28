from pathlib import Path

# =============== SOLUTION PART =============== #

def expand_universe(universe):

    # column
    for x in range(len(universe) - 1, -1, -1):
        if all(line[x] == '.' for line in universe):
            for line in universe:
                line.insert(x, '.')

    # line
    for y in range(len(universe) - 1, -1, -1):
        if '#' not in universe[y]:
            universe.insert(y, universe[y].copy())

    return universe


def solve(input):

    universe = [list(line) for line in input.split('\n')]
    expand_universe(universe)

    galaxies = [(int(x), int(y)) for y in range(len(universe)) for x in range(len(universe[y])) if universe[y][x] == '#']
    result = 0

    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            result += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

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
