safe = 0

def is_safe(values, index):
    if index >= 0:
        del values[index]
    prev_val = values[0]
    diffFirst = prev_val - values[1]
    if diffFirst == 0:
        return 1
    for level in range(1, len(values)):
        diff = prev_val - values[level]
        if diffFirst * diff < 0:
            return level
        if abs(diff) > 3 or diff == 0:
            return level
        prev_val = values[level]
    return -1

with open('inputs/02.txt', 'r') as file:
    for line in file:
        line_split = list(map(int, line.rstrip().split(' ')))
        if is_safe(line_split, -1) == -1:
            safe += 1

print("Part 1: {0}".format(safe))

safe = 0
with open('inputs/02.txt', 'r') as file:
    for line in file:
        line_split = list(map(int, line.rstrip().split(' ')))
        unsave_index = is_safe(line_split, -1)
        if unsave_index == -1:
            safe += 1
            continue

        if (is_safe(line_split.copy(), unsave_index) == -1 or
            is_safe(line_split.copy(), unsave_index - 1) == -1 or
                (unsave_index == 2 and is_safe(line_split.copy(), 0) == -1)):
            safe += 1
            continue

print("Part 2: {0}".format(safe))