from collections import Counter

# Read input
with open("input.txt", "r") as f:
    data = f.read().strip().split()

# Part 1

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

# Part 2
# Part 1 code was incredibly inefficient, so using a counter instead

def blink_v2(data):
    new_counts = Counter()
    for stone, count in data.items():
        if stone == "0":
            new_counts["1"] += count
        elif len(stone) % 2 == 0:
            new_len = len(stone) // 2
            a, b = str(int(str(stone)[:new_len])), str(int(str(stone)[new_len:]))
            new_counts[a] += count
            new_counts[b] += count
        else:
            new_counts[str(int(stone) * 2024)] += count
    return new_counts

def run_blinks_v2(data, n):
    counts = Counter(data)
    for _ in range(n):
        counts = blink_v2(counts)
    return counts

# Test data
# data = "125 17".split()
# print(sum(run_blinks_v2(data, 6).values())) # 22
# print(sum(run_blinks_v2(data, 25).values())) # 55312

print(f"Part 2: {sum(run_blinks_v2(data, 75).values())}")
