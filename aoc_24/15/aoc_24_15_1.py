from pathlib import Path

# =============== SOLUTION PART =============== #

DIRECTIONS = {'<': (-1, 0), '>': (1, 0), 'v': (0, 1), '^': (0, -1)}

def find_robot(grid):
    for j, row in enumerate(grid):
        for i, cell in enumerate(row):
            if cell == '@':
                return i, j
    return -1, -1

def make_move(grid, x, y, move):
    direction = DIRECTIONS[move]
    new_x, new_y = x, y

    # find all obstacles forwards
    while grid[new_y][new_x] not in {'#', '.'}:
        new_x += direction[0]
        new_y += direction[1]

    # shift obstacles
    if grid[new_y][new_x] == '.':
        grid[new_y][new_x] = 'O'

        # move robot itself
        grid[y][x] = '.'
        x += direction[0]
        y += direction[1]
        grid[y][x] = '@'
        return x, y
    
    return x, y

def calculate_gps(grid):
    res = 0
    for j, row in enumerate(grid[1:], start=1):
        for i, cell in enumerate(row[1:], start=1):
            if cell == 'O':
                res += i + j * 100
    return res

def solver(input):
    blocks = input.split('\n\n')
    grid = [list(line) for line in blocks[0].split('\n')]
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
