import time

start_time = time.time()

matrix = []
heads = []

with open('inputs/10.txt', 'r') as file:
    for y, line in enumerate(file):
        row = []
        matrix.append(row)
        for x, c in enumerate(line.rstrip()):
            row.append(int(c))
            if c == '0':
                heads.append((y, x))

width = len(matrix[0])
height = len(matrix)

def count_heads(st_y, st_x):
    cells = []
    found = set()
    cells.append((st_y, st_x))

    while len(cells) > 0:
        (y, x) = cells.pop()
        if matrix[y][x] == 9:
            found.add((y, x))
        else:
            if y - 1 >= 0 and matrix[y - 1][x] == matrix[y][x] + 1:
                cells.append((y - 1, x))
            if x - 1 >= 0 and matrix[y][x - 1] == matrix[y][x] + 1:
                cells.append((y, x - 1))

            if y + 1 < height and matrix[y + 1][x] == matrix[y][x] + 1:
                cells.append((y + 1, x))
            if x + 1 < width and matrix[y][x + 1] == matrix[y][x] + 1:
                cells.append((y, x + 1))
    return len(found)

def count_trails(st_y, st_x):
    cells = []
    found = 0
    cells.append((st_y, st_x))

    while len(cells) > 0:
        (y, x) = cells.pop()
        if matrix[y][x] == 9:
            found += 1
        else:
            if y - 1 >= 0 and matrix[y - 1][x] == matrix[y][x] + 1:
                cells.append((y - 1, x))
            if x - 1 >= 0 and matrix[y][x - 1] == matrix[y][x] + 1:
                cells.append((y, x - 1))

            if y + 1 < height and matrix[y + 1][x] == matrix[y][x] + 1:
                cells.append((y + 1, x))
            if x + 1 < width and matrix[y][x + 1] == matrix[y][x] + 1:
                cells.append((y, x + 1))
    return found

sum_heads = 0
sum_trails = 0
for (y, x) in heads:
    sum_heads += count_heads(y, x)
    sum_trails += count_trails(y, x)
    

print(f"Part 1: {sum_heads}") # 638
print(f"Part 2: {sum_trails}") # 1289

# print(f"Time: {time.time() - start_time}")

