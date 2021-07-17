import sys

n = int(input())
l = []

for i in range(n):
  l.append(int(input()))

def cstairs(n, l, target, past):
  
  if(n>=target):
    return 0
  
  ans = sys.maxsize
  if(past[n]!=-1):
    return past[n]
  
  
  for i in range(1,l[n]+1):

    p = cstairs(n+i, l, target, past)
    
    ans = min(ans, p)
  
  past[n] = ans +1
  return ans+1
 
    
    
print(cstairs(0, l, n, [-1]*(n+1))) 
    
    
  

