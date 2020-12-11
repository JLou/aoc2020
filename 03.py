from functools import reduce

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

print("Part 1:" + str(treeCount))

# Part 2

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

counts = []
for slopeX, slopeY in slopes:
    x = 0
    treeCount = 0
    for y in range(0, len(lines), slopeY):
        line = lines[y]
        if line[x] == '#':
            treeCount += 1
        x = (x+slopeX) % lineLength
    counts.append(treeCount)

product = reduce((lambda x, y: x * y), counts)
print(product)
