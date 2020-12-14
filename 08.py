instructions = []

i = 0
acc = 0
visited_instructions = set()

operations = {
    'nop': lambda x, i, acc: (i+1, acc),
    'acc': lambda x, i, acc: (i+1, acc + x),
    'jmp': lambda x, i, acc: (i + x, acc),
}


with open('inputs/08.txt') as f:
    for line in f.readlines():
        chunks = line.split(' ')
        instructions.append((chunks[0], int(chunks[1])))


def exec(instruction, i, acc):
    instruction_code, number = instruction
    return operations[instruction_code](number, i, acc)


while i not in visited_instructions:
    visited_instructions.add(i)
    i, acc = exec(instructions[i], i, acc)

print(acc)
