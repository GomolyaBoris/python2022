import re
import numpy as np
from functools import reduce
from operator import mul

input = open("input.txt", "r")
input = input.read()
m = []
for line in input.split('\n'):
    c, d, f, t, cal = map(int, re.findall('-?\d+', line))
    m.append([c, d, f, t, cal])
m = np.array(m)

def min_zero_sum(*ns):
    return max(0, sum(ns))

scores = [(reduce(mul, map(min_zero_sum,
                          *map(mul, [i, j, k, l], m[:, :-1]))),
           sum(map(mul, [i, j, k, l], m[:, -1])))
          for i in range(101)
          for j in range(0, 101-i)
          for k in range(0, 101-j-i)
          for l in [100 - i - j - k]]

out = open("output1.txt", "w")
out.write(str(max(s[0] for s in scores)))
out.close()
