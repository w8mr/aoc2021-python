import collections

with open('input/2021/day7.txt') as f:
    i = list(map(int,list(f)[0][:-1].split(",")))

i.sort()
#print(i)
hi = len(i) // 2 - 1
#print(hi)
#print(i[hi])
#print(i[hi+1])
#print(list(map(lambda x:x-i[hi], i)))
#print(list(map(lambda x:abs(x-i[hi]), i)))
print(sum(map(lambda x:abs(x-i[hi]), i)))

def fuel(x,j):
    d = abs(x-j)
    return d*(d+1)//2

m = [sum(map(lambda x:fuel(x,j), i)) for j in range(0,len(i))]
#print(m)
print(min(m))


