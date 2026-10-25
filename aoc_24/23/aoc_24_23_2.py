from pathlib import Path
import networkx as nx

# =============== SOLUTION PART =============== #

def solver(input):

    connections = set()

    # parse
    for line in input.split('\n'):
        c1, c2 = line.split('-')

        connections.add((c1, c2))

    # Bron–Kerbosch algorithm from lib
    graph = nx.Graph()
    graph.add_edges_from(connections)
    return ','.join(sorted(max(nx.find_cliques(graph), key=len)))


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
