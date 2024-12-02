# Read input 
reports = []
with open("input.txt") as f:
    for line in f:
        report = line.strip().split()
        reports.append(report)

# Part 1
def is_safe(report):
    differences = [int(b) - int(a) for a, b in zip(report, report[1:])]
    return all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences)

safe_count = 0
for report in reports:
    safe_count += is_safe(report)

print(f"Safe count: {safe_count}")

# Part 2
safe_count = 0
for report in reports:
    if is_safe(report):
        safe_count += 1
    else:
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]
            if is_safe(new_report):
                safe_count += 1
                break

print(f"Modified safe count: {safe_count}")
