import sys

m = int(input())

n = int(input())





mat = []
for i in range(m):
  mat.append(list(map(int,input().split())))



def minpath(mat, m, n):
  
  if(m<0 or n<0):
    return sys.maxsize 
    
    
  if(m==0 and n==0):
    return mat[m][n]
  
  
  
  p= minpath(mat, m-1, n)
  

  q = minpath(mat, m, n-1)
  
 
  ans = min(p, q)
  
  nans = ans + mat[m][n]
  
  
  return nans
  
  
  
print(minpath(mat, m-1,n-1))
  