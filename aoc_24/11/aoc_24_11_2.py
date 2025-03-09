from pathlib import Path
from collections import Counter

# =============== SOLUTION PART =============== #

def solver(input):
    nums = Counter(map(int, input.split()))

    for _ in range(75):
        next_nums = {}
    
        for n, count in nums.items():
            if count == 0:
                continue
            if n == 0:
                next_nums[1] = next_nums.get(1, 0) + count
            elif len(str(n)) % 2 == 0:
                half_len = len(str(n)) // 2
                first_half = int(str(n)[:half_len])
                second_half = int(str(n)[half_len:])
                next_nums[first_half] = next_nums.get(first_half, 0) + count
                next_nums[second_half] = next_nums.get(second_half, 0) + count
            else:
                next_nums[n * 2024] = next_nums.get(n * 2024, 0) + count
        nums = next_nums

    return sum(nums.values())


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
