from collections import Counter
from itertools import chain

with open('6.in', 'r') as f:
    data =  f.read().split('\n\n')

print(sum(len(set(x)) for x in map(lambda x: x.replace('\n', ''), data)))

answer_sets = [[set(y) for y in x.split('\n')] for x in data]
answer_counts = [Counter(chain.from_iterable(x)) for x in answer_sets]
tally = sum(sum(1 for y in c.values() if y == len(s)) for c, s in zip(answer_counts, answer_sets))

print(tally)

