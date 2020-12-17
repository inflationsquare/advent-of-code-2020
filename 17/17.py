from itertools import product, chain
from functools import reduce, lru_cache
import operator as op
from pprint import pprint


def get_neighbour_coordinates(p):
    deltas = [x for x in product([-1, 0, 1], repeat=len(p)) if not all(i == 0 for i in x)]
    return [tuple(sum(x) for x in zip(p, d)) for d in deltas]


@lru_cache()
def new_status(status, local_status):
    if status == "#" and local_status in [2, 3]:
        return "#"
    elif status == "." and local_status == 3:
        return "#"
    else:
        return "."


def get_coords_to_check(coord_data, neighbours):
    already_on = [c for c, v in coord_data.items() if v == "#"]
    on_neighbours = [*reduce(op.add, [neighbours[c] for c, v in coord_data.items() if v == "#"], [])]
    return set(already_on + on_neighbours)


def solve(inital_coordinates):

    coordinate_data = {x: "#" for x in initial_coordinates}

    neighbours = {}
    for i in initial_coordinates:
        neighbours[i] = get_neighbour_coordinates(i)

    change = {}

    t = 0
    while t < 6:
        # go through all coordinates to check and get their update
        for c in get_coords_to_check(coordinate_data, neighbours):
            status = coordinate_data.get(c, ".")
            local_count = sum(coordinate_data.get(x, ".") == "#" for x in get_neighbour_coordinates(c))
            change[c] = new_status(status, local_count)
            if c not in neighbours.keys():
                neighbours[c] = get_neighbour_coordinates(c)

        # set all the updates in the data
        for (c, v) in change.items():
            coordinate_data[c] = v

        # flush the data
        coordinate_data = {k: v for k, v in coordinate_data.items() if v == "#"}
        t += 1

    return sum(v == "#" for v in coordinate_data.values())


# ---


with open("17.in", "r") as f:
    data = f.read().splitlines()

initial_coordinates = []
for j, row in enumerate(data):
    for i, _ in enumerate(row):
        if row[i] == "#":
            initial_coordinates.append((i, j, 0))

print(solve(initial_coordinates))

# ---

initial_coordinates = []
for j, row in enumerate(data):
    for i, _ in enumerate(row):
        if row[i] == "#":
            initial_coordinates.append((i, j, 0, 0))

print(solve(initial_coordinates))
