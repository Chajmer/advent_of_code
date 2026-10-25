from pathlib import Path

# =============== SOLUTION PART =============== #

def solver(input):

    comps = set()
    connections = set()

    # parse
    for line in input.split('\n'):
        c1, c2 = line.split('-')

        comps.add(c1)
        comps.add(c2)

        connections.add((c1, c2))
        connections.add((c2, c1))

    # bruce force
    comps = list(comps)
    result = 0

    for i in range(len(comps) - 2):
        for j in range(i + 1, len(comps) - 1):
            if (comps[i], comps[j]) not in connections:
                continue

            for k in range(j + 1, len(comps)):
                if ('t' in [comps[i][0], comps[j][0], comps[k][0]] and
                        (comps[i], comps[k]) in connections and
                        (comps[j], comps[k]) in connections):
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
