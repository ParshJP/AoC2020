#https://adventofcode.com/2020/day/5

nums = []
rows = []
col = []
ids = []

r = 0
c = 0

with open('Inputs/Input5.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        nums.append(line.strip('\n'))
        line = reader.readline()

for elem in nums:
    a = 0
    b = 127
    o = (b-a)+1
    for x in range(0,7):

        if elem[x] == 'F':
            o = o/2
            b = b-o
            r = a

        if elem[x] == 'B':
            o = o/2
            a = a+o
            r = b

        if x == 6:
            rows.append(r)

for elem in nums:
    a = 0
    b = 7
    o = (b-a)+1
    for x in range(7,10):
        if elem[x] == 'L':
            o = o/2
            b = b-o
            c = a

        if elem[x] == 'R':
            o = o/2
            a = a+o
            c = b

        if x == 9:
            col.append(c)

for x in range(len(nums)):
    i = rows[x] * 8 + col[x]
    ids.append(i)

print(max(ids))

ids.sort()
for x in range(1,len(ids)):
    if ids[x] != ids[x-1]+1:
        print(ids[x]-1)
