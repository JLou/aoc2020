from itertools import product

def print_cube(cube:set):
    min_x = min_y = min_z = 0
    max_x = max_y = max_z = 1
    for x,y,z in cube:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)
    for z in range(min_z,max_z+1):
        print('\n')
        print(f'z={z}')
        for x in range(min_x,max_x+1):
            line = ""
            for y in range(min_y,max_y+1):
                line += "#" if (x,y,z) in cube else '.'
            print(line)

def expand_boundaries(boundaries:tuple, cube):
    minx = min([x for x,_,_,_ in cube])
    miny = min([y for _,y,_,_ in cube])
    minz = min([z for _,_,z,_ in cube])
    minw = min([w for _,_,_,w in cube])

    maxx = max([x for x,_,_,_ in cube])
    maxy = max([x for _,y,_,_ in cube])
    maxz = max([x for _,_,z,_ in cube])
    maxw = max([x for _,_,_,w in cube])
    return [(minx-5, maxx+5),(miny-5, maxy+5),(minz-5, maxz+5),(minw-5, maxw+5)]

def active_neighbours_count(x,y,z,w):
    deltas = [x for x in product([-1,0,1], repeat=4) if x != (0,0,0,0)]
    count=0
    for off_x, off_y, off_z, off_w in deltas:
        if (x+off_x, y+off_y, z+off_z, w+off_w) in cube:
            count += 1
    return count

def is_active_next(x,y,z,w,cube):
    if (x,y,z,w) in cube:
        if active_neighbours_count(x,y,z,w) in [2,3]:
            return True
    elif active_neighbours_count(x,y,z,w)  == 3:
        return True
    return False


with open('inputs/17.txt', 'r') as f:
    lines = f.readlines()

# seed cube
cube = set()
cube_boundaries = [(0,3),(0,3),(0,0), (0,0)]
for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == '#':
            cube.add((x,y,0,0))


for i in range(1,7):
    new_state = set()
    print(f'Round {i}')
    cube_boundaries = expand_boundaries(cube_boundaries, cube)
    for x in range(cube_boundaries[0][0], cube_boundaries[0][1]+1):
        for y in range(cube_boundaries[1][0], cube_boundaries[1][1]+1):
            for z in range(cube_boundaries[2][0], cube_boundaries[2][1]+1):
                for w in range(cube_boundaries[3][0], cube_boundaries[3][1]+1):
                    if is_active_next(x,y,z,w,cube):                
                        new_state.add((x,y,z,w))
    cube = new_state

    

print(len(cube))