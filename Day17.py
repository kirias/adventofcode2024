import time
import re


a = b = c = 0

start_time = time.time()

pc = 0
instructions = []

with open('inputs/17.txt', 'r') as file:
    line = file.readline().strip()
    match = re.match(r'Register A: (\d+)', line)
    a = int(match.groups()[0])

    line = file.readline().strip()
    match = re.match(r'Register B: (\d+)', line)
    b = int(match.groups()[0])

    line = file.readline().strip()
    match = re.match(r'Register C: (\d+)', line)
    c = int(match.groups()[0])
    
    file.readline()
    line = file.readline().strip()
    match = re.match(r'Program: ([\d,]+)', line)
    program_str = match.groups()[0]

    for instr in program_str.split(','):
        instructions.append(int(instr))
        
def combo_operand(op):
    if op < 4:
        return op
    elif op == 4:
        return a
    elif op == 5:
        return b
    elif op == 6:
        return c

def truncate_to_int(i):
    return i

printed = []

def execute(pc):
    global a, b, c, instructions
    instruction = instructions[pc]
    operand = instructions[pc + 1]

    increase_pc = True

    if instruction == 0:
        operand = combo_operand(operand)
        a = truncate_to_int(a // (2**operand))
    elif instruction == 1:
        b = b ^ operand
    elif instruction == 2:
        b = combo_operand(operand) % 8
    elif instruction == 3:
        if a != 0:
            pc = operand
            increase_pc = False
    elif instruction == 4:
        b = b ^ c
    elif instruction == 5:
        operand = combo_operand(operand) % 8
        printed.append(operand)
    elif instruction == 6:
        operand = combo_operand(operand)
        b = truncate_to_int(a // (2**operand))
    elif instruction == 7:
        operand = combo_operand(operand)
        c = truncate_to_int(a // (2**operand))

    return pc + 2 if increase_pc else pc

while True:
    pc = execute(pc)
    if pc >= len(instructions):
        break

answer = ','.join([str(x) for x in printed])
print(f"Part 1: {answer}") # 7,3,0,5,7,1,4,0,5

def calculate_b_register(a):
    b = (a % 8) ^ 1
    c = a // (2 ** b)
    return b ^ c ^ 4

def check_valid(a_register):
    first_error_index = -1
    a = a_register if a_register != None else 0
    for instr_index, instr in enumerate(instructions):
        b = calculate_b_register(a)
        if b % 8 != instr:
            first_error_index = instr_index
        a //= 8
    if first_error_index == -1:
        print(f"Part 2: {a_register}") # 202972175280682
    return first_error_index

def calc_digit(digit_to_calc, a_from):
    if digit_to_calc == -1:
        return check_valid(a_from)

    a = 0 if a_from == None else a_from * 8
    while True:
        b = calculate_b_register(a)
        if b % 8 == instructions[digit_to_calc]:
            wrong_index = calc_digit(digit_to_calc - 1, a)
            if wrong_index != digit_to_calc:
                return wrong_index
        a += 1 

calc_digit(len(instructions) - 1, None)

print(f"Time: {time.time() - start_time}") # 0.001626
