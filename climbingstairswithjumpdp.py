n = int(input())
l = []

for i in range(n):
  l.append(int(input()))

def cstairs(n, l, target, past):
  
  if(n>target):
    return 0
 
  if(n==target):
    return 1
    
  if(past[n]!=-1):
    return past[n]
  
  ans = 0 
  for i in range(1,l[n]+1):
    
    p = cstairs(n+i, l, target, past)
    
    ans += p
    
  past[n] = ans
    
  return ans
    
    
print(cstairs(0, l, n, [-1]*(n+1))) 
    
    
  

