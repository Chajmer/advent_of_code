from pathlib import Path

# =============== SOLUTION PART =============== #

def solve(input):
    result = 0
    dial = 50

    for line in input.split('\n'):
    
        num = int(line[1:])

        result += num // 100
        num %= 100

        if line[0] == 'L':
            dial -= num
        else:
            dial += num

        # last cond in brackets prevents couting left move when dial is 0 already
        if dial == 0 or dial > 99 or (dial < 0 and dial + num != 0):
            result += 1

        dial %= 100

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
