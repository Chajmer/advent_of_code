from pathlib import Path

# =============== SOLUTION PART =============== #

def solver(input):
    nums = [int(x) for x in input.split()]

    for _ in range(25):
        next_nums = []

        for n in nums:
            if n == 0:
                next_nums.append(1)
            elif len(str(n)) % 2 == 0:
                half_len = len(str(n)) // 2
                next_nums.append(int(str(n)[:half_len]))
                next_nums.append(int(str(n)[half_len:]))
            else:
                next_nums.append(n * 2024)
        nums = next_nums

    return len(nums)


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
