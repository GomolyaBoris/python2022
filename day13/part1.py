import re
import itertools


def compute_happiness(order, dict):
    result = 0

    for i in range(len(order)):
        first = order[i]
        second = order[(i + 1) % len(order)]

        result += dict[(first, second)]
        result += dict[(second, first)]

    return result

with open("input.txt") as input_file:
    guest_list = set()
    happiness_dict = {}

    for line in input_file:
        line = re.sub("lose ", "-", line)
        tuple = (line.split(" ")[0], line.split(" ")[-1].strip(".\n"))
        for guest in tuple:
            guest_list.add(guest)

        happiness_delta = int(re.findall("-?\d+", line)[0])
        happiness_dict[tuple] = happiness_delta

    levels = {}
    for seating_order in itertools.permutations(guest_list):
        happiness = compute_happiness(seating_order, happiness_dict)
        levels[seating_order] = happiness

    out = open("output1.txt", "w")
    out.write(str(max(levels.values())))
    out.close()