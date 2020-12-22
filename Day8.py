#https://adventofcode.com/2020/day/8

def runloop1(nums):
    global val, count

    if count == len(nums)-1:
        print(val)

    elif nums[count][0] == 'acc':
        if count not in check:
            check.append(count)
            val += nums[count][1]
            count += 1
            runloop1(nums)
        else:
            print(str(val) + ' PART 1')

    elif nums[count][0] == 'jmp':
        if count not in check:
            check.append(count)
            count += nums[count][1]
            runloop1(nums)
        else:
            print(str(val) + ' PART 1')
    else:
        if count not in check:
            check.append(count)
            count += 1
            runloop1(nums)
        else:
            print(str(val) + ' PART 1')

check = []

nums = []

val = 0
count = 0

with open('Inputs/Input8.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        nums.append(line.strip('\n'))
        line = reader.readline()

for x in range(len(nums)):
    nums[x] = nums[x].split()
    nums[x][1] = int(nums[x][1])

runloop1(nums)

for x in range(len(nums)):

    check = []
    val = 0
    count = 0
    nums2 = nums.copy()

    if nums2[x][0] == 'jmp':
        nums2[x][0] = 'nop'
    elif nums2[x][0] == 'nop':
        nums2[x][0] = 'jmp'
    else:
        continue

    runloop1(nums2)






