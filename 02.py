import re

pattern = r"(\d+)-(\d+) (\w): (.+)"

lines = [re.split(pattern, x)[1:-1]
         for x in open("inputs/02.txt").read().split('\n') if x]
valid = len(list((password for min, max, char, password in lines
                  if int(min) <= password.count(char) <= int(max))))
print("Part 1:" + str(valid))

# Part 2
valid = (list((password for min, max, char, password in lines
               if (password[int(min)-1] == char) ^ (password[int(max)-1] == char))))
print("Part 2:" + str(len(valid)))
