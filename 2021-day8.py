from pyparsing import Word, Group, Suppress, alphas
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

def watson(deduced, wires):
   # print('deduced: '+str(deduced))
   # print('wires: '+str(list(wires)))
    not_deduced = list()
    for wire in wires:
   #     print('wire: '+str(wire))
        l = len(wire)
   #     print('len(wire): '+str(l))
        if l==2:
            deduced[1]=wire
        elif l==3:
            deduced[7]=wire
        elif l==4:
            deduced[4]=wire
        elif l==7:
            deduced[8]=wire
        elif l==6 and 4 in deduced and deduced[4] <= wire:
            deduced[9]=wire
        elif l==5 and 1 in deduced and deduced[1] <= set(wire):
            deduced[3]=wire
        elif l==6 and 9 in deduced and 1 in deduced and deduced[9] != wire and deduced[1] <= wire:
            deduced[0]=wire
        elif l==6 and 9 in deduced and 0 in deduced and deduced[9] != wire and deduced[0] != wire:
            deduced[6]=wire
        elif l==5 and 9 in deduced and 8 in deduced and (deduced[8] - deduced[9]) <= wire:
            deduced[2]=wire
        elif l==5 and 9 in deduced and 8 in deduced and not((deduced[8] - deduced[9]) <= wire):
            deduced[5]=wire
        else:
            not_deduced.append(wire)
    return (deduced, not_deduced)

def deduce_digits(wires):
    #print(input[0].wires)
    wires = list(map(set, wires))
    #print(wires)
    (deduced, not_deduced) = ({}, wires)
    while not_deduced:
    #    print(deduced)
    #    print(not_deduced)
        (deduced, not_deduced) = watson(deduced, not_deduced)
    return deduced

def find_number(deduced, number):
    return [k for (k,v) in deduced.items() if (v == set(number))][0]

def read_number(deduced, numbers):
    return int("".join(map(lambda n: str(find_number(deduced, n)), numbers)))

def read_input(input):
    deduced = deduce_digits(input.wires)
#    print(deduced)
    return read_number(deduced, input.numbers)

#print(list(map(read_input,input)))
print(sum(map(read_input,input)))

# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# 1: be
# 8: cfbegad
# 4: cgeb
# 7: ebd
# 9: cbdgef 
# 3: fecdb
# 6: fgaecd
# 0: agebfd
# 2: fdcge
# 5: fabcd
#
# 8 3 9 4


