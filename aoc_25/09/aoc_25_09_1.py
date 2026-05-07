from pathlib import Path

# =============== SOLUTION PART =============== #

def solve(input):

    tiles = [(int(x), int(y)) for line in input.split('\n') for x, y in [line.split(',')]]

    result = 0
    for i in range(len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            result = max(result, (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1))    

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
