import sympy as sym

# Read input
machines = []
with open("input.txt", "r") as f:
    for machine in f.read().split("\n\n"):
        machine_desc = {}
        a, b, p = machine.splitlines()
        machine_desc["a"] = [int(x.split("+")[1]) for x in a.split(": ")[1].split(", ")]
        machine_desc["b"] = [int(x.split("+")[1]) for x in b.split(": ")[1].split(", ")]
        machine_desc["p"] = [int(x.split("=")[1]) for x in p.split(":")[1].split(", ")]
        machines.append(machine_desc)

# Part 1

MAX_PRESSES = 100

# Solve a machine to find the minimum number of presses
# Brute force approach
def solve(machine):
    ax, ay = machine["a"]
    bx, by = machine["b"]
    px, py = machine["p"]

    solutions = []
    for a in range(MAX_PRESSES):
        for b in range(MAX_PRESSES):
            if (ax * a + bx * b) == px and (ay * a + by * b) == py:
                # Pressing A = 3 tokens, B = 1 token
                solutions.append(3 * a + b)

    return min(solutions) if solutions else 0

# total = 0
# for machine in machines:
#     total += solve(machine)

# print(f"Part 1: {total}")

# Part 2

OFFSET = 10000000000000

# For part 2, it can have an unlimited number of presses
# A brute force approach is incredibly inefficient here
# Solve as simultaneous equations instead
def solve_v2(machine):
    ax, ay = machine["a"]
    bx, by = machine["b"]
    px, py = machine["p"]
    px += OFFSET
    py += OFFSET

    x, y = sym.symbols("x y", integer=True, positive=True)
    x_eq = sym.Eq(ax * x + bx * y, px)
    y_eq = sym.Eq(ay * x + by * y, py)
    result = sym.solve([x_eq, y_eq], (x, y))

    return 3 * result[x] + result[y] if result else 0

total = 0
for machine in machines:
    total += solve_v2(machine)

print(f"Part 2: {total}")