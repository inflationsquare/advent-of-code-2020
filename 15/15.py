# Test input
# input = [0, 3, 6]

input = [8, 13, 1, 0, 18, 9]

turn = len(input)
number = input[-1]
storage = {}
for i, v in enumerate(input):
    storage[v] = storage.get(v, []) + [i + 1]


while turn < 2020:
    if len(storage.get(number)) == 1:
        number = 0
        turn += 1
        storage[number] = storage.get(number, []) + [turn]
    else:
        number = turn - storage[number][-2]
        turn += 1
        storage[number] = storage.get(number, [])[-2:] + [turn]

print(number)
