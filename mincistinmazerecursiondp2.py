import sys

m = int(input())

n = int(input())

past = [[None]*(n)]*(m)

mat = []
for i in range(m):
  mat.append(list(map(int,input().split())))



for i in range(m-1,-1,-1):
  for j in range(n-1,-1,-1):
    
    if(i==m-1 and j==n-1):
      past[i][j] = mat[i][j]
      
    elif(i==m-1):
      past[i][j] = past[i][j+1] + mat[i][j]
  
    elif(j==n-1):
      past[i][j] = past[i+1][j] + mat[i][j]
   
    else:
     
      past[i][j] = min(past[i+1][j],past[i][j+1]) + mat[i][j]
     
    
 
print(past[0][0])
