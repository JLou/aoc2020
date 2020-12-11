filename = 'inputs/03.txt'

with open(filename, 'r') as f:
    lines = [list(line)[:-1] for line in f]

lineLength = len(lines[0])
x = 0
treeCount = 0
for line in lines:
    if line[x] == '#':
        treeCount += 1
    x = (x+3) % lineLength

print(treeCount)
