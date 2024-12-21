from functools import cache
from itertools import permutations

NUM_PAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [" ", "0", "A"]
]

NUM_PAD_DIRS = {key: (x, y) for y, row in enumerate(NUM_PAD) for x, key in enumerate(row) if key != " "}

DIR_PAD = [
    [" ", "^", "A"],
    ["<", "v", ">"],
]

DIR_PAD_DIRS = {key: (x, y) for y, row in enumerate(DIR_PAD) for x, key in enumerate(row) if key != " "}

DIRS = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0)
}

# Find number of presses for a code on a keypad
@cache
def find_presses(code, depth = 2, use_num_pad = True, cur_key = None):
    keypad = NUM_PAD_DIRS if use_num_pad else DIR_PAD_DIRS

    if not code:
        return 0
    
    if not cur_key:
        cur_key = keypad["A"]

    # Find next key in the code
    x, y = cur_key
    kx, ky = keypad[code[0]]
    dx, dy = kx - x, ky - y

    # Find presses needed to move to next key
    presses = ""
    if dx > 0:
            presses += ">" * dx
    elif dx < 0:
        presses += "<" * abs(dx)
    
    if dy > 0:
        presses += "v" * dy
    elif dy < 0:
        presses += "^" * abs(dy)
    
    if depth:
        # Find lengths of all possible combinations of presses
        press_lens = []
        for combo in set(permutations(presses)):
            cx, cy = cur_key
            for co in combo:
                dx, dy = DIRS[co]
                cx, cy = cx + dx, cy + dy

                if not (cx, cy) in keypad.values():
                    break
            else:
                press_lens.append(find_presses(combo+("A",), depth = depth - 1, use_num_pad = False))
        min_presses = min(press_lens)
    else:
        # If final keypad
        min_presses = len(presses) + 1
    
    return min_presses + find_presses(code[1:], depth = depth, use_num_pad = use_num_pad, cur_key = (kx, ky))

# Read data
def read_data(data):
    codes = data.strip().split('\n')
    return codes

# Test data
data = """029A
980A
179A
456A
379A"""

# Read input
with open("input.txt", "r") as file:
    data = file.read()

codes = read_data(data)

# Part 1
complexity = 0
for code in codes:
    complexity += find_presses(code) * int(code[:-1])

print(f"Part 1: {complexity}")

# Part 2
complexity = 0
for code in codes:
    complexity += find_presses(code, depth = 25) * int(code[:-1])

print(f"Part 2: {complexity}")
