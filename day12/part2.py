import re
def compute_sum(string):


    for match in re.finditer(":\"red\"", string):
        start = match.span()[0]
        end = match.span()[1] - 1

        number_of_left = 1
        number_of_right = 1

        while number_of_left > 0:
            start -= 1

            if string[start] == "{":
                number_of_left -= 1

            if string[start] == "}":
                number_of_left += 1

        while number_of_right > 0:
            end += 1

            if string[end] == "}":
                number_of_right -= 1

            if string[end] == "{":
                number_of_right += 1

        string = string[:start] + re.sub("\d", "0", string[start:end + 1]) + string[end + 1:]


    return sum([int(n) for n in re.findall("-?\d+", string)])

if __name__ == "__main__":
    with open("input.txt") as input:
        inp = input.readline()

        out = open("output2.txt", "w")
        out.write(str(compute_sum(inp)))
        out.close()