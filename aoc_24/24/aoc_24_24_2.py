from pathlib import Path

# =============== SOLUTION PART =============== #

def process_gates(gates, gate_op_map):
    last_z = 0
    
    for in1, operator, in2, _, out in gates:

        if in1 not in gate_op_map:
            gate_op_map[in1] = set()
        if in2 not in gate_op_map:
            gate_op_map[in2] = set()

        gate_op_map[in1].add(operator)
        gate_op_map[in2].add(operator)

        if out[0] == 'z':
            last_z = max(last_z, int(out[1:]))

    return last_z


def verify_gates(gates, gate_op_map, last_z):
    errors = []

    for in1, operator, in2, _, out in gates:
        if "00" == in1[1:] or "00" == in2[1:]:
            continue

        # Conditions are Ripple-Carry Adder based
        x_in, y_in = 'x' in (in1[0], in2[0]), 'y' in (in1[0], in2[0])
        z_out = 'z' == out[0]

        # 1: z-outs have to be from XOR except last z-out
        if operator != 'XOR' and z_out and int(out[1:]) != last_z:
            errors.append(out)

        # 2: there are no internal XOR gates -> have to be z-out or x/y-in
        elif operator == 'XOR' and not z_out and not x_in and not y_in:
            errors.append(out)

        # 3: type (x XOR y) has to go to another XOR gate
        elif operator == 'XOR' and x_in and y_in and 'XOR' not in gate_op_map.get(out, set()):
            errors.append(out)

        # 4: type (x AND y) has to go to some OR gate
        elif operator == 'AND' and x_in and y_in and 'OR' not in gate_op_map.get(out, set()):
            errors.append(out)

    return ','.join(sorted(errors))


def parse_gates(input):
    return [x.split(' ') for x in input.split('\n\n')[1].split('\n')]


def solver(input):

    gates = parse_gates(input)
    gate_op_map = {}

    last_z = process_gates(gates, gate_op_map)

    return verify_gates(gates, gate_op_map, last_z)


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
