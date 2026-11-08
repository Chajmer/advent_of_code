from pathlib import Path

# =============== SOLUTION PART =============== #

def decode(d):
    return (0 if d % 2 == 0 else (1 if d == 1 else -1)), (0 if d % 2 else (1 if d else -1))


def move(x, y, d):
    dx, dy = decode(d)
    return x + dx, y + dy, d


def is_next(x, y, d, grid, visited):
    return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid) and ((x, y, d) not in visited)


def get_energy(grid, x, y, d):
    to_visit = [(x, y, d)]
    visited = set(to_visit[-1]) # visited with also direction
    energized = {(x, y)}        # just keep tack off count coordinates without direction

    while to_visit:
        x, y, d = to_visit.pop()
        to_proces = []

        if grid[y][x] == '.':
            to_proces.append(move(x, y, d))
        elif grid[y][x] == '/':
            to_proces.append(move(x, y, d ^ 1))
        elif grid[y][x] == '\\':
            to_proces.append(move(x, y, d ^ 3))
        elif grid[y][x] == '|':
            for nd in [0, 2]:
                if nd != (d + 2) % 4:
                    to_proces.append(move(x, y, nd))
        elif grid[y][x] == '-':
            for nd in [1, 3]:
                if nd != (d + 2) % 4:
                    to_proces.append(move(x, y, nd))

        for nx, ny, nd in to_proces:
            if is_next(nx, ny, nd, grid, visited):
                to_visit.append((nx, ny, nd))
                visited.add((nx, ny, nd))
                energized.add((nx, ny))
    
    return len(energized)


def solve(input):

    grid = input.split('\n')
    result = 0

    for x in range(len(grid[0])):
        result = max(result, get_energy(grid, x, 0, 2))
        result = max(result, get_energy(grid, x, len(grid) - 1, 0))

    for y in range(len(grid)):
        result = max(result, get_energy(grid, 0, y, 1))
        result = max(result, get_energy(grid, len(grid[0]) - 1, y, 3))

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
