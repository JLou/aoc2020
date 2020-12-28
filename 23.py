from collections import deque

example_input = "389125467"
my_input = '215694783'


def parse_input(input):
    return deque(map(int, input))


def parse_input2(input):
    arr = [None] * 1_000_001
    start = list(map(int, input))
    for i, e in enumerate(start[:-1]):
        arr[e] = start[i+1]

    arr[start[-1]] = 10
    for i in range(10, 1_000_000):
        arr[i] = i+1
    arr[-1] = start[0]
    return arr


def get_destination(current_cup, cups):
    dest = current_cup - 1
    while dest not in cups:
        dest = dest - 1 if dest > 1 else 9
    return dest


def play_cups(cups: deque, nb_moves):
    for i in range(0, nb_moves):
        #print(f'-- move {i+1} --')
        current_cup = cups[0]

        # print(cups)
        # print(f'current: {current_cup}')

        cups.rotate(-1)

        pickups = [cups.popleft(), cups.popleft(), cups.popleft()]
        destination_cup = get_destination(current_cup, cups)

        # print(f'pick up: {pickups}')
        # print(f'destination: {destination_cup}')

        dest_in = cups.index(destination_cup)

        # push dest to end right end of the queue
        # and add pickups to the right
        cups.rotate(-dest_in-1)
        cups.extend(pickups)

        # rotate the queue back into initial state shifted once
        cups.rotate(dest_in+4)
        # print('')

    return cups


def part1(input):
    cups = play_cups(parse_input(input), 100)
    index_of_one = cups.index(1)
    cups.rotate(-index_of_one)
    cups.popleft()
    return ''.join(map(str, cups))


def part2(input):
    cups = parse_input2(input)
    current_cup = int(input[0])
    for i in range(0, 10_000_000):

        pickup1 = cups[current_cup]
        pickup2 = cups[pickup1]
        pickup3 = cups[pickup2]
        next_cup = current_cup - 1
        while next_cup in [pickup1, pickup2, pickup3, 0]:
            next_cup = next_cup - 1 if next_cup > 1 else 1_000_000

        cups[current_cup] = cups[pickup3]
        cups[pickup3] = cups[next_cup]
        cups[next_cup] = pickup1

        current_cup = cups[current_cup]

    v1 = cups[1]
    v2 = cups[v1]
    return v1 * v2


# print(part2(example_input))
print(part1(my_input))
print(part2(my_input))
