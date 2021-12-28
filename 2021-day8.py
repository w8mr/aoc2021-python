from pyparsing import *
from itertools import chain

with open('input/2021/day8.txt') as f:
    i = list(f)

wire_note = Word(alphas)
wires = Group(wire_note*10)
numbers = Group(wire_note*4)

line = (
        wires('wires') +
        Suppress("|") +
        numbers('numbers')
)

input = list(map(line.parseString, i))

def flat_list(regular_list): 
    return [item for sublist in regular_list for item in sublist]

print(len(list(filter(lambda l:len(l) in [2,3,4,7], flat_list(list(map(lambda line: list(line.numbers),input)))))))