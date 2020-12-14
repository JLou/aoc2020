# Part 1
with open('inputs/06.txt', 'r') as f:
    answer_group = list()
    answer_set = set()
    for line in f.readlines():
        if(line == '\n'):
            answer_group.append(answer_set)
            answer_set = set()
        else:
            for c in (x for x in line if x != '\n'):
                answer_set.add(c)

    answer_group.append(answer_set)

sum1 = sum(map(lambda x: len(x), answer_group))
print("Part 1: " + str(sum1))

# Part 2
with open('inputs/06.txt', 'r') as f:
    answer_group = list()
    answer_set = None
    for line in f.readlines():
        if(line == '\n'):
            answer_group.append(answer_set)
            answer_set = None
        else:
            new_set = set([x for x in line if x != '\n'])
            answer_set = new_set if answer_set == None else answer_set.intersection(new_set)


    answer_group.append(answer_set)

sum2 = sum(map(lambda x: len(x), answer_group))
print("Part 2: " + str(sum2))
