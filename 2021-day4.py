import functools
import itertools
from pyparsing import *
from functools import partial
import array

with open('input/2021/day4.txt') as f:
    i = list(f)

def readInput(i):
    l = len(i)
    randomNumbers = list(map(int,i[0].split(",")))

    
    def readBoard(index):
        return [list(map(int,i[index+r].split())) for r in range(1,6)]

    boards = [readBoard(index) for index in range(1,l,6)]
    return (randomNumbers, boards)

def transpose(x):
    return list(map(list, zip(*x)))

def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

(randomNumbers, boards) = readInput(i)
rowcolboards = list(map(lambda board: board + transpose(board), boards))

try:
    for rn in randomNumbers:
        #   print(rn)
        #   print(list(rowcolboards))
        rowcolboards = list(map(compose(list, partial(map, compose(list, partial(filter, lambda n: n != rn)))), rowcolboards))
        #   print(list(rowcolboards))
        rowcolboards = list(map(compose(list, partial(map, compose(list, partial(filter, lambda n: n != rn)))), rowcolboards))
        winners = list(filter(lambda board: len(list(filter(lambda rc: len(rc) == 0, board))) > 0, rowcolboards))
        if len(winners) > 0:
            print(rn*sum(map(sum,winners[0][0:5])))
            raise Exception
except Exception:
    print()