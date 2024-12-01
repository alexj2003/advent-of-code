# Read input
with open("input.txt") as f:
    lines = f.readlines()

left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()

# Part 1
total = 0
for i in range(len(left_list)):
    total += abs(left_list[i] - right_list[i])
print(f"Total distance: {total}")

# Part 2
total = 0
for i in range(len(left_list)):
    total += left_list[i] * right_list.count(left_list[i])
print(f"Similarity score: {total}")
