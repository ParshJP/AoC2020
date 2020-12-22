#https://adventofcode.com/2020/day/4

nums = []
nums2 = []
a = ''
n = 0

with open('Inputs/Input4.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        nums.append(line.strip('\n'))
        line = reader.readline()

for x in range(len(nums)):
    if nums[x] == '':
        nums[x] = '@'

for x in range(len(nums)):
    a += nums[x]

a = a.split('@')

for elem in a:
    if 'byr' not in elem or 'iyr' not in elem or 'eyr' not in elem or 'hgt' not in elem or 'hcl' not in elem or 'ecl' not in elem or 'pid' not in elem:
        pass
    else:
        n += 1

print(a)
print(n)

