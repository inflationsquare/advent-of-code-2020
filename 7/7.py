import re
import itertools

with open("7.in", "r") as f:
    data = f.read().splitlines()
    data = [x.split(' contain ') for x in data]

parent_pattern = re.compile(r'^([\w\s?]+) bags?')
child_pattern = re.compile(r'(\d+) ([\w\s?]+) bags?')

parents = map(lambda x: parent_pattern.findall(x[0]), data)
children = map(lambda x: child_pattern.findall(x[1]), data)

rules = {p[0]: {x[1]: int(x[0]) for x in c} for p, c in zip(parents, children)}

def get_ancestors(name):
    parents = [parent for parent, children in rules.items() if name in children]
    if not parents:
        return parents
    else:
        return parents + [*itertools.chain.from_iterable(get_ancestors(x) for x in parents)]
    
ancestors = set(get_ancestors('shiny gold')) 
print(len(ancestors))


def get_children(name):
    children = [*itertools.chain.from_iterable([x]*y for x, y in rules[name].items())]
    if not children:
        return children
    else:
        return children + [*itertools.chain.from_iterable(get_children(x) for x in children)]

print(len(get_children('shiny gold')))





