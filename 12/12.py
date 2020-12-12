import itertools
import re

with open("12.in", "r") as f:
    data = f.read().splitlines()

pattern = re.compile("^(.)(\d+)$")
instructions = [(x, int(y)) for [(x, y)] in [pattern.findall(x) for x in data]]
dir_signs = {"W": -1, "E": 1, "N": 1, "S": -1}
idx = {"W": 0, "E": 0, "N": 1, "S": 1}

facing = "E"
ship_displacement = [0, 0]
waypoint_displacement = [10, 1]


def rotate(starting, direction, degrees):

    directions = {"N": 0, "E": 90, "S": 180, "W": 270}
    decode = {v: k for k, v in directions.items()}
    lr = {"L": -1, "R": 1}

    return decode[(directions[starting] + lr[direction] * degrees) % 360]


def rotate_waypoint(p, direction, degrees):
    lr = {"L": -1, "R": 1}
    x, y = p

    degrees = (lr[direction] * degrees) % 360
    if degrees == 0:
        return [x, y]
    elif degrees == 90:
        return [y, -x]
    elif degrees == 180:
        return [-x, -y]
    else:
        return [-y, x]


# part 1
for l, n in instructions:
    if l in ["R", "L"]:
        facing = rotate(facing, l, n)
    elif l == "F":
        ship_displacement[idx[facing]] += n * dir_signs[facing]
    else:
        ship_displacement[idx[l]] += n * dir_signs[l]

print(sum(abs(x) for x in ship_displacement))

# part 2
ship_displacement = [0, 0]
for l, n in instructions:
    if l in ["R", "L"]:
        waypoint_displacement = rotate_waypoint(waypoint_displacement, l, n)
    elif l == "F":
        ship_displacement[0] += n * waypoint_displacement[0]
        ship_displacement[1] += n * waypoint_displacement[1]
    else:
        waypoint_displacement[idx[l]] += dir_signs[l] * n

print(sum(abs(x) for x in ship_displacement))
