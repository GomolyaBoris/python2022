def dimensions_parser(raw_dimensions):
    return sorted([int(raw_dimension) for raw_dimension in raw_dimensions.strip("\n").split("x")])


def get_parsed_dimensions():
    result = []

    with open("input.txt") as file:
        for line in file:
            raw_dimensions = str(line)

            result.append(dimensions_parser(raw_dimensions))

    return result

def area(dimensions):
    surface_areas = [dimensions[0] * dimensions[1], dimensions[0] * dimensions[2], dimensions[1] * dimensions[2]]

    side = 2 * sum(surface_areas) + surface_areas[0]

    return side


parsed_dimensions = get_parsed_dimensions()

total = sum([area(dimensions) for dimensions in parsed_dimensions])


a = open('output1.txt', 'w')
a.write(str(total))
a.close()