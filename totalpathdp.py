n =int(input())

def totalstep(vn,fn, past):
  
  if(vn>fn):
    #here in this case we need not to return 
    #because whole matrix is filled with needed 
    #value if we do we have to increase size
    #for that otherwise index out if bound
    return 0
  if(vn==fn):
    past[vn] = 1
    return 1
    
  if(past[vn]!=None):
    return past[vn]
    
  
  
  a = totalstep(vn+1,fn, past)
  b = totalstep(vn+2,fn, past)
  c = totalstep(vn+3,fn, past)
  
  ans = a+b+c
  
  past[vn] = ans
  
  return ans
  
past = [None]*(n+1)

print(totalstep(0,n,past)) 
  
  
  