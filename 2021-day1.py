from pyparsing import *


with open('input/2021/day1.txt') as f:
    i = list(map(int,f))
    old = i[0]
    print (i[0])
    count = 0
    for d in i:
        if old<d:
            count = count + 1
        old = d
        print(str(d)+" "+str(count))

    print(count)

    old1 = i[0]
    old2 = i[1]
    old3 = i[2]
    print (i[0])
    count = 0
    for d in i:
        if old1<d:
            count = count + 1
        old1 = old2
        old2 = old3
        old3 = d
        print(str(d)+" "+str(count))

    print(count)



