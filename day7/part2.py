with open('input.txt') as h:
    home = h.read().split('\n')

def bit(inp):
    if inp in result:
        return result[inp]
    if inp not in inputs:
        return int(inp)
    k = inputs[inp]

    parts = k.split(' ')

    if len(parts) == 1:
        a, = parts
        result[inp] = bit(a)
        return result[inp]

    elif len(parts) == 2:

        name,a = parts[0], parts[1]

        if name =="NOT":
            result[inp] = ~bit(a)
            return result[inp]

    elif len(parts) == 3:

        a,name,b =parts[0],parts[1],parts[2]

        if name == "AND":
            result[inp] = bit(a) & bit(b)
            return result[inp]
        elif name =="XOR":
            result[inp] = bit(a) ^ bit(b)
            return result[inp]
        elif name == "OR":
            result[inp] = bit(a) | bit(b)
            return result[inp]
        elif name == "RSHIFT":
            result[inp] = bit(a) >> bit(b)
            return  result[inp]
        elif name == 'LSHIFT':
            result[inp] = bit(a) << bit(b)
            return result[inp]

inputs = {}
result= {}

for k in home:

    d = k.split(' -> ')
    inp,res = d[0], d[1]
    inputs[res]= inp

i = bit('a')
result = dict()
result['b'] = i

output = open('output2.txt', 'w')
output.write(str(bit('a')))

output.close()
h.close()
