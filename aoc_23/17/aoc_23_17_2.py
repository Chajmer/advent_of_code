from pathlib import Path
from heapq import heappop, heappush

# =============== SOLUTION PART =============== #

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_in_bounds(position, grid):
    x, y = position
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def opposite(d1, d2):
    return -d1[0] == d2[0] and -d1[1] == d2[1]


def ultra_crubicle_filter(direction, facing, facing_count):
    return (direction == facing and facing_count == 10) or\
           (direction != facing and facing_count < 4) or\
            opposite(direction, facing)


def need_relax_cell(costs, cost, state):
    return state not in costs or cost < costs[state]


def solve(input):
    grid = [list(x) for x in input.split('\n')]

    start = (0, 0)
    end = (len(grid[0]) - 1, len(grid) - 1)

    costs = {(start, (0, 0), 0): 0} # (position, facing, facing_count)
    pq = [(0, start, (0, 0), 0)]    # (cost, position, facing, facing_count)

    # djikstra
    while pq:
        cur_cost, (x, y), facing, facing_count = heappop(pq)

        if (x, y) == end and facing_count >= 4:
            return cur_cost

        for direction in DIRECTIONS:

            new_pos = (x + direction[0], y + direction[1])

            # handle start, bounds and (no 3-/11+ same or oposite direction)
            if facing != (0, 0) and (not is_in_bounds(new_pos, grid) or ultra_crubicle_filter(direction, facing, facing_count)):
                continue

            new_cost = cur_cost + int(grid[new_pos[1]][new_pos[0]])
            new_facing_count = 1 + (facing_count if direction == facing else 0)
            new_state = (new_pos, direction, new_facing_count)
            
            if need_relax_cell(costs, new_cost, new_state):
                costs[new_state] = new_cost
                heappush(pq, (new_cost, new_pos, direction, new_facing_count))

    return -1  # If no path is found


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
