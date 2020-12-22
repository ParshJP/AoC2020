#https://adventofcode.com/2020/day/9

nums = []

b = 0

with open('Inputs/Input9.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        nums.append(int(line.strip('\n')))
        line = reader.readline()

for x in range(25, len(nums)):
    a = False
    for i in range(x-25, x):
        for i2 in range(x - 25, x):
            if nums[i] != nums[i2]:
                n = nums[i] + nums[i2]
                if n == nums[x]:
                    a = True
                elif a == False and i == x-1 and i2 == x-2:
                    b = nums[x]
                    break
                else:
                    pass
            else:
                pass

print(b)

contiguous = 3      #numbers in set

while True:
    for x in range(len(nums) - contiguous):     #go through list, set for each num
        if sum(nums[x:x+contiguous]) == b:
            print(max(nums[x:x+contiguous]) + min(nums[x:x+contiguous]))
    contiguous += 1     #increase the set amount, iterate

