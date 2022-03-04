def repeated(string):
    for i in range(len(string) - 3):
        pair = string[i:i+2]

        if pair in string[i+2:]:
            return True

    return False


def separated(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True

    return False


def nice(string):
    return repeated(string)\
           and separated(string)


with open("input.txt") as file:
    counter = 0

    for line in file:
        if nice(line):
            counter += 1


    out = open('output2.txt', 'w')
    out.write(str(counter))
    out.close()