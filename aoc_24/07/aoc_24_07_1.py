from pathlib import Path

# =============== SOLUTION PART =============== #

def is_solvable(test_val, nums, cur_num):
    if not nums:
        return test_val == cur_num
    if test_val < cur_num:
        return False
    # recursion call with 2 different operations
    return is_solvable(test_val, nums[1:], cur_num + nums[0]) or\
           is_solvable(test_val, nums[1:], cur_num * nums[0])

def solver(input):
    res = 0
    
    for line in input.split('\n'):
        line_split = line.split(': ')
        test_val, nums = int(line_split[0]), [int(x) for x in line_split[1].split()]

        if is_solvable(test_val, nums[1:], nums[0]):
            res += test_val

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
