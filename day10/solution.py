# Read input
grid = dict()
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            grid[(i, j)] = int(c)

# Get the score of a trailhead
def explore_trail(trailhead):
    unique_endpoints = set()
    rating = 0
    visited = set()
    queue = [trailhead]

    while len(queue) > 0:
        position = queue.pop(0)

        # If at the end of a trail
        height = grid[position]
        if height == 9:
            rating += 1
            unique_endpoints.add(position)
            continue

        # Explore surrounding positions
        new_positions = [(position[0] + i, position[1] + j) for i, j in directions]
        queue += [p for p in new_positions if p in grid and p not in visited and grid[p] == height + 1]
        visited.add(position)
    return len(unique_endpoints), rating

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
trailheads = [(i, j) for i, j in grid if grid[(i, j)] == 0]

total_endpoints = 0
total_rating = 0
for trailhead in trailheads:
    endpoints, rating = explore_trail(trailhead)
    total_endpoints += endpoints
    total_rating += rating

print(f"Part 1: {total_endpoints}")
print(f"Part 2: {total_rating}")
