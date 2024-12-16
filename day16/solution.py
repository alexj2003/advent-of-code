import heapq

# Get start and end positions
def get_start_end(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "S":
                start = (x, y)
            elif cell == "E":
                end = (x, y)
    return start, end

# Dijkstra's algorithm
def dijkstra(maze, score_limit=None):
    start, end = get_start_end(maze)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    queue = [(0, start, (1, 0), {start})]
    visited = set()

    while len(queue) > 0:
        d, (x, y), (dx, dy), path = heapq.heappop(queue)

        if (x, y) in visited:
            continue

        # For part 2, skip paths that are longer than the shortest path
        if score_limit is not None and d > score_limit:
            continue

        visited.add((x, y))

        if (x, y) == end:
            return d, path
        
        for i, j in directions:
            if i == -dx and j == -dy:
                continue

            nx, ny = x + i, y + j

            is_straight = abs(i) == abs(dx) and abs(j) == abs(dy)
            cost = 1 if is_straight else 1001

            if maze[ny][nx] == "#" or (nx, ny) in visited:
                continue

            new_path = path.copy()
            new_path.add((nx, ny))
            heapq.heappush(queue, (d + cost, (nx, ny), (i, j), new_path))
    
    return None, None

def read_input(data):
    grid = data.split("\n")
    maze = [[cell for cell in row] for row in grid]
    return maze

# Test data
test_grid = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
maze = read_input(test_grid)

# Read input
with open("input.txt", "r") as f:
    maze = read_input(f.read())

# Part 1
lowest, path = dijkstra(maze)
print(f"Part 1: {lowest}")

# Part 2
tiles = set()
tiles.update(path)

# For each tile in path, replace with a wall and try to find a new path
# Pretty slow but it works
# I couldn't come up with a better way without completely rewriting part 1
(sx, sy), (ex, ey) = get_start_end(maze)
for x, y in path:
    if (x, y) == (sx, sy) or (x, y) == (ex, ey):
        continue

    maze[y][x] = "#"
    score, new_path = dijkstra(maze, lowest)
    if score == lowest:
        tiles.update(new_path)
    
    maze[y][x] = "."

print(f"Part 2: {len(tiles)}")
