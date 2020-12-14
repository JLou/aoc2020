def compute_seat_id(row, col):
    return row*8+col


def count_seat_id(line):
    min, max = 0, 127
    col_min, col_max = 0, 7
    for c in line:

        row_size = (max-min+1)/2
        col_size = (col_max-col_min+1)/2
        if c == 'B':
            min += row_size
        elif c == 'F':
            max -= row_size
        elif c == 'L':
            col_max -= col_size
        elif c == 'R':
            col_min += col_size
    return compute_seat_id(max, col_max)


def find_missing_id(ids):
    ids.sort()
    prev = ids[0]

    for id in ids[1:]:
        if id != prev+1:
            return prev+1
        else:
            prev = id
    return -1


with open('inputs/05.txt') as f:
    ids = list(map(count_seat_id, f.readlines()))
    print(f"Part 1: {max(ids)}")
    print(f'Part 2: {find_missing_id(ids)}')
