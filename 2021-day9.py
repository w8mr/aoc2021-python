from pyparsing import Word, Group, Suppress, alphas
from itertools import chain

with open('input/2021/day9.txt') as f:
    i = list(map(lambda l: list(map(int, l[:-1])), list(f)))

print(i)

def get_cell(row, col):
    if row < 0 or row >= len(i):
        return None
    r = i[row]
    if col < 0 or col >= len(r):
        return None
    return r[col]

t=0
neighbours = [(-1,0),(0,1),(1,0),(0,-1)]
for ri, row in enumerate(i):
    for ci, cell in enumerate(row):
        m = min(filter(lambda x: x!=None,map(lambda yx: get_cell(ri+yx[0], ci+yx[1]), neighbours)))
        if cell<m:
            t+=cell+1
print(t)