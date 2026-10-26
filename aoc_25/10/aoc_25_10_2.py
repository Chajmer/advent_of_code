from pathlib import Path
from fractions import Fraction

# =============== SOLUTION PART =============== #

def calculate_vars(matrix, free_map):
    res = 0
    line = 0

    for col in range(len(matrix[0]) - 1):
        if line < len(matrix) and matrix[line][col]:

            # calculate var on line
            cur = matrix[line][-1]

            for i in range(col + 1, len(matrix[0]) - 1):
                cur -= matrix[line][i] * Fraction(free_map[i])

            if cur.denominator != 1 or cur < 0:
                return float('inf')
            
            res += cur
            line += 1

    return res


def rec_joltage(matrix, wiring, joltages, frees, presses):

    # calculate end of recursion
    if len(frees) == len(presses):
        free_map = [0] * len(wiring)

        for i in range(len(frees)):
            free_map[frees[i]] = presses[i]
            
        return calculate_vars(matrix, free_map)

    # recursion deeper
    wi = frees[len(presses)]
    limit = min(joltages[w] for w in wiring[wi])
    res = float('inf')

    for round in range(limit + 1):
        presses.append(round)
        res = min(res, round + rec_joltage(matrix, wiring, joltages, frees, presses))
        presses.pop()

        for i in wiring[wi]:
            joltages[i] -= 1

    for i in wiring[wi]:
        joltages[i] += limit + 1

    return res


def equations(wiring, joltages):
    matrix = [[Fraction(0)] * len(wiring) for _ in range(len(joltages))]

    for i in range(len(wiring)):
        for w in wiring[i]:
            matrix[w][i] = Fraction(1)
    for i in range(len(joltages)):
        matrix[i].append(Fraction(joltages[i]))
        
    return matrix


def gauss_elimination(matrix):
    missed = 0

    for col in range(len(matrix[0]) - 1):

        # find 1 (or other?) on diagonal-th column under pyramid build process
        cur = col - missed
        for i in range(cur, len(matrix)):
            if matrix[i][col] != 0:
                if cur != i:
                    matrix[cur], matrix[i] = matrix[i], matrix[cur]
                break
        else:
            missed += 1
            continue

        # pivot set to 1
        if matrix[cur][col] != 1:
            for i in range(col + 1, len(matrix[0])):
                matrix[cur][i] /= matrix[cur][col]
            matrix[cur][col] = Fraction(1)

        # make every other line zero -> down and up
        for line in range(len(matrix)):
            if line == cur:
                continue
            factor = matrix[line][col]
            for i in range(col, len(matrix[0])):
                matrix[line][i] -= matrix[cur][i] * factor

        # break if we have enough already
        if cur + 1 == len(matrix[0]) - 1:
            break


def get_frees(matrix):
    frees = []
    line = 0

    for col in range(len(matrix[0]) - 1):
        if line < len(matrix) and matrix[line][col] != 0:
            line += 1
        else:
            frees.append(col)

    return frees


def configure_joltage(wiring, joltages):

    matrix = equations(wiring, joltages)

    gauss_elimination(matrix)

    # brute force free ones without pivot
    return rec_joltage(matrix, wiring, joltages, get_frees(matrix), [])


def solve(input):
    # parse
    lines = [
        [
            [[int(x) for x in y[1:-1].split(',')] for y in l.split(']')[1].split('{')[0].split()],
            [int(x) for x in l.split('{')[1][:-1].split(',')]
        ]
        for l in input.split('\n')
    ]
    # process lines
    result = 0

    for wiring, joltages in lines:
        result += configure_joltage(wiring, joltages)

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
