import time

start_time = time.time()

locks = []
keys = []


MAX_HEIGHT = 5

def process_fig(lines):
    heights = []
    lock = lines[0][0] == '#'
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            if lines[j][i] != lines[0][i]:
                if lock:
                    heights.append(j - 1)
                else:
                    heights.append(MAX_HEIGHT - j + 1)
                break
    if lock:
        locks.append(heights)
    else:
        keys.append(heights)


with open('inputs/25.txt', 'r') as file:
    current_fig = []
    for y, line in enumerate(file):
        if line.rstrip():
            current_fig.append(line.rstrip())
        else:
            process_fig(current_fig)
            current_fig.clear()
    process_fig(current_fig)

count_match = 0

for key in keys:
    for lock in locks:
        match = True
        for i in range(len(key)):
            if key[i] + lock[i] > MAX_HEIGHT:
                match = False
                break
        if match:
            count_match += 1

print(f"Part 1: {count_match}") # 2840
