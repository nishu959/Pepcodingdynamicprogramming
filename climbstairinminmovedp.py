import sys 

n =int(input())

past = [None]*(n+1)

l = []
for i in range(n):
  l.append(int(input()))
 

def minjump(vn, l):
   
  if(vn > len(l)):
    return sys.maxsize   
   
      
  if(vn == len(l)):
    past[vn] = 0
    return 0
  
  if(past[vn]!=None):
    return past[vn]
  
  
  ans = sys.maxsize 
  for j in range(1,l[vn]+1):   
    a = minjump(vn+j, l)
    ans = min(ans, a)
   
  nans = ans +1
  past[vn] = nans
     
  return nans
  
  
print(minjump(0, l))
    
  