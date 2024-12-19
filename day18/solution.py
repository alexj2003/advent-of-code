import heapq

# Dijkstra's algorithm
def dijkstra(maze):
    maze_len = len(maze) - 2
    start, end = (1, 1), (maze_len, maze_len)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    queue = [(0, start, (0, 1), {start})]
    visited = set()

    while len(queue) > 0:
        d, (x, y), (dx, dy), path = heapq.heappop(queue)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if (x, y) == end:
            return d
        
        for i, j in directions:
            if i == -dx and j == -dy:
                continue

            nx, ny = x + i, y + j

            if maze[ny][nx] == "#" or (nx, ny) in visited:
                continue

            new_path = path.copy()
            new_path.add((nx, ny))
            heapq.heappush(queue, (d + 1, (nx, ny), (i, j), new_path))
    
    return None

# Fill grid
def fill_grid(grid, byte_positions, number):
    for i in range(number):
        x, y = byte_positions[i]
        grid[y][x] = "#"
    return grid

# Print grid
def print_grid(grid):
    for line in grid:
        print("".join(line))

# Read input
with open("input.txt", "r") as f:
    byte_positions = []
    for line in f:
        byte_positions.append(tuple(map(int, line.strip().split(","))))

# Make grid
memory_loc = 1024
grid = [["." for _ in range(71)] for _ in range(71)]
grid = fill_grid(grid, byte_positions, memory_loc)

# # Test data
# grid = """...#...
# ..#..#.
# ....#..
# ...#..#
# ..#..#.
# .#..#..
# #.#...."""
# grid = [[cell for cell in row] for row in grid.split("\n")]
# byte_positions = """5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0"""
# byte_positions = [tuple(map(int, line.strip().split(","))) for line in byte_positions.split("\n")]
# grid = fill_grid(grid, byte_positions, 12)

# Surround grid with walls
new_grid = []
new_len = len(grid) + 2
new_grid.append(["#" for _ in range(new_len)])
for line in grid:
    new_grid.append(["#"] + line + ["#"])
new_grid.append(["#" for _ in range(new_len)])

# Part 1
# Reuseing dijkstra function from day 16
steps = dijkstra(new_grid)
print(f"Part 1: {steps}")

# Part 2
# I'm not sure if there's a better way to do this but its not *too* slow
while True:
    # Add new byte
    x, y = byte_positions[memory_loc]
    new_grid[y + 1][x + 1] = "#" # Need to +1 because of the surrounding walls
    memory_loc += 1

    # Search for path
    steps = dijkstra(new_grid)

    if steps is None:
        print(f"Part 2: {x},{y}")
        break
