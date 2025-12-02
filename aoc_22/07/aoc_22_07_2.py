from pathlib import Path

# =============== SOLUTION PART =============== #

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.dir_children = []
        self.file_children = []
        self.parent = None


def parse_file_tree(input, initial_place):
    current_place = initial_place

    for line in input.split('\n'):

        if line == "$ cd /":
            current_place = initial_place

        elif line == "$ cd ..":
            current_place = current_place.parent

        elif line[0:5] == "$ cd ":
            if line[5:] not in [x.name for x in current_place.dir_children]:
                new_place = Directory(line[5:])
                current_place.dir_children.append(new_place)
                new_place.parent = current_place
                current_place = new_place
            else:
                for child in current_place.dir_children:
                    if child.name == line[5:]:
                        current_place = child
                        break

        elif line == "$ ls":
            pass # list cases are both catched below

        elif line[0:4] == "dir ":
            if line[4:] not in [x.name for x in current_place.dir_children]:
                new_place = Directory(line[4:])
                current_place.dir_children.append(new_place)
                new_place.parent = current_place
        
        else: # it is number and file name
            atributes = line.split()
            name = atributes[1]
            size = int(atributes[0])
            if name not in [x.name for x in current_place.file_children]:
                current_place.file_children.append(File(name, size))


def get_dir_sum(dir: Directory):
    dir.size = sum([x.size for x in dir.file_children])
    for child in dir.dir_children:
        get_dir_sum(child)
        dir.size += child.size


def come_through_dirs(dir: Directory, mini, factor):
    if factor + dir.size >= 0 and (mini is None or mini > dir.size):
        mini = dir.size
        
    for child in dir.dir_children:
        rec = come_through_dirs(child, mini, factor)
        if rec < mini:
            mini = rec
        
    return mini


def solve(input):
    initial_place = Directory("/")
    initial_place.parent = initial_place
    
    parse_file_tree(input, initial_place)

    # get sum into all dirs
    get_dir_sum(initial_place)

    return come_through_dirs(initial_place, None, 40000000 - initial_place.size)


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
