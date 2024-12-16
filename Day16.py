import time
from enum import Enum
from heapq import heappush, heappop

start_time = time.time()

maze = []
start_pos = (0, 0)
end = (0, 0)

class Direction:
    def __init__(self, offset):
        self.dy = offset[0]
        self.dx = offset[1]

    def rot_clock(self):
        if self == Directions.UP:
            return Directions.RIGHT
        if self == Directions.DOWN:
            return Directions.LEFT
        if self == Directions.LEFT:
            return Directions.UP
        if self == Directions.RIGHT:
            return Directions.DOWN

    def rot_cclock(self):
        if self == Directions.UP:
            return Directions.LEFT
        if self == Directions.DOWN:
            return Directions.RIGHT
        if self == Directions.LEFT:
            return Directions.DOWN
        if self == Directions.RIGHT:
            return Directions.UP
        

class Directions:
    UP = Direction((-1, 0))
    DOWN = Direction((1, 0))
    LEFT = Direction((0, -1))
    RIGHT = Direction((0, 1))

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

def astar_all_solutions(initial, test_goal_reached, calc_next, calc_heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0, calc_heuristic(initial)))

    explored = { initial: 0 }

    solutions = []
    solution_score = None

    while not frontier.empty():
        current_node = frontier.pop()

        current_state = current_node.coord
        if test_goal_reached(current_state):
            if solution_score == None or solution_score == current_node.cost:
                solutions.append(current_node)
                solution_score = current_node.cost
                continue
            else:
                return solutions
        
        for (child, cost) in calc_next(current_state):
            new_cost = current_node.cost + cost
            if child not in explored or explored[child] >= new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, calc_heuristic(child)))
    return solutions

def is_goal_reached(state):
    y, x, _ = state
    return end == (y, x)

def calc_next_steps(state):
    y, x, d = state
    ny = y + d.dy
    nx = x + d.dx
    if ny >= 0 and nx >= 0 and ny < len(maze) and nx < len(maze[0]):
        if maze[ny][nx] == '.':
            yield ((ny, nx, d), 1)
    yield ((y, x, d.rot_clock()), 1000)
    yield ((y, x, d.rot_cclock()), 1000)

def calc_heuristics(state):
    y, x, _ = state
    h = end[0] - y + end[1] - x
    return h


with open('inputs/16.txt', 'r') as file:
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

start = (*start_pos, Directions.RIGHT)

node = astar(start, is_goal_reached, calc_next_steps, calc_heuristics)

print(f"Part 1: {node.cost}") # 89460

solutions = astar_all_solutions(start, is_goal_reached, calc_next_steps, calc_heuristics)
tiles = set()
for solution in solutions:
    y, x, _ = solution.coord
    tiles.add((y, x))
    while solution.parent != None:
        solution = solution.parent
        y, x, _ = solution.coord
        tiles.add((y, x))

print(f"Part 2: {len(tiles)}") # 504

print(f"Time: {time.time() - start_time}") # 0.44216
