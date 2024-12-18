import time
from heapq import heappush, heappop

start_time = time.time()

WIDTH = 71
HEIGHT = 71
LIMIT_B = 1024

matrix = []
end = (HEIGHT - 1, WIDTH - 1)

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

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
    
    def contains(self, coord):
        if self.parent == None:
            return self.coord == coord
        return True if self.coord == coord else self.parent.contains(coord)

def astar(initial, test_goal_reached, calc_next, calc_heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0, calc_heuristic(initial)))

    explored = { initial: 0 }

    while not frontier.empty():
        current_node = frontier.pop()

        current_state = current_node.coord
        if test_goal_reached(current_state):
            return current_node
        for (child, cost) in calc_next(current_state):
            new_cost = current_node.cost + cost
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, calc_heuristic(child)))
    return None

def is_goal_reached(state):
    return end == state

def calc_next_steps(state):
    y, x = state
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny = y + dy
        nx = x + dx
        if ny >= 0 and nx >= 0 and ny < HEIGHT and nx < WIDTH:
            if matrix[ny][nx]:
                yield ((ny, nx), 1)

def calc_heuristics(state):
    y, x = state
    h = end[0] - y + end[1] - x
    return h

matrix = [[True for x in range(WIDTH)] for y in range(HEIGHT)]

with open('inputs/18.txt', 'r') as file:
    for y, line in enumerate(file):
        if y >= LIMIT_B:
            break
        x, y = line.rstrip().split(',')
        matrix[int(y)][int(x)] = False

node = astar((0, 0), is_goal_reached, calc_next_steps, calc_heuristics)

print(f"Part 1: {node.cost}") # 226

with open('inputs/18.txt', 'r') as file:
    for y, line in enumerate(file):
        if y < LIMIT_B:
            continue
        x, y = line.rstrip().split(',')

        matrix[int(y)][int(x)] = False
        if node.contains((int(y), int(x))):
            node = astar((0, 0), is_goal_reached, calc_next_steps, calc_heuristics)
            if node == None:
                print(f"Part 2: {x},{y}") # 60,46
                break

print(f"Time: {time.time() - start_time}") # 0.41070
