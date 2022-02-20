file = 'input.txt'

with open(file, 'r') as input_file:
    for line in input_file:
        print(str(len(line.split('('))-len((line.split(')')))))

a = open('output1.txt', 'w')
a.write(str(len(line.split('('))-len((line.split(')')))))
a.close()
