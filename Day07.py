import time

start_time = time.time()

def is_valid(result, parts, variant):
    sum = parts[0]
    for i, opertr in enumerate(variant):
        if opertr == 0:
            sum += parts[i + 1]
        elif opertr == 1:
            sum *= parts[i + 1]
        else:
            sum = int(str(sum) + str(parts[i + 1]))
    return sum == result

def mutate(size, variants, permutations):
    if len(variants) == size:
        yield variants
    else:
        for permutation in permutations:
            variants.append(permutation)
            yield from mutate(size, variants, permutations)
            variants.pop()

def is_valid_eq(result, parts, permutations):
    for variant in mutate(len(parts) - 1, [], permutations):
        if is_valid(result, parts, variant):
            return True
    return False

sum = 0
sum2 = 0

with open('inputs/07.txt', 'r') as file:
    for line in file:
        parts = line.rstrip().split(': ')
        result = int(parts[0])
        nums = list(map(int, parts[1].split(' ')))
        if is_valid_eq(result, nums, [0, 1]):
            sum += result
        if is_valid_eq(result, nums, [0, 1, 2]):
            sum2 += result

print(f"Part 1: {sum}") # 1260333054159
print(f"Part 2: {sum2}") # 162042343638683

print(f"Time: {time.time() - start_time}") # 14.165586

