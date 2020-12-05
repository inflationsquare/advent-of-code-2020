with open('5.in', 'r') as f:
    data = f.read().splitlines()

def get_seat_index(s):
    bin_map = {'F': '0', 'B': '1', 'R': '1', 'L': '0'}
    s = ''.join(map(lambda c: bin_map[c], s))
    return int(s, 2)

seat_indexes = set(get_seat_index(s) for s in data)

print(max(seat_indexes))
print(set(range(min(seat_indexes), max(seat_indexes))).difference(seat_indexes))
