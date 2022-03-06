import re

def instruction():
    if line.startswith("turn off"):
        return lambda x: 0
    elif line.startswith("toggle"):
        return lambda x: (x + 1) % 2
    elif line.startswith("turn on"):
        return lambda x: 1
    else:
        return lambda x: x


matrix = {}

for i in range(1000):
    for j in range(1000):
        matrix[(i, j)] = 0

with open("input.txt") as file:
    for line in file:
        coordinates = re.match("[\D]*(\d+),(\d+)[\D]*(\d+),(\d+)", line)

        apply = instruction()

        for i in range(int(coordinates.group(1)), int(coordinates.group(3)) + 1):
            for j in range(int(coordinates.group(2)), int(coordinates.group(4)) + 1):
                matrix[(i, j)] = apply(matrix[(i, j)])

    count = 0

    for light in matrix.items():
        count += light[1]


    a = open('output1.txt', 'w')
    a.write(str(count))
    a.close()