from collections import defaultdict
from functools import cache

# Calculate next number in the sequence
@cache
def next_number(n):
    # Multiply by 64, mix and prune
    n1 = n * 64
    n = n ^ n1
    n = n % 16777216

    # Divide by 32, mix and prune
    n1 = n // 32
    n = n ^ n1
    n = n % 16777216

    # Multiply by 2048, mix and prune
    n1 = n * 2048
    n = n ^ n1
    n = n % 16777216

    return n

# Calculate 2000th number in each sequence
def calc_numbers(nums):
    answers = []
    changes = []
    for n in nums:
        # Track change of final digit for each of the 2000 numbers
        current_prices = []
        current_changes = []
        for _ in range(2000):
            prev = n % 10

            n = next_number(n)

            current_prices.append(n % 10)

            # Calculate change of final digit
            cur = n % 10
            current_changes.append(cur - prev)

        answers.append(n)
        changes.append((current_prices, current_changes))
    
    return answers, changes

# Find the best sequence of changes
# This is a little slow but not too bad
def calc_best_change(changes):
    change_sequences = defaultdict(int)

    for change in changes:
        current_prices, current_changes = change
        seq_seen = set()

        # Get all sequences of 4 changes
        for i in range(len(current_changes) - 3):
            seq = tuple(current_changes[i:i+4])
            val = current_prices[i+3]

            # Only consider first occurence of a sequence per buyer
            if seq in seq_seen:
                continue

            change_sequences[seq] += val
            seq_seen.add(seq)

    # Find the best sequence
    best_seq = max(zip(change_sequences.values(), change_sequences.keys()))[0]

    return best_seq

# Test data
data = """1
10
100
2024"""

data = """1
2
3
2024"""

# Read data
with open("input.txt", "r") as f:
    data = f.read()

# Parse data
data = [int(x) for x in data.strip().split("\n")]

# Part 1
nums, changes = calc_numbers(data)
print(f"Part 1: {sum(nums)}")

# Part 2
best_seq = calc_best_change(changes)
print(f"Part 2: {best_seq}")
