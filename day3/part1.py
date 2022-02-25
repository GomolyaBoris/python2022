import operator


def update_current_location(current_location, instruction):
    return tuple(map(operator.add, current_location,
                     {
                         "^": (0,  1),
                         ">": (1,  0),
                         "v": (0, -1),
                         "<": (-1, 0)
                     }[instruction]))


def increment_count_for_location(location, coordinate):
    if location not in coordinate:
        coordinate[location] = 0

    coordinate[location] += 1

with open("input.txt") as file:
    elf = file.readline()

    location = (0, 0)
    coordinate_visit_counts = {location: 1}

    for instruction in elf:
        location = update_current_location(location, instruction)

        increment_count_for_location(location, coordinate_visit_counts)


a = open('output1.txt', 'w')
a.write(str(len(coordinate_visit_counts)))
a.close()
