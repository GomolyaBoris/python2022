with open('input.txt') as d:
    house = int(d.read())//11

for houses in range(100, house):
    sum = 0
    pip = 1

    while pip <= 50:
        if houses % pip == 0:
            sum += houses//pip
        pip +=1

    if sum >= house:

        out = open('output2.txt', 'w')
        out.write(str(houses))
        out.close()
        d.close()
        break


