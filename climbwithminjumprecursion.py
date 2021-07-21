import sys 

n =int(input())

l = []
for i in range(n):
  l.append(int(input()))
 

def minjump(vn, l):
   
  if(vn > len(l)):
    return sys.maxsize   
   
      
  if(vn == len(l)):
    return 0
  
  
  ans = sys.maxsize 
  for j in range(1,l[vn]+1):   
    a = minjump(vn+j, l)
    ans = min(ans, a)
 
  nans = ans +1
      
  return nans
  
  
print(minjump(0, l))
    
  