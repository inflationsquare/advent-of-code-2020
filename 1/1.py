from itertools import combinations
from math import prod

with open("1-1.in", "r") as f:
    data = f.read().splitlines()
print(next(prod(x) for x in combinations([int(x) for x in data], 2) if sum(x) == 2020))
print(next(prod(x) for x in combinations([int(x) for x in data], 3) if sum(x) == 2020))
