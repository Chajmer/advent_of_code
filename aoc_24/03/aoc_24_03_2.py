from pathlib import Path

# =============== SOLUTION PART =============== #

# fast version of the state machine
def mul_state_machine(mul_mode, char, on_mul_state, off_mul_state):

    if on_mul_state == 0 and char == 'd':
        return mul_mode, on_mul_state + 1, 0

    if (on_mul_state == 1 and char == 'o') or (on_mul_state == 2 and off_mul_state == 0 and char == '('):
        return mul_mode, on_mul_state + 1, off_mul_state

    if on_mul_state == 2 and off_mul_state == 0 and char == 'n':
        return mul_mode, on_mul_state, off_mul_state + 1

    if on_mul_state == 3 and off_mul_state == 0:
        return True, 0, off_mul_state

    if (char == "'" and off_mul_state == 1) or (char == 't' and off_mul_state == 2) or \
        (char == '(' and off_mul_state == 3):
        return mul_mode, on_mul_state, off_mul_state + 1

    return False if (off_mul_state == 4 and char == ')') else mul_mode, 0, 0

def solver(input):
    res = 0
    operation_state = 0 # automaton state
    mul_mode = True
    # these both are automaton states for enabling and disabling the mul_mode
    on_mul_state = 0
    off_mul_state = 0

    for char in input:

        if operation_state == 0:
            X, Y = 0, 0
            if char == 'm':
                operation_state += 1
                on_mul_state, off_mul_state = 0, 0
            else:
                mul_mode, on_mul_state, off_mul_state = mul_state_machine(mul_mode, char, on_mul_state, off_mul_state)

        elif (operation_state == 1 and char == 'u') or (operation_state == 2 and char == 'l') or \
             (operation_state == 3 and char == '(') or (operation_state == 4 and char == ','):
            operation_state += 1

        elif operation_state == 4 and char.isdigit():
            X = X * 10 + ord(char) - ord('0')

        elif operation_state == 5 and char.isdigit():
            Y = Y * 10 + ord(char) - ord('0')

        elif operation_state == 5 and char == ')' and mul_mode:
            res += X * Y
            operation_state = 0

        else:
            operation_state = 0

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
