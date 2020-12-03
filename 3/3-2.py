from math import prod

with open('3.in', 'r') as f:
    data = f.read().splitlines()

def trees(right, down):
    output = []
    for i, line in enumerate(data[::down]):
        output.append(line[(i*right)%len(line)])
    return len([x for x in output[1:] if x == '#'])

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
print(prod([trees(r,d) for r,d in slopes]))
