from pathlib import Path

# =============== SOLUTION PART =============== #

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.size = 0
        self.dir_children = []
        self.file_children = []
        self.parent = parent if parent else self


def parse_file_tree(input, initial): # could be much more better decomposited
    current = initial

    for line in input.split('\n'):

        if line == "$ cd /":
            current = initial

        elif line == "$ cd ..":
            current = current.parent

        elif line[0:5] == "$ cd ":
            if line[5:] not in [x.name for x in current.dir_children]:
                current.dir_children.append(Directory(line[5:], current))
                current = current.dir_children[-1]
            else:
                for child in current.dir_children:
                    if child.name == line[5:]:
                        current = child
                        break

        elif line == "$ ls":
            pass # list cases are both catched below

        elif line[0:4] == "dir ":
            if line[4:] not in [x.name for x in current.dir_children]:
                current.dir_children.append(Directory(line[4:], current))
        
        else: # it's number and file name
            size, name = line.split()
            if name not in [x.name for x in current.file_children]:
                current.file_children.append(File(name, int(size)))


def update_dir_sizes(dir: Directory):
    dir.size = sum([x.size for x in dir.file_children])
    
    for child in dir.dir_children:
        update_dir_sizes(child)
        dir.size += child.size


def sum_dirs_to_size(dir: Directory, size):
    result = dir.size if dir.size <= size else 0

    for child in dir.dir_children:
        result += sum_dirs_to_size(child, size)
        
    return result


def solve(input):
    initial = Directory("/")
    
    parse_file_tree(input, initial)

    update_dir_sizes(initial)

    return sum_dirs_to_size(initial, 100000)


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
