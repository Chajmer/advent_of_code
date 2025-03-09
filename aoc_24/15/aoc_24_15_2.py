from pathlib import Path

# =============== SOLUTION PART =============== #

DIRECTIONS = {'<': (-1, 0), '>': (1, 0), 'v': (0, 1), '^': (0, -1)}
MAPPING = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}

def find_robot(grid):
    for j, row in enumerate(grid):
        for i, cell in enumerate(row):
            if cell == '@':
                return i, j
    return -1, -1

def horizontal_move(grid, x, y, d):
    new_x = x
    while grid[y][new_x] not in {'#', '.'}:
        new_x += d

    if grid[y][new_x] == '.':
        # shift boxes
        for i in range(abs(new_x - x) - 1):
            grid[y][new_x - d * i] = grid[y][new_x - d * (i + 1)]
        # move robot itself
        grid[y][x] = '.'
        grid[y][x + d] = '@'
        return x + d, y

    return x, y

def vertical_move(grid, x, y, d):
    new_y = y
    moving_layers = [{(x, y)}]

    while moving_layers[-1]:
        new_y += d
        next_layer = set()

        for xi, yi in moving_layers[-1]:
            # obstacle detected
            if grid[yi + d][xi] == '#':
                return x, y
            # save for later box shifting
            if grid[yi + d][xi] != '.':
                next_layer.add((xi, yi + d))
                if grid[yi + d][xi] == '[':
                    next_layer.add((xi + 1, yi + d))
                else:
                    next_layer.add((xi - 1, yi + d))
        moving_layers.append(next_layer)

    # shift boxes
    for layer in reversed(moving_layers[:-1]):
        for xi, yi in layer:
            grid[yi + d][xi] = grid[yi][xi]
            grid[yi][xi] = '.'

    return x, y + d

def make_move(map, x, y, move):
    direction = DIRECTIONS[move]
    return horizontal_move(map, x, y, direction[0]) if direction[0] != 0\
        else vertical_move(map, x, y, direction[1])

def calculate_gps(grid):
    res = 0
    for j, row in enumerate(grid[1:], start=1):
        for i, cell in enumerate(row[1:], start=1):
            if cell == '[':
                res += i + j * 100
    return res

def solver(input):
    blocks = input.split('\n\n')
    grid = [[y for c in list(x) for y in MAPPING[c]] for x in blocks[0].split('\n')]
    moves = ''.join(blocks[1].split('\n'))
    x, y = find_robot(grid)

    for m in moves:
        x, y = make_move(grid, x, y, m)
        
    return calculate_gps(grid)


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
