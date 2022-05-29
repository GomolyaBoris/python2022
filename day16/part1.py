with open('input.txt') as h:
    home = h.read().split('\n')

TrueSue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

def FindSue(things, values):
    for thing, value in zip(things,values):
        if TrueSue[thing] != int(value):
            return False
    return True

for line in home:
    num = line.split(' ')[1][:-1]
    things = [line.split(' ')[2][:-1],line.split(' ')[4][:-1],line.split(' ')[6][:-1]]
    values = [line.split(' ')[3][:-1],line.split(' ')[5][:-1],line.split(' ')[7]]

    if FindSue(things,values) == True:
        s = num

out = open('output1.txt', 'w')
out.write(str(s))

out.close()
h.close()