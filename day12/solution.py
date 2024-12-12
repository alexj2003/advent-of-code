# Read input
garden = dict()
with open("input.txt") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            garden[(i, j)] = c

# Test data
# test_input = """
# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
# """
# for i, line in enumerate(test_input.strip().split("\n")):
#     for j, c in enumerate(line.strip()):
#         garden[(i, j)] = c
    
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
fencing_total = 0
unexplored = set(garden.keys())

while unexplored:
    start = unexplored.pop()
    plant = garden[start]
    area = 0
    perimeter = 0
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()        

        if current in visited:
            continue
        visited.add(current)

        unexplored.discard(current)
        area += 1

        for d in directions:
            neighbour = (current[0] + d[0], current[1] + d[1])
            if neighbour not in garden or garden[neighbour] != plant:
                perimeter += 1
            elif neighbour not in visited:
                stack.append(neighbour)

    fencing_total += perimeter * area

print(f"Part 1: {fencing_total}")

