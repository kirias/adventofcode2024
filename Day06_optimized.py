import time

speed_down = -1
speed_right = 0

start_time = time.time()

def rotate90(speed_down, speed_right):
    if speed_down == -1 or speed_down == 1:
        new_speed_down = 0
    else:
        new_speed_down = 1 if speed_right == 1 else -1
    
    if speed_right == 1 or speed_right == -1:
        new_speed_right = 0
    else:
        new_speed_right = 1 if speed_down == -1 else -1
    return new_speed_down, new_speed_right

class Cell:
    def __init__(self, obstacle, visited, x, y):
        self.obstacle = obstacle
        self.start = visited
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.y=}, {self.x=})"

cells = []
start = None

def check_loop(start, speed_down, speed_right):
    global cells
    visits = set()
    try:
        while True:
            if start.y + speed_down < 0 or start.x + speed_right < 0:
                raise IndexError()
            next = cells[start.y + speed_down][start.x + speed_right]
            while next.obstacle:
                speed_down, speed_right = rotate90(speed_down, speed_right)
                next = cells[start.y + speed_down][start.x + speed_right]

            start = next
            # print_cell()

            if (next.y, next.x, speed_down, speed_right) in visits:
                return None
            visits.add((next.y, next.x, speed_down, speed_right))
    except IndexError:
        cells_visited = set((v[0], v[1]) for v in visits)
        return cells_visited
    
def binary_search_closest(arr, x, greater, index = False):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid
        elif arr[mid] > x:
            high = mid
        if low + 1 == high or low == high:
            if greater:
                if arr[low] > x:
                    return low if index else arr[low]
                elif arr[high] > x:
                    return high if index else arr[high]
                else:
                    return -1
            else:
                if arr[high] < x:
                    return high if index else arr[high]
                elif arr[low] < x:
                    return low if index else arr[low]
                else:
                    return -1
            
    return -1
    
def next_obstacle(start, speed_down, speed_right):
    global cells, x_obst, y_obst
    res = 0
    if speed_down == 0:
        res = binary_search_closest(y_obst[start.y], start.x, speed_right == 1)
        if res >= 0:
            return cells[start.y][res]
        else:
            return None
    else:
        res = binary_search_closest(x_obst[start.x], start.y, speed_down == 1)
        if res >= 0:
            return cells[res][start.x]
        else:
            return None
    
def check_loop_w_cache(start, speed_down, speed_right):
    global cells, x_obst, y_obst
    visits = set()
    try:
        while True:
            if start.y + speed_down < 0 or start.x + speed_right < 0:
                raise IndexError()
            next = next_obstacle(start, speed_down, speed_right)
            if next == None:
                return False
            
            next = cells[next.y - speed_down][next.x - speed_right]

            speed_down, speed_right = rotate90(speed_down, speed_right)

            start = next
            if (next.x, next.y, speed_down, speed_right) in visits:
                return True
            visits.add((next.x, next.y, speed_down, speed_right))
    except IndexError:
        return False
    

with open('inputs/06.txt', 'r') as file:
    for y, line in enumerate(file):
        cells_row = []
        cells.append(cells_row)
        for x, ch in enumerate(line.rstrip()):
            if ch == '.':
                cells_row.append(Cell(False, False, x, y))
            elif ch == '#':
                cells_row.append(Cell(True, False, x, y))
            else:
                start = Cell(False, True, x, y)
                cells_row.append(start)

    x_obst = [[] for i in range(len(cells[0]))]
    y_obst = [[] for i in range(len(cells))]

    for y in range(len(cells)):
        for x in range(len(cells[y])):
            if cells[y][x].obstacle:
                x_obst[x].append(y)
                y_obst[y].append(x)

    visited_cells = check_loop(start, speed_down, speed_right)

    part1_end_time = time.time()
    print(f"Part 1: {len(visited_cells)}, time: {part1_end_time - start_time}")

    count_obst = 0
    for cell_coords in visited_cells:
        cell = cells[cell_coords[0]][cell_coords[1]]
        if cell == start:
            continue

        cell.obstacle = True

        next_bigger_index_x = binary_search_closest(x_obst[cell.x], cell.y, True, True)
        if next_bigger_index_x >= 0:
            x_obst[cell.x].insert(next_bigger_index_x, cell.y)
        else:
            x_obst[cell.x].append(cell.y)
            next_bigger_index_x = len(x_obst[cell.x]) - 1

        next_bigger_index_y = binary_search_closest(y_obst[cell.y], cell.x, True, True)
        if next_bigger_index_y >= 0:
            y_obst[cell.y].insert(next_bigger_index_y, cell.x)
        else:
            y_obst[cell.y].append(cell.x)
            next_bigger_index_y = len(y_obst[cell.y]) - 1

        if check_loop_w_cache(start, speed_down, speed_right):
            count_obst += 1

        cell.obstacle = False
        del x_obst[cell.x][next_bigger_index_x]
        del y_obst[cell.y][next_bigger_index_y]

    print(f"Part 2: {count_obst}, time: {time.time() - part1_end_time}")

    # Part 1: 5409, time: 0.00894021987915039
    # Part 2: 2022, time: 0.39230966567993164




