from itertools import product
from itertools import chain
from collections import Counter

with open("test.in", "r") as f:
    data = [[y for y in x] for x in f.read().splitlines()]


def print_data(d):
    print("\n".join("".join(x for x in y) for y in d))
    print("\n")


def get_adjacent(d, x, y):
    xs = [i for i in [x - 1, x, x + 1] if 0 <= i < len(d[0])]
    ys = [i for i in [y - 1, y, y + 1] if 0 <= i < len(d)]
    adjacent = [[i, j] for i, j in product(xs, ys) if [x, y] != [i, j]]
    return adjacent


def get_adjacent_2(d, x, y):
    indices = [[i, j] for i, j in product(range(len(d[0])), range(len(d))) if [x, y] != [i, j]]
    chairs = [[i, j] for i, j in indices if d[j][i] != "."]
    offsets = [[i - x, j - y] for i, j in chairs]
    line_of_sight = [
        [i, j, dx, dy] for [[i, j], [dx, dy]] in zip(chairs, offsets) if dx == 0 or dy == 0 or abs(dx) == abs(dy)
    ]

    directions = [
        [[i, j, abs(dx) + abs(dy)] for [i, j, dx, dy] in line_of_sight if dx > 0 and dy == 0],
        [[i, j, abs(dx) + abs(dy)] for [i, j, dx, dy] in line_of_sight if dx < 0 and dy == 0],
        [[i, j, abs(dx) + abs(dy)] for [i, j, dx, dy] in line_of_sight if dx == 0 and dy > 0],
        [[i, j, abs(dx) + abs(dy)] for [i, j, dx, dy] in line_of_sight if dx == 0 and dy < 0],
        [[i, j, abs(dx) + abs(dy)] for [i, j, dx, dy] in line_of_sight if dx > 0 and dy > 0],
        [[i, j, abs(dx) + abs(dy)] for [i, j, dx, dy] in line_of_sight if dx < 0 and dy < 0],
        [[i, j, abs(dx) + abs(dy)] for [i, j, dx, dy] in line_of_sight if dx < 0 and dy > 0],
        [[i, j, abs(dx) + abs(dy)] for [i, j, dx, dy] in line_of_sight if dx > 0 and dy < 0],
    ]

    return [sorted(l, key=lambda q: q[-1])[0][:2] for l in directions if l]


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
nearest_neighbours = {(x, y): get_adjacent_2(data, x, y) for x, y in indices}


def stabilise(data):
    new_data = [[x for x in "." * len(data[0])] for x in range(len(data))]
    for x, y in indices:
        adjacent = Counter(data[j][i] for i, j in nearest_neighbours[(x, y)])
        new_data[y][x] = change(data[y][x], adjacent)
    if new_data == data:
        return Counter(chain.from_iterable(new_data))
    else:
        return stabilise(new_data)


print(stabilise(data))
