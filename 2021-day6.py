import functools
import itertools
from pyparsing import *
from functools import reduce
import array

with open('input/2021/day6.txt') as f:
    i = list(map(int,list(f)[0][:-1].split(",")))

flat_map = lambda f, xs: [y for ys in xs for y in f(ys)]


def step(i):
    return flat_map(lambda x: [x-1] if x > 0 else [6,8], i)

for c in range(80):
  #  print(i)
    i = step(i)
    
print(len(i))