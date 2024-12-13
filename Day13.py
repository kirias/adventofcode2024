import time
import re

start_time = time.time()

def solve(xa, ya, xb, yb, xp, yp, prize_offset):
    xp += prize_offset
    yp += prize_offset
    p1 = (xb * yp / yb - xp) / (ya * xb / yb - xa)
    p2 = (xa * yp / ya - xp) / (yb * xa / ya - xb)
    
    p1_int = round(p1)
    p2_int = round(p2)

    if p1_int * xa + p2_int * xb == xp and p1_int * ya + p2_int * yb == yp:
        return (p1_int, p2_int)
    return (0, 0)

sum1 = 0
sum2 = 0

with open('inputs/13.txt', 'r') as file:
    while True:
        line = file.readline().strip()
        if len(line) == 0:
            break
        
        match = re.match(r'Button \w: X\+(\d+), Y\+(\d+)', line)
        xa = int(match.groups()[0])
        ya = int(match.groups()[1])

        line = file.readline().strip()
        match = re.match(r'Button \w: X\+(\d+), Y\+(\d+)', line)
        xb = int(match.groups()[0])
        yb = int(match.groups()[1])

        line = file.readline().strip()
        match = re.match(r'Prize: X=(\d+), Y=(\d+)', line)
        xp = int(match.groups()[0])
        yp = int(match.groups()[1])

        line = file.readline()

        (p1, p2) = solve(xa, ya, xb, yb,xp, yp, 0)
        if p1 != 0 and p2 != 0:
            sum1 += 3 * p1 + p2

        (p1, p2) = solve(xa, ya, xb, yb,xp, yp, 10000000000000)
        if p1 != 0 and p2 != 0:
            sum2 += 3 * p1 + p2


print(f"Part 1: {sum1}") # 29201
print(f"Part 2: {sum2}") # 104140871044942

print(f"Time: {time.time() - start_time}") # 0.00137
