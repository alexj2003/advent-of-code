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
def check_ordered(update, rules):
    for i, page in enumerate(update):
        check_pages = update[:i]
        if not set(check_pages).issubset(rules[page]):
            return False
    return True

def calc_middle(update):
    middle_index = int(len(update) // 2)
    return int(update[middle_index])

middle_total = 0
incorrect_updates = set()
for update in updates:
    if check_ordered(update, rules):
        update_list = list(update)
        middle_total += calc_middle(update_list)
    else:
        incorrect_updates.add(update)

print(f"Total of middle elements: {middle_total}")

# Part 2
def order_update(update, rules):
    ordered_update = list(update).copy()
    while not check_ordered(ordered_update, rules):
        for i in range(len(ordered_update)):
            for key, pages in rules.items():
                if key in ordered_update and ordered_update[i] in pages:
                    key_index = ordered_update.index(key)
                    page_index = ordered_update.index(ordered_update[i])
                    if page_index > key_index:
                        ordered_update.insert(key_index, ordered_update.pop(page_index))
    return ordered_update

middle_total = 0
for update in incorrect_updates:
    ordered_update = order_update(update, rules)
    middle_total += calc_middle(ordered_update)

print(f"Total of middle elements with updates ordered: {middle_total}")
