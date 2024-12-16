import heapq

# Get start and end positions
def get_start_end(maze):
    #for pos, cell in maze.items():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "S":
                start = (x, y)
            elif cell == "E":
                end = (x, y)
    return start, end

# Dijkstra's algorithm
def dijkstra(maze):
    start, end = get_start_end(maze)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    queue = [(0, start, (1, 0))]
    visited = set()

    while len(queue) > 0:
        d, (x, y), (dx, dy) = heapq.heappop(queue)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if (x, y) == end:
            return d
        
        for i, j in directions:
            if i == -dx and j == -dy:
                continue

            nx, ny = x + i, y + j

            is_straight = abs(i) == abs(dx) and abs(j) == abs(dy)
            cost = 1
            if not is_straight:
                cost += 1000

            if maze[ny][nx] == "#" or (nx, ny) in visited:
                continue

            heapq.heappush(queue, (d + cost, (nx, ny), (i, j)))
    
    return None

def read_input(data):
    grid = data.split("\n")
    # maze = {(i, j): cell for i, row in enumerate(grid) for j, cell in enumerate(row)}
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
lowest = dijkstra(maze)
print(f"Part 1: {lowest}")
