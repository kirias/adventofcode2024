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
        self.visited = visited
        self.start = visited
        self.x = x
        self.y = y
        self.prev_visits = []

    def visit(self, speed_down, speed_right):
        self.prev_visits.append((speed_down, speed_right))
        self.visited = True

    def visited_check(self, speed_down, speed_right):
        for last_visit in self.prev_visits:
            if last_visit == (speed_down, speed_right):
                return True
        return False
    
    def reset(self):
        self.prev_visits = []
        self.visited = self.start

    def __repr__(self) -> str:
        return f"({self.y=}, {self.x=})"


cells = []
start = None

count_obst = 0

def print_cell():
    print('--------')
    for row in cells:
        for cell in row:
            if cell.obstacle:
                print('#', end='')
            elif cell.visited:
                print('x', end='')
            else:
                print('.', end='')
        print('')

def check_loop(start, speed_down, speed_right, with_visited = False):
    global cells
    visited_cells = set()
    try:
        while True:
            if start.y + speed_down < 0 or start.x + speed_right < 0:
                raise IndexError()
            next = cells[start.y + speed_down][start.x + speed_right]
            while next.obstacle:
                speed_down, speed_right = rotate90(speed_down, speed_right)
                next = cells[start.y + speed_down][start.x + speed_right]
            if with_visited:
                visited_cells.add(next)
            start = next
            # print_cell()
            if (next.visited_check(speed_down, speed_right)):
                return -1, None
            next.visit(speed_down, speed_right)
    except IndexError:
        count_visited = 0
        for row in cells:
            for cell in row:
                if cell.visited:
                    count_visited += 1
        return count_visited, visited_cells

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

    count_visited, visited_cells = check_loop(start, speed_down, speed_right, True)

    part1_end_time = time.time()
    print(f"Part 1: {count_visited}, time: {part1_end_time - start_time}")

    for cell in visited_cells:
        if cell == start:
            continue
        for reset_row in cells:
            for reset_cell in reset_row:
                reset_cell.reset()

        cell.obstacle = True
        if check_loop(start, speed_down, speed_right) == (-1, None):
            count_obst += 1
        cell.obstacle = False

    print(f"Part 2: {count_obst}, time: {time.time() - part1_end_time}")

    # Part 1: 5409, time: 0.010045
    # Part 2: 2022, time: 15.96109




