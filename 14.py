import re
mask_pattern = re.compile(r'mask = (.*)')
mem_pattern = re.compile(r'mem\[(\d+)\] = (\d+)')
with open('inputs/14.txt', 'r') as f:
    lines = f.readlines()

set_mask = 0
unset_mask = 0

memory = {}

for line in lines:
    is_mask = mask_pattern.match(line)
    if is_mask:
        set_mask = 0
        unset_mask = 0
        mask = is_mask.group(1)
        for i, c in enumerate(mask):
            if c == '0':
                unset_mask |= 1 << 35-i
            if c == '1':
                set_mask |= 1 << 35-i
        unset_mask = ~unset_mask & ((1 << 36)-1)
        print(mask)
        print(f'  set mask = {"{0:b}".format(set_mask).zfill(36)}')
        print(f'unset mask = {"{0:b}".format(unset_mask).zfill(36)}')
    else:
        match = mem_pattern.match(line)
        address, value = (match.group(1), int(match.group(2)))
        memory[address] = (value & unset_mask) | set_mask
        #print(f'set {"{0:b}".format(memory[address])} ({memory[address]}) in adress {address}')

print(sum(memory.values()))