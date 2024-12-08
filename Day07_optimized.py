import time

start_time = time.time()

def mutate(size, mutation_no, parts, expected_sum, running_sum, all_perms):
    if running_sum > expected_sum:
        return
    if mutation_no == size:
        yield running_sum
    else:
        next = parts[mutation_no + 1]

        yield from mutate(size, mutation_no + 1, parts, expected_sum, running_sum + next, all_perms)
        yield from mutate(size, mutation_no + 1, parts, expected_sum, running_sum * next, all_perms)
        if all_perms:
            yield from mutate(size, mutation_no + 1, parts, expected_sum, int(str(running_sum) + str(next)), all_perms)

def is_valid_eq(result, parts, running_sum, all_perms):
    for variant in mutate(len(parts) - 1, 0, parts, result, running_sum, all_perms):
        if variant == result:
            return True
    return False

sum = 0
sum2 = 0

with open('inputs/07.txt', 'r') as file:
    for line in file:
        parts = line.rstrip().split(': ')
        result = int(parts[0])
        nums = list(map(int, parts[1].split(' ')))
        if is_valid_eq(result, nums, nums[0], False):
            sum += result
            sum2 += result
        elif is_valid_eq(result, nums, nums[0], True):
            sum2 += result

print(f"Part 1: {sum}") # 1260333054159
print(f"Part 2: {sum2}") # 162042343638683

print(f"Time: {time.time() - start_time}") # 2.2097678

