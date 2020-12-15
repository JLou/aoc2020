from itertools import product

with open('inputs/11.txt') as f:
    lines = [list(x)[:-1] for x in f.readlines()]


def print_board(lines):
    print('\n')
    print('\n'.join([''.join(['{:1}'.format(item) for item in row])
                     for row in lines]))


def is_in_bound(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])


def count_occupied_adjacent(grid, i, j):
    coords_to_check = [(x+i, y+j)
                       for x, y in product((-1, 0, 1), repeat=2) if x != 0 or y != 0]
    count = 0
    for x, y in coords_to_check:
        if is_in_bound(grid, x, y) and grid[x][y] == '#':
            count += 1
    return count


def count_occupied_eyesight(grid, i, j):
    coords_to_check = [(x, y) for x, y in product(
        (-1, 0, 1), repeat=2) if x != 0 or y != 0]
    count = 0
    for offset_x, offset_y in coords_to_check:
        x = i + offset_x
        y = j + offset_y
        while is_in_bound(grid, x, y):
            if grid[x][y] == '#':
                count += 1
                break
            elif grid[x][y] == 'L':
                break
            else:
                x += offset_x
                y += offset_y
    return count


def should_change_empty(grid, i, j):
    return count_occupied_adjacent(grid, i, j) == 0


def should_change_occupied(grid, i, j):
    return count_occupied_adjacent(grid, i, j) >= 4


def should_change_empty2(grid, i, j):
    return count_occupied_eyesight(grid, i, j) == 0


def should_change_occupied2(grid, i, j):
    return count_occupied_eyesight(grid, i, j) >= 5


changed = True
while changed:
    #print_board(lines)
    changed = False
    next = [row[:] for row in lines]  # deep copy
    for i, val in enumerate(lines):
        for j, seat in enumerate(val):
            if seat == 'L' and should_change_empty2(lines, i, j):
                changed = True
                next[i][j] = '#'
            if seat == '#' and should_change_occupied2(lines, i, j):
                changed = True
                next[i][j] = 'L'
    lines = next

print(len([c for row in lines for c in row if c == '#']))
