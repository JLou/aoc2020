example_input = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"


def find_matching_bracket(operation, index):
    bracket_count = 0
    for i in range(index, len(operation)):
        if operation[i] == '(':
            bracket_count += 1
        elif operation[i] == ')':
            bracket_count -= 1
        if bracket_count == 0:
            return i


def compute(input):
    left_operand = i = 0
    operation = ''
    while i < len(input):
        c = input[i]
        if c == '(':
            jump_to = find_matching_bracket(input, i)
            c = str(compute(input[i+1: jump_to]))
            i = jump_to
        if c.isdigit():
            if operation == '':
                left_operand = int(c)
            else:
                if operation == '+':
                    left_operand = left_operand + int(c)
                else:
                    left_operand *= int(c)
                operation = ''
        elif c in ['+', '*']:
            operation = c
        i += 1
    return left_operand
    # print(left_operand)


def compute2(input):
    left_operand = i = 0
    operation = ''
    while i < len(input):
        c = input[i]
        if c == '(':
            jump_to = find_matching_bracket(input, i)
            c = str(compute2(input[i+1: jump_to]))
            i = jump_to
        if c.isdigit():
            if operation == '':
                left_operand = int(c)
            else:
                if operation == '+':
                    left_operand = left_operand + int(c)
                else:
                    left_operand *= int(c)
                operation = ''
        elif c in ['+']:
            operation = c
        elif c == '*':
            res = left_operand * compute2(input[i+1:])
            return res
        i += 1
    return left_operand
    # print(left_operand)


with open('inputs/18.txt') as f:
    lines = f.readlines()


print(sum([compute(x) for x in lines]))
print(sum([compute2(x) for x in lines]))
