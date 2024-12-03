import re

# Read input
with open("input.txt") as f:
    lines = f.readlines()

# Part 1
total = 0
for line in lines:
    matches = re.findall(r"mul\(\d+,\d+\)", line)
    for match in matches:
        a, b = map(int, re.findall(r"\d+", match))
        total += a * b

print(f"Multiplication total: {total}")