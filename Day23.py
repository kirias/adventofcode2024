import time

start_time = time.time()


connections = set()
connections_all = set()
comps = set()

with open('inputs/23.txt', 'r') as file:

    for y, line in enumerate(file):
        if line.rstrip():
            con1, con2 = line.rstrip().split('-')
            comps.add(con1)
            comps.add(con2)
            connections.add((con1,con2))
            connections_all.add((con1,con2))
            connections_all.add((con2,con1))

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

parties = []
for c in connections:
    party = set()
    party.add(c[0])
    party.add(c[1])
    parties.append(party)



added = True
while added:
    added = False
    for comp in comps:
        for party in parties:
            if comp in party:
                continue
            all_have_connections = True
            for p in party:
                if (p, comp) not in connections_all:
                    all_have_connections = False
                    break
            if all_have_connections:
                party.add(comp)
                added = True

max_party_len = max([len(x) for x in parties])
max_party = None
for party in parties:
    if len(party) == max_party_len:
        max_party = party
        break

part2 = ','.join(sorted(max_party))

print(f"Part 1: {part2}") # ac,ed,fh,kd,lf,mb,om,pe,qt,uo,uy,vr,wg

print(f"Time: {time.time() - start_time}") # 0.7240538
