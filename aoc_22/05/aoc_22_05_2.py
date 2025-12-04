from pathlib import Path

# =============== SOLUTION PART =============== #

def parse_stacks(input):

    lines = input.split('\n')
    length = int(lines[-1].split()[-1])
    result = [[] for _ in range(length)]
    lines.pop() # end is now burden -> pop to nice for cycle

    for line in reversed(lines):
        for i in range(length):
            cargo =  line[1 + i*4]
            if cargo != ' ':
                result[i].append(cargo)

    return result


def solve(input):
    
    stacks, operations = input.split('\n\n')

    stacks = parse_stacks(stacks)
    operations = [[int(x) for x in list(filter(lambda x: x.isdigit(), x.split()))] for x in operations.split('\n')]

    for op in operations:
        ship = []
        for _ in range(op[0]):
            ship.append(stacks[op[1] - 1].pop())
        
        for cargo in reversed(ship):
            stacks[op[2] - 1].append(cargo)

    return ''.join(s[-1] for s in stacks)


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
