import re
def read(s):
    return [i.strip() for i in open(s, 'r')]
lines = read('input.txt')

replacements = []
for i in lines[:-2]:
    m = re.findall(r'(\S+) => (\S+)', i)
    replacements.append(m[0])
X = lines[-1]

steps = set()
for i, j in replacements:
    for k in range(len(X)):
        if X[k:k+len(i)] == i:
            y = X[:k] + j + X[k+len(i):]
            steps.add(y)

out = open('output1.txt', 'w')
out.write(str(len(steps)))
out.close()