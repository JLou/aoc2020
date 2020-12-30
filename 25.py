from math import log
example_input = """5764801
17807724"""

myinput = """14082811
5249543"""


def parse_input(input):
    return map(int, input.split('\n'))


def transform_subject(subject_number, value, times):
    for _ in range(0, times):
        value *= subject_number
        value %= 20201227

    return value


def find_loop_number(subject_number, expected_key):
    i = 1
    value = subject_number
    while value != expected_key:
        value = transform_subject(subject_number, value, 1)
        i += 1

    return i


def part1(input):
    card_key, door_key = parse_input(input)

    card_loop = find_loop_number(7, card_key)
    #door_loop = find_loop_number(7, door_key)

    encrypted_key = transform_subject(door_key, door_key, card_loop-1)
    print(f'Part 1, encrypted_key is: {encrypted_key}')


part1(example_input)
part1(myinput)
