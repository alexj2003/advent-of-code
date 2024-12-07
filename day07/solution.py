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
def try_equation(result, params):
    if len(params) == 1:
        return result == params[0]
    
    a, b, *remaining = params
    for op in [add, mul]:
        if try_equation(result, [op(a, b)] + remaining):
            return True
    return False


total = 0
for equation in equations:
    result, params = equation
    if try_equation(result, params):
        total += result

print(f"Part 1: {total}")
