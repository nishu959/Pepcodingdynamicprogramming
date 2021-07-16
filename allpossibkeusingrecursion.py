n = int(input())


def patholto(n):
  if(n<0):
    return 0
  if(n==0):
    return 1
  
  #n1psf = psf + str(1)
  #print(n)
  p = patholto(n-1)
  
  #n2psf = psf + str(2)
  q = patholto(n-2)
 
  #n3psf = psf + str(3) 
  r = patholto(n-3)
 
  
  ans = p+q +r
  
  return ans
    
      
print(patholto(n)) 

