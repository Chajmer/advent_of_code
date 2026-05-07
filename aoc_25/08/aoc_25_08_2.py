from pathlib import Path
from math import sqrt

# =============== SOLUTION PART =============== #

def point_distance(point_1, point_2):
    return sqrt(sum((point_1[i] - point_2[i])**2 for i in range(len(point_1))))


def solve(input):

    boxes = [{(int(x), int(y), int(z))} for line in input.split('\n') for x, y, z in [line.split(',')]]

    # make all pairs and sort
    sorted_pairs = []
    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            sorted_pairs.append((next(iter(boxes[i])), next(iter(boxes[j]))))
    sorted_pairs.sort(key=lambda x: point_distance(x[0], x[1]))

    # connect boxes
    for i in range(len(sorted_pairs)):

        point_1, point_2 = sorted_pairs[i]
        set_i_1, set_i_2 = None, None

        for j in range(len(boxes)):
        
            if point_1 in boxes[j]:
                set_i_1 = j
            if point_2 in boxes[j]:
                set_i_2 = j

            if set_i_1 and set_i_2:
                break

        if set_i_1 != set_i_2:
            low, high = min(set_i_1, set_i_2), max(set_i_1, set_i_2)                                           
            boxes[low] |= boxes[high]
            boxes[high] = set()

            # check if is one large circuit already
            if len(boxes[0]) == len(boxes):
                return point_1[0] * point_2[0]

    return -1


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
