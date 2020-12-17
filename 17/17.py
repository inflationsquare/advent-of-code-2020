from itertools import product, chain
from functools import reduce
import operator as op


def get_neighbour_coordinates(x, y, z):
    deltas = [x for x in product([-1, 0, 1], repeat=3) if x != (0, 0, 0)]
    return [(sum(x) for x in zip((1, 2, 3), d)) for d in deltas]


def new_status(status, local_status):
    if v == "#" and local_count in [2, 3]:
        return "#"
    elif v == "." and local_count == 3:
        return "#"
    else:
        return "."


neighbours = {}

initial_coordinates = []
for i in initial_coordinates:
    neighbours[i] = get_neighbour_coordinates(*i)

coordinate_data = {}
change = {}

# need to consider only coordinates near an active node, others will never change, but need to update possible coordinates from neighbours


def get_coords_to_check(coord_data, neighbours):
    already_on = [c for c, v in coordinate_data.items() if v == "#"]
    on_neighbours = [*reduce(op.add, [neighbours[c] for c, v in coordinate_data.items() if v == "#"], [])]
    yield from set(already_on + on_neighbours)


t = 0
while t < 6:
    # go through all coordinates to check and get their update
    for c in get_coords_to_check(coordinate_data, neighbours):
        status = coordinate_data.get(c, ".")
        local_count = sum(coordinate_data.get(x, ".") == "#" for x in neighbours[x])
        change[c] = new_status(status, local_count)
        if c not in neighbours.keys():
            neighbours[c] = get_neighbour_coordinates(*c)

    # set all the updates in the data
    for c, v in change.items():
        coordinate_data[c] = v

    # flush the data
    coordinate_data = {k: v for k, v in coordinate_data if v == "#"}

print(sum(v == "#" for v in coordinate_data.values()))
