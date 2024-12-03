import re

# Read input
with open("input.txt") as f:
    lines = f.readlines()

# Part 1
def mul(mul_str):
    a, b = map(int, re.findall(r"\d+", mul_str))
    return a * b

total = 0
multiply_pattern = r"mul\(\d+,\d+\)"
for line in lines:
    matches = re.findall(multiply_pattern, line)
    for match in matches:
        total += mul(match)

print(f"Multiplication total: {total}")

# Part 2
total = 0
do = True
do_pattern = r"do\(\)|don\'t\(\)"
for line in lines:
    parts = re.split(f"({do_pattern}|{multiply_pattern})", line)
    for part in parts:
        if part == "do()":
            do = True
        elif part == "don't()":
            do = False
        
        match = re.match(multiply_pattern, part)
        if match and do:
            total += mul(match.group())

print(f"Multiplication total with do/don't: {total}")