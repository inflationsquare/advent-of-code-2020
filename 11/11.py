from itertools import product
from itertools import chain
from collections import Counter

with open("11.in", "r") as f:
    data = [[y for y in x] for x in f.read().splitlines()]


def get_adjacent(d, x, y):
    xs = [i for i in [x - 1, x, x + 1] if 0 <= i < len(d[0])]
    ys = [i for i in [y - 1, y, y + 1] if 0 <= i < len(d)]
    adjacent = [[i, j] for i, j in product(xs, ys) if [x, y] != [i, j]]
    return adjacent


def change(status, adjacent):
    if status == ".":
        return "."
    elif status == "L" and adjacent["#"] == 0:
        return "#"
    elif status == "#" and adjacent["#"] >= 4:
        return "L"
    else:
        return status


def print_data(d):
    print("\n".join("".join(x for x in y) for y in d))
    print("\n")


def stabilise(data):
    new_data = [[x for x in "." * len(data[0])] for x in range(len(data))]
    for x, y in product(range(len(data[0])), range(len(data))):
        adjacent = Counter(data[j][i] for i, j in get_adjacent(data, x, y))
        new_data[y][x] = change(data[y][x], adjacent)
    if new_data == data:
        return Counter(chain.from_iterable(new_data))
    else:
        return stabilise(new_data)


print(stabilise(data))
