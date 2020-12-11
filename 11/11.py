from itertools import product, permutations
from itertools import chain
from collections import Counter

with open("11.in", "r") as f:
    data = [[y for y in x] for x in f.read().splitlines()]


def print_data(d):
    print("\n".join("".join(x for x in y) for y in d))
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
        try:
            assert x >= 0
            assert y >= 0
            if data[y][x] != ".":
                return (x, y)
        except:
            return None


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

by = set([*permutations([-1, -1, 0, 1, 1], 2)])
neighbours = {(x, y): [get_nn(data, x, y, x_by, y_by) for x_by, y_by in by] for x, y in indices if data[y][x] != "."}
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
