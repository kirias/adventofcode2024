import time

start_time = time.time()

def mutate(mutation_no, parts, running_sum, all_perms):
    if mutation_no == -1:
        yield running_sum == 0
    else:
        next = parts[mutation_no]

        if all_perms:
            next_copy = next
            running_sum_copy = running_sum
            while next_copy > 0:
                if next_copy % 10 == running_sum_copy % 10:
                    next_copy //= 10
                    running_sum_copy //= 10
                    if next_copy == 0:
                        yield from mutate(mutation_no - 1, parts, running_sum_copy, all_perms)
                else:
                    break
        if running_sum % next == 0:
            yield from mutate(mutation_no - 1, parts, running_sum // next, all_perms)
        if running_sum - next >= 0:
            yield from mutate(mutation_no - 1, parts, running_sum - next, all_perms)


def is_valid_eq(result, parts, all_perms):
    for variant in mutate(len(parts) - 1, parts, result, all_perms):
        if variant:
            return True
    return False

sum = 0
sum2 = 0

with open('inputs/07.txt', 'r') as file:
    for line in file:
        parts = line.rstrip().split(': ')
        result = int(parts[0])
        nums = list(map(int, parts[1].split(' ')))
        if is_valid_eq(result, nums, False):
            sum += result
            sum2 += result
        elif is_valid_eq(result, nums, True):
            sum2 += result

print(f"Part 1: {sum}") # 1260333054159
print(f"Part 2: {sum2}") # 162042343638683

print(f"Time: {time.time() - start_time}") # 0.0078721

