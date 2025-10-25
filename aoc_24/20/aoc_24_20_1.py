from pathlib import Path

# =============== SOLUTION PART =============== #

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
CHEAT_BOUND = 100

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

def is_occupated_cell(maze, position):
    return is_in_bounds(position, maze) and maze[position[1]][position[0]] == '#'

def get_way_and_distances(maze, start, end):
    prev_pt = (-1, -1)
    curr_pt = start
    maze_way = [start]
    point_order = {start: 0}

    while curr_pt != end:
        x, y = curr_pt
        for dx, dy in DIRECTIONS:
            next_pt = (x + dx, y + dy)
            if next_pt != prev_pt and is_free_cell(maze, next_pt):
                prev_pt = curr_pt
                curr_pt = next_pt
                break
        else:
            assert False
        maze_way.append(curr_pt)
        point_order[curr_pt] = point_order[prev_pt] + 1
    
    return maze_way, point_order

def solver(input):
    maze = [list(x) for x in input.split('\n')]
    start = find_point('S', maze)
    end = find_point('E', maze)

    # for each point get distance to goal
    maze_way, point_order = get_way_and_distances(maze, start, end)

    # try cheat for each point
    result = 0
    for point in maze_way:
        x, y = point
        for (dx, dy) in DIRECTIONS:
            # cheat trough wall look up
            cheat_pt = (x + 2*dx, y + 2*dy)
            if point_order.get(cheat_pt, 0) - point_order[point] - 2 >= CHEAT_BOUND:
                result += 1
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
    print(solver(read_input(input_file)))

print("Test done")
