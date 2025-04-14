from pathlib import Path
from collections import Counter

# =============== SOLUTION PART =============== #

CARD_VALUES = {'A': 94, 'K': 93, 'Q': 92, 'J': 91,
               'T': 90, '9': 89, '8': 88, '7': 87,
               '6': 86, '5': 85, '4': 84, '3': 83,
               '2': 82}

def hand_to_num(hand):
    res = 0
    for card in hand:
        res *= 100
        res += CARD_VALUES[card]
    return res

def first_rule(hand):
    match sorted(Counter(hand).values(), reverse=True):
        case [5]:
            return 0  # Five of a kind
        case [4, 1]:
            return 1  # Four of a kind
        case [3, 2]:
            return 2  # Full house
        case [3, 1, 1]:
            return 3  # Three of a kind
        case [2, 2, 1]:
            return 4  # Two pairs
        case [2, 1, 1, 1]:
            return 5  # One pair
        case _:
            return 6  # High card

def solve(input):
    hand_types = [[] for _ in range(7)]
    # sort first rule
    for line in input.split('\n'):
        hand, bid = line.split()
        hand_types[first_rule(hand)].append((-hand_to_num(hand), int(bid)))
    # sort second rule
    rank: int = 0
    for type in hand_types:
        rank += len(type)
        type.sort()
    # for cycle whole sorted items and get sum
    result = 0
    for type in hand_types:
        for _, bid in type:
            result += bid * rank
            rank -= 1
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
