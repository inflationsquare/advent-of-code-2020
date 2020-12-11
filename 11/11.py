from itertools import chain, product, permutations
from collections import Counter

with open("11.in", "r") as f:
    data = [x for x in f.read().splitlines()]


def print_data(d):
    print("\n".join(y for y in d))
    print("\n")


def get_adjacent(d, x, y):
    xs = [i for i in [x - 1, x, x + 1] if 0 <= i < len(d[0])]
    ys = [i for i in [y - 1, y, y + 1] if 0 <= i < len(d)]
    adjacent = [[i, j] for i, j in product(xs, ys) if [x, y] != [i, j]]
    return adjacent


def get_nn(data, x, y, x_by, y_by):
    while True:
        x += x_by
        y += y_by
        if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
            return None
        else:
            if data[y][x] != ".":
                return (x, y)


def change(status, adjacent):
    if status == ".":
        return "."
    elif status == "L" and adjacent["#"] == 0:
        return "#"
    elif status == "#" and adjacent["#"] >= 5:
        return "L"
    else:
        return status


indices = [*product(range(len(data[0])), range(len(data)))]

by = set(permutations([-1, -1, 0, 1, 1], 2))
neighbours = {(x, y): [get_nn(data, x, y, x_by, y_by) for x_by, y_by in by] for x, y in indices}
for key, value in neighbours.items():
    neighbours[key] = [x for x in neighbours[key] if x]


def stabilise(data):
    new_data = {x: "." for x in indices}
    for x in indices:
        if data[x] != ".":
            adjacent = Counter(data[(i, j)] for i, j in neighbours[x])
            new_data[x] = change(data[x], adjacent)
    if new_data == data:
        return Counter(new_data.values())
    else:
        return stabilise(new_data)


print(stabilise({(x, y): data[y][x] for x, y in indices}))
