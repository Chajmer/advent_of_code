from pathlib import Path

# =============== SOLUTION PART =============== #

def solver(input):
    ordering, orders = input.split('\n\n')
    ordering = [[(int(y)) for y in x.split('|')] for x in ordering.split()]
    orders = [[int(y) for y in x.split(',')] for x in orders.split()]

    res = 0
    rules = {}

    for rule in ordering:
        rules[rule[0]] = [True]

    for rule in ordering:
        rules[rule[0]].append(rule[1])

    for order in orders:
        valid_order = True

        for i in range(len(order) - 1):
            for j in range(i + 1, len (order)):

                if order[i] not in rules.keys() or order[j] not in rules[order[i]]:
                    valid_order = False
                    break

            if not valid_order:
                break
    
        if valid_order:
            res += order[len(order) // 2]

    return res
from pathlib import Path


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
