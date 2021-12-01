import itertools

from pyparsing import *

def drop(it, n):
    return itertools.islice(it, n, None)

def solve(i, n):
    return len(list(filter(lambda nm:  nm[1] < nm[0], zip(drop(i,n), i))))

with open('input/2021/day1.txt') as f:
    i = list(map(int,f))
    
print(solve(i,1))
print(solve(i,3))