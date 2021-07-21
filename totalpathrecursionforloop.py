n =int(input())

def totalstep(vn,fn):
  
  if(vn>fn):
    return 0
  if(vn==fn):
    return 1
    
  ans = 0
  for i in range(1,4):
    ans += totalstep(vn+i,fn)
  
  
  
  return ans
  

print(totalstep(0,n)) 
  