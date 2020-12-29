example_input = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

with open('inputs/24.txt') as f:
    myinput = f.read()

# axial coordinate system
# https://www.redblobgames.com/grids/hexagons/
direction_offset = {
    'e': (1,0),
    'w': (-1,0),
    'ne': (1,-1),
    'se': (0,1),
    'nw': (0,-1),
    'sw': (-1,1),
}

def follow_instructions(floor):
    flipped_tiles = set()

    for line in floor.split("\n"):
        coords = (0,0)
        prev = ''
        for c in line:
            if c not in ['e', 'w']:
                prev = c
            else:
                direction = prev + c
                x,y = direction_offset[direction]
                coords = (coords[0] + x, coords[1] + y)
                prev = ''
        
        if coords in flipped_tiles:
            flipped_tiles.remove(coords)
            #print(f'flipped tile {coords} back to white')
        else:
            flipped_tiles.add(coords)
            #print(f'flipped tile {coords} to black')
    
    return flipped_tiles

def find_boundaries(floor):
    minx = maxx = miny = maxy = 0
    for (x, y) in floor:
        minx = min(x, minx)
        miny = min(y, miny)
        
        maxx = max(x, maxx)
        maxy = max(y, maxy)
    
    return ((minx - 1, maxx + 1), (miny - 1, maxy + 1))

def count_black_neighbours(tiles, x, y):
    count = 0
    for offx, offy in direction_offset.values():
        if (x + offx, y + offy) in tiles:
            count += 1

    return count

def part1(floor):
    tiles = follow_instructions(floor)

    return len(tiles)

def part2(floor, days):
    # Day 0
    tiles = follow_instructions(floor)

    for i in range(1, days + 1):
        (minx, maxx), (miny, maxy) = find_boundaries(tiles)
        next_tiles = set()
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy+1):
                black_neighbours = count_black_neighbours(tiles, x, y)
                if (x, y ) in tiles and not (black_neighbours == 0 or black_neighbours > 2):
                    next_tiles.add((x,y))
                elif (x, y) not in tiles and black_neighbours == 2:
                    next_tiles.add((x,y))
        
        #print(f'Day {i}: {len(next_tiles)}')
        tiles = next_tiles
    return len(tiles)

print(f'Part 1: {part1(myinput)} tiles still black')
print(f'Part 2: {part2(myinput, 100)} tiles still black')