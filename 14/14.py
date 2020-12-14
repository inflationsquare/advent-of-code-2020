import re
from itertools import product
from collections import Counter
from functools import reduce

pattern = re.compile("^(\w*)\[?(\d+)?\]?\s=\s(.*)$")

with open("14.in", "r") as f:
    data = f.read().splitlines()
    instructions = [pattern.findall(x) for x in data]


def apply_mask(s, m):
    m1 = int(m.replace("X", "0"), 2)
    m2 = int(m.replace("X", "1"), 2)
    return m2 & (m1 | s)


storage = {}


mask = ""
for [(op, addr, val)] in instructions:
    if op == "mask":
        mask = val
    else:
        storage[int(addr)] = apply_mask(int(val), mask)

print(sum(storage.values()))

# ---


def generate_addrs(adr, m):
    change = []
    bits = list(bin(int(adr)))[2:]

    for a, b in zip(["0"] * (36 - len(bits)) + bits, ["0"] * (36 - len(list(m))) + list(m)):
        if b == "1":
            change.append("1")
        if b == "0":
            change.append(a)
        if b == "X":
            change.append("X")

    to_replace = [i for i, v in enumerate(change) if v == "X"]
    floating = len(to_replace)
    for vals in product(*(["0", "1"] for _ in range(floating))):
        for i, v in zip(to_replace, vals):
            change[i] = v
        yield "".join(change)


storage = {}
mask = ""
high = int("".join(["1"] * 36), 2)
for [(op, addr, val)] in instructions:
    if op == "mask":
        mask = val
    else:
        for a in generate_addrs(addr, mask):
            storage[int(a, 2) % high] = int(val)


print(sum(storage.values()))
