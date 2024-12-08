import re

result1 = 0
result2 = 0
enabled = True
with open('inputs/03.txt', 'r') as file:
    for line in file:
        for match in re.finditer(r'mul\((\d{1,3})\,(\d{1,3})\)', line):
            result1 += int(match[1]) * int(match[2])
        for match in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3})\,(\d{1,3})\)', line):
            if match[0].startswith('mul'):
                if enabled:
                    result2 += int(match[1]) * int(match[2])
            elif match[0].startswith('don'):
                enabled = False
            elif match[0].startswith('do'):
                enabled = True

print(f"Part 1: {result1}")
print(f"Part 2: {result2}")