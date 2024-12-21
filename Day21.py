import time
from functools import cache

start_time = time.time()

connections1 = {
    ('A', '0'): {'<'},
    ('A', '3'): {'^'},
    ('0', '2'): {'^'},
    ('3', '2'): {'<'},
    ('1', '2'): {'>'},
    ('4', '5'): {'>'},
    ('6', '5'): {'<'},
    ('1', '4'): {'^'},
    ('2', '5'): {'^'},
    ('3', '6'): {'^'},
    ('7', '8'): {'>'},
    ('9', '8'): {'<'},
    ('7', '4'): {'v'},
    ('8', '5'): {'v'},
    ('9', '6'): {'v'},
}

connections2 = {
    ('^', 'A'): {'>'},
    ('v', '>'): {'>'},
    ('^', 'v'): {'v'},
    ('A', '>'): {'v'},
    ('<', 'v'): {'>'},
}

VALS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
VALS2 = ['^', 'A', 'v', '>', '<']


def mirror(c):
    if c == '>':
        return '<'
    if c == '<':
        return '>'
    if c == '^':
        return 'v'
    if c == 'v':
        return '^'
    if c == 'A':
        return 'A'

def fill_in_all_conns(vals, connections):

    new_connections = {}
    for c in connections:
        v1, v2 = c
        new_connections[(v2, v1)] = { mirror(next(iter(connections[c]))) }
        new_connections[(v2, v1)] = { mirror(next(iter(connections[c]))) }
    connections.update(new_connections)

    missing_connections = []
    for v1 in vals:
        for v2 in vals:
            if v1 == v2 or (v1, v2) in connections:
                continue
            missing_connections.append((v1, v2))

    while len(missing_connections) > 0:
        new_connections = {}
        for m in missing_connections:
            val1, val2 = m
            if m in new_connections:
                continue
            for mid in vals:
                if (val1, mid) in connections and (val2, mid) in connections:
                    if (val1, val2) not in new_connections:
                        new_connections[(val1, val2)] = set()
                        new_connections[(val2, val1)] = set()
                    for left in connections[(val1, mid)]:
                        for right in connections[(mid, val2)]:
                            new_connections[(val1, val2)].add(left + right)

                    for left in connections[(val2, mid)]:
                        for right in connections[(mid, val1)]:
                            new_connections[(val2, val1)].add(left + right)
        connections.update(new_connections)
        for i in reversed(range(len(missing_connections))):
            if missing_connections[i] in connections:
                del missing_connections[i]


fill_in_all_conns(VALS, connections1)
fill_in_all_conns(VALS2, connections2)

def create_paths(line, connections):
    start = 'A'
    paths = []
    paths.append('')

    new_paths = []
    for c in line:
        if c == start:
            for p in range(len(paths)):
                paths[p] = paths[p] + 'A'
        else:
            shortest_paths = connections[(start, c)]
            for p in range(len(paths)):
                if len(shortest_paths) == 1:
                    paths[p] = paths[p] + next(iter(shortest_paths)) + 'A'
                else:
                    for s in shortest_paths:
                        new_paths.append(paths[p] + s + 'A')
            if len(new_paths) > 0:
                paths = new_paths
                new_paths = []
        start = c

    return paths


def process(line):
    paths = create_paths(line, connections1)

    paths_2 = []
    for p in paths:
        paths_2.extend(create_paths(p, connections2))

    paths_3 = []
    for p in paths_2:
        paths_3.extend(create_paths(p, connections2))

    min_length = min(len(ele) for ele in paths_3)

    return int(line[0:-1]) * min_length




with open('inputs/21.txt', 'r') as file:
    sum = 0
    for y, line in enumerate(file):
        if line.rstrip():
            sum += process(line.rstrip())


print(f"Part 1: {sum}") # 155252

# print(f"Part 2: {count_cheats}") #

print(f"Time: {time.time() - start_time}") #
