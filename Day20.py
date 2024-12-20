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

def astar_in_a_wall(initial, count_walls, entry_cost, test_goal_reached, calc_next):
    frontier = []
    frontier.append((Node(initial, None, 0, 0), count_walls + 1, entry_cost, None))

    explored = { initial: 0 }

    count_walls_initial = count_walls + 1

    exits = set()
    first = True

    while len(frontier) > 0:
        current_node, count_walls, entry_cost, first_entry = frontier.pop()

        current_state = current_node.coord
        if not first:
            goal_reached, can_continue_cheat = test_goal_reached(current_state, entry_cost, count_walls_initial - count_walls, count_walls)
            if goal_reached == True:
                # if maze[current_node.parent.coord[0]][current_node.parent.coord[1]] == '#':
                    # if (*first_entry, *current_state) not in exits:
                    #     print_cheat(current_node)
                    exits.add((*first_entry, *current_state))
            if not can_continue_cheat:
                continue
        for (child, cost) in calc_next(current_state, first):
            new_cost = current_node.cost + cost
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.append(((Node(child, current_node, new_cost, 0)), count_walls - 1, entry_cost, initial if first_entry == None else first_entry))
        if first:
            first = False
    return len(exits)

def print_cheat(node):
    for y, row in enumerate(maze):
        for x, i in enumerate(row):
            if (y, x) == start_pos:
                print('S', end='')
            elif (y, x) == end:
                print('E', end='')
            elif node.contains((y, x)):
                if i == '.':
                    print('o', end='')
                else:
                    print('O', end='')
            else:
                print(i, end='')
        print()

def is_end_reached(state):
    return end == state

def is_start_reached(state):
    return start_pos == state

def is_cheat_goal_reached(state, entry_cost, cheat_len, walls_left):
    y, x = state
    if (maze[y][x] == '#'):
        return None, walls_left > 0
    exit_cost = all_lengths_reverse.get((y, x))
    # if entry_cost + SAVE_CHEAT + cheat_len + exit_cost == shortest:
    #     breakpoint()
    return entry_cost + SAVE_CHEAT + cheat_len + exit_cost <= shortest, walls_left > 0
        

def calc_next_steps(state):
    y, x = state
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny = y + dy
        nx = x + dx
        if ny >= 0 and nx >= 0 and ny < HEIGHT and nx < WIDTH:
            if maze[ny][nx] == '.':
                yield ((ny, nx), 1)


def calc_cheat_next_steps(state, first):
    y, x = state
    for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ny = y + dy
        nx = x + dx
        if ny >= 0 and nx >= 0 and ny < HEIGHT and nx < WIDTH:
            # if first and maze[ny][nx] == '#':
            #     yield ((ny, nx), 1)
            # elif not first:
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

all_lengths, shortest = astar(start_pos, is_end_reached, calc_next_steps, calc_heuristics)
all_lengths_reverse, shortest = astar(end, is_start_reached, calc_next_steps, calc_heuristics)



WALLS_FIRST_CHEAT = 1
WALLS_SECOND_CHEAT = 19
SAVE_CHEAT = 100

count_cheats = 0;
for field, cost in all_lengths.items():
    if cost > shortest - SAVE_CHEAT - 1:
        continue
    count_cheats += astar_in_a_wall(field, WALLS_FIRST_CHEAT, cost, is_cheat_goal_reached, calc_cheat_next_steps)


print(f"Part 1: {count_cheats}") # 1351

count_cheats = 0;
for field, cost in all_lengths.items():
    if cost > shortest - SAVE_CHEAT - 1:
        continue
    count_cheats += astar_in_a_wall(field, WALLS_SECOND_CHEAT, cost, is_cheat_goal_reached, calc_cheat_next_steps)
print(f"Part 2: {count_cheats}") # 966130

# tiles = set()
# for solution in solutions:
#     y, x, _ = solution.coord
#     tiles.add((y, x))
#     while solution.parent != None:
#         solution = solution.parent
#         y, x, _ = solution.coord
#         tiles.add((y, x))

# print(f"Part 2: {len(tiles)}") # 504

# print(f"Time: {time.time() - start_time}") # 0.44216
