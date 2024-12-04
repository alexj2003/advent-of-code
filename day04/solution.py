# Read file
wordsearch = []
with open("input.txt") as f:
    for line in f:
        wordsearch.append(list(line.strip()))

# Part 1
word = "XMAS"
count = 0
search_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(len(wordsearch)):
    for j in range(len(wordsearch[0])):
        for direction in search_directions:
            new_word = ""
            for k in range(len(word)):
                if 0 <= i + k * direction[0] < len(wordsearch) and 0 <= j + k * direction[1] < len(wordsearch[0]):
                    new_word += wordsearch[i + k * direction[0]][j + k * direction[1]]
                else:
                    break
            if new_word == word:
                count += 1

print(f"Count of {word}: {count}")
