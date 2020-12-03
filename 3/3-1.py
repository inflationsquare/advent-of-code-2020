with open('3.in', 'r') as f:
    data = f.read().splitlines()

output = []
for i, line in enumerate(data):
    output.append(line[(i*3)%len(line)])

print(len([x for x in output if x == '#']))

