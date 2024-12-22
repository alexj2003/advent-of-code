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
    for n in nums:
        for _ in range(2000):
            n = next_number(n)
        answers.append(n)
    
    return answers

# Test data
data = """1
10
100
2024"""

# Read data
with open("input.txt", "r") as f:
    data = f.read()

# Parse data
data = [int(x) for x in data.strip().split("\n")]

# Part 1
nums = calc_numbers(data)
print(f"Part 1: {sum(nums)}")
