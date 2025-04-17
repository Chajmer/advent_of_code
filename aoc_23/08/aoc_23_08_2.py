from pathlib import Path
from math import gcd

# =============== SOLUTION PART =============== #

def lcm(a, b): # least common multiple
    return abs(a*b) // gcd(a, b)

def solve(input):
    # make node map
    literal, map_info = input.split('\n\n')
    map_nodes = {}
    for line in map_info.split('\n'):
        key, val_info = line.split(' = ')
        left, right = val_info.split(', ')
        map_nodes[key] = (left[1::], right[:-1:])
    # for cycle endings 'A' and for each:
    # while not final node found iterate through instructions
    steps_arr = []
    for current in map_nodes.keys():
        if (current[2] != 'A'):
            continue
        steps = 0
        end_flag = False
        while not end_flag:
            for dir in literal:
                steps += 1
                current = map_nodes[current][0] if dir == 'L'\
                    else map_nodes[current][1]
                if (current[2] == 'Z'):
                    steps_arr.append(steps)
                    end_flag = True
                    break
    # calculate lcm of all step counts
    res = steps_arr[0]
    for steps in steps_arr:
        res = lcm(res, steps)
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
