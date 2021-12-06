import collections

with open('input/2021/day6.txt') as f:
    i = list(map(int,list(f)[0][:-1].split(",")))

step = lambda i: i[1:7]+[i[0]+i[7],i[8],i[0]]

d = counter=collections.Counter(i)
#print(d)
e=[d[k] for k in range(9)]
#print(e)

for c in range(80):
#    print([e, sum(e)])
    e = step(e)
    
print(sum(e))

for c in range(80,256):
    #    print([e, sum(e)])
    e = step(e)

print(sum(e))
