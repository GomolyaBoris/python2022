from hashlib import md5

input = 'ckczppom'
n = 1
a = False

while a == False:
    input_hash = md5((input + str(n)).encode()).hexdigest()
    if a != True and input_hash[:5] == '00000':
        out = open('output1.txt', 'w')
        out.write(str(n))
        out.close()
        a = True

    n += 1

