left = []
right = []
with open('inputs/01.txt', 'r') as file:
    for line in file:
        line_split = line.rstrip().split('   ')
        left.append(int(line_split[0]))
        right.append(int(line_split[1]))

left.sort()
right.sort()

sum = 0

for x in range(len(left)):
    diff = abs(left[x] - right[x])
    sum += diff

print("Part 1: {0}".format(sum))


counts = {}
for x in right:
    if x not in counts:
        counts[x] = 1
    else:
        counts[x] = counts[x] + 1

sum = 0

for x in left:
    if x in counts:
        sum += counts[x] * x

print("Part 2: {0}".format(sum))