from itertools import combinations

inp = list(map(int, open("input.txt").read().splitlines()))

q1 = 0
q2 = 0
for i in range(len(inp)-1):
    for perm in combinations(inp, i):
        if sum(perm) == 150:
            q1 += 1
    if q1 and not q2:
        q2 = q1
out = open("output1.txt", "w")
out.write(str("{0}".format(q1, q2)))
out.close()