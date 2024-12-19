import time
import functools

start_time = time.time()

towels = []
towels_2 = []
patterns = 0
patterns_all = 0


def check_pattern(pattern):
    for towel in towels:
        if pattern == towel:
            return 1
        if pattern.startswith(towel):
            if check_pattern(pattern[len(towel):]) == 1:
                return 1
    return 0

@functools.cache
def check_pattern_all(pattern):
    possible_patterns = 0
    for towel in towels:
        if pattern == towel:
            possible_patterns += 1
        elif pattern.startswith(towel):
            possible_patterns += check_pattern_all(pattern[len(towel):])
    return possible_patterns

with open('inputs/19.txt', 'r') as file:
    towels = file.readline().rstrip().split(', ')

    file.readline()

    line = file.readline().rstrip()
    while line:
        patterns += check_pattern(line)
        patterns_all += check_pattern_all(line)
        line = file.readline().rstrip()

    

print(f"Part 1: {patterns}") # 233
print(f"Part 2: {patterns_all}") # 691316989225259


print(f"Time: {time.time() - start_time}") # 0.802564
