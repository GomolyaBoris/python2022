with open('input.txt') as d:
    home = d.read().split('\n')

q = home[-1]
replacements = [(l.split()[0], l.split()[-1]) for l in home if ' => ' in l]
di = dict()

for i in replacements:
    ap = 0
    for j in i[-1]:
        if j.isupper():
            ap +=1
    di[i] = ap

replacements = list(di.items())
replacements.sort(key=lambda x: x[-1])
replacements = [i[0] for i in replacements]

lst = replacements[::-1]

steps = 0

while q != 'e':
    for l, r in lst:
        if r in q:
            q = q.replace(r, l, 1)
            steps += 1
            break

out = open('output2.txt', 'w')
out.write(str(steps))
out.close()
d.close()
