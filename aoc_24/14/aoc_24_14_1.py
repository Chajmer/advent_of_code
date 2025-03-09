from pathlib import Path

# =============== SOLUTION PART =============== #

DIMENSIONS = [(11, 7), (101, 103)]

def solver(input, input_num):
    dimension = DIMENSIONS[input_num - 1]
    quadrants = [0, 0, 0, 0]

    for line in input.split('\n'):
        line = [[int(n) for n in c.split('=')[1].split(',')] for c in line.split()]
        x, y = [(line[0][i] + 100 * line[1][i]) % dimension[i] for i in range(2)]

        # dimension params are odd - seems like that - lets use that
        if x != dimension[0] // 2 and y != dimension[1] // 2:
            quadrants[(2 if y > dimension[1] // 2 else 0) + (1 if x > dimension[0] // 2 else 0)] += 1

    result = 1
    for q in quadrants:
        result *= q

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
    print(solver(read_input(input_file), int(input_file.stem.split('_')[-1])))

print("Test done")
