# Read input 
reports = []
with open("input.txt") as f:
    for line in f:
        report = line.strip().split()
        reports.append(report)

# Part 1
safe_count = 0

for report in reports:
    differences = [int(b) - int(a) for a, b in zip(report, report[1:])]
    
    if all(1 <= diff <= 3 for diff in differences):
        safe_count += 1
    elif all(-3 <= diff <= -1 for diff in differences):
        safe_count += 1

print(f"Safe count: {safe_count}")
