with open("input.txt") as file:

    b = 0
    c = 1
    input = []

    for line in file:
        trimmed_line = line[:-1]

        escaped_quotes = trimmed_line.replace("\\", "\\\\")
        escaped_slashes = escaped_quotes.replace("\"", "\\\"")

        b += len(trimmed_line)
        c += (len(escaped_slashes) + 2)
        input.append(trimmed_line)


out = open("output2.txt", "w")
out.write(str(c - b))
out.close()