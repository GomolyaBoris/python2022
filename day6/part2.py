import re

def instruction():
    if line.startswith("turn off"):
        return lambda x: max(x - 1, 0)
    elif line.startswith("toggle"):
        return lambda x: x + 2
    elif line.startswith("turn on"):
        return lambda x: x + 1
    else:
        return lambda x: x


matrix = {}

for i in range(1000):
    for j in range(1000):
        matrix[(i, j)] = 0

with open("input.txt") as f:
    for line in f:
        coordinates = re.match("[\D]*(\d+),(\d+)[\D]*(\d+),(\d+)", line)

        apply = instruction()

        for i in range(int(coordinates.group(1)), int(coordinates.group(3)) + 1):
            for j in range(int(coordinates.group(2)), int(coordinates.group(4)) + 1):
                matrix[(i, j)] = apply(matrix[(i, j)])

    brightness = 0

    for light in matrix.values():
        brightness += light

    a = open('output2.txt', 'w')
    a.write(str(brightness))
    a.close()