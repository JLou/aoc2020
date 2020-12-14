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

with open("inputs/1.txt", 'r') as f:
    numbers = map(int, f.readlines())
perm = (x*y*z for x, y, z in combinations(numbers, 3) if x + y + z == 2020)

print(list(perm))
