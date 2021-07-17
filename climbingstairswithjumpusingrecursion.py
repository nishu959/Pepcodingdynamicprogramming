n = int(input())
l = []

for i in range(n):
  l.append(int(input()))

def cstairs(n, l, target):
  
  if(n>target):
    return 0
 
  if(n==target):
    return 1
  
  ans = 0 
  for i in range(1,l[n]+1):
    
    p = cstairs(n+i, l, target)
    
    ans += p
    
  return ans
    
    
print(cstairs(0, l, n)) 
    
    
  

