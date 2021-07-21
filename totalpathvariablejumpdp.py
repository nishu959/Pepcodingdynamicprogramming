
m =int(input())

l = []
for i in range(m):
  l.append(int(input()))
  
   
def vjpath(vn, l,past):
  
  if(vn>len(l)):
    return 0
    
  if(vn==len(l)):
    past[vn] =1
    return 1
    
  if(past[vn]!=None):
    return past[vn]
    
  ans = 0
  
  for i in range(1,l[vn]+1):
    ans += vjpath(vn+i, l,past)
    
  past[vn] = ans
    
  return ans
  

past= [None]*(m+1)
print(vjpath(0, l, past))


    

