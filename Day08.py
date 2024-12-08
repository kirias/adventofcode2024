import time

start_time = time.time()

rows_c = 0
cols_c = 0
towers = {}


with open('inputs/08.txt', 'r') as file:
    for y, line in enumerate(file):
        rows_c += 1
        if cols_c == 0:
            cols_c = len(line.rstrip())
        for x, cell in enumerate(line.rstrip()):
            if cell != '.':
                if cell not in towers:
                    towers[cell] = []
                tower_entries = towers[cell]
                tower_entries.append((x, y))

def checkadd(intersects, coords):
    if coords[0] < 0 or coords[1] < 0:
        return False
    if coords[0] >= cols_c or coords[1] >= rows_c:
        return False
    intersects.add(coords)
    return True

intersects1 = set()
intersects2 = set()

for type_i in towers:
    type = towers[type_i]
    for i in range(len(type) - 1):
        for j in range(i + 1, len(type)):
            tower1 = type[i]
            tower2 = type[j]
            xdelt = tower2[0] - tower1[0]
            ydelt = tower2[1] - tower1[1]
            checkadd(intersects1, (tower1[0] - xdelt, tower1[1] - ydelt))
            checkadd(intersects1, (tower2[0] + xdelt, tower2[1] + ydelt))
            times = 0
            while checkadd(intersects2, (tower1[0] - xdelt * times, tower1[1] - ydelt * times)):
                times += 1
            times = 0
            while checkadd(intersects2, (tower2[0] + xdelt * times, tower2[1] + ydelt * times)):
                times += 1
            if xdelt % 3 == 0 and ydelt % 3 == 0:
                checkadd(intersects1, (tower1[0] + xdelt // 3, tower1[1] + ydelt // 3))
                checkadd(intersects2, (tower1[0] + xdelt // 3, tower1[1] + ydelt // 3))
                checkadd(intersects1, (tower2[0] - xdelt // 3, tower2[1] - ydelt // 3))
                checkadd(intersects2, (tower2[0] - xdelt // 3, tower2[1] - ydelt // 3))
        

print(f"Part 1: {len(intersects1)}") # 318
print(f"Part 2: {len(intersects2)}") # 1126

print(f"Time: {time.time() - start_time}") # 0.0009417

