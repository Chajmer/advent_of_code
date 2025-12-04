from pathlib import Path

# =============== SOLUTION PART =============== #

def is_valid(num):
    num = str(num)
    l = len(num)

    for d in range(2, l + 1):
        if l % d != 0:
            continue

        valid_status = False
        prev_seg = num[:int(l/d)] 
        for i in range(d - 1):
            cur_seg = num[(i + 1) * int(l/d):(i + 2) * int(l/d)]
            
            if prev_seg != cur_seg:
                valid_status = True
                break
            prev_seg = cur_seg

        if not valid_status:
            return False
    
    return True


def solve(input):
    result = 0

    for seq in input.split(','):
        start, end = [int(x) for x in seq.split('-')]

        for n in range(start, end + 1):
            if not is_valid(n):
                result += n

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
