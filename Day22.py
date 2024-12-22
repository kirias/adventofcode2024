import time

start_time = time.time()


def process(initial):
    num = initial
    
    for i in range(2000):
        num = ((num * 64) ^ num) % 16777216
        num = ((num // 32) ^ num) % 16777216
        num = ((num * 2048) ^ num) % 16777216

    return num

with open('inputs/22.txt', 'r') as file:
    sum = 0
    for y, line in enumerate(file):
        if line.rstrip():
            sum += process(int(line.rstrip()))




print(f"Part 1: {sum}") # 16619522798


# print(f"Part 2: {sum}") #

print(f"Time: {time.time() - start_time}") #
