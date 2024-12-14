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

MAX_PRESSES = 100

# Solve a machine to find the minimum number of presses
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

# Part 1
total = 0
for machine in machines:
    total += solve(machine)

print(f"Part 1: {total}")