# Read input
lab_map = []
with open("input.txt") as f:
    for line in f:
        lab_map.append(list(line.strip()))

# Part 1
directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

def rotate(direction):
    if direction == "^":
        return ">"
    elif direction == ">":
        return "v"
    elif direction == "v":
        return "<"
    else:
        return "^"

def check_bounds(lab_map, i, j):
    return 0 <= i < len(lab_map) and 0 <= j < len(lab_map[0])

def move_guard(lab_map, x, y, direction):
    unique_visited = set()
    position_directions = set()
    position_directions.add((x, y, direction))

    while check_bounds(lab_map, x, y):
        unique_visited.add((x, y))

        # Find the next position
        dx, dy = directions[direction]
        new_x, new_y = x + dx, y + dy

        # Check if the guard is out of the map
        if check_bounds(lab_map, new_x, new_y) and lab_map[new_x][new_y] == "#":
            direction = rotate(direction)
        else:
            x, y = new_x, new_y
        
        # If we've visited this position before in same direction, we have a loop
        if (((x, y, direction)) in position_directions):
            return True, unique_visited
        else:
            position_directions.add((x, y, direction))

    return False, unique_visited

def find_initial_position(lab_map):
    for i in range(len(lab_map)):
        for j in range(len(lab_map[i])):
            if lab_map[i][j] in ["^", ">", "v", "<"]:
                return i, j, lab_map[i][j]

# Part 1
x, y, direction = find_initial_position(lab_map)
_, unique_positions = move_guard(lab_map, x, y, direction)
print(f"Positions guard visits: {len(unique_positions)}")

# Part 2 - this is fairly slow, but works
loop_count = 0
unique_positions.remove((x, y))
for pos in unique_positions:
    map_copy = [row[:] for row in lab_map]
    map_copy[pos[0]][pos[1]] = "#"
    if move_guard(map_copy, x, y, direction)[0]:
        loop_count += 1

print(f"Number of possible loops: {loop_count}")
