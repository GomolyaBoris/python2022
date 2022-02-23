from functools import reduce


def dimensions_parser(raw_dimensions):
    return sorted([int(raw_dimension) for raw_dimension in raw_dimensions.strip("\n").split("x")])


def get_parsed_dimensions():
    result = []

    with open("input.txt") as file:
        for line in file:
            raw_dimensions = str(line)

            result.append(dimensions_parser(raw_dimensions))

    return result

def ribbon(dimensions):
    A = 2*(dimensions[0] + dimensions[1])
    B = reduce(lambda x, y: x*y, dimensions, 1)
    C = A + B

    return C


parsed_dimensions = get_parsed_dimensions()

total = sum([ribbon(dimensions) for dimensions in parsed_dimensions])


a = open('output2.txt', 'w')
a.write(str(total))
a.close()