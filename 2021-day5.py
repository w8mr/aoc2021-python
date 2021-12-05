import functools
import itertools
from pyparsing import *
from functools import reduce
import array

with open('input/2021/day5.txt') as f:
    i = list(f)

pos = Word(nums).setParseAction(lambda x: list(map(int,x)))
coord = Group(
    pos('x') +
    Suppress(",") +
    pos('y')
)

line = (
    coord('c1') +
    Suppress("->") +
    coord('c2')
)

input = list(map(line.parseString, i))

def index(x,y):
    return x+y*d

def addVLine(grid, line):
    y1 = line.c1.y
    y2 = line.c2.y
    (y1, y2) = (y1, y2) if y1 <= y2 else (y2, y1)
    for y in range(y1, y2 + 1):
        #print(y)
        grid[index(line.c1.x, y)] += 1
    return grid

def addHLine(grid, line):
    x1 = line.c1.x
    x2 = line.c2.x
    (x1, x2) = (x1, x2) if x1 <= x2 else (x2, x1)    
    for x in range(x1, x2 + 1):
        #print(x)
        grid[index(x, line.c1.y)] += 1
    return grid

def addLine(grid, line):
#    print([line.c1.x, line.c1.y, line.c2.x, line.c2.y])
    if (line.c1.x == line.c2.x):
#        print('vline')
        return addVLine(grid, line)
    elif (line.c1.y == line.c2.y):
#        print('hline')
        return addHLine(grid, line)
    else:
        return grid
    
d = 1000
grid =array.array('i', [0 for r in range(0,d*d)])
#print(input)
grid = reduce(lambda grid, line: addLine(grid, line), input, grid)
#print(grid)
print(len(list(filter(lambda x: x>1, grid))))
