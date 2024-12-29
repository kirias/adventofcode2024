import time
import re

start_time = time.time()

regs = {}
logic = []

with open('inputs/24.txt', 'r') as file:
    registers_parse = True
    for y, line in enumerate(file):
        if line.rstrip():
            if registers_parse:
                match = re.match(r'(.*): ([0,1])', line.rstrip())
                reg = match.groups()[0]
                val = int(match.groups()[1])
                regs[reg] = val
            else:

                match = re.match(r'(.{3}) ([XORAND]+) (.{3}) -> (.{3})', line.rstrip())
                op1 = match.groups()[0]
                type = match.groups()[1]
                op2 = match.groups()[2]
                out = match.groups()[3]

                logic.append((out, op1, op2, type))
        else:
            registers_parse = False

while len(logic) > 0:
    for l in logic:
        (out, op1, op2, type) = l
        if out in regs:
            logic.remove(l)
            break
        if op1 in regs and op2 in regs:
            if type == 'XOR':
                regs[out] = regs[op1] ^ regs[op2]
            elif type == 'OR':
                regs[out] = regs[op1] | regs[op2]
            elif type == 'AND':
                regs[out] = regs[op1] & regs[op2]
            logic.remove(l)
            break

answer = 0
for r in regs:
    if r.startswith('z'):
        bit_offs = int(r[1:])
        answer = answer | int(regs[r]) << bit_offs

print(f"Part 1: {answer}") # 66055249060558

        





# print(f"Part 1: {part2}") # ac,ed,fh,kd,lf,mb,om,pe,qt,uo,uy,vr,wg

print(f"Time: {time.time() - start_time}") # 
