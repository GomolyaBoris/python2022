import operator

floor = 0
char_count = 0
position = False

with open('input.txt', 'r') as input_file:
    for line in input_file:
        for char in line:
            if operator.eq('(', char):
                floor += 1
            elif operator.eq(')', char):
                floor -= 1
            char_count += 1
            if(floor < 0):
                if not position:
                    position = True
                    a = open('output2.txt', 'w')
                    a.write(str(char_count))
a.close()
input_file.close()



#print(str(char_count))