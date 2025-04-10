from pathlib import Path

# =============== SOLUTION PART =============== #

def mapper_solve(seed, maps):
    for map in maps:
        for elem in map:
            if elem[1] <= seed < elem[1] + elem[2]:
                seed += elem[0] - elem[1]
                break
    return seed

def solve(almanac: str) -> int:
    # parse
    initsplit = almanac.split('\n\n')
    seeds = [int(x) for x in initsplit[0].split(':')[1].split()]
    maps = []
    for x in initsplit[1:]:
        maps.append([[int(z) for z in y.split()]
                     for y in x.split(':')[1].split('\n')[1:]])
    # solve
    result = float('inf')
    for seed in seeds:
        result = min(result, mapper_solve(seed, maps))
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
