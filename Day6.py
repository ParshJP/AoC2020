#https://adventofcode.com/2020/day/6
nums = ''
a = 0

with open('Inputs/Input6.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        if line == '\n':
            line = '@'
        nums += line
        line = reader.readline()
    nums = nums.split('@')

for elem in nums:
    letters = '\n'
    for x in elem:
        if x not in letters:
            letters += x
            a += 1
        else:
            pass

print(a)

for x in range(len(nums)):
    nums[x] = nums[x].split('\n')
    if nums[x][-1] == '':
        del nums[x][-1]

a = 0

for x in range(len(nums)):
    c = None
    for y in range(len(nums[x])):
        t = set(nums[x][y])         #letters in each line/person
        if c is None:
            c = t
        else:
            c &= t                  #combine/overlap letter set with the last line, any nonmatching letters will get cut
    a += len(c)     #answer for the group of lines (letters that were consistent)

print(a)
