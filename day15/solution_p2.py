# Couldn't get my code for part 1 working with part 2, so here's a rewrite
# Updates the grid directly instead of tracking each box location

# Get grid and list of moves
def read_grid(data):
    grid, moves = data.split("\n\n")

    # Scale grid
    grid = [row for row in grid.strip().split("\n")]
    grid = [list(row.replace("O", "[]").replace(".", "..").replace("#", "##").replace("@", "@.")) for row in grid]

    moves = "".join(moves.strip().split("\n"))

    return grid, moves

# Find (row, col) position of robot
def find_robot(grid):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "@":
                return (r, c)

# Check if a position is valid and can be moved to
def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != "#"

# Check if a box can be moved
def can_move(grid, row, col, dr, dc, visited):
    if (row, col) in visited:
        return True
    
    visited.add((row, col))

    nr, nc = row + dr, col + dc

    if grid[nr][nc] == "#":
        return False
    elif grid[nr][nc] == "[":
        return can_move(grid, nr, nc, dr, dc, visited) and can_move(grid, nr, nc + 1, dr, dc, visited)
    elif grid[nr][nc] == "]":
        return can_move(grid, nr, nc, dr, dc, visited) and can_move(grid, nr, nc - 1, dr, dc, visited)
    elif grid[nr][nc] == "O":
        return can_move(grid, nr, nc, dr, dc, visited)
    
    return True

# Find all box positions
def find_boxes(grid):
    boxes = set()

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "[":
                boxes.add((r, c))
    
    return boxes

# Simulate a robot move
def make_move(grid, move, row, col):
    dr, dc = DIRECTIONS[move]

    nr, nc = row + dr, col + dc

    if not is_valid(grid, nr, nc):
        return row, col

    if grid[nr][nc] in ["[", "]", "O"]:
        visited = set()

        if not can_move(grid, row, col, dr, dc, visited):
            return row, col

        while len(visited) > 0:
            for r, c in visited.copy():
                nnr, nnc = r + dr, c + dc
                if (nnr, nnc) not in visited:
                    if grid[nnr][nnc] != "@" and grid[r][c] != "@":
                        grid[nnr][nnc] = grid[r][c]
                        grid[r][c] = "."
                    visited.remove((r, c))

        grid[row][col], grid[nr][nc] = grid[nr][nc], grid[row][col]
        return nr, nc

    grid[row][col], grid[nr][nc] = grid[nr][nc], grid[row][col]
    return nr, nc

DIRECTIONS = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

# Test data
test_grid = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
grid, moves = read_grid(test_grid)   

# Read input
with open("input.txt", "r") as f:
    grid, moves = read_grid(f.read())

row, col = find_robot(grid)

for move in moves:
    row, col = make_move(grid, move, row, col)

# Calculate box coordinate total
total = sum(100 * box[0] + box[1] for box in find_boxes(grid))
print(f"Part 2: {total}")
