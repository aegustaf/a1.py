from collections import Counter
import sys
lines = [line.lstrip('0').rstrip('\n') for line in open(sys.argv[1], 'r')]
c = Counter(lines)
for k,v in c.items():
    if v < 2:
        del c[k]
sorted(c, key=func, reverse=True)
for k,v in c.items():
    print(k + " " + str(v))

def func(x):
    return int(x, 16)
