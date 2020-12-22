#https://adventofcode.com/2020/day/2

x = 0

with open('Inputs/Input2.txt', 'r') as reader:

    line = reader.readline()
    while line != '':
        line = (line.strip('\n'))
        line = line.replace('-', ',')
        line = line.replace(' ', ',')
        line = line.replace(':', '')
        line = line.split(',')

        counter = line[3].count(line[2])

        if int(line[0]) <= counter <= int(line[1]):
            x += 1
        else:
            pass

        line = reader.readline()

print(x)

x = 0

with open('Inputs/Input2.txt', 'r') as reader:

    line = reader.readline()
    while line != '':
        line = (line.strip('\n'))
        line = line.replace('-', ',')
        line = line.replace(' ', ',')
        line = line.replace(':', '')
        line = line.split(',')

        l = line[3]
        p1 = int(line[0])-1
        p2 = int(line[1]) - 1

        if l[p1] == line[2] and l[p2] == line[2]:
            pass
        elif l[p1] == line[2] or l[p2] == line[2]:
            x += 1
        else:
            pass

        line = reader.readline()

print(x)
