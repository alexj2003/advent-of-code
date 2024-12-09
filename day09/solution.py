# Read input
def build_data(raw_data):
    data = []
    for i, d in enumerate(raw_data):
        if i % 2 == 0:
            # Even index = ID number
            data += [int(i / 2)] * int(d)
        else:
            # Odd index = free space
            data += ["."] * int(d)
    return data

# Calculate checksum
def calc_checksum(data):
    checksum = 0
    for i, d in enumerate(data):
        if d != ".":
            checksum += i * d
    return checksum

# Fragment data
# Probably a more efficient way to do this
def fragment(data):
    while True:
        # Get index of last ID
        last_id = None
        for i, d in enumerate(reversed(data)):
            if d != ".":
                last_id = len(data) - i - 1
                break
        
        # Get index of first "."
        first_free = data.index(".")
        
        if first_free > last_id:
            return data

        # Swap
        data[first_free], data[last_id] = data[last_id], data[first_free]

# Test data
# data = build_data("2333133121414131402")
# fragmented = fragment(data)
# print(fragmented)
# checksum = calc_checksum(fragmented)
# print(checksum)

# Part 1
data = []
with open("input.txt", "r") as file:
    data = build_data(file.read().strip())

fragmented = fragment(data)
checksum = calc_checksum(fragmented)
print(f"Part 1: {checksum}")
