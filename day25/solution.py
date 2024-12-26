# Check if a key fits
def check_key(key, lock):
    key = key.split("\n")
    lock = lock.split("\n")

    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j] == "#" and lock[i][j] == "#":
                return False
    return True

# Parse data
def parse_data(data):
    shapes = data.split("\n\n")
    keys = []
    locks = []

    for shape in shapes:
        split_shape = shape.split("\n")

        if split_shape[0] == ".....":
            keys.append(shape)
        elif split_shape[0] == "#####":
            locks.append(shape)
    
    return keys, locks

# Test data 
data = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

# Read input
with open("input.txt", "r") as file:
    data = file.read()

keys, locks = parse_data(data)

# Check each key with each lock
count = 0
for key in keys:
    for lock in locks:
        if check_key(key, lock):
            count += 1

print(f"Day 25: {count}")
