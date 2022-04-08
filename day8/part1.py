import re
a = "P"
with open("input.txt") as file:

    b = 0
    c = 0
    input = []

    for line in file:
        trimmed_line = line[:-1]

        no_line = trimmed_line.replace("\\\\", a)
        no_quotes = no_line.replace("\\\"", a)
        no_hexcode_line = re.sub("\\\\x..", a, no_quotes)

        b += len(trimmed_line)
        c += (len(no_hexcode_line) - 2)
        input.append(trimmed_line)

out = open("output1.txt", "w")
out.write(str(b - c))
out.close()