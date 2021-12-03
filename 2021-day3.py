import itertools

from pyparsing import *
from functools import reduce
import array

def count(i):
    a = array.array('i',(0 for i in range(1,len(i[0]))))
    for l in i:
        for index, b in enumerate(l):
            if b == '1':
                a[index] += 1;
    return a

def most(i):
    return "1" if i*2 > c else "0"

def least(i):
    return "1" if i*2 < c else "0"

with open('input/2021/day3.txt') as f:
    i = list(f)


a = count(i)
    
c = len(i)

        
gamma = int("".join(map(most,a)),2)
epsilon = int("".join(map(least,a)),2)

print (gamma*epsilon)

