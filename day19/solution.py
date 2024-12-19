from functools import cache

# Read data
def read_data(data):
    patterns, designs = data.split("\n\n")
    patterns = patterns.strip().split(", ")
    designs = [design.strip() for design in designs.strip().split("\n")]
    return patterns, designs

# Calculate if a design is possible
@cache
def calc_possible(design, patterns):
    if design == "":
        return True
    
    return any((calc_possible(design[len(pattern):], patterns) if design.startswith(pattern) else False) for pattern in patterns)

# Test data
data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

# Read input
with open("input.txt") as f:
    data = f.read()

patterns, designs = read_data(data)
patterns = frozenset(patterns)

# Part 1
possible = 0
for design in designs:
    if calc_possible(design, patterns):
        possible += 1

print(f"Part 1: {possible}")
