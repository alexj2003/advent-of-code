# Read input
def read_input(inp):
    grid, moves = inp.split("\n\n")
    grid = [list(row) for row in grid.split("\n")]
    moves = "".join(moves.split("\n"))
    return grid, moves

# Test data
test_grid = """
##########
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
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
grid, moves = read_input(test_grid.strip())

DIRECTIONS = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

# Part 1
with open("input.txt", "r") as f:
    grid, moves = read_input(f.read().strip())

# Get initial robot and box positions
robot = None
boxes = set()

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "@":
            robot = (i, j)
        elif cell == "O":
            boxes.add((i, j))

for move in moves:
    di, dj = DIRECTIONS[move]
    robot_pos = (robot[0] + di, robot[1] + dj)

    # If moving to a wall, do nothing
    if grid[robot_pos[0]][robot_pos[1]] == "#":
        continue

    # If moving to a chain of boxes, check if they can move
    chain = []
    box_pos = robot_pos
    while box_pos in boxes:
        chain.append(box_pos)
        box_pos = (box_pos[0] + di, box_pos[1] + dj)
    
    # If chain ends with a wall, do nothing
    if grid[box_pos[0]][box_pos[1]] == "#":
        continue

    # Move boxes
    for box in reversed(chain):
        boxes.remove(box)
        boxes.add((box[0] + di, box[1] + dj))
    
    # Move robot
    robot = robot_pos

# Calculate box coordinate total
total = sum(100 * box[0] + box[1] for box in boxes)
print(f"Part 1: {total}")