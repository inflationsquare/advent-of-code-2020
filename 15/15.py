# Test input
# input = [0, 3, 6]

input = [8, 13, 1, 0, 18, 9]

turn = len(input)
number = input[-1]
storage = {}
for i, v in enumerate(input):
    storage[v] = i + 1


while turn < 30000000:
    if not storage.get(number, None):
        storage[number] = turn
        number = 0
        turn += 1
    else:
        last_seen = storage[number]
        storage[number] = turn
        number = turn - last_seen
        turn += 1

print(number)
