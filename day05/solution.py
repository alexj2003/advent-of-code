# Read input
rules = dict()
updates = set()

with open("input.txt", "r") as f:
    for line in f:
        if '|' in line:
            before, after = line.strip().split('|')
            if after not in rules:
                rules[after] = set()
            rules[after].add(before)
        elif ',' in line:
            updates.add(tuple(line.strip().split(',')))

# Part 1
middle_total = 0
for update in updates:
    ordered = True
    for i, page in enumerate(update):
        if not ordered:
            break

        check_pages = update[:i]
        if not set(check_pages).issubset(rules[page]):
            ordered = False
            break
    
    if ordered:
        update_list = list(update)
        middle_index = int((len(update_list) - 1) / 2)
        middle_total += int(update_list[middle_index])

print(f"Total of middle elements: {middle_total}")
