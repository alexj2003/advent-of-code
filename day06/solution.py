# Read input
lab_map = []
with open("input.txt") as f:
    for line in f:
        lab_map.append(list(line.strip()))

# Part 1
def update_guard(lab_map):
    # Find the starting position of the guard
    for i in range(len(lab_map)):
        for j in range(len(lab_map[i])):
            if lab_map[i][j] in ["^", ">", "v", "<"]:
                guard_direction = lab_map[i][j]
                
                # Update the guard position
                if guard_direction == "^":
                    if lab_map[i - 1][j] == "#":
                        # Turn right
                        new_position = (i, j + 1)
                        new_direction = ">"
                    else:
                        # Move up
                        new_position = (i - 1, j)
                        new_direction = "^"
                elif guard_direction == ">":
                    if lab_map[i][j + 1] == "#":
                        # Turn down
                        new_position = (i + 1, j)
                        new_direction = "v"
                    else:
                        # Move right
                        new_position = (i, j + 1)
                        new_direction = ">"
                elif guard_direction == "v":
                    if lab_map[i + 1][j] == "#":
                        # Turn left
                        new_position = (i, j - 1)
                        new_direction = "<"
                    else:
                        # Move down
                        new_position = (i + 1, j)
                        new_direction = "v"
                else:
                    if lab_map[i][j - 1] == "#":
                        # Turn up
                        new_position = (i - 1, j)
                        new_direction = "^"
                    else:
                        # Move left
                        new_position = (i, j - 1)
                        new_direction = "<"
                
                # Update map
                lab_map[i][j] = "X"
                lab_map[new_position[0]][new_position[1]] = new_direction

                # Check if the guard is out of the map
                if 0 <= new_position[0] < len(lab_map) and 0 <= new_position[1] < len(lab_map[0]):
                    return lab_map, True
                else:
                    return lab_map, False

guard_in_map = True
while guard_in_map:
    lab_map, guard_in_map = update_guard(lab_map)

count = sum(x.count("X") for x in lab_map)
print(f"Positions guard visits: {count}")
