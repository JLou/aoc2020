instructions = []


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

def part1():
    i = 0
    acc = 0
    visited_instructions = set()

    while i not in visited_instructions:
        visited_instructions.add(i)
        i, acc = exec(instructions[i], i, acc)

    print(acc)


def part2():

    # yeah, just bruteforce it
    for x in range(len(instructions)):
        i = 0
        acc = 0
        visited_instructions = set()
        copy_instructions = instructions[:]
        curr_inst, curr_number = copy_instructions[x]
        if curr_inst != "acc":
            copy_instructions[x] = ("jmp" if curr_inst == 'nop' else 'nop', curr_number)
        else:
            continue

        while i not in visited_instructions and i < len(copy_instructions):
            visited_instructions.add(i)
            i, acc = exec(copy_instructions[i], i, acc)
        
        if i == len(copy_instructions):
            print(acc)
            break

part1()
part2()

