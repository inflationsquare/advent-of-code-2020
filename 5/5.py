with open('5.in', 'r') as f:
    data = f.read().splitlines()

def get_seat_index(s):
    bin_map = [['F', '0'], ['B', '1'], ['R', '1'], ['L', '0']]
    for x, y in bin_map:
        s = s.replace(x,y)
    return int(s[:7], 2)*8 + int(s[7:], 2)

seat_indexes = set(get_seat_index(s) for s in data)

print(max(seat_indexes))
print(set(range(min(seat_indexes), max(seat_indexes))).difference(seat_indexes))
