import itertools

from pyparsing import *
from functools import partial
import array

def count(i):
    a = array.array('i',(0 for i in range(1,len(i[0]))))
    for l in i:
        for index, b in enumerate(l):
            if b == '1':
                a[index] += 1;
    return a

with open('input/2021/day3.txt') as f:
    i = list(f)

def part1(f):
    a = count(i)
    c = len(i)
    return int("".join(map(partial(f,c), a)), 2)

gamma = part1(lambda c, i: "1" if i*2 > c else "0")
epsilon = part1(lambda c, i: "1" if i*2 < c else "0")

print (gamma*epsilon)

def part2(i, f):
    bp=0
    while len(i)>1:
        a = count(i)
        c = len(i)
        b = f(a[bp], c)
        #print(", ".join([str(bp), str(a), str(c), str(b)]))
        i = list(filter(lambda x: x[bp] == b, i))
        bp += 1
    return int("".join(i[0]),2)

oxygen = part2(i, lambda i,c: "1" if i*2 >= c else "0")
co2 = part2(i, lambda i,c: "1" if i*2 < c else "0")

print(oxygen * co2)
