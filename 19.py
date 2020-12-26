import re

example_input = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

with open('inputs/19.txt') as f:
    lines = f.read()

rules = {}
messages = []
is_messages = False
for line in lines.split('\n'):
    if line == "":
        is_messages = True

    elif is_messages:
        messages.append(line)
    else:
        id, rule = line.split(':')
        rules[id] = rule[1:]

built_rules = {}
rule_count = len(rules)
while len(built_rules) < rule_count:
    to_delete = []
    build_set = set(built_rules)
    for id in rules:
        rule = rules[id]
        if rule.startswith("\""):
            built_rules[id] = f'{rule[1:-1]}'
            to_delete.append(id)
        else:
            children = set([x for x in rule.split(' ') if x.isdigit()])
            if children.intersection(build_set) == children:
                if id == '11':
                    rule42 = built_rules['42']
                    rule31 = built_rules['31']
                    rule = '(' + '|'.join(
                        [f'{rule42}{{{n}}}{rule31}{{{n}}}' for n in range(1, 15)]) + ')'
                else:
                    chunks = rule.split('|')
                    for i, chunk in enumerate(chunks):
                        keys = ''.join(['(' + built_rules[x] + ')'
                                        for x in chunk.split(' ') if x.isdigit()])
                        chunks[i] = keys
                    # for i in sorted(children, key=lambda x: int(x), reverse=True):
                    #     for j, c in enumerate(chunks):
                    #         chunks[j] = '(' + c.replace(i,
                    #                                     built_rules[i]) + ')'
                    rule = '|'.join(chunks)
                    rule = f'({rule})'.replace(' ', '')
                if id == '8':
                    rule += '+'
                built_rules[id] = rule
                to_delete.append(id)

    for i in to_delete:
        del rules[i]

regexp_rule0 = built_rules['0']
pattern = f'^{regexp_rule0}$'
compiled_pattern = re.compile(pattern)

matchs = [x for x in messages if compiled_pattern.match(x)]
print(len(matchs))
