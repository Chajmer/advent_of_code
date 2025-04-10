from pathlib import Path

# =============== SOLUTION PART =============== #

def mapper_solve(seed_ranges, maps):
    for map in maps:
        new = []
        while seed_ranges:
            x, y = seed_ranges.pop()
            for elem in map:
                a, b = elem[1], elem[1] + elem[2]
                if y > max(a, x) and x < min(b, y):
                    new.append((max(a, x) + elem[0] - a, min(b, y) + elem[0] - a))
                    if x < a:
                        seed_ranges.append((x, a))
                    if b < y:
                        seed_ranges.append((b, y))
                    break
            else:
                new.append((x, y))
        seed_ranges = new
    return min(seed_ranges)[0]

def solve(almanac: str) -> int:
    # parse
    initsplit = almanac.split('\n\n')
    seeds_init = [int(x) for x in initsplit[0].split(':')[1].split()]
    seed_ranges = []
    for i in range(0, len(seeds_init)//2 + 1, 2):
        seed_ranges.append((seeds_init[i], seeds_init[i] + seeds_init[i + 1]))
    maps = []
    for x in initsplit[1:]:
        maps.append([[int(z) for z in y.split()]
                     for y in x.split(':')[1].split('\n')[1:]])
    # solve & return
    return mapper_solve(seed_ranges, maps)


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
