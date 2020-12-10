from collections import Counter
from math import prod


with open("10.in", "r") as f:
    data = [int(x) for x in f.read().splitlines()]

joltages = [0] + sorted(data) + [max(data) + 3]
diffs = Counter(joltages[i + 1] - joltages[i] for i, _ in enumerate(joltages) if i + 1 < len(joltages))
print(prod(y for x, y in diffs.items() if x in [1, 3]))


count = Counter((0,))
for i, x in enumerate(joltages):
    # for each joltage, tally up the previously calculated tallies in the valid window
    # if something doesn't exist it won't contribute because it's 0 in the counter
    count[x] += sum(count[i] for i in range(x - 3, x))

print(count[joltages[-1]])


def part2(l, reach=3, i=1, count=Counter((0,))):
    if i == len(l):
        return count[l[i - 1]]
    else:
        for r in range(reach):
            count[l[i]] += count[l[i] - r - 1]
        return part2(l, reach, i + 1, count)


print(part2(joltages))
