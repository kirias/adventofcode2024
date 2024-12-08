rules = []
sum = 0
sum_2 = 0

class Rule:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.first_printed = False
        self.second_printed = False

def check_correct(nums):
    for rule in rules:
        rule.first_printed = False
        rule.second_printed = False

    for num in nums:
        for rule in rules:
            if rule.first == num:
                if rule.second_printed:
                    return False
                rule.first_printed = True
            if rule.second == num:
                rule.second_printed = True
    return True

def get_middle(nums):
    return nums[int((len(nums) - 1)/2)]

def reorder(nums):
    correct = False
    while not correct:
        for rule in rules:
            if rule.first in nums and rule.second in nums and nums.index(rule.second) < nums.index(rule.first):
                nums.remove(rule.second)
                nums.insert(nums.index(rule.first) + 1, rule.second)
        correct = check_correct(nums)

with open('inputs/05.txt', 'r') as file:
    for line in file:
        if '|' in line:
            nums = line.rstrip().split('|')
            rules.append(Rule(int(nums[0]), int(nums[1])))
        elif ',' in line:
            nums = list(map(int, line.rstrip().split(',')))
            if check_correct(nums):
                sum += get_middle(nums)
            else:
                reorder(nums)
                sum_2 += get_middle(nums)


print(f"Part 1: {sum}")
print(f"Part 2: {sum_2}")

