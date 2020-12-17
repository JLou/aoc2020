import re
from dataclasses import dataclass


@dataclass
class Rule:
    name: str
    interval1: (int, int)
    interval2: (int, int)

    def is_valid(self, value: int) -> bool:
        return (self.interval1[0] <= value <= self.interval1[1]) or (self.interval2[0] <= value <= self.interval2[1])


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

invalid_fields = []
for ticket in nearby_tickets:
    for field in ticket:
        if not is_field_valid(field, rules):
            invalid_fields.append(field)

print(sum(invalid_fields))