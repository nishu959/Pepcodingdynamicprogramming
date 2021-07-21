n =int(input())

def totalstep(vn,fn):
  
  if(vn>fn):
    return 0
  if(vn==fn):
    return 1
  
  
  a = totalstep(vn+1,fn)
  b = totalstep(vn+2,fn)
  c = totalstep(vn+3,fn)
  
  ans = a+b+c
  
  return ans
  

print(totalstep(0,n)) 
  
  
  

