from pathlib import Path
from heapq import heappop, heappush

# =============== SOLUTION PART =============== #

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def find_point(s, maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == s:
                maze[y][x] = '.'
                return (x, y)
    assert False

def is_in_bounds(position, maze):
    x, y = position
    return 0 <= y < len(maze) and 0 <= x < len(maze[0])

def is_free_cell(maze, position):
    return is_in_bounds(position, maze) and maze[position[1]][position[0]] == '.'

def need_relax_cell(costs, cost, state):
    return state not in costs or cost < costs[state]

def solver(input):
    maze = [list(x) for x in input.split('\n')]
    start = find_point('S', maze)
    end = find_point('E', maze)
    facing = (1, 0)
    # cost in position is also dependent on facing
    costs = {(start, facing): 0}
    pq = [(0, start, facing)]  # (cost, position, facing)

    # djikstra
    while pq:
        cur_cost, (x, y), facing = heappop(pq)

        if (x, y) == end:
            return cur_cost

        for direction in DIRECTIONS:
            new_cost = cur_cost + (1 if direction == facing else 1001)
            new_pos = (x + direction[0], y + direction[1])
            new_state = (new_pos, direction)
            
            if is_free_cell(maze, new_pos) and need_relax_cell(costs, new_cost, new_state):
                costs[new_state] = new_cost
                heappush(pq, (new_cost, new_pos, direction))

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
    print(solver(read_input(input_file)))

print("Test done")
