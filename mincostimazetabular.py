
import sys

row = int(input())
col = int(input())

l = []
for i in range(row):
  l.append(list(map(int, input().split())))
 

past = [[None for i in range(col+1)] for j in range(row+1)]

for i in range(row, -1,-1):
  for j in range(col,-1,-1):
    
    if(i==row-1 and j ==col-1):
      past[i][j] = l[i][j]
      
    elif(i == row):
      past[i][j] = sys.maxsize 
      
    elif(j==col):
      past[i][j] = sys.maxsize 
      
    else:
      past[i][j]= l[i][j]+ min(past[i+1][j], past[i][j+1])
      
      
print(past[0][0])
    
    
  