from pathlib import Path
import numpy as np

# =============== SOLUTION PART =============== #

def mix_prune(n, m):
    return (n ^ m) % 16777216


def next_secret(n):
    n = mix_prune(n, n * 64)
    n = mix_prune(n , int(n / 32))
    return mix_prune(n, n * 2048)


def n_secret(cycles, n):

    dp = np.full((19, 19, 19, 19), -1, dtype=np.int8)
    changes = [-1, -1, -1, -1] # already shifted +9 to better indexing

    for _ in range(cycles):
        prev = n % 10
        n = next_secret(n)

        changes[:4] = changes[1:4] + [n % 10 - prev + 9] # +9 to get first index to 0

        if changes[0] != -1 and dp[changes[0], changes[1], changes[2], changes[3]] == -1:
            dp[changes[0], changes[1], changes[2], changes[3]] = n % 10

    return dp


def choose_generator(count, items):
    if count == 1:
        for item in items:
            yield [item]
        return
    
    for chosen in items:
        for child in choose_generator(count - 1, items):
            yield [chosen] + child


def solver(input):
    dps = [n_secret(2000, int(n)) for n in input.split('\n')]
    res = 0

    for a, b, c, d in choose_generator(4, set(range(0, 19))):
        res = max(res, sum(int(dp[a, b, c, d]) for dp in dps if dp[a, b, c, d] != -1))

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
