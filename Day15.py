import time


start_time = time.time()

m = []

class Cell:
    def __init__(self, c, m, y, x):
        self.wall = False
        self.box = False
        self.robot = False
        self.empty = False

        self.y = y
        self.x = x
        self.m = m

        if c == '#':
            self.wall = True
        elif c == 'O':
            self.box = True
        elif c == '@':
            self.robot = True
        else:
            self.empty = True
    
    def print_c(self):
        if self.wall:
            print('#', end = '')
        elif self.robot:
            print('@', end = '')
        elif self.empty:
            print('.', end = '')
        elif self.box:
            print('0', end = '')
    
    def gps(self):
        if self.box:
            return 100 * self.y + self.x
        else:
            return 0

    def move(self, d):
        dy, dx = d
        if self.wall:
            return False
        if self.empty:
            return True
        if self.m[self.y + dy][self.x + dx].move(d):
            if self.robot:
                self.m[self.y][self.x] = Cell('.', self.m, self.y, self.x)
            self.y += dy
            self.x += dx
            self.m[self.y][self.x] = self
            return True

robot = None

movements = []
movements_parse = False

with open('inputs/15.txt', 'r') as file:
    for y, line in enumerate(file):
        if len(line.rstrip()) == 0:
            movements_parse = True
            continue
        if not movements_parse:
            row = []
            for x, c in enumerate(line.rstrip()):
                cell = Cell(c, m, y, x)
                row.append(cell)
                if cell.robot:
                    robot = cell
            m.append(row)
        else:
            for c in line.rstrip():
                if c == '<':
                    movements.append((0, -1))
                elif c == '>':
                    movements.append((0, 1))
                elif c == '^':
                    movements.append((-1, 0))
                elif c == 'v':
                    movements.append((1, 0))

def sum_gps(m):
    sum = 0
    for row in m:
        for cell in row:
            sum += cell.gps()
    return sum

for move in movements:
    robot.move(move)

print(f"Part 1: {sum_gps(m)}") # 1559280


class Cell2:
    def __init__(self, c, m, y, x):
        self.wall = False
        self.box = False
        self.robot = False
        self.empty = False
        self.connected = None

        self.y = y
        self.x = x
        self.m = m

        self.c = c

        if c == '#':
            self.wall = True
        elif c in '[]':
            self.box = True
        elif c == '@':
            self.robot = True
        else:
            self.empty = True

    def set_connected(self, c):
        self.connected = c
    
    def print_c(self):
        print(self.c, end = '')
 
    
    def gps(self):
        if self.c == '[':
            return 100 * self.y + self.x
        else:
            return 0

    def can_move(self, d, moving_set):
        moving_set.add(self)
        dy, dx = d
        if self.wall:
            return False
        if self.empty:
            return True
        next_cell = self.m[self.y + dy][self.x + dx]
        if next_cell == self.connected:
            if next_cell.can_move(d, moving_set):
                return True
        else:
            if next_cell.can_move(d, moving_set) and (self.connected == None or self.connected in moving_set or self.connected.can_move(d, moving_set)):
                return True
        return False
    
    def move(self, d, moving_set):
        moving_set.add(self)
        dy, dx = d
        if self.wall:
            return False
        if self.empty:
            return True
        next_cell = self.m[self.y + dy][self.x + dx]
        if next_cell == self.connected:
            if next_cell.move(d, moving_set):
                self.m[self.y][self.x] = Cell2('.', self.m, self.y, self.x)
                self.y += dy
                self.x += dx
                self.m[self.y][self.x] = self
                return True
        else:
            if next_cell.move(d, moving_set) and (self.connected == None or self.connected in moving_set or self.connected.move(d, moving_set)):
                self.m[self.y][self.x] = Cell2('.', self.m, self.y, self.x)
                self.y += dy
                self.x += dx
                self.m[self.y][self.x] = self
                return True
        return False

m = []
movements = []
movements_parse = False
with open('inputs/15.txt', 'r') as file:
    for y, line in enumerate(file):
        if len(line.rstrip()) == 0:
            movements_parse = True
            continue
        if not movements_parse:
            row = []
            for x, c in enumerate(line.rstrip()):
                if c == '#':
                    cell = Cell2('#', m, y, x * 2)
                    row.append(cell)
                    cell = Cell2('#', m, y, x * 2 + 1)
                    row.append(cell)
                elif c == 'O':
                    cell1 = Cell2('[', m, y, x * 2)
                    row.append(cell1)
                    cell2 = Cell2(']', m, y, x * 2 + 1)
                    row.append(cell2)
                    cell1.set_connected(cell2)
                    cell2.set_connected(cell1)
                elif c == '.':
                    cell = Cell2('.', m, y, x * 2)
                    row.append(cell)
                    cell = Cell2('.', m, y, x * 2 + 1)
                    row.append(cell)
                elif c == '@':
                    cell = Cell2('@', m, y, x * 2)
                    row.append(cell)
                    robot = cell
                    cell = Cell2('.', m, y, x * 2 + 1)
                    row.append(cell)
            m.append(row)
        else:
            for c in line.rstrip():
                if c == '<':
                    movements.append((0, -1))
                elif c == '>':
                    movements.append((0, 1))
                elif c == '^':
                    movements.append((-1, 0))
                elif c == 'v':
                    movements.append((1, 0))

for move in movements:
    if robot.can_move(move, set()):
        robot.move(move, set())

print(f"Part 2: {sum_gps(m)}") # 1576353

print(f"Time: {time.time() - start_time}") # 0.0462
