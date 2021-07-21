
m =int(input())

l = []
for i in range(m):
  l.append(int(input()))
  
   
def vjpath(vn, l):
  
  if(vn>len(l)):
    return 0
    
  if(vn==len(l)):
    return 1
    
  ans = 0
  for i in range(1,l[vn]+1):
    ans += vjpath(vn+i, l)
    
  return ans
  
  
print(vjpath(0, l))
    

