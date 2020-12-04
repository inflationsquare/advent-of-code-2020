from math import prod

with open('3.in', 'r') as f:
    data = f.read().splitlines()

def trees(right, down):
    return [line[(i*right)%len(line)] for i, line in enumerate(data[::down])].count('#')

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
print(prod([trees(r,d) for r,d in slopes]))