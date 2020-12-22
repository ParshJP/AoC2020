#https://adventofcode.com/2020/day/3

lines = []
trees = 1

with open('Inputs/Input3.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        lines.append(line.strip('\n'))
        line = reader.readline()
x = 1
t = 0

for elem in lines:
    if elem[x-1] == '#':
        t += 1
    x += 3
    if x > 31:
        x = x % 31

print(t)
trees = trees * t

x = 1
t = 0

for elem in lines:
    if elem[x-1] == '#':
        t += 1
    x += 1
    if x > 31:
        x = x % 31

print(t)
trees = trees * t

x = 1
t = 0

for elem in lines:
    if elem[x-1] == '#':
        t += 1
    x += 5
    if x > 31:
        x = x % 31

print(t)
trees = trees * t

x = 1
t = 0

for elem in lines:
    if elem[x-1] == '#':
        t += 1
    x += 7
    if x > 31:
        x = x % 31

print(t)
trees = trees * t

x = 1
t = 0
a = 1

for elem in lines:
    if a % 2 == 1:
        if elem[x-1] == '#':
            t += 1
    a += 1
    x += 1
    if x > 31:
        x = x % 31

print(t)
trees = trees * t
print(trees)