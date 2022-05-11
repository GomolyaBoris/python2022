import re
import itertools
import collections

text = open('input.txt').read()
line = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
history = collections.defaultdict(list)
for who, speed, duration, rest in re.findall(line, text):
    steps = itertools.cycle([int(speed)]*int(duration) + [0]*int(rest))
    history[who] = list(itertools.accumulate(next(steps) for _ in range(2503)))

dist = max(h[-1] for h in history.values())
out = open('output1.txt', 'w')
out.write(str(dist))
out.close()