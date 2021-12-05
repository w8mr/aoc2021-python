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

def solve(rowcolboards):
    ws = []
    for rn in randomNumbers:
        #print(rn)
        #print(list(rowcolboards))
        rowcolboards = list(map(compose(list, partial(map, compose(list, partial(filter, lambda n: n != rn)))), rowcolboards))
        #print(list(rowcolboards))
        
        w = won(rowcolboards)
        t = list(zip(rowcolboards, w))
        #print(list(t))
        ws = ws + [score(rn, board) for (board, b) in t if b]
        rowcolboards = [board for (board, b) in t if not b]
        #print(ws)
        #print(rowcolboards)
    return ws    


def score(rn, board):
    return rn*sum(map(sum, board[0:5]))

def won(rowcolboards):
    return list(map(lambda board: len(list(filter(lambda rc: len(rc) == 0, board))) > 0, rowcolboards))

solve1 = solve(rowcolboards)
print(solve1[0])
print(solve1[-1])