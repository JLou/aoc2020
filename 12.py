import re
from enum import IntEnum

input_pattern = re.compile(r'(\w)(\d+)')
with open('inputs/12.txt') as f:
    matches = [input_pattern.match(line) for line in f.readlines()]
    instructions = [(match.group(1), int(match.group(2))) for match in matches]

class Direction(IntEnum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

current_direction = Direction.EAST
vectors = {
    Direction.NORTH: (1,0),
    Direction.SOUTH: (-1,0),
    Direction.EAST: (0,1),
    Direction.WEST: (0,-1)
}

coordinates = (0,0)

for direction, amount in instructions:
    applied_direction = current_direction
    if direction == 'E':
        applied_direction = Direction.EAST
    elif direction == 'S':
        applied_direction = Direction.SOUTH
    elif direction == 'W':
        applied_direction = Direction.WEST
    elif direction == 'N':
        applied_direction = Direction.NORTH
    elif direction == 'L':
        quarter_turn = amount / 90
        current_direction = (current_direction - quarter_turn) % 4
        continue
    elif direction == 'R':
        quarter_turn = amount / 90
        current_direction = (current_direction + quarter_turn) % 4
        continue
    print(f'going {applied_direction} for {amount} units')
    offset_x, offset_y = [x * amount for x in vectors[applied_direction]]
    coordinates = (coordinates[0] + offset_x, coordinates[1] + offset_y)

x,y = coordinates
print(f'manhanttan distance of ({x},{y}) is {abs(x) + abs(y)}')

