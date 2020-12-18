import re
from dataclasses import dataclass


@dataclass
class Rule:
    name: str
    interval1: (int, int)
    interval2: (int, int)
    field_index: int = None

    def is_valid(self, value: int) -> bool:
        return (self.interval1[0] <= value <= self.interval1[1]) or (self.interval2[0] <= value <= self.interval2[1])
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()
    def __hash__(self):
        return hash(self.name)


rule_pattern = re.compile(r'^(.+): (\d+)-(\d+) or (\d+)-(\d+)$')

STATE_RULES = 0
STATE_MYTICKET = 1
STATE_NEARBY_TICKETS = 2

with open('inputs/16.txt', 'r') as f:
    lines = f.readlines()

state = STATE_RULES
rules = []
myticket = []
nearby_tickets = []

for line in lines:
    if state == STATE_RULES:
        groups = rule_pattern.match(line)
        if groups:
            interval1 = (int(groups.group(2)), int(groups.group(3)))
            interval2 = (int(groups.group(4)), int(groups.group(5)))
            rule = Rule(groups.group(1), interval1, interval2)
            rules.append(rule)
        else:
            state = STATE_MYTICKET
    elif state == STATE_MYTICKET and not line.startswith("your ticket"):
        if not ',' in line:
            state = STATE_NEARBY_TICKETS
        else:
            myticket = [int(i)for i in line[:-1].split(',')]
    else:
        if ',' in line:
            nearby_tickets.append([int(i)for i in line[:-1].split(',')])

def is_field_valid(value, rules):
    return any(map(lambda rule: rule.is_valid(value), rules))

def is_valid_ticket(ticket, rules):
    for field in ticket:
        if not is_field_valid(field, rules):
            return False
    return True

def part1():
    invalid_fields = []
    for ticket in nearby_tickets:
        for field in ticket:
            if not is_field_valid(field, rules):
                invalid_fields.append(field)
    print(sum(invalid_fields))


def part2():
    valid_tickets = [x for x in  nearby_tickets if is_valid_ticket(x, rules)]
    candidates = {}
    rule_associations = {}
    ticket_length = len(valid_tickets[0])
    for i in range(ticket_length):
        candidates[i] = []
        for rule in rules:
            a = [rule.is_valid(fields[i]) for fields in valid_tickets]
            if all(a):
                candidates[i].append(rule)

    to_remove = set()
    while len(rule_associations) < ticket_length:
        for i in candidates:
            if len(candidates[i]) == 1:
                to_remove.add(candidates[i][0])
                rule_associations[i] = candidates[i][0]
            else:
                for r in to_remove:
                    if r in candidates[i]:
                        candidates[i].remove(r)
    product = 1
    for i in rule_associations:
        if rule_associations[i].name.startswith("departure"):
            product *= myticket[i]
        print(f'rule {rule_associations[i].name} is for field index #{i}' )
    print(product)
part2()