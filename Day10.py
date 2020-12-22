#https://adventofcode.com/2020/day/10

nums = []
one = 0
two = 0
three = 0

with open('Inputs/Input10.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        nums.append(int(line.strip('\n')))
        line = reader.readline()
    nums.append(0)
    nums.append(max(nums) + 3)
    nums.sort()

for x in range(len(nums)-1):
    if nums[x + 1] - nums[x] == 1:
        one += 1
    elif nums[x + 1] - nums[x] == 2:
        two += 1
    elif nums[x + 1] - nums[x] == 3:
        three += 1

print(one*three)
