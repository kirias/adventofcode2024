import time
import re

WIDTH = 101
HEIGHT = 103
SECONDS = 100

q1 = q2 = q3 = q4 = 0

start_time = time.time()

with open('inputs/14.txt', 'r') as file:
    while True:
        line = file.readline().strip()
        if len(line) == 0:
            break
        
        match = re.match(r'p=(\d+),(\d+) v=(-*\d+),(-*\d+)', line)
        x = int(match.groups()[0])
        y = int(match.groups()[1])
        vx = int(match.groups()[2])
        vy = int(match.groups()[3])

        x = (x + vx * SECONDS) % WIDTH
        y = (y + vy * SECONDS) % HEIGHT

        if x < 50:
            if y < 51:
                q1 += 1
            elif y > 51:
                q2 += 1
        elif x > 50:
            if y < 51:
                q3 += 1
            elif y > 51:
                q4 += 1

print(f"Part 1: {q1 * q2 * q3 * q4}") # 226548000

robots = []
robots_current = set()
speeds = []
with open('inputs/14.txt', 'r') as file:
    while True:
        line = file.readline().strip()
        if len(line) == 0:
            break
        
        match = re.match(r'p=(\d+),(\d+) v=(-*\d+),(-*\d+)', line)
        x = int(match.groups()[0])
        y = int(match.groups()[1])
        vx = int(match.groups()[2])
        vy = int(match.groups()[3])
        robots.append((x, y))
        speeds.append((vx, vy))

def recalc_robots(seconds):
    global robots_current
    robots_current = set()
    duplicates = 0
    for i in range(len(robots)):
        new_val = ((robots[i][0] + speeds[i][0] * seconds) % WIDTH,
                             (robots[i][1] + speeds[i][1] * seconds) % HEIGHT
                             )
        robots_current.add(new_val)

def print_robots(f, seconds):
    f.write(f'Seconds: {seconds}\n')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in robots_current:
                f.write('0')
            else:
                f.write('.')
        f.write('\n')

max_neighbours = 0
max_neighbours_secs = 0

def calc_max_neighbours(secs):
    global max_neighbours, max_neighbours_secs, robots_current
    touching = 0
    for (x, y) in robots_current:
        for of_x in range(-1, 2):
            for of_y in range(-1, 2):
                if of_x == 0 and of_y == 0:
                    continue
                if (x + of_x, y + of_y) in robots_current:
                    touching += 1
    if touching > max_neighbours:
        max_neighbours = touching
        max_neighbours_secs = secs
        print(f'New max neighbours {max_neighbours} at {max_neighbours_secs}')

max_dups = 0
max_dups_sec = 0

secs = 0

while secs < 10000:
    # f = open(f"out{secs}.txt", "a")
    for i in range(200):
        recalc_robots(secs)
        # print_robots(f, secs)
        calc_max_neighbours(secs)
        secs += 1
    # f.close()

print(f"Part 2: {max_neighbours_secs}") # 7753

# print(f"Time: {time.time() - start_time}") #
