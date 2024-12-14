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

# Find number of sides for a region of nodes
def find_sides(nodes):
    sides = set()
    total = 0
    for n in nodes:
        for d in directions:
            neighbour = (n[0] + d[0], n[1] + d[1])
            if neighbour in nodes:
                continue
            new_x, new_y = n[0], n[1]
            while (new_x + d[1], new_y + d[0]) in nodes and (new_x + d[0], new_y + d[1]) not in nodes:
                new_x += d[1]
                new_y += d[0]
            if (new_x, new_y, d) not in sides:
                sides.add((new_x, new_y, d))
                total += 1
    return total      

p1_total = 0
p2_total = 0
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

        # Skip if already visited in this region
        if current in visited:
            continue
        visited.add(current)

        unexplored.discard(current)
        area += 1

        # Check neighbours
        for d in directions:
            neighbour = (current[0] + d[0], current[1] + d[1])

            if neighbour not in garden or garden[neighbour] != plant:
                perimeter += 1
            elif neighbour not in visited:
                stack.append(neighbour)

    p1_total += perimeter * area
    p2_total += find_sides(visited) * area

print(f"Part 1: {p1_total}")
print(f"Part 2: {p2_total}")

