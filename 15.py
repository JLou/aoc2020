def play_game(starting_numbers:list, count:int):
    prev = None
    history = {}
    for i in range(1, count + 1):
        number = 0
        if i <= len(starting_numbers):
            number = starting_numbers[i-1]
        elif prev in history:
            number = i-1 - history[prev]
        else:
            number = 0
        history[prev] = i-1
        prev = number
        #print(number)
    return number

def part1(starting_numbers:list):
    return play_game(starting_numbers, 2020)

def part2(starting_numbers:list):
    return play_game(starting_numbers, 30000000)

tests1 = [
    ('1,3,2', 1),
    ('2,1,3', 10),
    ('1,2,3', 27),
    ('2,3,1', 78),
    ('3,2,1', 438),
    ('3,1,2', 1836),
    ('2,0,1,7,4,14,18', -1),
]
print("PART 1")
for data, expected in tests1:
    starting_numbers = list(map(int, data.split(',')))
    result = part1(starting_numbers)
    print(f'for input {data}, expected {expected} and got {result}')

print("PART 2")
tests2 = [
    ('0,3,6', 175594),
    ('1,3,2', 2578),
    ('2,1,3', 3544142),
    ('1,2,3', 261214),
    ('2,3,1', 6895259),
    ('3,2,1', 18),
    ('3,1,2', 362),
    ('2,0,1,7,4,14,18', -1),
]
for data, expected in tests2:
    starting_numbers = list(map(int, data.split(',')))
    result = part2(starting_numbers)
    print(f'for input {data}, expected {expected} and got {result}')