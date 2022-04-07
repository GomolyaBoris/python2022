import re
import itertools


def compute(input_file):
    locations = set()
    distance = {}

    for line in input_file:
        start = line.split(" ")[0]
        end = line.split(" ")[2]

        locations.add(start)
        locations.add(end)

        distance_between = int(re.findall("\d+", line)[0])
        distance[(start, end)] = distance_between
        distance[(end, start)] = distance_between

    return locations, distance


if __name__ == "__main__":
    with open("input.txt") as input_file:
        (locations, distance) = compute(input_file)

        path_lengths = {}

        for path in itertools.permutations(locations):
            segments = [(path[i], path[i + 1]) for i in range(0, len(locations) - 1)]
            lengths = [distance[segment] for segment in segments]

            path_lengths[path] = sum(lengths)
        out = open("output1.txt", "w")
        out.write(str(min(path_lengths.values())))
        out.close()

