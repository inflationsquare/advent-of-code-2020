from collections import Counter
from itertools import chain

with open('6.in', 'r') as f:
    data =  f.read().split('\n\n')

print(sum(len(set(x)) for x in map(lambda x: x.replace('\n', ''), data)))

answer_sets = [[set(y) for y in x.split('\n')] for x in data]
tally = sum(sum(1 for y in Counter(chain.from_iterable(s)).values() if y == len(s)) for s in answer_sets)

print(tally)

