from pathlib import Path

# =============== SOLUTION PART =============== #

def parse(input):
    graph = {}

    for line in [x.split(': ') for x in input.split('\n')]:
        graph[line[0]] = []

        for node in line[1].split(' '):
            graph[line[0]].append(node)

    return graph


def dfs(graph, visited, cur):
    if cur == "out":
        return 1

    res = 0

    for next in graph[cur]:
        if next not in visited:
            visited.add(next)
            res += dfs(graph, visited, next)
            visited.remove(next)

    return res


def solve(input):
    try:
        return dfs(parse(input), {"you"}, "you")
    except KeyError as e:
        return f"KeyError {str(e)}"


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
