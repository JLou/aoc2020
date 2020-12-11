from itertools import combinations
# f = open("inputs/1.txt", "r")

# numbers = set()
# for l in f:
#     x = int(l)
#     complement = 2020-x
#     if complement in numbers:
#         print("combo found:" + str(x) + " " + str(complement))
#         print('their multiplication is:' + str(x*complement))
#     else:
#         numbers.add(x)

# f.close()

# part 2


numbers = list(map(int, filter(None, open("inputs/1.txt").read().split('\n'))))
perm = (x*y*z for x, y, z in combinations(numbers, 3) if sum((x, y, z)) == 2020)

print(list(perm))
