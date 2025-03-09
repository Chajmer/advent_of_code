from pathlib import Path

# =============== SOLUTION PART =============== #

def check(line):
    report = [int(x) for x in line.split()]
    if report[0] > report[-1]:
        report = report[::-1]

    prev = report[0]
    for i in range(1, len(report)):
        if prev > report[i] or not (0 < abs(prev - report[i]) < 4):
            return False
        prev = report[i]
    return True

def solver(input):
    res = 0
    for line in input.split('\n'):
        if check(line):
            res += 1
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
