import sys

m = int(input())

n = int(input())

mat = []
for i in range(m):
  mat.append(list(map(int,input().split())))
  

def minpath(mat, m, n):
  
  if(m==len(mat)-1 and n==len(mat[0])-1):
    
    return mat[m][n]
  
  if(m>=len(mat) or n>=len(mat[0])):
    return sys.maxsize 
    
  
  
  p= minpath(mat, m+1, n)
  

  q = minpath(mat, m, n+1)
  
 
  
  
  nans = min(p, q)+ mat[m][n]
  
  
  return nans
  
  
  
  
print(minpath(mat, 0, 0))
   
  