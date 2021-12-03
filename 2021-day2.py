import itertools

from pyparsing import *
from functools import reduce

with open('input/2021/day2.txt') as f:
    i = list(f)

def step1(pd, cmd):
    (p,d) = pd
    (c, v) = cmd.split()
    if c == 'forward':
        p += int(v)
    elif c == 'down':
        d += int(v)
    elif c == 'up':
        d -= int(v)
    return (p,d)

(p,d) = reduce(step1, i, (0,0))
print(p*d)

def step2(pda, cmd):
    (p,d,a) = pda
    (c, v) = cmd.split()
    if c == 'forward':
        p += int(v)
        d += int(v)*a
    elif c == 'down':
        a += int(v)
    elif c == 'up':
        a -= int(v)
    return (p,d,a)

(p,d,a) = reduce(step2, i, (0,0,0))
print(p*d)
