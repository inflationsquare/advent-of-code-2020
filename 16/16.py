from math import prod
import re
from itertools import chain

rule_pattern = re.compile("^(.+): (\d+)-(\d+) or (\d+)-(\d+)$")


def make_rule(b1, b2):
    return lambda x: (b1[0] <= x <= b1[1]) or (b2[0] <= x <= b2[1])


with open("16.in", "r") as f:
    data = f.read().split("\n\n")
    data = [x.split("\n") for x in data if x]
    rules, own_ticket, tickets = data
    parsed_rules = map(lambda s: rule_pattern.findall(s), rules)
    rules = {n: make_rule([int(a1), int(a2)], [int(b1), int(b2)]) for [(n, a1, a2, b1, b2)] in parsed_rules}
    tickets = [[int(x) for x in t.split(",")] for t in tickets[1:]]

print(sum(x for x in chain.from_iterable(tickets) if not any(r(x) for r in rules.values())))


# ---

valid_tickets = [t for t in tickets if all(any(r(x) for r in rules.values()) for x in t)]

fields = {}
for idx in range(len(valid_tickets[0])):
    vals = [x[idx] for x in valid_tickets]
    for n, f in rules.items():
        if all(map(f, vals)):
            fields[idx] = fields.get(idx, []) + [n]

final_fields = {}
while len(final_fields.keys()) < len(fields.keys()):
    val = [(k, v) for k, v in fields.items() if len(v) == 1][0]
    final_fields[val[0]] = val[1][0]
    for k, v in fields.items():
        fields[k] = [x for x in v if x != val[1][0]]

needed_fields = [k for k, v in final_fields.items() if v[:9] == "departure"]
my_ticket = [int(x) for x in own_ticket[1].split(",")]

print(prod(x for i, x in enumerate(my_ticket) if i in needed_fields))
