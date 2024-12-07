from operator import add, mul

# Read input
equations = []
with open("input.txt", "r") as f:
    for line in f:
        result, params = line.strip().split(": ")
        result = int(result)
        params = [int(x) for x in params.split()]
        equations.append((result, params))

# Part 1
def try_equation(result, params, ops):
    if len(params) == 1:
        return result == params[0]
    
    a, b, *remaining = params
    for op in ops:
        if try_equation(result, [op(a, b)] + remaining, ops):
            return True
    return False

total = 0
for equation in equations:
    result, params = equation
    if try_equation(result, params, [add, mul]):
        total += result

print(f"Part 1: {total}")

# Part 2
def concat_int(a, b):
    return int(str(a) + str(b))

total = 0
for equation in equations:
    result, params = equation
    if try_equation(result, params, [add, mul, concat_int]):
        total += result

print(f"Part 2: {total}")
