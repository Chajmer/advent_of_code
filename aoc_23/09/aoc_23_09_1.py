from pathlib import Path

# =============== SOLUTION PART =============== #

def extrapolate(nums):
    res = 0
    while any(n != 0 for n in nums):
        # result is sum of last elems of each sequence
        res += nums[-1]
        # next sequence
        nums = [nums[x] - nums[x - 1] for x in range(1, len(nums))]
    return res

def solve(input):
    res = 0
    for line in input.split('\n'):
        res += extrapolate([int(x) for x in line.split()])
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
    print(solve(read_input(input_file)))

print("Test done")
