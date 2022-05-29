ON = "#"
OFF = "."


def animate(matrix):
    result = []

    rows = len(matrix)
    columns = len(matrix[0])

    for row in range(0, rows):
        result_row = []

        for column in range(0, columns):
            neighbors = [matrix[row + i][column + j] for i in range(-1, 2) for j in range(-1, 2) if
                               abs(i) + abs(j) in [1, 2] and 0 <= row + i < rows and 0 <= column + j < columns]

            result_row.append(update(matrix[row][column], neighbors))

        result.append(result_row)

    return result


def update(initial_state, neighbors):
    number = len([neighbor for neighbor in neighbors if neighbor == ON])

    if initial_state == ON:
        return ON if number in [2, 3] else OFF
    if initial_state == OFF:
        return ON if number == 3 else OFF


if __name__ == "__main__":
    with open("input.txt") as input_file:
        matrix = []

        for line in input_file:
            matrix.append([char for char in line.strip("\n")])

        step_count = 0

        while step_count < 100:
            matrix = animate(matrix)
            step_count += 1

        lights = sum(sum([1 for light in row if light == ON]) for row in matrix)


        out = open("output1.txt", "w")
        out.write(str(int(lights)))
        out.close()