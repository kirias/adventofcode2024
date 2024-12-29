import time

start_time = time.time()


connections = set()
comps = set()

with open('inputs/23.txt', 'r') as file:

    for y, line in enumerate(file):
        if line.rstrip():
            con1, con2 = line.rstrip().split('-')
            comps.add(con1)
            comps.add(con2)
            connections.add((con1,con2))

triples = set()
for conn in connections:
    con1, con2 = conn
    for comp in comps:
        if comp == con1 or comp == con2:
            continue
        if (con1, comp) in connections or (comp, con1) in connections:
            if (con2, comp) in connections or (comp, con2) in connections:
                triples.add((con1, con2, comp))

triples_with_t = 0
for con1, con2, con3 in triples:
    if con1.startswith('t') or con2.startswith('t') or con3.startswith('t'):
        triples_with_t += 1 

print(f"Part 1: {triples_with_t // 3}") # 1512

print(f"Time: {time.time() - start_time}") # 3.3168
