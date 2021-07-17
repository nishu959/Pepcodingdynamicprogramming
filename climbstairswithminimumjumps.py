import sys

n = int(input())
l = []

for i in range(n):
  l.append(int(input()))

def cstairs(n, l, target):
  
  if(n>=target):
    return 0
  
  ans = sys.maxsize
  
  
  for i in range(1,l[n]+1):

    p = cstairs(n+i, l, target)
    
    ans = min(ans, p)
  
  return ans+1
 
    
    
print(cstairs(0, l, n)) 
    
    
  

