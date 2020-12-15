from functools import cache 

with open('inputs/10.txt') as f:
    numbers = [int(x) for x in f.readlines()]

numbers.sort()

diffs = [0,0,0,1]
prev = 0
for number in numbers:
    diffs[number-prev] += + 1
    prev = number

diff1, diff3 = diffs[1::2] 
print(diff1 * diff3)

@cache #memoization for noobs
def compute_combinations(index):
    number = numbers[index]
    upper_bound = min(3, len(numbers)-1-index)
    possibilities = [x for x in numbers[index+1:index+upper_bound+1] if x - number < 4]
    
    if possibilities:
        s = sum([compute_combinations(numbers.index(x)) for x in possibilities])
        #print(f'{number} has {s} possibilities')
        return s
    else:
        #print(f'{number} is the biggest')
        return 1

def part2():
    return sum([compute_combinations(i) for i in range(3) if numbers[i] < 4])

print(part2())