from hashlib import md5

with open("input.txt", 'r') as f:
    ff = f.readline()
    for i in range(9999999):
        input_hash = ff
        input_hash = (str(input_hash) + str(i))

        input_hash = md5((str(input_hash)).encode()).hexdigest()

        if input_hash[:6] == '000000':
            out = open('output2.txt', 'w')
            out.write(str(i))
            out.close()
            break
