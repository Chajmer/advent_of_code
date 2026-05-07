from pathlib import Path
from collections import defaultdict
import bisect

# =============== SOLUTION PART =============== #

def sgn(x):
    return 1 if x > 0 else (-1 if x < 0 else 0)


def rectangle_size(tile_1, tile_2):
    return (abs(tile_1[0] - tile_2[0]) + 1) * (abs(tile_1[1] - tile_2[1]) + 1)


 # add all between 2 tiles to edges
def add_to_edges(edges, tile_1, tile_2):
    if tile_1[0] == tile_2[0]:
        for y in range(min(tile_1[1], tile_2[1]), max(tile_1[1], tile_2[1]) + 1):
            edges.add((tile_1[0], y))

    if tile_1[1] == tile_2[1]:
        for x in range(min(tile_1[0], tile_2[0]), max(tile_1[0], tile_2[0]) + 1):
            edges.add((x, tile_1[1]))


def has_between(arr, lo, hi):
    i = bisect.bisect_left(arr, lo)
    return i < len(arr) and arr[i] <= hi


# test if rectangle defined by 2 tiles is inside edges
def is_inside_edges(tile_1, tile_2, edges_by_x, edges_by_y):
    dx, dy = sgn(tile_2[0] - tile_1[0]), sgn(tile_2[1] - tile_1[1])

    if dx == 0 or dy == 0:
        return True
    
    x_1, x_2, y_1, y_2 = tile_1[0] + dx, tile_2[0] - dx, tile_1[1] + dy, tile_2[1] - dy

    # adjust for 1 type off position control
    if x_1 > x_2:
        x_1, x_2 = x_2, x_1
    if y_1 > y_2:
        y_1, y_2 = y_2, y_1
    
    # vertical check
    # check line from [x_1, y_1] to [x_1, y_2]
    if has_between(edges_by_x[x_1], y_1, y_2):
        return False
    
    # check line from [x_2, y_1] to [x_2, y_2]
    if has_between(edges_by_x[x_2], y_1, y_2):
        return False
    
    # horizontal check
    # check line from [x_1, y_1] to [x_2, y_1]
    if has_between(edges_by_y[y_1], x_1, x_2):
        return False
    
    # check line from [x_1, y_2] to [x_2, y_2]
    if has_between(edges_by_y[y_2], x_1, x_2):
        return False

    return True


def solve(input):
    tiles = [(int(x), int(y)) for line in input.split('\n') for x, y in [line.split(',')]]

    # get all edges
    edges = set()

    for i in range(len(tiles)):
        add_to_edges(edges, tiles[i], tiles[(i + 1) % len(tiles)])

    # devide edges by line or cols into separate sorted lists
    edges_by_x = defaultdict(list)
    edges_by_y = defaultdict(list)

    for x, y in edges:
        edges_by_x[x].append(y)
        edges_by_y[y].append(x)

    for x in edges_by_x:
        edges_by_x[x].sort()
    for y in edges_by_y:
        edges_by_y[y].sort()

    # control using bisect if couples are valid
    result = 0

    for i in range(len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            size = rectangle_size(tiles[i], tiles[j])

            if size > result and is_inside_edges(tiles[i], tiles[j], edges_by_x, edges_by_y):
                result = size

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
