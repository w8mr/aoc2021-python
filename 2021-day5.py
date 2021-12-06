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



def solve(i, diag):
    def index(x,y):
        return x+y*d

    def addVLine(grid, x, y1, y2):
#        print('vline')
        for y in range(y1, y2 + 1):
#            print(str(x)+", "+str(y))
            grid[index(x, y)] += 1
        return grid
    
    def addHDLine(grid, x1, x2, y, dir):
#        print('line')
        for x in range(x1, x2 + 1):
#            print(str(x)+", "+str(y + dir*(x-x1)))
            grid[index(x, y + dir*(x-x1))] += 1
        return grid
    
    def addLine(grid, line, diag):
#        print([line.c1.x, line.c1.y, line.c2.x, line.c2.y])
        x1 = line.c1.x
        y1 = line.c1.y
        x2 = line.c2.x
        y2 = line.c2.y
        
        if (x1 == x2):
            if (y1<=y2):
                return addVLine(grid, x1, y1, y2)
            else:
                return addVLine(grid, x1, y2, y1)
        elif (x1<x2):
            if (y1<y2) and diag:
                return addHDLine(grid, x1, x2, y1, 1)
            elif (y1>y2) and diag:
                return addHDLine(grid, x1, x2, y1, -1)
            elif (y1==y2):
                return addHDLine(grid, x1, x2, y1, 0)
            else:
                return grid
        elif (x1>x2):
            if (y1<y2) and diag:
                return addHDLine(grid, x2, x1, y2, -1)
            elif (y1>y2) and diag:
                return addHDLine(grid, x2, x1, y2, 1)
            elif (y1==y2):
                return addHDLine(grid, x2, x1, y2, 0)
            else: 
                return grid

    d = 1000
    grid = array.array('i', [0 for r in range(0, d * d)])
    # print(input)
    grid = reduce(lambda grid, line: addLine(grid, line, diag), input, grid)
    # print(grid)
    return len(list(filter(lambda x: x > 1, grid)))


print("part1: " + str(solve(i, False)))
print("part2: " + str(solve(i, True)))
