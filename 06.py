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

sum = sum(map(lambda x: len(x), answer_group))
print(sum)
