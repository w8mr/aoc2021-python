import itertools

from pyparsing import *

with open('input/2021/day2.txt') as f:
    i = list(f)

pos = 0
depth = 0

for cmd in i:
    (c, a) = cmd.split()
    if c == 'forward':
        pos += int(a)
    elif c == 'down':
        depth += int(a)
    elif c == 'up':
        depth -= int(a)

    #print(" ".join((c, a, str(pos),str(depth))))

print(pos*depth)

pos = 0
depth = 0
aim = 0
for cmd in i:
    (c, a) = cmd.split()
    if c == 'forward':
        pos += int(a)
        depth += int(a)*aim
    elif c == 'down':
        aim += int(a)
    elif c == 'up':
        aim -= int(a)

    #print(" ".join((c, a, str(pos),str(depth),str(aim))))

print(pos*depth)
