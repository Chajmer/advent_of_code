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

def end_found(end, path_pts):
    places = set()
    for (place, _),(dist, way) in path_pts.items():
        if place == end and dist == 1:
            places |= way
    return len(places)

def is_in_bounds(position, maze):
    x, y = position
    return 0 <= y < len(maze) and 0 <= x < len(maze[0])

def is_free_cell(maze, position):
    return is_in_bounds(position, maze) and maze[position[1]][position[0]] == '.'

def need_relax_cell(costs, cost, state):
    return state not in costs or cost <= costs[state][0]

def solver(input):
    maze = [list(x) for x in input.split('\n')]
    start = find_point('S', maze)
    end = find_point('E', maze)
    facing = (1, 0)
    ways_pts = {start}
    # cost in position is also dependent on facing
    costs = {(start, facing): [0, ways_pts]}
    pq = [(0, start, facing, ways_pts)]  # (cost, position, facing, ways_pts)

    # djikstra
    while pq:
        cur_cost, (x, y), facing, ways_pts = heappop(pq)

        if (x, y) == end:
            return len(ways_pts)

        for direction in DIRECTIONS:
            new_cost = cur_cost + (1 if direction == facing else 1001)
            next_pos = (x + direction[0], y + direction[1])
            next_state = (next_pos, direction)

            if is_free_cell(maze, next_pos) and need_relax_cell(costs, new_cost, next_state):
                info_next_state = costs.get(next_state, [float('inf'), None])

                if new_cost == info_next_state[0]:
                    info_next_state[1].update(ways_pts) # ensures copy data from ways_pts - not linking
                    continue
                
                # need copy ways_pts - not link
                new_ways_pts = {next_pos} | ways_pts
                costs[next_state] = [new_cost, new_ways_pts]
                heappush(pq, (new_cost, next_pos, direction, new_ways_pts))

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
