filename = 'inputs/04.txt'


def split_file(f):
    return (line.split(' ') for line in f.read().replace(
        '\n', ' ').replace('  ', '\n').split('\n'))


def to_dict(line):
    return {key: value for (key, value) in filter(lambda x: len(x) == 2, line)}


hex_characters = list(hex(i)[2:] for i in range(16))
eye_color = (
    'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
)

required_keys = (
    ('byr', lambda x: 1920 <= int(x) <= 2002),
    ('iyr', lambda x: 2010 <= int(x) <= 2020),
    ('eyr', lambda x: 2020 <= int(x) <= 2030),
    ('hgt',
     lambda x: 59 <= int(x[:-2]) <= 76 if x[-2:] == 'in' else
     (150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' else
      False)),
    ('hcl', lambda x: len(x) == 7 and x[0] == '#' and (
        c in hex_characters for c in x[1:])),
    ('ecl', lambda x: x in eye_color),
    ('pid', lambda x: len(x) == 9 and x.isdigit())
)


def is_valid_part1(line):
    return all(k in line for (k, _) in required_keys)


def is_valid(line):
    return all(k in line and validator(line[k]) for (k, validator) in required_keys)


with open(filename, 'r') as f:
    lines = (map(lambda x: x.split(':'), line) for line in split_file(f))

l = (x for x in (to_dict(line) for line in lines) if is_valid(x))
print(len(list(l)))
