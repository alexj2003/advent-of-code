# Read input
with open("input.txt", "r") as f:
    data = f.read().strip().split()

# Update an individual stone
def update_stone(stone):
    if stone == "0":
        return ["1"]
    
    stone_len = len(stone) % 2
    if stone_len == 0:
        new_len = len(stone) // 2
        a, b = str(stone)[:new_len], str(stone)[new_len:]
        return [str(int(a)), str(int(b))]

    return [str(int(stone) * 2024)]

# Update all stones once
def blink(data):
    new_data = []
    for stone in data:
        new_data += update_stone(stone)
    return new_data

# Update all stones n times
def run_blinks(data, n):
    for _ in range(n):
        data = blink(data)
    return data

# Test data
# data = "0 1 10 99 999".split()
# print(len(run_blinks(data, 1))) # 7

# data = "125 17".split()
# print(len(run_blinks(data, 6))) # 22
# print(len(run_blinks(data, 25))) # 55312

print(f"Part 1: {len(run_blinks(data, 25))}")
