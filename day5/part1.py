def vowel(string):
    vowels = [char for char in string if char in ['a', 'e', 'i', 'o', 'u']]

    return len(vowels) >= 3


def twice(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True

    return False


def blacklist(string):
    for blacklisted in ['ab', 'cd', 'pq', 'xy']:
        if blacklisted in string:
            return False

    return True


def nice(string):
    return vowel(string)\
            and twice(string)\
            and blacklist(string)


with open("input.txt") as file:
    counter = 0

    for line in file:
        if nice(line):
            counter += 1


    out = open('output1.txt', 'w')
    out.write(str(counter))
    out.close()