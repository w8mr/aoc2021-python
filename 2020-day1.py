from pyparsing import *


with open('input/2020/day1.txt') as f:
  i = list(map(int,f))
  old = i[0]
  
  count = 0
  for d in i:
    if d<old:
      count = count + 1
  
  print(count)    
      
            


