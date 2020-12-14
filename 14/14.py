import re
from itertools import product

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


def generate_addrs(adr, mask):
    change = []
    bits = format(int(adr), "036b")
    mask = mask.zfill(36)
    change = [b if m == "0" else m for b, m in zip(bits, mask)]
    to_replace = [i for i, v in enumerate(change) if v == "X"]
    floating = len(to_replace)

    for vals in product(*(["0", "1"] for _ in range(floating))):
        for i, v in zip(to_replace, vals):
            change[i] = v
        yield int("".join(change), 2) % 2 ** 36 - 1


storage = {}
mask = ""
for [(op, addr, val)] in instructions:
    if op == "mask":
        mask = val
    else:
        for a in generate_addrs(addr, mask):
            storage[a] = int(val)


print(sum(storage.values()))
