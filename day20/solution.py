from collections import defaultdict, deque
import heapq
from itertools import combinations

# Get start and end positions
def get_start_end(maze):
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == "S":
                start = (r, c)
            elif cell == "E":
                end = (r, c)
    return start, end

# Read data
def read_input(data):
    maze = [list(line) for line in data.strip().split("\n")]
    return maze

# Is position valid
def is_valid(maze, r, c):
    return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != "#"

# BFS to pre-compute distances
def compute_dist(maze):
    start, end = get_start_end(maze)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(start[0], start[1], 0)])
    distances = {}

    while queue:
        r, c, n = queue.popleft()

        # Skip if already visited
        if (r, c) in distances:
            continue

        distances[(r, c)] = n

        if (r, c) == end:
            continue

        # Add neighbours to queue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if is_valid(maze, nr, nc):
                queue.append((nr, nc, n + 1))
    
    return distances

def count_cheats(maze):
    distances = compute_dist(maze)

    cheats = 0
    for ((r1, c1), n1), ((r2, c2), n2) in combinations(distances.items(), 2):
        dist = abs(r1 - r2) + abs(c1 - c2)

        if dist <= 2 and abs(n2 - n1) >= dist + 100:
            cheats += 1
    
    return cheats

# Test data
# test_data = """###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############"""
# maze = read_input(test_data)

# Read input
with open("input.txt", "r") as f:
    maze = read_input(f.read())

cheats = count_cheats(maze)

print(f"Number of cheats: {cheats}")
