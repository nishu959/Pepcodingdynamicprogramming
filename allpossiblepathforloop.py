n = int(input())


def patholto(n, his):
  if(n<0):
    return 0
  if(n==0):
    return 1
  
  if(his[n]!=-1):
      return his[n]
      
  #print(n)
  ans =0
  
  for i in range(1,4):
    
    nn = n - i
    
    p = patholto(nn, his)
    
    ans += p
    
  his[n] = ans
  
  
  return ans
    
      
print(patholto(n, [-1]*(n+1))) 

