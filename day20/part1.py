with open('input.txt') as d:
    house = int(d.read())//10

for houses in range(10000, house):
    sum = 0
    pip = 1
    while pip*pip < houses:
        if houses % pip == 0:
            sum += pip
            sum += houses//pip
        pip +=1

    if pip*pip == house:
        sum += pip
    if sum >= house:
        out = open('output1.txt', 'w')
        out.write(str(houses))
        out.close()
        d.close()
        break