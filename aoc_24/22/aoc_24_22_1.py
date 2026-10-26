from pathlib import Path

# =============== SOLUTION PART =============== #

def mix_prune(n, m):
    return (n ^ m) % 16777216


def next_secret(n):
    n = mix_prune(n, n * 64)
    n = mix_prune(n , int(n / 32))
    return mix_prune(n, n * 2048)


def n_secret(cycles, n):

    for _ in range(cycles):
        n = next_secret(n)

    return n


def solver(input):
    return sum(n_secret(2000, int(n)) for n in input.split('\n'))


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
