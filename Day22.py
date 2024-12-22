import time

start_time = time.time()

def secret(num):
    num = ((num * 64) ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216
    return num

def process(initial):
    num = initial
    
    for i in range(2000):
        num = secret(num)

    return num

def hash(el1, el2, el3, el4):
    rez = abs(el1) * 1000 + abs(el2) * 100 + abs(el3) * 10 + abs(el4)
    rez = rez << 4
    if el1 < 0:
        rez = rez ^ 0b1
    if el2 < 0:
        rez = rez ^ 0b10
    if el3 < 0:
        rez = rez ^ 0b100
    if el4 < 0:
        rez = rez ^ 0b1000
    return rez

def process2(initial):
    num = initial

    change_seq = []

    price_history = {}

    last_digit_prev = initial % 10
    
    for i in range(2000):
        num = secret(num)

        last_digit_current = num % 10
        change_seq.append(last_digit_current - last_digit_prev)
        last_digit_prev = last_digit_current
        if len(change_seq) >= 4:
            hashed = hash(change_seq[-1], change_seq[-2], change_seq[-3], change_seq[-4])
            if hashed not in price_history:
                price_history[hashed] = last_digit_prev
    return price_history

with open('inputs/22.txt', 'r') as file:
    sum = 0
    for y, line in enumerate(file):
        if line.rstrip():
            sum += process(int(line.rstrip()))

with open('inputs/22.txt', 'r') as file:
    price_changes = {}
    for y, line in enumerate(file):
        if line.rstrip():
            price_history = process2(int(line.rstrip()))
            for ph in price_history:
                if ph not in price_changes:
                    price_changes[ph] = 0
                price_changes[ph] = price_changes[ph] + price_history[ph]

    max_count = max([price_changes[x] for x in price_changes])

print(f"Part 1: {sum}") # 16619522798
print(f"Part 2: {max_count}") # 1854
print(f"Time: {time.time() - start_time}") # 3.3168
