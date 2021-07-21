n =int(input())

def totalstep(vn,fn, past):
  
  if(vn>fn):
    return 0
  if(vn==fn):
    past[vn] = 1
    return 1
   
  if(past[vn]!=None):
    return past[vn]
    
  
  ans = 0
  for i in range(1,4):
    ans += totalstep(vn+i,fn, past)
  
  past[vn] = ans
  
  return ans
  


past = [None]*(n+1)

print(totalstep(0,n, past)) 
  