import time

start_time = time.time()

matrix = []
width = 0
height = 0
region_starts = []
regions = []
regions_borders = []
mapped_to_regions = set()

def is_valid(y, x):
    return x >=0 and y >= 0 and x < width and y < height

def check_region(start):
    if start not in mapped_to_regions:
        to_check_list = []
        region = set()
        regions.append(region)
        regions_borders.append(0)
        reg_id = matrix[start[0]][start[1]]

        to_check_list.append(start)
        while len(to_check_list) > 0:
            check = to_check_list.pop()
            if check not in mapped_to_regions:
                mapped_to_regions.add(check)
                region.add(check)
                y, x = check

                if is_valid(y - 1, x) and matrix[y - 1][x] == reg_id:
                    to_check_list.append((y - 1, x))
                else:
                    regions_borders[-1] += 1

                if is_valid(y, x - 1) and matrix[y][x - 1] == reg_id:
                    to_check_list.append((y, x - 1))
                else:
                    regions_borders[-1] += 1

                if is_valid(y + 1, x) and matrix[y + 1][x] == reg_id:
                    to_check_list.append((y + 1, x))
                else:
                    regions_borders[-1] += 1

                if is_valid(y, x + 1) and matrix[y][x + 1] == reg_id:
                    to_check_list.append((y, x + 1))
                else:
                    regions_borders[-1] += 1
        

with open('inputs/12.txt', 'r') as file:
    for y, line in enumerate(file):
        row = []
        matrix.append(row)
        for x, ch in enumerate(line.rstrip()):
            row.append(ch)
            region_starts.append((y, x))

height = len(matrix)
width = len(matrix[0])

for start in region_starts:
    check_region(start)

sum = 0
for i, region in enumerate(regions):
    sum += len(region) * regions_borders[i]

print(f"Part 1: {sum}") # 1477762

sum2 = 0

for region in regions:
    (y, x) = next(iter(region))
    id = matrix[y][x]
    min_y = min([y for (y, _) in region])
    max_y = max([y for (y, _) in region])
    min_x = min([x for (_, x) in region])
    max_x = max([x for (_, x) in region])
    borders = 0
    for scan_y in range(min_y, max_y + 1):
        border = False
        for dx in range(min_x, max_x + 1):
            if (scan_y, dx) in region and (not is_valid(scan_y - 1, dx) or matrix[scan_y - 1][dx] != id):
                border = True
            elif border:
                borders += 1
                border = False
        if border:
            borders += 1
            border = False

    for scan_y in range(max_y, min_y - 1, -1):
        border = False
        for dx in range(min_x, max_x + 1):
            if (scan_y, dx) in region and (not is_valid(scan_y + 1, dx) or matrix[scan_y + 1][dx] != id):
                border = True
            elif border:
                borders += 1
                border = False
        if border:
            borders += 1
            border = False

    for scan_x in range(min_x, max_x + 1):
        border = False
        for dy in range(min_y, max_y + 1):
            if (dy, scan_x) in region and (not is_valid(dy, scan_x - 1) or matrix[dy][scan_x - 1] != id):
                border = True
            elif border:
                borders += 1
                border = False
        if border:
            borders += 1
            border = False

    for scan_x in range(max_x, min_x - 1, -1):
        border = False
        for dy in range(min_y, max_y + 1):
            if (dy, scan_x) in region and (not is_valid(dy, scan_x + 1) or matrix[dy][scan_x + 1] != id):
                border = True
            elif border:
                borders += 1
                border = False
        if border:
            borders += 1
            border = False

    sum2 += len(region) * borders

print(f"Part 2: {sum2}") # 923480

print(f"Time: {time.time() - start_time}") # 0.04740
