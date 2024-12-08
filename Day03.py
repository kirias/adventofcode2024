import re

from sympy import true

result = 0
with open('inputs/03.txt', 'r') as file:
    for line in file:
        matches = re.finditer(r'mul\((\d{1,3})\,(\d{1,3})\)', line)
        for match in matches:
            result += int(match[1]) * int(match[2])

print("Part 1: {0}".format(result))

result = 0
enabled = True
with open('inputs/03.txt', 'r') as file:
    for line in file:
        matches = re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3})\,(\d{1,3})\)', line)
        for match in matches:
            if match[0].startswith('mul'):
                if enabled:
                    result += int(match[1]) * int(match[2])
            elif match[0].startswith('don'):
                enabled = False
            elif match[0].startswith('do'):
                enabled = True

print("Part 2: {0}".format(result))