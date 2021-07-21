import sys

m = int(input())

n = int(input())


past = [[None for i in range(n+1)] for j in range(m+1)]


mat = []
for i in range(m):
  mat.append(list(map(int,input().split())))



def minpath(mat, m, n):
  
  if(m<0 or n<0):
    return sys.maxsize 
   
    
  if(m==0 and n==0):
    past[m][n] = mat[m][n]
    return mat[m][n]
  
  if(past[m][n]!=None):
    return past[m][n]
  
  p= minpath(mat, m-1, n)
  

  q = minpath(mat, m, n-1)
  
 
  ans = min(p, q)
  
  nans = ans + mat[m][n]
  
  past[m][n] = nans
  
  return nans
  
  
  
print(minpath(mat, m-1,n-1))
  