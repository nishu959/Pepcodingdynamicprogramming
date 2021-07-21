n = int(input())

def fibo(n, past):
  
  if(n==0 or n==1):
    past[n] = n
    return n
  
  if(past[n]!=None):
    return past[n]
    
  
  a = fibo(n-1, past)
  b = fibo(n-2, past) 
  ans = a + b
  
  past[n] = ans
  
  return ans
 
 
past =  [None]*(n+1)

print(fibo(n, past))

