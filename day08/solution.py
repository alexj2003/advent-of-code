from itertools import permutations

# Read input
grid = dict()
antennas = dict()
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            grid[(i, j)] = c

            if c == ".":
                continue
                
            if c not in antennas:
                antennas[c] = []
            antennas[c].append((i, j))
    last_i, last_j = i, j

# Part 1
antinodes = set()

for a, nodes in antennas.items():
    for (i1, j1), (i2, j2) in permutations(nodes, 2):
        di = (2 * i1) - i2
        dj = (2 * j1) - j2
        if (di, dj) in grid:
            antinodes.add((di, dj))

print(f"Part 1: {len(antinodes)}")

# Part 2
antinodes = set()

for a, nodes in antennas.items():
    for (i1, j1), (i2, j2) in permutations(nodes, 2):
        di = (2 * i1) - i2
        dj = (2 * j1) - j2
        antinodes.add((i2, j2))

        while (di, dj) in grid:
            antinodes.add((di, dj))
            di += i1 - i2
            dj += j1 - j2

print(f"Part 2: {len(antinodes)}")
