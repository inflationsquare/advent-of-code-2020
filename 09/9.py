from collections import deque

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
print(first_invalid)

# move across the array like a snake, grow the right until it's greater than the target, then shrink from the left until it's smaller than the target, repeat until equal to the target
invalid_summer = deque()
running_total = 0
data_stream = iter(data)

while running_total != first_invalid or len(invalid_summer) == 1:
    if running_total < first_invalid:
        next_number = next(data_stream)
        invalid_summer.append(next_number)
        running_total += next_number
    elif running_total > first_invalid:
        tail_number = invalid_summer[0]
        invalid_summer.popleft()
        running_total -= tail_number
    else:
        pass

print(min(invalid_summer) + max(invalid_summer))
