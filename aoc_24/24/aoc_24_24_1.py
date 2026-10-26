from pathlib import Path

# =============== SOLUTION PART =============== #

class Gate:
    def __init__(self, operator, out):
        self.input = []
        self.operator = operator
        self.out = out
        self.evaluation = None

    def add_input(self, val):
        if len(self.input) == 2:
            return

        self.input.append(val)

        if len(self.input) == 2:
            self.calculation()

    def calculation(self):
        self.evaluation = ((self.input[0] & self.input[1]) if self.operator == 'AND' else
                          ((self.input[0] | self.input[1]) if self.operator == 'OR' else
                           (self.input[0] ^ self.input[1])))


def create_gates(info):
    gate_map = {}
    
    for in1, operator, in2, _, out in info:
        next_gate = Gate(operator, out)

        if in1 not in gate_map:
            gate_map[in1] = []
        if in2 not in gate_map:
            gate_map[in2] = []

        gate_map[in1].append(next_gate)
        gate_map[in2].append(next_gate)

    return gate_map


def evaulate_gates(gate_map, values):
    # reacalculate gates with updating cycle
    active = list(values.keys())

    while active:
        cur_gate = active.pop()

        if cur_gate not in gate_map:
            continue
    
        for next_gate in gate_map[cur_gate]:
            next_gate.add_input(values[cur_gate])

            if next_gate.evaluation is not None:
                values[next_gate.out] = next_gate.evaluation
                active.append(next_gate.out)

    return values


def solver(input):

    values, gates = input.split('\n\n')

    gate_map = create_gates([x.split(' ') for x in gates.split('\n')])

    # called with init values
    values = evaulate_gates(gate_map, {y: int(z) for x in values.split('\n') for y, z in [x.split(': ')]})

    # put z values to result
    result = 0
    n = 0

    while ('z' + f'{n:02d}') in values:
        result += values['z' + f'{n:02d}'] * 2**n
        n += 1

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
