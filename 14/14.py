import re
from itertools import product

pattern = re.compile("^(\w*)(?:\[(\d+)\]|)\s=\s([0-9X]+)$")

with open("14.in", "r") as f:
    data = f.read().splitlines()
    instructions = [pattern.findall(x) for x in data]


def apply_mask(s, m):
    m1 = int(m.replace("X", "0"), 2)
    m2 = int(m.replace("X", "1"), 2)
    return m2 & (m1 | s)


storage = {}
mask = ""
for [(op, adr, val)] in instructions:
    if op == "mask":
        mask = val
    else:
        storage[int(adr)] = apply_mask(int(val), mask)

print(sum(storage.values()))

# ---


def generate_adrs(adr, mask):
    masked = (b if m == "0" else m for b, m in zip(format(int(adr), "036b"), mask.zfill(36)))
    adrs = (x for x in product(*(x if x != "X" else "01" for x in masked)))
    yield from map(lambda x: int("".join(x), 2) % 2 ** 36 - 1, adrs)


storage = {}
mask = ""
for [(op, adr, val)] in instructions:
    if op == "mask":
        mask = val
    else:
        for a in generate_adrs(adr, mask):
            storage[a] = int(val)

print(sum(storage.values()))
