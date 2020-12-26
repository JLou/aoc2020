import math
from collections import deque
import re

with open('inputs/20.txt') as f:
    inputs = f.read()

tiles_input = inputs.split('\n\n')


def rotate(l, n):
    return l[n:] + l[:n]


def part1():

    def get_top_edge(tile):
        return set([tile[0], tile[0][::-1]])

    def get_bottom_edge(tile):
        return set([tile[-1], tile[-1][::-1]])

    def get_left_edge(tile):
        left_edge = ''.join([line[0] for line in tile])
        return set([left_edge, left_edge[::-1]])

    def get_right_edge(tile):
        left_edge = ''.join([line[-1] for line in tile])
        return set([left_edge, left_edge[::-1]])

    tiles = {}
    for tile in tiles_input:
        tile_lines = tile.split('\n')
        tile_id = tile_lines[0][5:-1]
        edges = set()
        edges |= get_top_edge(tile_lines[1:])
        edges |= get_bottom_edge(tile_lines[1:])
        edges |= get_left_edge(tile_lines[1:])
        edges |= get_right_edge(tile_lines[1:])

        tiles[tile_id] = edges

    matching_map = {}
    for tile_id, edges in tiles.items():
        matching_edges = []
        for other_id, other_edges in tiles.items():
            if tile_id == other_id:
                continue
            else:
                if len(edges & other_edges) > 1:
                    matching_edges.append(other_id)
        matching_map[tile_id] = matching_edges

    print('Part 1: ' + str(math.prod([int(i)
                                      for i, edges in matching_map.items() if len(edges) == 2])))


part1()


def part2():
    def get_top_edge(tile):
        return tile[0]

    def get_bottom_edge(tile):
        return tile[-1]

    def get_left_edge(tile):
        return ''.join([line[0] for line in tile])

    def get_right_edge(tile):
        return ''.join([line[-1] for line in tile])

    def find_edges(neighbour_map):
        return [i for i, tile in neighbour_map.items() if tile.count(None) == 2]

    def position_tile(tile_id, neighbour_left, neighbour_top, match_map, tiles_content):
        neighbours = match_map[tile_id]
        while neighbours[0] != neighbour_top:
            neighbours = rotate(neighbours, 1)

            for i in range(0, 3):
                tiles_content[tile_id] = list(
                    ''.join(x) for x in zip(*tiles_content[tile_id][::-1]))

        if neighbours[3] != neighbour_left:
            neighbours = [neighbours[0], neighbours[3],
                          neighbours[2], neighbours[1]]
            tiles_content[tile_id] = [x[::-1] for x in tiles_content[tile_id]]
        match_map[tile_id] = neighbours

    def print_puzzle(puzzle, tiles_content):
        tile_length = len(tiles_content[puzzle[0][0]])
        lines = []
        for tile_line in puzzle:
            for i in range(1, tile_length-1):
                printable_line = ''
                for tile in tile_line:
                    printable_line += ''.join(tiles_content[tile][i][1:-1])
                lines.append(printable_line)
        return lines

    def count_monsters(puzzle):
        regexes = [
            re.compile(r'(?=(.{18}#.))'),
            re.compile(r'(?=(#.{4}##.{4}##.{4}###))'),
            re.compile(r'(?=(.#..#..#..#..#..#...))')
        ]
        total = 0
        for i, line in enumerate(puzzle[:-3]):
            indexes = set([x.start(0) for x in regexes[0].finditer(line)])

            if indexes:
                for j in range(1, 3):
                    nextindexes = set([x.start(0)
                                       for x in regexes[j].finditer(puzzle[i+j])])
                    indexes &= nextindexes

            if indexes:
                print(f'found {len(indexes)} line {i}')
                total += len(indexes)
        return total

    tiles = {}
    tiles_content = {}
    for tile in tiles_input:
        tile_lines = tile.split('\n')
        tile_id = tile_lines[0][5:-1]
        tile_content = tile_lines[1:]

        top = get_top_edge(tile_content)
        bottom = get_bottom_edge(tile_content)
        left = get_left_edge(tile_content)
        right = get_right_edge(tile_content)

        tiles[tile_id] = [top, right, bottom, left]
        tiles_content[tile_id] = tile_content

    match_map = {}
    for i, tile in tiles.items():
        matches = [None, None, None, None]

        for j, other_tile in tiles.items():
            if j == i:
                continue
            else:
                for k in range(0, 4):
                    if tile[k] in other_tile:
                        matches[k] = j
                    elif tile[k][::-1] in other_tile:
                        matches[k] = j
        match_map[i] = matches

    a = find_edges(match_map)
    first_edge = a[0]

    puzzle_side = int(math.sqrt(len(tiles_content)))
    puzzle = [['' for i in range(puzzle_side)]
              for j in range(puzzle_side)]

    for i in range(puzzle_side):
        if i > 0:
            first_edge = match_map[puzzle[i-1][0]][2]
        for j in range(puzzle_side):
            top = None if i == 0 else puzzle[i-1][j]
            left = None if j == 0 else puzzle[i][j-1]

            position_tile(first_edge, left, top, match_map, tiles_content)
            puzzle[i][j] = first_edge

            # take next tile to the right
            first_edge = match_map[first_edge][1]

    puzzle_content = print_puzzle(puzzle, tiles_content)
    nb_monsters = 0
    for i in range(0, 2):
        puzzle_content = [x[::-1] for x in puzzle_content]
        rotated = puzzle_content.copy()
        for j in range(0, 4):
            rotated = [''.join(x) for x in (zip(*rotated[::-1]))]
            nb_monsters = max(nb_monsters, count_monsters(rotated))

    nb_pound = sum([line.count('#') for line in puzzle_content])
    print(f"part 2: {nb_pound - 15* nb_monsters}")


part2()
