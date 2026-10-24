from pathlib import Path

# =============== SOLUTION PART =============== #

def get_keypad(code, mapping, depth, memo):

    if depth == 0:
        return len(code)

    cur = 'A'
    result = 0

    for c in code:

        key = (cur, c , depth)

        if key in memo:
            result += memo[key]
            cur = c
            continue

        dx = mapping[cur][0] - mapping[c][0]
        dy = mapping[cur][1] - mapping[c][1]

        sx = '<' * dx if dx > 0 else '>' * -dx
        sy = 'v' * dy if dy > 0 else '^' * -dy

        x_first = mapping[cur][1] + mapping[c][0] if '0' in mapping else (mapping[cur][1] != 1 or mapping[c][0] != 0)
        y_first = mapping[cur][0] + mapping[c][1] if '0' in mapping else (mapping[cur][0] != 0 or mapping[c][1] != 1)

        res_x = get_dir_keypad(sx + sy + 'A', depth - 1, memo) if x_first else float('inf')
        res_y = get_dir_keypad(sy + sx + 'A', depth - 1, memo) if y_first else float('inf')

        memo[key] = min(res_x, res_y)
        result += memo[key]
        cur = c

    return result


def get_dir_keypad(code, depth, memo):
    mapping = {             '^': (1, 1), 'A': (2, 1),
               '<': (0, 0), 'v': (1, 0), '>': (2, 0)}
    return get_keypad(code, mapping, depth, memo)


def get_num_keypad(code, memo):
    mapping = {'7': (0, 3), '8': (1, 3), '9': (2, 3),
               '4': (0, 2), '5': (1, 2), '6': (2, 2),
               '1': (0, 1), '2': (1, 1), '3': (2, 1),
                            '0': (1, 0), 'A': (2, 0)}
    return get_keypad(code, mapping, 26, memo)


def solver(input):
    result = 0
    memo = {}

    for code in input.split('\n'):
        result += int(code[:-1]) * get_num_keypad(code, memo)

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
