import time

start_time = time.time()

matrix = []
width = 0
height = 0
regions = []
regions_borders = []
mapped_to_regions = set()

def is_valid(y, x):
    return x >=0 and y >= 0 and x < width and y < height

def get_region_id(y, x):
    return matrix[y][x] if is_valid(y, x) else None

def check_region(start):
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

            for (y_neighbour, x_neighbour) in [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]:
                if get_region_id(y_neighbour, x_neighbour) == reg_id:
                    to_check_list.append((y_neighbour, x_neighbour))
                else:
                    regions_borders[-1] += 1
        

with open('inputs/12.txt', 'r') as file:
    for y, line in enumerate(file):
        row = []
        matrix.append(row)
        for x, ch in enumerate(line.rstrip()):
            row.append(ch)

height = len(matrix)
width = len(matrix[0])

for row in range(height):
    for cell in range(width):
        if (row, cell) not in mapped_to_regions:
            check_region((row, cell))

sum = 0
for i, region in enumerate(regions):
    sum += len(region) * regions_borders[i]

print(f"Part 1: {sum}") # 1477762

sum2 = 0

def count_borders_x(min_x, max_x, y_line, region_id, top):
    border = False
    borders = 0
    neighbour_offset = -1 if top else 1
    for dx in range(min_x, max_x + 1):
        if (y_line, dx) in region and get_region_id(y_line + neighbour_offset, dx) != region_id:
            border = True
        elif border:
            borders += 1
            border = False
    if border:
        borders += 1
    return borders

def count_borders_y(min_y, max_y, x_line, region_id, top):
    border = False
    borders = 0
    neighbour_offset = -1 if top else 1
    for dy in range(min_y, max_y + 1):
        if (dy, x_line) in region and get_region_id(dy, x_line + neighbour_offset) != region_id:
            border = True
        elif border:
            borders += 1
            border = False
    if border:
        borders += 1
    return borders

for region in regions:
    (y, x) = next(iter(region))
    id = matrix[y][x]
    min_y = min([y for (y, _) in region])
    max_y = max([y for (y, _) in region])
    min_x = min([x for (_, x) in region])
    max_x = max([x for (_, x) in region])
    borders = 0
    for scan_y in range(min_y, max_y + 1):
        borders += count_borders_x(min_x, max_x, scan_y, id, True)
        borders += count_borders_x(min_x, max_x, scan_y, id, False)

    for scan_x in range(min_x, max_x + 1):
        borders += count_borders_y(min_y, max_y, scan_x, id, True)
        borders += count_borders_y(min_y, max_y, scan_x, id, False)

    sum2 += len(region) * borders

print(f"Part 2: {sum2}") # 923480

print(f"Time: {time.time() - start_time}") # 0.04740
