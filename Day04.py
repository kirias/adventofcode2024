matrix = []
with open('inputs/04.txt', 'r') as file:
    for line in file:
        matrix_row = []
        matrix.append(matrix_row)
        for char in line:
            matrix_row.append(char)

xmas_total = 0

def count_xmas(r, c):
    count = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            for i, char in enumerate('MAS'):
                next_i = r + di * (i + 1)
                next_j = c + dj * (i + 1)
                if (next_i < 0 or next_j < 0 or next_i >= len(matrix) or next_j >= len(matrix[next_i])):
                    break

                if matrix[next_i][next_j] == char:
                    if char == 'S':
                        count += 1
                else:
                    break;
    return count

for row_i in range(len(matrix)):
    row = matrix[row_i]
    for col_i in range(len(row)):
        if row[col_i] == 'X':
            xmas_total += count_xmas(row_i, col_i)

print(f"Part 1: {xmas_total}")

xmas_total = 0

def is_x_mas(r, c):
    count_mas = 0
    for i_offs in [-1, 1]:
        di = 1 if i_offs == -1 else -1
        for j_offs in [-1, 1]:
            dj = 1 if j_offs == -1 else -1
            for i, char in enumerate('MAS'):
                next_i = r + i_offs + di * i
                next_j = c + j_offs + dj * i
                if (next_i < 0 or next_j < 0 or next_i >= len(matrix) or next_j >= len(matrix[next_i])):
                    break

                if matrix[next_i][next_j] == char:
                    if i == 2:
                        count_mas += 1
                else:
                    break;
    return count_mas == 2

for row_i in range(len(matrix)):
    row = matrix[row_i]
    for col_i in range(len(row)):
        if row[col_i] == 'A':
            if is_x_mas(row_i, col_i):
                xmas_total += 1

print(f"Part 2: {xmas_total}")