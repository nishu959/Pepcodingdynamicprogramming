n = int(input())


def patholto(n, his):
  if(n<0):
    return 0
  if(n==0):
    return 1
  
  if(his[n]!=-1):
    return his[n]    
  #n1psf = psf + str(1)
  #print(n)
  p = patholto(n-1, his)
  
  #n2psf = psf + str(2)
  q = patholto(n-2, his)
 
  #n3psf = psf + str(3) 
  r = patholto(n-3, his)
 
  
  ans = p+q +r
  his[n] = ans
  return ans
    
      
print(patholto(n, [-1]*(n+1))) 

