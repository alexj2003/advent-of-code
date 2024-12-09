# Read input
def build_data(raw_data):
    data = []
    ids = set()
    for i, d in enumerate(raw_data):
        if i % 2 == 0:
            # Even index = ID number
            data += [int(i / 2)] * int(d)
            ids.add(int(i / 2))
        else:
            # Odd index = free space
            data += ["."] * int(d)
    return data, ids

# Calculate checksum
def calc_checksum(data):
    checksum = 0
    for i, d in enumerate(data):
        if d != ".":
            checksum += i * d
    return checksum

# Part 1 - fragment individual blocks
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

# Part 2 - fragment whole files
def fragment_files(data, ids):
    # Calculate file and span locations
    spans = []
    file_starts = {}

    i = 0
    while i < len(data):
        if data[i] == ".":
            start = i
            while i < len(data) and data[i] == ".":
                i += 1
            spans.append((start, i - start))
        else:
            if data[i] not in file_starts:
                file_starts[data[i]] = i
            i += 1

    for id in reversed(list(ids)):
        file_start = file_starts[id]
        file_size = data.count(id)

        # Find empty span large enough to fit file
        for span_id, (span_start, span_size) in enumerate(spans):
            if span_start < file_start and span_size >= file_size:
                # Move file
                file_end = file_start + file_size
                data[span_start:span_start + file_size] = data[file_start:file_end]
                data[file_start:file_end] = ["."] * file_size

                # Update span
                remaining_length = span_size - file_size
                if remaining_length == 0:
                    spans.pop(span_id)
                else:
                    spans[span_id] = (span_start + file_size, remaining_length)
                break
    return data

# Test data
# data, ids = build_data("2333133121414131402")
# fragmented = fragment(data)
# checksum = calc_checksum(fragmented)
# print(checksum)

# fragmented = fragment_files(data, ids)
# checksum = calc_checksum(fragmented)
# print(checksum)

# Part 1
with open("input.txt", "r") as file:
    data, ids = build_data(file.read().strip())

fragmented = fragment(data)
checksum = calc_checksum(fragmented)
print(f"Part 1: {checksum}")

# Part 2
fragmented = fragment_files(data, ids)
checksum = calc_checksum(fragmented)
print(f"Part 2: {checksum}")
