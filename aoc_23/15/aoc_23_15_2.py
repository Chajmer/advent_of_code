from pathlib import Path

# =============== SOLUTION PART =============== #

def get_hash(string):
    res = 0

    for c in string:
        res = ((res + ord(c)) * 17) % 256

    return res


def solve(input):
    hash_map = [[] for _ in range(256)]

    for string in input.split(','):
        string, focal_len = (string[:-1], 0) if string[-1] == '-' else string.split('=')
        hash = get_hash(string)

        i = 0

        while i < len(hash_map[hash]):
            if hash_map[hash][i][0] == string:
                break
            i += 1

        if i < len(hash_map[hash]):
            if focal_len == 0:
                del hash_map[hash][i]
            else:
                hash_map[hash][i][1] = int(focal_len)
        elif focal_len != 0:
            hash_map[hash].append([string, int(focal_len)])

    result = 0

    for i in range(len(hash_map)):
        for j in range(len(hash_map[i])):
            result += (i + 1) * (j + 1) * hash_map[i][j][1]

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
