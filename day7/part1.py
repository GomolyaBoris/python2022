import re
from z3 import *

fu = {}
s = Solver()

with open('input1.txt') as f:
    lines = f.readlines()

    for line in lines:
        res = re.search(r'(.*)\s*->\s*(.*)', line)
        command, store_var = res.group(1).strip(), res.group(2)

        if store_var not in fu:
            fu[store_var] = BitVec(store_var, 32)

        res = re.search(r'^(\d*?)$', command)
        if res and res.group(1) != '':
            s.add(fu[store_var] == res.group(1))
            continue

        # AND
        res = re.search(r'(\d*)\s*AND\s*(.*)', command)
        if res and res.group(1) != '' and res.group(2) != '':

            if res.group(2) not in fu:
                fu[res.group(2)] = BitVec(res.group(2), 32)

            s.add(fu[store_var] == int(res.group(1)) & fu[res.group(2)])
            continue

        res = re.search(r'(.*?)\s*AND\s*(.*)', command)
        if res and res.group(1) != '' and res.group(2) != '':
            if res.group(1) not in fu:
                fu[res.group(1)] = BitVec(res.group(1), 32)

            if res.group(2) not in fu:
                fu[res.group(2)] = BitVec(res.group(2), 32)

            s.add(fu[store_var] == fu[res.group(1)] & fu[res.group(2)])
            continue

        # OR
        res = re.search(r'(.*?)\s*OR\s*(.*)', command)
        if res and res.group(1) != '' and res.group(2) != '':
            if res.group(1) not in fu:
                fu[res.group(1)] = BitVec(res.group(1), 32)

            if res.group(2) not in fu:
                fu[res.group(2)] = BitVec(res.group(2), 32)

            s.add(fu[store_var] == fu[res.group(1)] | fu[res.group(2)])
            continue

        # LSHIFT
        res = re.search(r'(.*?)\s*LSHIFT\s*(\d*)', command)
        if res and res.group(1) != '' and res.group(2) != '':
            if res.group(1) not in fu:
                fu[res.group(1)] = BitVec(res.group(1), 32)

            s.add(fu[store_var] == fu[res.group(1)] << int(res.group(2)))
            continue

        # RSHIFT
        res = re.search(r'(.*?)\s*RSHIFT\s*(\d*)', command)
        if res and res.group(1) != '' and res.group(2) != '':
            if res.group(1) not in fu:
                fu[res.group(1)] = BitVec(res.group(1), 32)

            s.add(fu[store_var] == fu[res.group(1)] >> int(res.group(2)))
            continue

        # NOT
        res = re.search(r'NOT\s*(.*)', command)
        if res and res.group(1) != '':
            if res.group(1) not in fu:
                fu[res.group(1)] = BitVec(res.group(1), 32)

            s.add(fu[store_var] == (
                ~fu[res.group(1)]) & 0xFFFF)

            continue

        res = re.search(r'(.*)', command)
        if res and res.group(1) != '':
            if res.group(1) not in fu:
                fu[res.group(1)] = BitVec(res.group(1), 32)

            s.add(fu[store_var] == fu[res.group(1)])

            continue

set_option(max_args=10000000, max_lines=1000000, max_depth=10000000, max_visited=1000000)
print(s.check())
out = open('output1.txt', 'w')
out.write(str(s.model()))
out.close()
