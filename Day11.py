import time

import functools

start_time = time.time()

@functools.cache
def count_stones(stone, blinks):
    if blinks == 0:
        return 1
    else:
        if stone == 0:
            return count_stones(1, blinks - 1)
        else:
            stone_tmp = stone
            num_digits = 0
            while stone_tmp > 0:
                num_digits += 1
                stone_tmp //= 10
            if num_digits % 2 == 0:
                first_stone = stone
                second_stone = 0
                for i in range(num_digits // 2):
                    second_stone += (first_stone % 10) * pow(10, i)
                    first_stone //= 10
                return count_stones(first_stone, blinks - 1) + count_stones(second_stone, blinks - 1)
            else:
                return count_stones(stone * 2024, blinks - 1)

with open('inputs/11.txt', 'r') as file:
    line = file.readline().rstrip()
    stones = [stone for stone in map(int, line.split(' '))]

count = 0
for stone in stones:
    count += count_stones(stone, 25)

print(f"Part 1: {count}") # 212655

count = 0
for stone in stones:
    count += count_stones(stone, 75)

print(f"Part 2: {count}") # 253582809724830

# print(f"Time: {time.time() - start_time}")

