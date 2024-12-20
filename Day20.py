import time
from heapq import heappush, heappop

start_time = time.time()

maze = []
start_pos = (0, 0)
end = (0, 0)

class PriorityQueue:
    def __init__(self):
        self._container = []

    def empty(self):
        return not self._container
    
    def push(self, item):
        heappush(self._container, item)

    def pop(self):
        return heappop(self._container)
    
    def __repr__(self) -> str:
        return repr(self._container)
    
class Node:
    def __init__(self, coord, parent, cost, heuristic):
        self.coord = coord
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def contains(self, coord):
        if self.coord == coord:
            return True
        if self.parent != None:
            return self.parent.contains(coord)
        return False

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(initial, test_goal_reached, calc_next, calc_heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0, calc_heuristic(initial)))

    explored = { initial: 0 }
    shortest_length = None

    while not frontier.empty():
        current_node = frontier.pop()

        current_state = current_node.coord
        if test_goal_reached(current_state):
            if not shortest_length:
                shortest_length = current_node.cost
            continue
        for (child, cost) in calc_next(current_state):
            new_cost = current_node.cost + cost
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, calc_heuristic(child)))
    return explored, shortest_length

def calc_cheat_exits(initial, cheat_length, entry_cost):
    y, x = initial
    exits_count = 0
    for width in range(cheat_length + 1):
        for height in range(cheat_length + 1 - width):
            if width == 0 and height == 0:
                continue
            for dx in [0] if width == 0 else [-width, width]:
                 for dy in [0] if height == 0 else [-height, height]:
                    ny = y + dx
                    nx = x + dy
                    if ny >= 0 and nx >= 0 and ny < HEIGHT and nx < WIDTH:
                        if maze[ny][nx] == '.':
                            exit_cost = all_lengths_reverse.get((ny, nx))
                            if exit_cost != None:
                                if entry_cost + width + height + exit_cost + SAVE_CHEAT <= shortest:
                                    exits_count += 1
    return exits_count
        
def calc_next_steps(state):
    y, x = state
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny = y + dy
        nx = x + dx
        if ny >= 0 and nx >= 0 and ny < HEIGHT and nx < WIDTH:
            if maze[ny][nx] == '.':
                yield ((ny, nx), 1)

def calc_heuristics(state):
    y, x = state
    h = end[0] - y + end[1] - x
    return h

with open('inputs/20.txt', 'r') as file:
    for y, line in enumerate(file):
        row = []
        maze.append(row)
        for x, c in enumerate(line.rstrip()):
            if c == 'S':
                start_pos = (y, x)
                row.append('.')
            elif c == 'E':
                end = (y, x)
                row.append('.')
            else:
                row.append(c)

HEIGHT = len(maze)
WIDTH = len(maze[0])

all_lengths, shortest = astar(start_pos, lambda test : test == end, calc_next_steps, calc_heuristics)
all_lengths_reverse, shortest = astar(end, lambda test : test == start_pos, calc_next_steps, calc_heuristics)

LENGTH_FIRST_CHEAT = 2
LENGTH_SECOND_CHEAT = 20
SAVE_CHEAT = 100

count_cheats = 0;
for field, cost in all_lengths.items():
    if cost > shortest - SAVE_CHEAT - 1:
        continue
    count_cheats += calc_cheat_exits(field, LENGTH_FIRST_CHEAT, cost)


print(f"Part 1: {count_cheats}") # 1351

count_cheats = 0;
for field, cost in all_lengths.items():
    if cost + SAVE_CHEAT >= shortest:
        continue
    count_cheats += calc_cheat_exits(field, LENGTH_SECOND_CHEAT, cost)
print(f"Part 2: {count_cheats}") # 966130

print(f"Time: {time.time() - start_time}") # 1.44104
