import operator
import re

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
    grouped_elf = re.findall('..', elf)

    start_location = (0, 0)
    location = start_location
    robo_santa = start_location
    coordinate = {start_location: 2}

    for grouped_instruction in grouped_elf:
        location = update_current_location(location, grouped_instruction[0])
        robo_santa = update_current_location(robo_santa, grouped_instruction[1])

        increment_count_for_location(location, coordinate)
        increment_count_for_location(robo_santa, coordinate)


a = open('output2.txt', 'w')
a.write(str(len(coordinate)))
a.close()