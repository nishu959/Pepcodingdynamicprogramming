import sys

row = int(input())
col = int(input())

l = []
for i in range(row):
  l.append(list(map(int, input().split())))
 

past = [[None for i in range(col+1)] for j in range(row+1)]

def minmaze(l, row, col, past):
  
  if(row==len(l) or col==len(l[0])):
    return sys.maxsize 
  
  if(row==len(l)-1 and col==len(l[0])-1):
    return l[row][col]
  
  
  if(past[row][col]!=None):
    return past[row][col]
  
  
  
  
  a = minmaze(l, row+1, col, past)
  
  b = minmaze(l, row, col+1, past)
  
  ans = min(a, b) + l[row][col]
  
  past[row][col] = ans
  
  return ans
  
 
print(minmaze(l, 0, 0, past)) 

  