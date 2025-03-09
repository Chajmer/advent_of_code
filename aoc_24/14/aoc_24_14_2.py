from pathlib import Path

# =============== SOLUTION PART =============== #

DIMENSIONS = [(11, 7), (101, 103)]

def solver(input, input_num):
    dimension = DIMENSIONS[input_num - 1]
    robots = []
    velocities = []
    positions = set()

    for line in input.split('\n'):
        line = [[int(n) for n in c.split('=')[1].split(',')] for c in line.split()]
        robots.append((line[0][0], line[0][1]))
        velocities.append((line[1][0], line[1][1]))
        positions.add(robots[-1])

    result = 0
    while len(robots) != len(positions):
        result += 1
        next_robots = []
        positions = set()

        for i in range(len(robots)):
            new_x = (robots[i][0] + velocities[i][0]) % dimension[0]
            new_y = (robots[i][1] + velocities[i][1]) % dimension[1]
            next_robots.append((new_x, new_y))
            positions.add(next_robots[-1])
        robots = next_robots
 
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
    print(solver(read_input(input_file), int(input_file.stem.split('_')[-1])))

print("Test done")
