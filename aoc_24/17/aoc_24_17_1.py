from pathlib import Path
from math import floor

# =============== SOLUTION PART =============== #

def solver(input):
    result = []
    blocks = input.split('\n\n')
    # registers
    A, B, C = [int(line.split()[2]) for line in blocks[0].split('\n')]
    program = [int(x) for x in blocks[1].split()[1].split(',')]

    # Internal custom operations:

    # operand
    def op():
        return program[pointer + 1]
    
    # combo operand
    def combo_op_val(op):
        return [A, B, C][op - 4] if 3 < op < 7 else op

    def div():
        return floor(A / (2**combo_op_val(op())))

    def mod():
        return combo_op_val(op()) % 8

    # main process
    pointer = 0
    while pointer < len(program):
        match program[pointer]:
            case 0: # adv [operation]
                A = div()
            case 1: # bxl
                B ^= op()
            case 2: # bst
                B = mod()
            case 3: # jnz
                if A != 0:
                    pointer = op()
                    continue
            case 4: # bxc
                B ^= C
            case 5: # out
                result.append(mod())
            case 6: # bdv
                B = div()
            case 7: # cdv
                C = div()
        pointer += 2

    return ','.join([str(x) for x in result])


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
