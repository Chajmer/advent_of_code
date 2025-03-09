from pathlib import Path

# =============== SOLUTION PART =============== #

def solver(input):
    res = 0
    state = 0 # automaton state

    for char in input:

        if state == 0 and char == 'm':
            X, Y = 0, 0
            state += 1

        elif (state == 1 and char == 'u') or (state == 2 and char == 'l') or \
             (state == 3 and char == '(') or (state == 4 and char == ','):
            state += 1

        elif state == 4 and char.isdigit():
            X = X * 10 + ord(char) - ord('0')

        elif state == 5 and char.isdigit():
            Y = Y * 10 + ord(char) - ord('0')

        elif state == 5 and char == ')':
            res += X * Y
            state = 0

        else:
            state = 0

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
    print(solver(read_input(input_file)))

print("Test done")
