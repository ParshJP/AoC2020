# https://adventofcode.com/2020/day/1

nums = []

with open('Inputs/Input1.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        nums.append(int(line.strip('\n')))
        line = reader.readline()

for x in nums:
    for y in nums:
        if y == x:
            pass
        else:
            z = x + y
            if z == 2020:
                a = x * y
                break
            else:
                pass

print(a)

for x in nums:
    for y in nums:
        for z in nums:

            if y == x:
                pass
            elif x == z:
                pass
            elif z == y:
                pass
            else:
                a = x + y + z
                if a == 2020:
                    b = x * y * z
                    break
                else:
                    pass
print(b)
