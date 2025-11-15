from pathlib import Path

# =============== SOLUTION PART =============== #

def solve(input):

    rounds = [(ord(x) - ord('A'), ord(y) - ord('X')) for x, y in map(str.split, input.split('\n'))]
    result = 0

    for opponent, me in rounds:
        result += (me - opponent + 1) % 3 * 3 + 1 + me # win_state + base + symbol
        
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
