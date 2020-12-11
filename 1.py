f = open("inputs/1.txt", "r")

numbers = set()
for l in f:
    x = int(l)
    complement = 2020-x
    if complement in numbers:
        print("combo found:" + str(x) + " " + str(complement))
        print('their multiplication is:' + str(x*complement))
    else:
        numbers.add(x)

f.close()
