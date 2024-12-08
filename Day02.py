safe = 0

def is_safe(values, without_index):
    if without_index >= 0:
        del values[without_index]
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

print(f"Part 1: {safe}")

safe = 0
with open('inputs/02.txt', 'r') as file:
    for line in file:
        line_split = list(map(int, line.rstrip().split(' ')))
        unsafe_index = is_safe(line_split, -1)
        if unsafe_index == -1:
            safe += 1
            continue

        if (is_safe(line_split.copy(), unsafe_index) == -1 or
            is_safe(line_split.copy(), unsafe_index - 1) == -1 or
                (unsafe_index == 2 and is_safe(line_split.copy(), 0) == -1)):
            safe += 1
            continue

print(f"Part 2: {safe}")