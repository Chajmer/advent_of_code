from pathlib import Path

# =============== SOLUTION PART =============== #

def rec_lights(lights, wiring, i):
    
    if 0 == sum(lights):
        return 0
    if i >= len(wiring):
        return float('inf')
    
    # curr wire off
    res = rec_lights(lights, wiring, i + 1)

    # curr wire on
    for wire in wiring[i]:
        lights[wire] = not lights[wire]

    res = min(res, 1 + rec_lights(lights, wiring, i + 1))

    for wire in wiring[i]:
        lights[wire] = not lights[wire]

    return res


def solve(input):
    # parse
    lines = [
        [
            [c == '#' for c in l.split(']')[0][1:]],
            [[int(x) for x in y[1:-1].split(',')] for y in l.split(']')[1].split('{')[0].split()],
            [int(x) for x in l.split('{')[1][:-1].split(',')]
        ]
        for l in input.split('\n')
    ]

    # cycle lines
    result = 0

    for lights, wiring, _ in lines:
        result += rec_lights(lights, wiring, 0)

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
