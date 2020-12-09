with open("9.in", "r") as f:
    data = [int(x) for x in f.read().splitlines()]


def is_valid(candidate, source):
    return any((candidate - s) in source for s in source)


def find_first_invalid(start, end, data):
    if end >= len(data):
        return None
    else:
        valid = is_valid(data[end], data[start:end])
        if not valid:
            return data[end]
        else:
            return find_first_invalid(start + 1, end + 1, data)


first_invalid = find_first_invalid(0, 25, data)

matching_array = next(
    data[i : i + j]
    for i in range(0, len(data))
    for j in range(2, len(data) - i + 1)
    if sum(data[i : i + j]) == first_invalid
)

print(min(matching_array) + max(matching_array))
